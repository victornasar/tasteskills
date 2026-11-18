# AGENTS

This repository holds **taste skills**: judgment-based design work for agents, each area backed by curated data and evals. It is the counterpart to `webskills`, which stays deterministic. Nothing here scaffolds an app.

## Areas

| Folder | Job | Start at |
| --- | --- | --- |
| [`typography/`](typography/) | Curated free typefaces, an avoid list of AI-default fonts, the `find-font` skill, evals | [typography/AGENTS.md](typography/AGENTS.md) |
| [`color/`](color/) | Curated OKLCH ground + figure pairs, the `find-color` skill and engine, evals | [color/AGENTS.md](color/AGENTS.md) |
| [`lab/`](lab/) | Whole-page design experiments: briefs, runs, blind ratings, findings | [lab/README.md](lab/README.md) |

Work inside one area at a time and follow that area's `AGENTS.md`. Each area keeps its own data, scripts and checks; don't share code between areas until two of them need the same thing.

## Rules

- Evidence before skills: a new skill or rule needs a finding in `lab/` or an area's evals behind it.
- Evals check two things: the output avoids the known defaults, and opposite briefs get clearly different results. A catalog that sends every brief to the same picks has become a new default.
- Root-only files (`.github/`, `.githooks/`) serve the areas; keep their paths pointing into the area folders.
- No plugin manifests: apps install skills straight from this repo with `npx skills add`.

## Checks

- Typography: `cd typography && python3 scripts/build.py --check && python3 -m unittest discover -s tests -q` (also CI and the pre-commit hook; enable the hook with `git config core.hooksPath .githooks`).
- Color: `cd color && node tools/build.mjs all`, then `git diff --exit-code` (also CI).
- Lab: `cd lab/tools && npm test` (the layout detector's calibration; needs Google Chrome).
