# lab

Experiments on whole-page design quality.

The color and typography skills pick better parts. The lab asks the bigger question: **what actually moves an
AI agent from an acceptable website to a distinctive one, and how much of that is the model versus the tools
and process around it?**

**Status:** a 90-site corpus of AI defaults is measured; 54 runs across three conditions (no skills, font and
color skills, plus check-layout) are measured automatically; blind human ratings are open. Results so far are in
[`findings.md`](findings.md).

## What's here

| Path | What it is |
| --- | --- |
| [`findings.md`](findings.md) | What the lab has found, with evidence and limits. Start here |
| [`corpus/`](corpus/) | 90 sites built by three models from generic briefs, and how often each layout pattern appears |
| [`briefs/`](briefs/) | Two opposite-register briefs with real copy, audience and constraints |
| [`run.py`](run.py) | Runs the experiment: each brief × model × condition, 3 times |
| `runs/<brief>/<condition>/<model>-<n>/` | One folder per run: the page, the agent's notes and the exact prompt |
| [`analyze.py`](analyze.py) | Automatic measures for the runs → [`runs/measures.md`](runs/measures.md) |
| [`ratings/`](ratings/) | The blind rating page (A vs B and B vs C), its answer key and the scoring script |
| [`tools/`](tools/) | Renders pages in Chrome and detects layout slop; calibrated on fixtures |
| [`taste-grilling/`](taste-grilling/) | Design for a skill that questions the client before building (designed, not run) |

## Run it yourself

Needs Python 3, Node 22+, Google Chrome and the `claude` CLI.

```bash
cd lab/tools && npm install && npm test && cd ../..        # set up and calibrate the detector
node lab/tools/resolve-fonts.mjs && node lab/tools/fetch-fonts.mjs   # fonts for faithful renders
python3 lab/run.py --conditions A,B,C                       # 54 runs; skips ones that exist
node lab/tools/detect.mjs lab/runs --out lab/runs/detect.json --shots lab/runs/shots --full
python3 lab/analyze.py
```

Conditions so far: **A**, no skills; **B**, `find-font` and `find-color` installed and asked for; **C**, B plus
`check-layout`. Add a condition by extending `run.py` and rerun; existing runs are kept.

## How an experiment runs

1. **Same starting point.** Every run starts from an empty project with personal settings, plugins and skills
   off, and records the repo commit it ran from. Pages are single HTML files so they render identically.
2. **Baseline first.** No-skills runs come before any intervention, with the same prompt for every model.
3. **Rate blind.** People compare two sites at a time without knowing which condition made which, and write
   what's wrong in plain words. Those critiques become the rubric.
4. **One change at a time:** skills, then a screenshot feedback loop, then a separate critic, then a pass that
   may only delete things.
5. **What counts as better:** fewer corrections needed before you'd ship it.

## What gets measured

- **Layout slop:** nine patterns detected on the rendered page (see [`tools/README.md`](tools/README.md)).
- **Default fonts:** whether the page uses a font from typography's avoid list.
- **Convergence:** how many different fonts nine runs of one brief used, and how alike opposite briefs came out.
- **Fit and distinctiveness:** judged by people, blind, two at a time.
