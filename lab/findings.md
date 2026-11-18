# Findings

What the lab has measured, newest first. Each finding names its evidence and its limits. A finding here is what
allows a new skill or rule elsewhere in the repo.

## 2026-11-18 · /taste keeps C's gains and writes an honest direction, but doesn't move the page further yet

**Evidence:** 18 runs, condition D: C plus [`taste`](../direction/) in fast mode, asked to write `DIRECTION.md`
from the brief with provenance tags, use the sibling skills, build against it and critique for at most two
rounds. Non-interactive, so no gate could be approved. Same briefs, models and run counts as A–C. Measures in
[`runs/measures.md`](runs/measures.md); each run's `DIRECTION.md` sits next to its page.

| Measure (all models) | A | B | C | D |
|---|---|---|---|---|
| Layout slop patterns per page (of 9) | 1.83 | 1.33 | 0.06 | 0.17 |
| Pages using an avoid-list font | 50% | 0% | 0% | 0% |
| Heading and body fonts from the catalog | 50% | 100% | 100% | 100% |
| Structure change from A | – | 0.47 | 0.65 | 0.59 |
| Run-to-run structure variation (noise floor) | 0.45 | 0.45 | 0.59 | 0.58 |

- **The workflow ran as written.** All 18 runs wrote a `DIRECTION.md` using at least three provenance tags,
  none marked anything `approved`, and every one kept `Status: draft` and noted that no approval was given.
  Gaps were tagged as inferences rather than client facts (for example, "visitor's first question is 'is it
  open right now?' — [inferred]"). Overrides of the engine were recorded with a reason (Sonnet dropped
  find-font's top headline pick as "reads technical" for a bakery).
- **No invented fonts.** Every page's heading and body fonts are in the catalog, as in B and C.
- **Automatic measures match C, not beyond it.** Patterns stay near zero (three pages of 18 keep one).
  Structure change from A is 0.59 against a noise floor of 0.58; by model, Sonnet moves (0.69 against 0.61),
  Opus and Haiku don't beat their own run-to-run variation. Fast mode on a rich brief adds a written direction,
  not a different page.
- **The "one memorable thing" comes from the brief, which is the point.** All 9 Tallyroll runs led with the
  brief's own expandable invoice line; bakery runs led with the hours or the day's bake list. Grounded, not
  novel for its own sake, but it also means the brief, not the skill, supplied the idea.
- **Convergence inside a model.** On Tallyroll each model chose the same heading font in all three runs (Opus
  IBM Plex Serif, Sonnet Overpass), and IBM Plex Sans was the body font on 6 of 9 pages. Across models the
  spread is unchanged (5 heading fonts). IBM Plex as a technical default stays an open typography question.
- **Self-critique is uneven.** 13 of 18 directions recorded constraint results in Checkpoints; five left it
  empty. These are the agent grading its own constraints, so they aren't evidence of quality.
- **Cost:** 2–5½ minutes a run, about the same as C.

**What it doesn't show:** anything about guided mode (still experimental, untested), whether the direction
holds across sessions, or whether people prefer D. Fast mode's value should show most on thin briefs, where C
has nothing to plan from; both lab briefs are rich.

**Next:** run D against C on thin one-line briefs from the corpus; build the persona-B simulator for guided
mode; add D pairs to the rating page.

## 2026-11-17 · check-layout removes the overused patterns and changes structure, except on Haiku

**Evidence:** 18 more runs, condition C: B plus [`check-layout`](../layout/), which has the agent plan the page's
structure from the brief, render it, check it and fix what the brief doesn't justify. Same briefs, models and
run counts as A and B. C also gets Write and Edit so it can save and check its page. Measures in
[`runs/measures.md`](runs/measures.md).

| Measure (all models) | A | B | C |
|---|---|---|---|
| Layout slop patterns per page (of 9) | 1.83 | 1.33 | 0.06 |
| Pages using an avoid-list font | 50% | 0% | 0% |
| Structure change from A | – | 0.47 | 0.65 |
| Run-to-run structure variation (noise floor) | 0.45 | 0.45 | 0.59 |

- **Patterns nearly vanish:** one pattern on one page in 18. Read this with care: C was told to satisfy the
  same checker that measures it, so this partly shows the agent passed its own test.
- **Structure changes, which is the more independent signal** (the checker never shows the agent its skeleton).
  C moves 0.65 from A against a noise floor of 0.45. By model: Opus 0.65 against 0.41, Sonnet 0.61 against 0.30,
  **Haiku no different from noise** (0.69 against 0.64). C's own runs also vary more (0.59), so pages depend more
  on the brief and less on habit.
- **The plan step shows up on the page.** The clearest case: Opus's C bakery leads with the brief's line set on
  a 7:00 / 9:00 / 14:00 timeline, with today's opening time and the menu with prices, where A and B led with a
  slogan beside a photo placeholder.
- **Fonts keep spreading:** the 9 Tallyroll runs used 6 heading fonts in C, against 5 in B and 2 in A.
- **Cost:** C runs take several times longer (render, check, revise), and two of 18 replied without the page,
  having saved it to disk; the runner now falls back to the saved file.

**What it doesn't show yet:** that people prefer C. The rating page now holds B-vs-C pairs too (36 pairs in all).

**Limits:** as before (two briefs, one company's models, three runs per cell), plus the measurement overlap
noted above. A fairer test of the patterns would score C with checks it never saw.

## 2026-11-17 · The font and color skills remove default fonts, but don't change composition

**Evidence:** 36 runs in [`runs/`](runs/): two opposite briefs ([`briefs/`](briefs/)), each built 3 times by
Opus 5.5, Sonnet 5.5 and Haiku 5.5, in condition A (no skills) and condition B (`find-font` and `find-color`
installed and asked for). Same prompt, tools and empty project otherwise. Automatic measures in
[`runs/measures.md`](runs/measures.md), from [`analyze.py`](analyze.py).

- **Default fonts disappear.** In A, half the pages use an avoid-list font. **Every one of the 9 bakery pages
  used Fraunces for headings, across all three models.** In B, none do.
- **Models converge on one font per brief.** A's 9 bakery runs used 1 heading font; B's used 2. A's 9 Tallyroll
  runs used 2 (IBM Plex Sans on 8 of 9); B's used 5.
- **IBM Plex Sans is the AI default for technical briefs.** It's in the catalog, not the avoid list, and the
  generic corpus didn't surface it (its briefs are one line). Worth measuring with richer briefs before deciding.
- **Fewer layout patterns, mostly from colour and corners.** 1.83 patterns per page in A, 1.33 in B (Haiku 2.17 →
  1.0, Opus 1.33 → 1.0, Sonnet unchanged at 2.0). "Rounded boxes everywhere" on the bakery went from 9 of 9 to 2
  of 9.
- **Composition doesn't change beyond normal variation.** Side by side, A and B pages from the same model share
  their skeleton: the same status bar, split hero, button pair and section order. Measured with section
  skeletons (added later), B's distance from A is 0.47, the same as the distance between two A runs of the same
  model (0.45). The skills change type and colour, which is all they cover.
- **Agents mostly follow the skills, sometimes with reasons.** Opus dropped `find-font`'s top technical headline
  pick, Steps Mono, because it has two weights and lacks code symbols; that's a fair catch and a ranking
  question for typography. Haiku once justified a switch with a claim the brief doesn't make.

**What it doesn't show yet:** whether people prefer B. Blind pairwise ratings of all 18 pairs are open on the
rating page (see [`ratings/`](ratings/)); results go in `ratings/results.md`.

**Limits:** two briefs, one company's models, three runs per cell. Single-file HTML pages rather than the frozen
app commit the protocol describes, so runs are cheap and render identically; recorded as a protocol change.

## 2026-11-17 · Layout slop is common, measurable, and depends on the kind of site

**Evidence:** 90 pages in [`corpus/`](corpus/): 30 generic one-line briefs, each built by Claude Opus 5.5,
Sonnet 5.5 and Haiku 5.5 with no skills or personal settings. Measured on the rendered page by
[`tools/detect.mjs`](tools/detect.mjs). Full table: [`corpus/layout-slop.md`](corpus/layout-slop.md).

- Across all 90 pages: rounded boxes everywhere 61%, a pill badge above the headline 40%, a row of three cards
  39%, emoji as icons 37%, a centered hero 32%, a decorative gradient 31%.
- **Landing pages are the worst:** rounded boxes 100%, pill badge 93%, emoji icons 93%, decorative gradient 87%.
  The "AI landing page" is close to a single template.
- **Portfolios have their own tell:** a row of big numbers ("12 years · 80 projects · 40 clients") on 80%.
- **Docs and dashboards are cleaner,** mostly because the genre already constrains them.
- The average page shows 2.9 of the 9 patterns; 29 of 90 show four or more; 4 show none.
- **Fonts:** only 18 of 90 pages load a web font at all; the rest use system fonts. Of those 18, Inter appears on
  72% and Fraunces on 50%, matching typography's avoid list. Cormorant Garamond (22%) and Jost (17%) cross the
  15% threshold and are suggested additions, pending a decision (see `typography/evals/slop/2026-11-17.json`).

**What it allows:** layout and composition are now a measured weakness, so a layout skill has evidence behind
it. The detector doubles as an automatic check for any lab run.

**Limits:**
- One company's models. Fable 5.2 needed paid usage credits; other providers weren't installed.
- The checks are heuristics on computed styles. They're calibrated on [`layout/tests/fixtures/`](../layout/tests/fixtures/) and
  were spot-checked against screenshots; two false positives found that way were fixed (photo scrims counted as
  gradients; blue buttons counted as purple).
- One generic line per brief invites generic pages. The briefs in [`briefs/`](briefs/) are richer on purpose.
