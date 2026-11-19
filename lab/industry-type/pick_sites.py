#!/usr/bin/env python3
"""Propose the real-site list for the industry-type study. Selection only: nothing here measures fonts.

Usage:
  python3 lab/industry-type/pick_sites.py            fetch missing sources, pre-check, write proposed-sites.json
  python3 lab/industry-type/pick_sites.py --offline  use cached sources/ only (the pre-check still visits homepages)

Steps, all fixed by methodology.md:
  1. Pools: each industry (or editorial stratum) unions several discovery sources (SOURCES below).
  2. Eligibility: the listed site's domain is in the frozen Tranco list, the listed site is that domain's
     homepage, no other organization lists the domain, it isn't struck for this industry in strikes.json, and
     it isn't already in an earlier industry or stratum (INDUSTRIES order).
  3. Leaders: the best Tranco ranks that pass the pre-check.
  4. Sample: source-balanced. Each source's eligible candidates are ordered by sha256(seed-industry-stratum-
     source-domain);
     sources take turns in a fixed order, each turn adding its next candidate that passes the pre-check and
     isn't already chosen.
  5. Pre-check (selection, not measurement): the homepage answers 200 within 20 s, stays on the same
     registrable domain and isn't a parking page. Writing system and lang are recorded, never excluded.
Every candidate that fails a step is written to exclusions with its reason. Standard library only.
"""
import argparse
import csv
import hashlib
import html as htmllib
import io
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources"
UA = "tasteskills-research/0.1 (font study; one request per site)"
SEED = 20261118
TRANCO_ID = "V38GN"
PROTOCOL = "industry-type/2"
PARKED = re.compile(r"domain (is|may be) for sale|buy this domain|parked free|sedoparking|hugedomains", re.I)

# --- discovery sources -------------------------------------------------------------------------------------
# Wikidata SPARQL bodies. ?item must have an official website (?site) and no dissolution date.
WD = {
    "fintech": "?item wdt:P452 wd:Q16319025.",
    "health": "?item wdt:P452 wd:Q31207.",
    "fashion-house": "?item wdt:P31 wd:Q1941779.",
    "luxury-good": "?item wdt:P452 wd:Q949715.",
    "restaurant-chain": "?item wdt:P31 wd:Q18534542.",
    "hotel-chain": "?item wdt:P31 wd:Q1631129.",
    "hospitality": "?item wdt:P452 wd:Q1495452.",
    "architectural-firm": "?item wdt:P31 wd:Q4387609.",
    "design-agency": "?item wdt:P31 wd:Q1200676.",
    "architecture": "?item wdt:P452 wd:Q12271.",
    "graphic-design": "?item wdt:P452 wd:Q185925.",
    "programming-tool-developer": "?tool wdt:P31 wd:Q1077784; wdt:P178 ?item. "
                                  "VALUES ?org { wd:Q4830453 wd:Q783794 wd:Q6881511 wd:Q891723 wd:Q1058914 } "
                                  "?item wdt:P31 ?org.",
    "national-newspaper": "?item wdt:P31 wd:Q11389521.",
    "online-newspaper": "?item wdt:P31 wd:Q1153191.",
    "news-website": "?item wdt:P31 wd:Q17232649.",
    "online-magazine": "?item wdt:P31 wd:Q847906.",
    "business-periodical": "?item wdt:P31 wd:Q2586014.",
    "business-newspaper": "?item wdt:P31 wd:Q106651372.",
    "magazine-with-publisher": "?item wdt:P31 wd:Q41298. FILTER EXISTS { ?item wdt:P123|wdt:P127 ?o }",
    "magazine-independent": "{ ?item wdt:P31 wd:Q41298 } UNION { ?item wdt:P31 wd:Q847906 } "
                            "FILTER NOT EXISTS { ?item wdt:P123|wdt:P127 ?o }",
}
# Apple App Store (US) genre ids; top free + top paid charts, 100 each, developer site from the lookup API.
APPSTORE = {"dev": [6026], "finance": [6015], "health": [6020], "all": [None]}
APPSTORE_ASSIGNED = {6026, 6015, 6020, 6009, 6021, 6014, 6024}
# Left out of the "all" chart: genres assigned to other industries, news, games (6014) and shopping (6024; retail
# and marketplaces selling physical goods are commerce, not consumer apps).
FINTECH_SOURCES = ("yc ", "wikidata fintech")  # fintech-specific classifications
FINTECH_MIN_FOUNDED = 2000  # a company found only in the Finance chart must be founded this year or later
WP_LISTS = {
    "architecture-firms": ("List_of_architecture_firms",
                           {"Q4387609", "Q4830453", "Q783794", "Q6881511", "Q43229", "Q1200676", "Q891723"}),
    "magazines-by-circulation": ("List_of_magazines_by_circulation", {"Q41298", "Q847906", "Q1002697"}),
    "newspapers-by-circulation": ("List_of_newspapers_by_circulation",
                                  {"Q11032", "Q11389521", "Q1153191", "Q1002697", "Q106651372"}),
}

