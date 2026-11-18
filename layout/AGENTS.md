# AGENTS.md

This area holds **check-layout**: a skill that plans a page's structure from its brief and checks the rendered page
for the layout patterns AI-built sites overuse. Its evidence is in `lab/findings.md` (the 90-site corpus and the
with/without-skills experiment).

## Using the skill

Follow [`skills/check-layout/SKILL.md`](skills/check-layout/SKILL.md). The checker is
`skills/check-layout/scripts/check_layout.mjs`; it needs Node 22+ and a Chromium-family browser, nothing else.

## Changing the checks

The nine checks live in [`skills/check-layout/scripts/patterns.mjs`](skills/check-layout/scripts/patterns.mjs).
`lab/tools/detect.mjs` imports the same file, so the skill and the lab always measure the same thing.

1. `measure()` runs inside the page: keep it self-contained (no imports, no outside variables).
2. A new check needs evidence: a rate from the lab corpus showing AI-built pages overuse it.
3. Every check must fire on `tests/fixtures/slop.html` and stay silent on `tests/fixtures/clean.html`. When you
   fix a false positive, add the case to `clean.html` so it stays fixed.
4. Spot-check against real screenshots (`lab/corpus/shots/` after running the lab detector) before trusting a
   new check's rate.
5. Run `node --test tests/*.test.mjs` and `cd ../lab/tools && npm test`. After changing a check, rerun the corpus report
   (`lab/corpus/README.md`) so the rates in `SKILL.md` stay true.

## Rules

- The skill gives options, never one prescribed layout. A skill that turns every brief into the same
  left-aligned serif page has become a new default.
- Rates quoted in `SKILL.md` come from `lab/corpus/layout-slop.md`; update both together.
