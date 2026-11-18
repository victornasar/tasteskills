#!/usr/bin/env python3
"""find-font engine: filter, rank and pair fonts from the tasteskills typography catalog.

The agent reads the brief into roles, feel tags and constraints. This script does the rest, so the same
input always gives the same picks.

Usage:
  find_font.py recommend --role headlines --role body --feel warm [--feel literary]
                         [--script latin-ext] [--public-repo] [--replaces Inter]
                         [--category mono] [--exclude id,id] [--count 3]
  find_font.py vocab                 the feel and use tags, with what they mean
  find_font.py get <id>              one font's full record
  find_font.py avoid [<name>]        the avoid list, or one entry with its replacements

Output is JSON. The catalog is catalog.json next to this folder (a generated copy of typography/fonts.json).
Standard library only, Python 3.8+.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "catalog.json"
VOICE = {"loud", "experimental", "playful"}
PAIR_DEPTH = 8  # how many ranked candidates per role the pairing step considers
FALLBACK = {
    "sans": 'system-ui, -apple-system, "Segoe UI", sans-serif',
    "serif": 'Georgia, "Times New Roman", serif',
    "mono": 'ui-monospace, "SF Mono", Menlo, Consolas, monospace',
}


def load(path=CATALOG):
    return json.loads(Path(path).read_text())


# --- filter -------------------------------------------------------------------------------------------

def passes(font, role, scripts, category=None):
    """AGENTS.md step 2: the hard requirements for a font to fill a role."""
    if role not in font["use"]:
        return False
    if not set(scripts) <= set(font["scripts"]):
        return False
    if role == "body" and not (font["italics"] and len(font["weights"]) >= 2):
        return False
    if role == "ui" and len(font["weights"]) < 3:
        return False
    if category and font["category"] != category:
        return False
    return True


def candidates(data, role, scripts=(), category=None, exclude=(), public_repo=False):
    """Fonts that can fill the role. With a public repo, Fontshare (FFL) fonts drop out while any OFL font
    remains, because FFL files can't be committed to a public repository."""
    found = [f for f in data["fonts"] if f["id"] not in exclude and passes(f, role, scripts, category)]
    if public_repo and any(f["license"] == "OFL" for f in found):
        found = [f for f in found if f["license"] == "OFL"]
    return found


# --- rank ---------------------------------------------------------------------------------------------

def score(font, role, feels, boost=()):
    """Higher is better. Feel comes first: it's what makes picks follow the brief instead of converging on
    the fonts that fit every role. Use fit refines within a feel."""
    s, why = 0.0, []
    primary = feels[0] if feels else None
    secondary = feels[1] if len(feels) > 1 else None
    if primary:
        if font["feel"][0] == primary:
            s += 4
            why.append(f"'{primary}' is its main feel")
        elif primary in font["feel"]:
            s += 3
            why.append(f"also reads '{primary}'")
    if secondary and secondary in font["feel"]:
        s += 1.5 if font["feel"][0] == secondary else 1
        why.append(f"shares the secondary feel '{secondary}'")
    rank = font["use"].index(role)
    s += (2.5, 1, 0.5)[rank]
    why.append(f"'{role}' is its {('first', 'second', 'third')[rank]} use")
    if font["id"] in boost:
        s += 10
        why.insert(0, "listed as a replacement for the font being replaced")
    return s, why


def tiebreak(font, key):
    """Fonts with equal scores are equally good fits. Order them by a hash of the brief, so different briefs
    don't all get the catalog's first font while the same brief always gets the same order."""
    return hashlib.sha256(f"{key}|{font['id']}".encode()).hexdigest()


def rank(data, role, feels, scripts=(), category=None, exclude=(), public_repo=False, boost=()):
    key = "|".join([role, *feels, *scripts])
    rows = []
    for f in candidates(data, role, scripts, category, exclude, public_repo):
        s, why = score(f, role, feels, boost)
        rows.append((s, f, why))
    rows.sort(key=lambda r: (-r[0], tiebreak(r[1], key)))
    return rows