# Industry -> {stratum: {"leaders": n, "sample": n, "sources": [...]}}; one stratum "all" unless stratified.
S = lambda leaders, sample, *src: {"leaders": leaders, "sample": sample, "sources": list(src)}
INDUSTRIES = {
    "dev-tools": {"all": S(5, 10, "yc:Engineering, Product and Design|Infrastructure", "appstore:dev",
                           "wikidata:programming-tool-developer")},
    "fintech": {"all": S(5, 10, "yc:Fintech", "wikidata:fintech", "appstore:finance")},
    "health": {"all": S(5, 10, "yc:Healthcare", "wikidata:health", "appstore:health")},  # Medical genre only
    "luxury-fashion": {"all": S(5, 10, "wikidata:fashion-house", "wikidata:luxury-good", "altagamma")},
    "food-hospitality": {"all": S(5, 10, "wikidata:restaurant-chain", "wikidata:hotel-chain",
                                  "wikidata:hospitality", "michelin")},
    "editorial-media": {
        "national": S(1, 2, "wikidata:national-newspaper", "wplist:newspapers-by-circulation"),
        "digital-native": S(1, 2, "wikidata:online-newspaper", "wikidata:news-website"),
        "magazines": S(1, 2, "wikidata:magazine-with-publisher", "wplist:magazines-by-circulation"),
        "business": S(1, 2, "wikidata:business-periodical", "wikidata:business-newspaper"),
        "independent": S(1, 2, "wikidata:magazine-independent", "wikidata:online-magazine"),
    },
    "architecture-design": {"all": S(5, 10, "wikidata:architectural-firm", "wikidata:design-agency",
                                     "wikidata:architecture", "wikidata:graphic-design",
                                     "wplist:architecture-firms")},
    "consumer-apps": {"all": S(5, 10, "yc:Consumer", "appstore:all")},
}
# The source order above also breaks merged-pool ties: a stratum walks its sources in this order.


