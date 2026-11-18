#!/usr/bin/env python3
"""Run lab experiments: build a brief with a model, with or without the tasteskills skills.

Usage:
  python3 lab/run.py                                    the baseline matrix (skips runs that exist)
  python3 lab/run.py --briefs tallyroll --conditions B --models claude-sonnet-5-5 --runs 1

Conditions:
  A  no skills: the model gets the brief in an empty project
  B  skills: find-font and find-color are installed in the project, and the prompt asks for them

Both conditions get the same prompt, the same tools and an empty project with personal settings, plugins and
skills off. Each run is saved as runs/<brief>/<condition>/<model>-<n>/ with index.html (the page), notes.md
(everything the model said besides the page) and meta.json (prompt, model, repo commit, timing).
Standard library only.
"""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LAB = Path(__file__).resolve().parent
REPO = LAB.parent
SKILLS = {"find-font": REPO / "typography" / "skills" / "find-font",
          "find-color": REPO / "color" / "skills" / "find-color"}
MODELS = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]
BASE = ("Build the website described in this brief. Reply with the complete page as a single HTML file in one "
        "code block, then at most five short lines on your main design decisions.")
USE_SKILLS = (" Before building, use the find-font skill to choose the typography and the find-color skill to "
              "choose the colors, and build with what they return.")
TOOLS = ["Read", "Glob", "Grep", "Bash(python3:*)", "Bash(node:*)"]


def prompt(brief_text, condition):
    return BASE + (USE_SKILLS if condition == "B" else "") + "\n\n" + brief_text


def split_reply(text):
    blocks = list(re.finditer(r"```(?:html)?\s*\n(.*?)```", text, re.S))
    if not blocks:
        return "", text
    page = max(blocks, key=lambda m: len(m.group(1)))
    return page.group(1), (text[:page.start()] + text[page.end():]).strip()


def run_one(brief, condition, model, n):
    out = LAB / "runs" / brief / condition / f"{model}-{n}"
    if (out / "index.html").exists():
        return f"skip {out.relative_to(LAB)}"
    text = (LAB / "briefs" / f"{brief}.md").read_text()
    p = prompt(text, condition)
    cmd = ["claude", "-p", p, "--model", model, "--setting-sources", "project", "--strict-mcp-config",
           "--allowedTools", *TOOLS]
    started = time.time()
    with tempfile.TemporaryDirectory() as project:
        if condition == "B":
            for name, src in SKILLS.items():
                shutil.copytree(src, Path(project) / ".claude" / "skills" / name)
        res = subprocess.run(cmd, cwd=project, capture_output=True, text=True, timeout=1800)
    page, notes = split_reply(res.stdout)
    if res.returncode != 0 or not page:
        return f"FAIL {out.relative_to(LAB)} (exit {res.returncode}) {res.stderr[:200]}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    (out / "notes.md").write_text(notes + "\n")
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip()
    meta = {"brief": brief, "condition": condition, "model": model, "run": n, "repo_commit": commit,
            "prompt": p, "tools": TOOLS, "seconds": round(time.time() - started),
            "date": time.strftime("%Y-%m-%d")}
    (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    return f"ok   {out.relative_to(LAB)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--briefs", default="tallyroll,fennel-street")
    ap.add_argument("--conditions", default="A,B")
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    jobs = [(b, c, m, n) for b in args.briefs.split(",") for c in args.conditions.split(",")
            for m in args.models.split(",") for n in range(1, args.runs + 1)]
    print(f"{len(jobs)} runs", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for line in pool.map(lambda j: run_one(*j), jobs):
            print(line, flush=True)


if __name__ == "__main__":
    main()
