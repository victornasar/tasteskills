# AGENTS.md

This area holds **taste**: a design-director skill that writes `DIRECTION.md` and coordinates `find-font`,
`find-color` and `check-layout`. It owns no catalogs or checkers. Evidence for the orchestration shape is in
`lab/taste-grilling/` and condition D in `lab/`; guided-mode discovery is experimental until persona-B scores
exist.

## Using the skill

Follow [`skills/taste/SKILL.md`](skills/taste/SKILL.md). The creative-direction format is
[`skills/taste/references/direction-template.md`](skills/taste/references/direction-template.md). Guided
interviewing rules are [`skills/taste/references/interviewing.md`](skills/taste/references/interviewing.md).

Sibling skills live in other areas. This skill tells the agent how to find and follow them; it never copies
their engines.

## Changing the skill

1. Edit `skills/taste/SKILL.md` and the files under `skills/taste/references/`.
2. Keep `lab/taste-grilling/examples.md` and `persona-b.md` out of this folder — they are answer keys.
3. `lab/taste-grilling/direction-spec.md` points here; do not fork a second template.
4. Run `node --test tests/test_skill.mjs` from this folder. Tests are static: no model calls.
5. Do not add font family names, curated color direction names, or HEX/OKLCH values to `SKILL.md`. Those come
   from sibling engines at run time.

## Rules

- Never invent engine output. If a sibling skill is missing, the agent reports that and leaves the row open.
- Provenance tags (`client`, `inferred`, `engine`, `agent`, `approved`) stay honest; inferences do not become
  client requirements by silence.
- Approval gates stay real in interactive sessions. Critique stops after two rounds.
- Fast mode uses the written brief with labelled gaps; it is not a licence to ship one familiar look.
