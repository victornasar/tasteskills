#!/usr/bin/env python3
"""Split sources/ into what may be deposited (Zenodo, restricted access) and what stays withheld, and write the
manifest. Nothing is uploaded here.

Usage:
  python3 lab/industry-type/archive.py OUT_DIR

Writes OUT_DIR/deposit/ (files that may be deposited, plus factual extracts of withheld sources),
OUT_DIR/private/ (what is retained privately: raw files whose terms allow a private research copy, and
PROVENANCE.md with retrieval details for every withheld source), OUT_DIR/industry-type-deposit-<date>.tar.gz,
and archive-manifest.json next to this script (committed): every file's SHA-256, source, license or terms,
retrieval details, and whether it was deposited or retained and why.

The extracts hold every field the selector reads, so deposit + the Tranco list (re-downloadable by id) rebuild
every candidate pool; main() checks this before writing anything. Standard library only.
"""
import csv
import hashlib
import io
import json
import re
import shutil
import sys
import tarfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources"

# Audit of each source: (filename pattern, source, license or terms, deposit?, reason, private raw copy?).
# A private raw copy is kept only where the source is published for research download (Tranco); otherwise the raw
# file stays out of every archive and only its checksum, retrieval details and factual extract are kept.
AUDIT = [
    (r"^wikidata-.*\.json$", "Wikidata SPARQL results", "CC0 1.0 (Wikidata structured data)", True,
     "public-domain dedication; redistribution allowed", False),
    (r"^wplist-.*\.json$", "Wikipedia list pages resolved to Wikidata entities",
     "Wikidata entity data CC0 1.0; list membership taken from English Wikipedia (CC BY-SA 4.0), attributed in the "
     "manifest", True, "contains only Wikidata claims and labels plus the list's title and link count", False),
    (r"^tranco-.*\.csv$", "Tranco research ranking, list V38GN",
     "Composite of Cisco Umbrella (free of charge, no stated license), Majestic (CC BY 3.0), Farsight "
     "(proprietary), Chrome UX Report (CC BY-SA 4.0) and Cloudflare Radar (CC BY-NC 4.0)", False,
     "mixed and partly proprietary terms; the frozen list stays downloadable by its id, so the id and checksum "
     "suffice", True),
    (r"^yc-all\.json$", "yc-oss.github.io mirror of the Y Combinator company directory",
     "No license on the mirror; content is Y Combinator's directory (its site terms)", False,
     "third-party content without a redistribution grant; no license, so no grant to retain a copy either", False),
    (r"^appstore-.*\.json$", "Apple App Store RSS charts and iTunes lookup API responses",
     "Apple Media Services terms; includes app descriptions and artwork links owned by developers", False,
     "API responses with copyrighted descriptions; no redistribution grant", False),
    (r"^altagamma-members\.html$", "Altagamma members web page", "Copyright Altagamma (all rights reserved)", False,
     "a copyrighted web page", False),
    (r"^michelin\.csv$", "ngshiheng/michelin-my-maps dataset",
     "Repository is MIT, but the rows (including review text) are scraped from the Michelin Guide, whose "
     "content is Michelin's", False, "the MIT grant can't cover Michelin's review text", False),
]