def get(url, timeout=60, tries=20, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", **(headers or {})})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            # 429/503: rate limit, wait it out. 502/504: the query itself is too heavy; give up after 3 tries.
            if e.code not in (429, 502, 503, 504) or attempt == tries - 1 or (e.code in (502, 504) and attempt >= 2):
                raise
            time.sleep(65)  # Wikidata's query service rate-limits to about 1 request a minute


def cached(name, fetch, offline):
    path = SOURCES / name
    if path.exists():
        return path.read_bytes()
    if offline:
        raise SystemExit(f"missing cached source {name}; run without --offline")
    data = fetch()
    SOURCES.mkdir(exist_ok=True)
    path.write_bytes(data)
    return data


def tranco(offline):
    raw = cached(f"tranco-{TRANCO_ID}.csv", lambda: zipfile.ZipFile(io.BytesIO(
        get(f"https://tranco-list.eu/download_daily/{TRANCO_ID}"))).read("top-1m.csv"), offline)
    return {d.strip(): int(r) for r, d in (l.split(",", 1) for l in raw.decode().splitlines())}


def entry(name, url, source, owner):
    return {"name": name, "url": url, "source": source, "owner": owner}


def src_yc(arg, offline):
    subs = set(arg.split("|"))
    data = json.loads(cached("yc-all.json", lambda: get("https://yc-oss.github.io/api/companies/all.json"), offline))
    return [entry(c["name"], c["website"], f"yc {c['slug']}", f"yc:{c['slug']}") for c in data
            if c.get("status") in {"Active", "Public"} and c.get("website") and set(c.get("industries") or []) & subs]


def src_wikidata(key, offline):
    query = f"""SELECT ?item ?itemLabel ?site WHERE {{ {WD[key]} ?item wdt:P856 ?site.
      FILTER NOT EXISTS {{ ?item wdt:P576 ?d }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} }}"""
    url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"query": query, "format": "json"})
    legacy = {"fintech": "P452-Q16319025", "health": "P452-Q31207", "fashion-house": "P31-Q1941779",
              "luxury-good": "P452-Q949715", "restaurant-chain": "P31-Q18534542", "hotel-chain": "P31-Q1631129",
              "hospitality": "P452-Q1495452", "architectural-firm": "P31-Q4387609", "design-agency": "P31-Q1200676",
              "architecture": "P452-Q12271", "graphic-design": "P452-Q185925"}
    name = f"wikidata-{legacy[key]}.json" if key in legacy else f"wikidata-{key}.json"
    rows = json.loads(cached(name, lambda: get(url, timeout=120), offline))["results"]["bindings"]
    out = []
    for r in rows:
        qid = r["item"]["value"].rsplit("/", 1)[-1]
        label = r.get("itemLabel", {}).get("value", "")
        out.append(entry("" if label == qid else label, r["site"]["value"], f"wikidata {key} {qid}", f"wd:{qid}"))
    return out


def src_appstore(key, offline):
    def fetch():
        ids, genre_of = [], {}
        for genre in APPSTORE[key]:
            for chart in ("topfreeapplications", "toppaidapplications"):
                g = f"/genre={genre}" if genre else ""
                feed = json.loads(get(f"https://itunes.apple.com/us/rss/{chart}/limit=100{g}/json"))
                for e in feed["feed"].get("entry", []):
                    ids.append(e["id"]["attributes"]["im:id"])
        apps = []
        for i in range(0, len(ids), 100):
            apps += json.loads(get("https://itunes.apple.com/lookup?id=" + ",".join(ids[i:i + 100])))["results"]
            time.sleep(1)
        return json.dumps(apps).encode()
    apps = json.loads(cached(f"appstore-{key}.json", fetch, offline))
    out = []
    for a in apps:
        if not a.get("sellerUrl"):
            continue
        if key == "all" and a.get("primaryGenreId") in APPSTORE_ASSIGNED:
            continue
        seller = a.get("sellerName") or a.get("artistName", "")
        out.append(entry(seller, a["sellerUrl"], f"appstore {key} {a['trackId']}", f"seller:{seller.lower()}"))
    return out


def src_altagamma(_, offline):
    page = cached("altagamma-members.html", lambda: get("https://altagamma.it/en/members/",
                                                       headers={"User-Agent": "Mozilla/5.0"}), offline).decode()
    urls = sorted(set(re.findall(r'href="(https?://[^"]+)"', page)))
    skip = re.compile(r"altagamma|browsehappy|facebook|twitter|instagram|linkedin|youtube|google|apple|cookie", re.I)
    return [entry("", u, f"altagamma {u}", f"altagamma:{urllib.parse.urlsplit(u).hostname}")
            for u in urls if not skip.search(u)]


def src_michelin(_, offline):
    raw = cached("michelin.csv", lambda: get(
        "https://raw.githubusercontent.com/ngshiheng/michelin-my-maps/main/data/michelin_my_maps.csv"), offline)
    rows = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    return [entry(r["Name"], r["WebsiteUrl"], f"michelin {r['Url'].rsplit('/', 1)[-1]}", f"michelin:{r['Url']}")
            for r in rows if r.get("WebsiteUrl")]


