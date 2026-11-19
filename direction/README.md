# direction

A skill that turns TasteSkills into one design-director workflow.

Agents that jump straight to building reach for the same website every time. Agents that only pick fonts or
colors still invent the rest. `/taste` sits in front: it works out what the business needs, writes a one-page
creative direction, calls the existing engines for type and color, plans structure with `check-layout`, then
builds and critiques against that file.

It does not replace `/find-font`, `/find-color` or `/check-layout`. It decides when, why and how to use them.

## Install

Works in Claude Code, Cursor, Codex and any agent that supports skills. For full direction work, also install
the three sibling skills (the conductor tells you if one is missing and will not invent replacements).

```bash
npx skills add https://github.com/victornasar/tasteskills --skill taste
npx skills add https://github.com/victornasar/tasteskills --skill find-font
npx skills add https://github.com/victornasar/tasteskills --skill find-color
npx skills add https://github.com/victornasar/tasteskills --skill check-layout
```

Then:

```
/taste independent daycare for local families
```

Or paste a written brief and use fast mode:

```
/taste fast <paste brief>
```

## Modes

| Mode | What it does | Status |
| --- | --- | --- |
| **fast** | Skips the interview; builds `DIRECTION.md` from a written brief with labelled inferences | Primary; what the lab measures first (condition D) |
| **guided** | Conversational discovery, one open question at a time | Experimental until discovery evals land |

## What you get

A `DIRECTION.md` in the project: context, values and positioning (category, alternatives, conventions to
adopt or challenge, intended perception, sophistication) with provenance tags; 2–3 directions that differ on
at least three of six visual axes, each checked against Taste's own house style; engine-backed type and color;
a small design system with an imagery plan; pass/fail constraints, an avoid list, and a critique pass capped at
two rounds.

## Files

| Path | What it is |
| --- | --- |
| `skills/taste/SKILL.md` | The conductor: phases, gates, skip rules, provenance |
| `skills/taste/references/direction-template.md` | Creative-direction format (single source for the repo) |
| `skills/taste/references/interviewing.md` | Guided-mode questions: open, no style labels |
| `skills/taste/references/visual-direction.md` | Six visual axes, the difference rule, the house-style check, the imagery plan |
| `tests/` | Static checks: `node --test tests/test_skill.mjs` |

Design for the discovery test (answer keys included) stays under [`lab/taste-grilling/`](../lab/taste-grilling/).
Do not ship those files with the skill.

## Checks

```bash
cd direction && node --test tests/test_skill.mjs
```
