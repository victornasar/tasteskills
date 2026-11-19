#!/usr/bin/env python3
"""Write methodology.md: methodology.head.md + the proposed list, source composition and the change log
from protocol 1, all generated from proposed-sites.json. Standard library only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
v2 = json.loads((HERE / "proposed-sites.json").read_text())
v1 = json.loads((HERE / "proposed-sites.v1.json").read_text())
strikes = json.loads((HERE / "strikes.json").read_text())["strikes"]


def label(s):
    return s["name"] or "(no English label)"


def src(s):
    return "; ".join(s.get("sources", [s["source"]]))


import hashlib

head = (HERE / "methodology.head.md").read_text().rstrip()
head = head.replace("{{SITES_SHA}}", hashlib.sha256((HERE / "proposed-sites.json").read_bytes()).hexdigest())
rated = json.loads((HERE / "rated-subset.json").read_text())
rows = [f"**Drawn {rated['seed']!r}** (industries in draw order: {', '.join(rated['drawn_order'])}):", "",
        "| Industry | Leaders | Sampled | AI pages (model/run) |", "|---|---|---|---|"]
for ind, d in rated["industries"].items():
    rows.append(f"| `{ind}` | {', '.join(d['leaders'])} | {', '.join(d['sampled'])} | {', '.join(d['ai_pages'])} |")
head = head.replace("{{RATED_SUBSET}}", "\n".join(rows))
out = [head, "", "## Source composition", "",
       "Raw = entries the source returned. Eligible = after the Tranco, homepage, shared-domain, strike and "
       "earlier-industry rules. Chosen = sampled sites drawn from that source (leaders are drawn by rank from the "
       "union and listed as `rank`).", ""]
for ind, strata in v2["composition"].items():
    for st, c in strata.items():
        name = ind if st == "all" else f"{ind} / {st}"
        out += [f"**{name}** (eligible union {c['eligible_union']:,})", "", "| Source | Raw | Eligible | Sampled from it |",
                "|---|---|---|---|"]
        for spec, n in c["sources"].items():
            out.append(f"| {spec} | {n['raw']:,} | {n['eligible']:,} | {c['chosen_by_source'].get(spec, 0)} |")
        out += [f"| leaders (by rank) | | | {c['chosen_by_source'].get('rank', 0)} |", ""]

out += ["## 5. Proposed sites", "",
        f"Generated from `proposed-sites.json` (protocol `{v2['protocol']}`, seed `{v2['seed']}`, Tranco "
        f"`{v2['tranco']}`, {v2['selected']}). Leaders and sampled sites are separate strata. *Scripts* = writing "
        "systems in the homepage text (≥5% of letters); *lang* = the page's declared language.", ""]
total = 0
for ind, sites in v2["sites"].items():
    out += [f"### `{ind}`", ""]
    strata = list(dict.fromkeys(s["stratum"] for s in sites))
    for st in strata:
        rows = [s for s in sites if s["stratum"] == st]
        if st != "all":
            out += [f"**{st}**", ""]
        out += ["| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |", "|---|---|---|---|---|---|---|"]
        for role in ("leader", "sample"):
            for s in rows:
                if s["role"] == role:
                    total += 1
                    out.append(f"| {role} | {s['domain']} | {label(s)} | {s['rank']:,} | {s.get('lang') or '–'} | "
                               f"{', '.join(s.get('scripts', []))} | {src(s)} |")
        out.append("")
out.insert(out.index("## 5. Proposed sites") + 1, f"\n**{total} sites.**")

# Change log: every protocol-1 site and what happened to it.
now = {s["domain"]: (ind, s) for ind, sites in v2["sites"].items() for s in sites}
struck = {(s["domain"], s["industry"]): s for s in strikes}
excl = {}
for e in v2["exclusions"]:
    excl.setdefault(e["domain"], e["reason"])
out += ["### Changes from the first proposal", "",
        "Every site in `proposed-sites.v1.json` (protocol 1) and its status under protocol 2. Sites new in "
        "protocol 2 are the ones above that don't appear here as kept.", "",
        "| Protocol 1 | Site | Status under protocol 2 |", "|---|---|---|"]
for ind, sites in v1["sites"].items():
    for s in sites:
        d = s["domain"]
        if (d, ind) in struck:
            status = f"**struck**: {struck[(d, ind)]['reason']} (asked by {struck[(d, ind)]['requested_by']})"
        elif d in now:
            ind2, s2 = now[d]
            status = f"kept: {ind2} {s2['role']}" + ("" if ind2 == ind else " (moved industry)")
        elif d in excl:
            status = f"not selected: {excl[d]}"
        elif s["role"] == "leader":
            status = "no longer a leader: new sources added higher-ranked sites"
        else:
            status = "not drawn: new sources and source-balanced sampling changed the pool and the draw"
        out.append(f"| {ind} {s['role']} | {d} | {status} |")
out.append("")
(HERE / "methodology.md").write_text("\n".join(out))
print(f"wrote methodology.md ({total} sites)")