# --- pair ---------------------------------------------------------------------------------------------

def pair_rules(a, b):
    """AGENTS.md step 4. Returns the rules the pair bends; empty means it follows all of them."""
    bent = []
    same_family = a["id"] == b["id"]
    if same_family and len(a["weights"]) < 5:
        bent.append("one family needs a wide weight range (5+) to pair with itself")
    if not same_family and a["category"] == b["category"]:
        bent.append(f"contrast: both are {a['category']}")
    if not (set(a["feel"]) & set(b["feel"]) or "neutral" in a["feel"] + b["feel"]):
        bent.append("share a feel: no feel in common and neither is neutral")
    if not same_family and sum(bool(set(f["feel"]) & VOICE) for f in (a, b)) > 1:
        bent.append("one voice: both are loud, experimental or playful")
    return bent


def best_pair(ranked_a, ranked_b):
    """Highest combined score among pairs that follow every rule; if none do, the one bending fewest."""
    best = None
    for i, (sa, fa, _) in enumerate(ranked_a[:PAIR_DEPTH]):
        for j, (sb, fb, _) in enumerate(ranked_b[:PAIR_DEPTH]):
            bent = pair_rules(fa, fb)
            same = fa["id"] == fb["id"]  # allowed, but contrast wins when the fit is otherwise equal
            key = (len(bent), -(sa + sb) + (0.5 if same else 0), i + j)
            if best is None or key < best[0]:
                best = (key, fa, fb, bent)
    return best


# --- output -------------------------------------------------------------------------------------------

def stack(font):
    base = FALLBACK.get(font["category"])
    if base is None:  # display faces: the stack follows their letter shapes, which the agent should check
        base = FALLBACK["serif"] if font["feel"][0] in ("elegant", "literary") else FALLBACK["sans"]
    return f'"{font["name"].split(" / ")[0]}", {base}'


def font_face(font):
    name = font["name"].split(" / ")[0]
    ws = font["weights"]
    weight = f"{ws[0]} {ws[-1]}" if font["variable"] and len(ws) > 1 else str(ws[0] if len(ws) == 1 else 400)
    return (f'@font-face {{\n  font-family: "{name}";\n  src: url("./fonts/{name.replace(" ", "")}.woff2") format("woff2");\n'
            f"  font-weight: {weight};\n  font-style: normal;\n  font-display: swap;\n}}")


def describe(font, why):
    keys = ("id", "name", "category", "license", "url", "feel", "use", "weights", "italics", "variable",
            "scripts", "caveats", "note")
    out = {k: font.get(k) for k in keys}
    out["why"] = why
    if font["license"] == "FFL":
        out["license_note"] = "Fontshare: self-host only, keep files out of public repos."
    if font.get("review"):
        out["review"] = "tags not yet reviewed by a human"
    return out


