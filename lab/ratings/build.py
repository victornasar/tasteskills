#!/usr/bin/env python3
"""Build the blind rating page from lab runs, and score the votes against the key.

Usage:
  python3 lab/ratings/build.py pairs            list the screenshots to upload (writes uploads.json stubs)
  python3 lab/ratings/build.py page             write page.html from page.template.html + uploads.json
  python3 lab/ratings/build.py score votes.json score exported votes → results.md

A pair is the condition A run and the condition B run with the same brief, model and run number. Left/right
and the order of pairs are shuffled with a fixed seed. The page only ever says "left" and "right"; key.json
(kept in the repo, never in the page) says which side was which condition. Standard library only.
"""
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / "runs"
SHOTS = RUNS / "shots"
SEED = 20261117


def pairs():
    found = []
    for a in sorted(RUNS.glob("*/A/*/index.html")):
        brief, run = a.parts[-4], a.parts[-2]
        b = RUNS / brief / "B" / run / "index.html"
        if not b.exists():
            continue
        shots = {c: {"fold": SHOTS / brief / c / run / "index.jpg", "full": SHOTS / brief / c / run / "index-full.jpg"}
                 for c in ("A", "B")}
        if all(p.exists() for s in shots.values() for p in s.values()):
            model, n = run.rsplit("-", 1)
            found.append({"brief": brief, "model": model, "run": int(n), "shots": shots})
    rng = random.Random(SEED)
    rng.shuffle(found)
    for i, p in enumerate(found, 1):
        p["id"] = f"p{i:02d}"
        p["left"] = rng.choice("AB")
        p["right"] = "B" if p["left"] == "A" else "A"
    return found


def cmd_pairs():
    ps = pairs()
    uploads_file = HERE / "uploads.json"
    uploads = json.loads(uploads_file.read_text()) if uploads_file.exists() else {}
    files = [str(path.relative_to(HERE.parent)) for p in ps for s in p["shots"].values() for path in s.values()]
    for f in files:
        uploads.setdefault(f, None)
    uploads_file.write_text(json.dumps(uploads, indent=2) + "\n")
    key = {p["id"]: {"brief": p["brief"], "model": p["model"], "run": p["run"], "left": p["left"], "right": p["right"]}
           for p in ps}
    (HERE / "key.json").write_text(json.dumps(key, indent=2) + "\n")
    print(f"{len(ps)} pairs, {len(files)} screenshots. Missing uploads: {sum(v is None for v in uploads.values())}")
    for f in files:
        if uploads[f] is None:
            print(f)


def cmd_page():
    uploads = json.loads((HERE / "uploads.json").read_text())
    data = []
    for p in pairs():
        url = lambda c, kind: uploads[str(p["shots"][c][kind].relative_to(HERE.parent))]
        data.append({"id": p["id"], "brief": p["brief"],
                     "left": {"fold": url(p["left"], "fold"), "full": url(p["left"], "full")},
                     "right": {"fold": url(p["right"], "fold"), "full": url(p["right"], "full")}})
    missing = [d["id"] for d in data if None in (d["left"]["fold"], d["left"]["full"], d["right"]["fold"], d["right"]["full"])]
    if missing:
        sys.exit(f"screenshots not uploaded yet for {missing}; run `pairs` and upload them first")
    page = (HERE / "page.template.html").read_text().replace("/*PAIRS*/[]", json.dumps(data))
    (HERE / "page.html").write_text(page)
    print(f"page.html: {len(data)} pairs")


def cmd_score(path):
    """votes.json: the `votes` collection exported from the page, one document per rater."""
    key = json.loads((HERE / "key.json").read_text())
    docs = json.loads(Path(path).read_text())
    docs = docs if isinstance(docs, list) else docs.get("documents", [])
    tally = defaultdict(Counter)
    notes = defaultdict(list)
    raters = 0
    for d in docs:
        votes = (d.get("data") or d).get("votes", {})
        raters += bool(votes)
        for pid, v in votes.items():
            k = key.get(pid)
            if not k:
                continue
            winner = "tie" if v["choice"] == "tie" else k[v["choice"]]
            for group in ("all", k["model"], k["brief"]):
                tally[group][winner] += 1
            if v.get("note"):
                loser = {"A": "B", "B": "A"}.get(winner, "either")
                notes[loser].append(f"{k['brief']} / {k['model']}: {v['note']}")
    lines = ["# Blind ratings: results", "", f"{raters} raters. A = no skills, B = find-font + find-color.", "",
             "| Group | B preferred | A preferred | Can't separate | Votes |", "|---|---|---|---|---|"]
    for group, c in sorted(tally.items(), key=lambda kv: kv[0] != "all"):
        n = sum(c.values())
        lines.append(f"| {group} | {c['B']} ({c['B'] / n:.0%}) | {c['A']} ({c['A'] / n:.0%}) | {c['tie']} | {n} |")
    for side in ("A", "B", "either"):
        if notes[side]:
            lines += ["", f"## What raters said was wrong with {side}", ""] + [f"- {n}" for n in notes[side]]
    (HERE / "results.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("pairs", "page", "score"):
        sys.exit(__doc__)
    {"pairs": cmd_pairs, "page": cmd_page, "score": lambda: cmd_score(sys.argv[2])}[sys.argv[1]]()
