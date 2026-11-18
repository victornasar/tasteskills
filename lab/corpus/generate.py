#!/usr/bin/env python3
"""Generate the corpus: generic website briefs built by AI models with no skills and no personal settings.

Usage:
  python3 lab/corpus/generate.py                         every model, every prompt (skips files that exist)
  python3 lab/corpus/generate.py --models claude-haiku-5-5 --workers 4

Each site is saved as sites/<model>/<NN>-<slug>.html. Prompts are the 30 used by
typography/scripts/measure_slop.py, so the font measurement and the corpus agree. Standard library only.
"""
import argparse
import json
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Fable 5.2 was planned too, but needs paid usage credits on the account that ran the corpus.
MODELS = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]
SITES = {
    "landing page": ["a meal-kit startup", "a B2B invoicing SaaS", "an AI note-taking app",
                     "a climate-tech nonprofit", "a mobile banking app"],
    "portfolio site": ["a product designer", "a wedding photographer", "a freelance developer",
                       "an architecture studio", "an illustrator"],
    "blog": ["a personal tech blog", "a travel writer", "a food blog",
             "a company engineering blog", "a parenting newsletter"],
    "dashboard": ["SaaS revenue analytics", "server monitoring", "a CRM pipeline",
                  "a personal finance tracker", "warehouse inventory"],
    "documentation site": ["a JavaScript library", "a public REST API", "a CLI tool",
                           "an internal design system", "a database product"],
    "online shop": ["a coffee roaster", "a sneaker brand", "a houseplant store",
                    "a skincare brand", "a bookshop"],
}
PROMPTS = [(kind, subject, f"Build a {kind} for {subject}. Reply with the complete page as a single HTML file in "
            "one code block, nothing else.") for kind, subjects in SITES.items() for subject in subjects]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def extract_html(text):
    blocks = re.findall(r"```(?:html)?\s*\n(.*?)```", text, re.S)
    html = max(blocks, key=len) if blocks else text
    # Models write example API keys into docs pages; redact anything key-shaped so pushes aren't blocked.
    html = re.sub(r"\b(sk|pk|rk)_(test|live)_[A-Za-z0-9]{10,}", r"\1_\2_EXAMPLE_KEY_REDACTED", html)
    return html if "<" in html else ""


def generate(model, prompt):
    cmd = ["claude", "-p", prompt, "--model", model, "--setting-sources", "project",
           "--disable-slash-commands", "--strict-mcp-config", "--tools", ""]
    with tempfile.TemporaryDirectory() as empty:
        res = subprocess.run(cmd, cwd=empty, capture_output=True, text=True, timeout=1200)
    if res.returncode != 0:
        print(f"  error ({model}): {(res.stderr or res.stdout).strip()[-200:]}", flush=True)
        return ""
    return extract_html(res.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    manifest = {f"{i:02d}": {"kind": k, "subject": s, "prompt": p} for i, (k, s, p) in enumerate(PROMPTS)}
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    jobs = []
    for model in args.models.split(","):
        out = HERE / "sites" / model
        out.mkdir(parents=True, exist_ok=True)
        for i, (kind, subject, prompt) in enumerate(PROMPTS):
            path = out / f"{i:02d}-{slug(kind)}-{slug(subject)}.html"
            if not path.exists():
                jobs.append((model, prompt, path))
    print(f"{len(jobs)} sites to generate", flush=True)

    def work(job):
        model, prompt, path = job
        html = generate(model, prompt)
        if html:
            path.write_text(html)
        print(("ok   " if html else "FAIL ") + str(path.relative_to(HERE)), flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(work, jobs))


if __name__ == "__main__":
    main()