# How each withheld source was retrieved (dates are the cache files' write times, Pacific).
RETRIEVAL = {
    "tranco-V38GN.csv": ("https://tranco-list.eu/download_daily/V38GN (top-1m.csv inside the zip)", "2026-11-18T15:20:30-08:00",
                         "list id V38GN; re-download: https://tranco-list.eu/list/V38GN"),
    "yc-all.json": ("https://yc-oss.github.io/api/companies/all.json", "2026-11-18T15:20:31-08:00",
                    "full directory; the selector keeps status Active or Public with a website and a matching industry"),
    "appstore-all.json": ("https://itunes.apple.com/us/rss/{topfreeapplications,toppaidapplications}/limit=100/json, "
                          "then https://itunes.apple.com/lookup?id=...", "2026-11-18T16:30:49-08:00",
                          "US store, all genres, top 100 free + top 100 paid"),
    "appstore-dev.json": ("same endpoints with /genre=6026", "2026-11-18T16:08:48-08:00", "US store, Developer Tools"),
    "appstore-finance.json": ("same endpoints with /genre=6015", "2026-11-18T16:08:58-08:00", "US store, Finance"),
    "appstore-health.json": ("same endpoints with /genre=6020", "2026-11-18T17:18:43-08:00", "US store, Medical"),
    "altagamma-members.html": ("https://altagamma.it/en/members/", "2026-11-18T16:09:15-08:00",
                               "one GET with User-Agent Mozilla/5.0"),
    "michelin.csv": ("https://raw.githubusercontent.com/ngshiheng/michelin-my-maps/main/data/michelin_my_maps.csv",
                     "2026-11-18T16:09:16-08:00", "main branch at retrieval time"),
}

# Withheld sources get a factual extract: identifiers, names and URLs only, no descriptive text or artwork.
def extract(name, data):
    if name == "yc-all.json":
        return [{"slug": c["slug"], "name": c["name"], "website": c.get("website"), "status": c.get("status"),
                 "industries": c.get("industries")} for c in json.loads(data)]
    if name.startswith("appstore-"):
        return [{"trackId": a.get("trackId"), "sellerName": a.get("sellerName"), "artistName": a.get("artistName"),
                 "sellerUrl": a.get("sellerUrl"), "primaryGenreId": a.get("primaryGenreId")} for a in json.loads(data)]
    if name == "altagamma-members.html":
        return sorted(set(re.findall(r'href="(https?://[^"]+)"', data.decode("utf-8", "replace"))))
    if name == "michelin.csv":
        rows = csv.DictReader(io.StringIO(data.decode("utf-8")))
        return [{"name": r["Name"], "guideUrl": r["Url"], "websiteUrl": r["WebsiteUrl"]} for r in rows]
    return None


def as_raw(name, ex):
    """Rebuild a withheld file's selector-readable form from its extract (for the reproducibility check)."""
    if name == "yc-all.json":
        return json.dumps(ex).encode()
    if name.startswith("appstore-"):
        return json.dumps(ex).encode()
    if name == "altagamma-members.html":
        return "".join(f'<a href="{u}"></a>' for u in ex).encode()
    if name == "michelin.csv":
        buf = io.StringIO()
        w = csv.DictWriter(buf, ["Name", "Url", "WebsiteUrl"])
        w.writeheader()
        w.writerows({"Name": r["name"], "Url": r["guideUrl"], "WebsiteUrl": r["websiteUrl"]} for r in ex)
        return buf.getvalue().encode()


