# Findings

What the lab has measured, newest first. Each finding names its evidence and its limits. A finding here is what
allows a new skill or rule elsewhere in the repo.

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
- **Composition barely changes.** Side by side, A and B pages from the same model share their skeleton: the same
  status bar, split hero, button pair and section order. The skills change type and colour, which is all they
  cover. This is the strongest evidence yet that layout needs its own work.
- **Agents mostly follow the skills, sometimes with reasons.** Opus dropped `find-font`'s top technical headline
  pick, Steps Mono, because it has two weights and lacks code symbols; that's a fair catch and a ranking
  question for typography. Haiku once justified a switch with a claim the brief doesn't make.

**What it doesn't show yet:** whether people prefer B. Blind pairwise ratings of all 18 pairs are open on the
rating page (see [`ratings/`](ratings/)); results go in `ratings/results.md`.

**Limits:** two briefs, one company's models, three runs per cell. Single-file HTML pages rather than the frozen
app commit the protocol describes, so runs are cheap and render identically; recorded as a protocol change.