def src_wplist(key, offline):
    title, allowed = WP_LISTS[key]

    def fetch():
        titles, cont = [], {}
        while True:
            params = {"action": "query", "titles": title, "prop": "links", "pllimit": "max", "plnamespace": 0,
                      "format": "json", **cont}
            d = json.loads(get("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)))
            for p in d["query"]["pages"].values():
                titles += [l["title"] for l in p.get("links", [])]
            if "continue" not in d:
                break
            cont = d["continue"]
        qids = []
        for i in range(0, len(titles), 50):
            params = {"action": "query", "titles": "|".join(titles[i:i + 50]), "prop": "pageprops",
                      "ppprop": "wikibase_item", "redirects": 1, "format": "json"}
            d = json.loads(get("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)))
            qids += [p["pageprops"]["wikibase_item"] for p in d["query"]["pages"].values() if "pageprops" in p]
            time.sleep(1)
        entities = {}
        for i in range(0, len(qids), 50):
            params = {"action": "wbgetentities", "ids": "|".join(qids[i:i + 50]), "props": "claims|labels",
                      "languages": "en", "format": "json"}
            entities.update(json.loads(get("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(params)))
                            ["entities"])
            time.sleep(2)
        slim = {}
        for q, e in entities.items():
            c = e.get("claims", {})
            val = lambda p: [x["mainsnak"].get("datavalue", {}).get("value") for x in c.get(p, [])]
            slim[q] = {"label": e.get("labels", {}).get("en", {}).get("value", ""),
                       "p31": [v["id"] for v in val("P31") if v], "p856": [v for v in val("P856") if v],
                       "p576": bool(c.get("P576"))}
        return json.dumps({"page": title, "titles": len(titles), "entities": slim}).encode()
    data = json.loads(cached(f"wplist-{key}.json", fetch, offline))
    return [entry(e["label"], e["p856"][0], f"wplist {key} {q}", f"wd:{q}") for q, e in data["entities"].items()
            if e["p856"] and not e["p576"] and set(e["p31"]) & allowed]


FETCH = {"yc": src_yc, "wikidata": src_wikidata, "appstore": src_appstore, "altagamma": src_altagamma,
         "michelin": src_michelin, "wplist": src_wplist}


def load_source(spec, offline):
    kind, _, arg = spec.partition(":")
    return FETCH[kind](arg, offline)


# --- eligibility ---------------------------------------------------------------------------------------------
def split(url):
    parts = urllib.parse.urlsplit(url if "//" in url else "https://" + url)
    return (parts.hostname or "").lower().removeprefix("www."), parts.path.strip("/")


def registrable(url, ranks):
    host, _ = split(url)
    labels = host.split(".")
    for i in range(len(labels) - 1):
        if ".".join(labels[i:]) in ranks:
            return ".".join(labels[i:])
    return None


SCRIPTS = [("Latin", r"[A-Za-zÀ-ɏ]"), ("Cyrillic", r"[Ѐ-ӿ]"), ("Greek", r"[Ͱ-Ͽ]"),
           ("Arabic", r"[؀-ۿ]"), ("Hebrew", r"[֐-׿]"), ("Devanagari", r"[ऀ-ॿ]"),
           ("Thai", r"[฀-๿]"), ("Hangul", r"[가-힯]"), ("Kana", r"[぀-ヿ]"),
           ("Han", r"[一-鿿]")]


def writing_system(page):
    text = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", page)
    text = htmllib.unescape(re.sub(r"(?s)<[^>]+>", " ", text))
    counts = {name: len(re.findall(rx, text)) for name, rx in SCRIPTS}
    total = sum(counts.values()) or 1
    ranked = sorted(((n, c) for n, c in counts.items() if c / total >= 0.05), key=lambda x: -x[1])
    return [n for n, _ in ranked] or ["unknown"]


def fetch_home(domain):
    """GET the homepage with a hard 20 s limit (curl --max-time), unlike urllib's per-read timeout."""
    r = subprocess.run(["curl", "-sL", "--max-time", "20", "--max-filesize", "5000000", "-A", UA,
                        "-H", "Accept: text/html", "-o", "-", "-w", "\n%{http_code} %{url_effective}",
                        f"https://{domain}/"], capture_output=True, timeout=30)
    body, _, tail = r.stdout.rpartition(b"\n")
    code, _, final = tail.decode("utf-8", "replace").partition(" ")
    # Reachable: a 200 (even if the connection dropped after some of the body arrived), or a 401/403 from bot
    # protection, which a real browser may pass; the measurement verifies those in Chrome.
    if code == "200" and (r.returncode == 0 or body):
        blocked = False
    elif code in ("401", "403"):
        blocked = True
    else:
        raise RuntimeError(f"curl exit {r.returncode}, HTTP {code}")
    return urllib.parse.urlsplit(final).hostname or "", body[:300_000].decode("utf-8", "replace"), blocked


def precheck(cand, tries=3):
    domain = cand["domain"]
    for attempt in range(tries):  # a homepage must fail 3 times, 30 s apart, before it's excluded
        try:
            final, page, blocked = fetch_home(domain)
            break
        except Exception as e:
            if attempt == tries - 1:
                return f"homepage failed 3 times: {e}", None
            time.sleep(30)
    if not (final == domain or final.endswith("." + domain)):
        return f"redirects off-domain to {final}", None
    if PARKED.search(page):
        return "parking page", None
    if blocked:
        return None, {"lang": None, "scripts": ["unknown"], "precheck_blocked": True}
    m = re.search(r"<html[^>]*\blang=[\"']?([A-Za-z-]{2,8})", page, re.I)
    return None, {"lang": m.group(1) if m else None, "scripts": writing_system(page)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--recheck-failures", action="store_true", help="retry homepages that failed before")
    args = ap.parse_args()
    ranks = tranco(args.offline)
    founded = json.loads((HERE / "founded.json").read_text())["founded"]
    strikes = {(s["domain"], s["industry"]): s for s in json.loads((HERE / "strikes.json").read_text())["strikes"]}

    loaded = {}
    for ind, strata in INDUSTRIES.items():
        for st in strata.values():
            for spec in st["sources"]:
                if spec not in loaded:
                    loaded[spec] = load_source(spec, args.offline)
                    print(f"source {spec}: {len(loaded[spec])}", file=sys.stderr)
    # A domain is shared when two different organizations list it within the same kind of source (many Wikidata
    # items listing github.com). The same company found in two kinds of source (YC and the App Store) is one owner.
    by_kind = {}
    for spec, rows in loaded.items():
        kind = spec.split(":", 1)[0]
        for c in rows:
            d = registrable(c["url"], ranks)
            if d:
                by_kind.setdefault(d, {}).setdefault(kind, set()).add(c["owner"])
    owners = {d: max(kinds.values(), key=len) for d, kinds in by_kind.items()}

    exclusions, seen, out_sites, composition = [], {}, {}, {}
    # Pre-check results are saved with their time, so reruns reuse them; --recheck-failures retries failures.
    pre_file = HERE / "prechecks.json"
    saved = json.loads(pre_file.read_text()) if pre_file.exists() else {}
    if args.recheck_failures:
        saved = {d: r for d, r in saved.items() if not r["reason"]}
    checked = {d: (r["reason"], r["info"]) for d, r in saved.items()}

    def check(cands):
        todo = [c for c in cands if c["domain"] not in checked]
        with ThreadPoolExecutor(8) as ex:
            for c, res in zip(todo, ex.map(precheck, todo)):
                checked[c["domain"]] = res
                saved[c["domain"]] = {"reason": res[0], "info": res[1],
                                      "checked": time.strftime("%Y-%m-%dT%H:%M:%S")}
        if todo:
            pre_file.write_text(json.dumps(dict(sorted(saved.items())), indent=0, ensure_ascii=False) + "\n")
            print(f"  pre-checked {len(todo)} ({len(saved)} saved)", file=sys.stderr, flush=True)

    for ind, strata in INDUSTRIES.items():
        out_sites[ind], composition[ind] = [], {}
        for stname, st in strata.items():
            per_source = {}
            for spec in st["sources"]:
                elig = {}
                for c in loaded[spec]:
                    d = registrable(c["url"], ranks)
                    if not d:
                        continue
                    host, path = split(c["url"])
                    reason = None
                    if host != d or path:
                        reason = "listed site is a page or subdomain, not its own domain's homepage"
                    elif len(owners[d]) > 1:
                        reason = f"domain listed by {len(owners[d])} organizations in one source"
                    elif (d, ind) in strikes:
                        reason = f"struck: {strikes[(d, ind)]['reason']}"
                    elif d in seen and seen[d] != (ind, stname):
                        reason = f"domain already in {seen[d][0]}/{seen[d][1]}"
                    if reason:
                        exclusions.append({**c, "domain": d, "industry": ind, "stratum": stname, "reason": reason})
                        continue
                    elig.setdefault(d, {**c, "domain": d, "rank": ranks[d]})
                for d in elig:
                    seen.setdefault(d, (ind, stname))
                per_source[spec] = elig
            merged = {}
            for spec, elig in per_source.items():
                for d, c in elig.items():
                    m = merged.setdefault(d, {**c, "sources": []})
                    m["sources"].append(c["source"])
            composition[ind][stname] = {
                "sources": {spec: {"raw": len(loaded[spec]), "eligible": len(per_source[spec])}
                            for spec in st["sources"]},
                "eligible_union": len(merged),
            }
            chosen = []

            def accept(c, role):
                if ind == "fintech" and not any(x.startswith(FINTECH_SOURCES) for x in c["sources"]):
                    f = founded.get(c["domain"])
                    if f is None:
                        raise SystemExit(f"founded.json needs {c['domain']} ({c['name']}): "
                                         "chart-only fintech candidate reached")
                    if f["year"] < FINTECH_MIN_FOUNDED:
                        exclusions.append({k: c[k] for k in ("name", "url", "domain", "source")} |
                                          {"industry": ind, "stratum": stname, "while": role,
                                           "reason": f"traditional financial institution: only in the Finance chart, "
                                                     f"founded {f['year']} ({f['source']})"})
                        return False
                reason, info = checked[c["domain"]]
                if reason:
                    exclusions.append({k: c[k] for k in ("name", "url", "domain", "source")} |
                                      {"industry": ind, "stratum": stname, "reason": reason, "while": role})
                    return False
                chosen.append({**c, **info, "industry": ind, "stratum": stname, "role": role})
                return True

            # Leaders: best Tranco rank in the merged pool.
            by_rank = sorted(merged.values(), key=lambda x: (x["rank"], x["domain"]))
            i = 0
            while sum(x["role"] == "leader" for x in chosen) < st["leaders"] and i < len(by_rank):
                check(by_rank[i:i + 8])
                for c in by_rank[i:i + 8]:
                    if sum(x["role"] == "leader" for x in chosen) >= st["leaders"]:
                        break
                    accept(c, "leader")
                i += 8
            # Sample: source-balanced round robin over seeded shuffles.
            queues = {}
            for spec, elig in per_source.items():
                # A fixed per-domain key, so adding or striking one candidate never reorders the others.
                key = lambda d: hashlib.sha256(f"{SEED}-{ind}-{stname}-{spec}-{d}".encode()).hexdigest()
                queues[spec] = sorted(elig, key=key)
            taken = {x["domain"] for x in chosen}
            while sum(x["role"] == "sample" for x in chosen) < st["sample"] and any(queues.values()):
                for spec in st["sources"]:
                    if sum(x["role"] == "sample" for x in chosen) >= st["sample"]:
                        break
                    q = queues[spec]
                    check([merged[d] for d in q[:8] if d not in taken])
                    while q:
                        d = q.pop(0)
                        if d in taken:
                            continue
                        c = merged[d]
                        check([merged[x] for x in [d] + q[:7] if x not in taken])
                        taken.add(d)
                        if accept({**c, "drawn_from": spec}, "sample"):
                            break
            composition[ind][stname]["chosen_by_source"] = dict(Counter(
                x.get("drawn_from", "rank") for x in chosen))
            out_sites[ind] += chosen
            print(f"{ind}/{stname}: {len(chosen)} chosen of {len(merged)} eligible", file=sys.stderr)

    out = {
        "protocol": PROTOCOL,
        "selected": time.strftime("%Y-%m-%d"),
        "seed": SEED,
        "tranco": TRANCO_ID,
        "sources": {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(SOURCES.iterdir())
                    if f.is_file()},
        "composition": composition,
        "sites": out_sites,
        "exclusions": list({(e["domain"], e["industry"], e["reason"]): e for e in exclusions}.values()),
    }
    pre_file.write_text(json.dumps(dict(sorted(saved.items())), indent=0, ensure_ascii=False) + "\n")
    (HERE / "proposed-sites.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