def check_extracts_reproduce(extracts):
    """Every withheld source's extract must give the selector exactly the entries the raw file gives."""
    sys.path.insert(0, str(HERE))
    import pick_sites as ps
    real_cached = ps.cached
    files = {"yc": lambda a: "yc-all.json", "appstore": lambda a: f"appstore-{a}.json",
             "altagamma": lambda a: "altagamma-members.html", "michelin": lambda a: "michelin.csv"}
    specs = {s for strata in ps.INDUSTRIES.values() for st in strata.values() for s in st["sources"]}
    for spec in sorted(specs):
        kind, _, arg = spec.partition(":")
        if kind not in files:
            continue
        name = files[kind](arg)
        ps.cached = real_cached
        raw = ps.FETCH[kind](arg, True)
        ps.cached = lambda n, f, o, name=name: as_raw(name, extracts[name]) if n == name else real_cached(n, f, o)
        if ps.FETCH[kind](arg, True) != raw:
            raise SystemExit(f"extract of {name} does not reproduce the selector's entries for {spec}")
    ps.cached = real_cached


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    out = Path(sys.argv[1]).resolve()
    dep, priv = out / "deposit", out / "private"
    for d in (dep / "sources", dep / "extracts", priv):
        d.mkdir(parents=True, exist_ok=True)
    files, extracts, prov = [], {}, []
    for f in sorted(SOURCES.iterdir()):
        data = f.read_bytes()
        rule = next((a for a in AUDIT if re.match(a[0], f.name)), None)
        if rule is None:
            raise SystemExit(f"no audit entry for {f.name}")
        _, source, terms, ok, why, keep = rule
        entry = {"file": f.name, "sha256": sha(data), "bytes": len(data), "source": source, "terms": terms,
                 "deposited": ok, "why": why, "private_raw_copy": keep}
        if ok:
            shutil.copy2(f, dep / "sources" / f.name)
        else:
            url, when, params = RETRIEVAL[f.name]
            entry["retrieval"] = {"url": url, "retrieved": when, "parameters": params}
            prov.append((f.name, url, when, params, entry["sha256"], len(data), keep))
            if keep:
                shutil.copy2(f, priv / f.name)
            ex = extract(f.name, data)
            extracts[f.name] = ex
            if ex is not None:
                ename = f.name.rsplit(".", 1)[0] + ".extract.json"
                eb = (json.dumps(ex, ensure_ascii=False, indent=0) + "\n").encode()
                (dep / "extracts" / ename).write_bytes(eb)
                entry["extract"] = {"file": ename, "sha256": sha(eb), "fields": "identifiers, names and URLs only"}
        files.append(entry)
    check_extracts_reproduce(extracts)
    outputs = ("proposed-sites.json", "proposed-sites.v1.json", "strikes.json", "founded.json", "prechecks.json",
               "rated-subset.json", "pick_sites.py", "draw_ratings.py", "methodology.md")
    for name in outputs:
        shutil.copy2(HERE / name, dep / name)
    stamp = time.strftime("%Y-%m-%d")
    manifest = {
        "study": "tasteskills lab/industry-type",
        "built": stamp,
        "access": "Zenodo, restricted file access (metadata public, files on request)",
        "attribution": "Wikidata (CC0). Wikipedia list membership from 'List of architecture firms', 'List of "
                       "magazines by circulation', 'List of newspapers by circulation' (English Wikipedia, CC BY-SA 4.0).",
        "files": files,
        "extracts_reproduce_selection": True,
        "selection_outputs": {n: sha((dep / n).read_bytes()) for n in outputs},
    }
    (dep / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    tar = out / f"industry-type-deposit-{stamp}.tar.gz"
    with tarfile.open(tar, "w:gz") as t:
        t.add(dep, arcname="industry-type-deposit")
    manifest["deposit_archive"] = {"file": tar.name, "sha256": sha(tar.read_bytes()), "bytes": tar.stat().st_size}
    (HERE / "archive-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    lines = ["# Withheld sources: provenance", "",
             "Not deposited (see archive-manifest.json for each source's terms). A raw copy is kept here only where",
             "noted; otherwise the raw file is held in no archive, and its checksum, retrieval details and the factual",
             "extract in the Zenodo deposit are what remain. The extracts hold every field the selector reads, checked",
             f"by archive.py on {stamp}. Deposit archive: {tar.name}, SHA-256 {manifest['deposit_archive']['sha256']}.", ""]
    for name, url, when, params, digest, size, keep in prov:
        lines += [f"## {name}", "", f"- Retrieved: {when}", f"- From: {url}", f"- Parameters: {params}",
                  f"- SHA-256: `{digest}` ({size:,} bytes)",
                  f"- Raw copy here: {'yes' if keep else 'no (terms give no grant to retain one)'}", ""]
    (priv / "PROVENANCE.md").write_text("\n".join(lines))
    (priv / "archive-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    kept = sum(e["deposited"] for e in files)
    print(f"{kept} files deposit, {len(files) - kept} withheld (extracts reproduce selection); "
          f"{tar.name} {manifest['deposit_archive']['sha256']}")


if __name__ == "__main__":
    main()
