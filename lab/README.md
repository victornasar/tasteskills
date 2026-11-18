# lab

Experiments on whole-page design quality. The question: what actually moves an agent from "acceptable" to "distinctive", and how much of it is the model versus the system around it.

```text
lab/
  briefs/        opposite-register briefs with real copy, audience and constraints
  runs/          one folder per run: screenshots at fixed viewports + the agent's notes
  ratings/       blind pairwise picks + free-text critiques
  findings.md    what helped, what didn't, per intervention
  taste-grilling/  design for a discovery skill: the creative direction format, worked examples,
                   and the Persona B simulated-client test (not a skill yet; no runs yet)
```

## Protocol

1. **Fixed start.** Every run branches from one frozen app commit (record the repo and SHA in the run folder). Run with and without shadcn to measure what its defaults contribute.
2. **Baseline first.** 2 briefs × 3 models × 3 runs, no skills. Same harness for every model where possible.
3. **Rate blind.** Strip model names, compare pairwise, write what's wrong in plain words. Critiques become the rubric; don't write criteria up front.
4. **One intervention at a time:** direction doc → design skill → screenshot loop → separate critic → delete-only pass.
5. **Outcome metric:** corrections needed before you'd ship it.

## Measures

- **Convergence:** same model, opposite briefs. Structurally similar sites mean the model isn't reasoning from the brief.
- **Craft defects:** contrast, type scale, spacing rhythm, line length, alignment — checked on the rendered DOM, not the screenshot.
- **Coherence:** does each section follow the written direction?
- **Fit and distinctiveness:** human, blind, pairwise only.
