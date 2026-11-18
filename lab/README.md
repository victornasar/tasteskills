# lab

Experiments on whole-page design quality.

The color and typography skills pick better parts. The lab asks the bigger question: **what actually moves an
AI agent from an acceptable website to a distinctive one, and how much of that is the model versus the tools
and process around it?**

**Status:** the protocol below is written, and one experiment is designed (taste-grilling). No runs, ratings
or findings exist yet.

## What's here

| Path | What it is | Status |
| --- | --- | --- |
| [`taste-grilling/`](taste-grilling/) | Design for a skill that questions the client about what they want before building, and a test for whether it works | Designed, not run |
| `briefs/` | Project briefs written in opposite registers, with real copy, audience and constraints | Not created yet |
| `runs/` | One folder per run: screenshots at fixed viewport sizes, plus the agent's notes | Not created yet |
| `ratings/` | Blind pairwise picks and written critiques | Not created yet |
| `findings.md` | What helped and what didn't, per intervention | Not created yet |

## How an experiment runs

1. **Same starting point.** Every run starts from one frozen app commit. Record the repo and commit SHA in the
   run folder. Run with and without shadcn/ui to measure what its default styling contributes.
2. **Baseline first.** 2 briefs × 3 models × 3 runs each, with no skills. Use the same setup for every model
   where possible.
3. **Rate blind.** Remove model names, compare sites two at a time, and write down what's wrong in plain words.
   Those critiques become the scoring rubric; don't write criteria in advance.
4. **One change at a time.** Add interventions one by one: a written direction, then a design skill, then a
   screenshot feedback loop, then a separate critic, then a pass that may only delete things.
5. **What counts as better:** fewer corrections needed before you'd ship it.

## What gets measured

- **Convergence:** the same model given opposite briefs. If the sites come out structurally similar, the model
  isn't reasoning from the brief.
- **Craft defects:** contrast, type scale, spacing rhythm, line length, alignment. Checked on the rendered page,
  not just the screenshot.
- **Coherence:** does each section follow the written direction?
- **Fit and distinctiveness:** judged by people, blind, comparing two sites at a time.

## Contributing a run

Create `runs/<date>-<model>-<brief>/` with the starting commit SHA, the exact prompt, the agent's notes and
screenshots at the fixed viewports. Don't rate your own runs; ratings happen blind, after the batch is done.