def recommend(data, roles, feels, scripts=(), public_repo=False, replaces=None, category=None,
              exclude=(), count=3):
    notes = []
    boost = ()
    if replaces:
        entry = next((a for a in data["avoid"] if a["name"].lower() == replaces.lower()), None)
        if entry:
            boost = tuple(entry["instead"])
        else:
            notes.append(f"'{replaces}' is not on the avoid list; no replacement preference applied.")

    ranked = {}
    for i, role in enumerate(roles):
        ranked[role] = rank(data, role, feels, scripts, category, exclude, public_repo,
                            boost if i == 0 else ())
        if not ranked[role]:
            notes.append(f"No catalog font fits '{role}' with these constraints. Say so; at most one outside "
                         "font, marked outside the catalog, license unverified.")
        if public_repo and any(f["license"] == "FFL" for f in data["fonts"] if passes(f, role, scripts, category)):
            notes.append(f"{role}: Fontshare (FFL) fonts left out because the repo is public.")
        if feels and ranked[role] and not set(feels) & set(ranked[role][0][1]["feel"]):
            notes.append(f"{role}: no font that fits shares the feel {feels}; the picks are the best use fit. "
                         "Say so.")
        if boost and i == 0 and ranked[role] and ranked[role][0][1]["id"] not in boost:
            notes.append(f"None of {replaces}'s listed replacements fit '{role}' here.")

    pair = None
    text_roles = [r for r in roles if r != "code" and ranked[r]]
    if len(text_roles) >= 2:
        a, b = text_roles[:2]
        found = best_pair(ranked[a], ranked[b])
        if found:
            _, fa, fb, bent = found
            for role, font in ((a, fa), (b, fb)):
                ranked[role].sort(key=lambda r: r[1]["id"] != font["id"])  # stable: pair font first
            pair = {"roles": [a, b], "ids": [fa["id"], fb["id"]], "bends": bent}
            if bent:
                notes.append("The top pair bends: " + "; ".join(bent) + ". Say which rule and why.")
    if "code" in roles and ranked["code"] and text_roles:
        tops = [ranked[r][0][1] for r in text_roles]
        feels_of_pair = {t for f in tops for t in f["feel"]}
        ranked["code"].sort(key=lambda r: not (set(r[1]["feel"]) & feels_of_pair or "neutral" in r[1]["feel"]))

    out_roles = []
    for role in roles:
        rows = ranked[role][:count]
        out_roles.append({
            "role": role,
            "candidates": len(ranked[role]),
            "picks": [describe(f, why) for _, f, why in rows],
        })
    top = {r["role"]: r["picks"][0] for r in out_roles if r["picks"]}
    css = {role: {"font_family": stack(next(f for f in data["fonts"] if f["id"] == p["id"])),
                  "font_face": font_face(next(f for f in data["fonts"] if f["id"] == p["id"]))}
           for role, p in top.items()}
    return {
        "input": {"roles": roles, "feel": feels, "scripts": list(scripts), "public_repo": public_repo,
                  "replaces": replaces, "category": category, "exclude": list(exclude)},
        "roles": out_roles,
        "pair": pair,
        "css": css,
        "notes": notes,
        "picks": {"picks": [{"role": r["role"], "ids": [p["id"] for p in r["picks"]]} for r in out_roles]},
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Pick fonts from the tasteskills catalog.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    rec = sub.add_parser("recommend")
    rec.add_argument("--role", action="append", required=True, help="a use tag; repeat for each role")
    rec.add_argument("--feel", action="append", default=[], help="a feel tag; primary first, at most two")
    rec.add_argument("--script", action="append", default=[], help="a scripts tag the text needs")
    rec.add_argument("--public-repo", action="store_true", help="font files will live in a public repo")
    rec.add_argument("--replaces", help="an avoid-list font the project uses now")
    rec.add_argument("--category", help="restrict to sans, serif, display or mono")
    rec.add_argument("--exclude", default="", help="comma-separated ids already shown")
    rec.add_argument("--count", type=int, default=3)
    sub.add_parser("vocab")
    g = sub.add_parser("get")
    g.add_argument("id")
    av = sub.add_parser("avoid")
    av.add_argument("name", nargs="?")
    args = ap.parse_args(argv)

    data = load()
    vocab = data["vocab"]
    if args.cmd == "vocab":
        result = {"feel": vocab["feel"], "use": vocab["use"], "category": vocab["category"]}
    elif args.cmd == "get":
        result = next((f for f in data["fonts"] if f["id"] == args.id), None)
        if result is None:
            sys.exit(f"unknown font id '{args.id}'")
    elif args.cmd == "avoid":
        rows = data["avoid"]
        if args.name:
            rows = [a for a in rows if a["name"].lower() == args.name.lower()]
            if not rows:
                sys.exit(f"'{args.name}' is not on the avoid list")
        result = rows
    else:
        bad = [r for r in args.role if r not in vocab["use"]] + [f for f in args.feel if f not in vocab["feel"]]
        if bad:
            sys.exit(f"unknown tags {bad}; run `vocab` for the list")
        if len(args.feel) > 2:
            sys.exit("give at most two --feel tags, primary first")
        result = recommend(data, args.role, args.feel, args.script, args.public_repo, args.replaces,
                           args.category, [x for x in args.exclude.split(",") if x], args.count)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
