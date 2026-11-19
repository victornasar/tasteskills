# industry-type

A study of how real companies in eight industries set type, and how AI models set type for the same
industries. It is the evidence behind any industry-aware change to `find-font` or `/taste`. **This folder changes
no skills.**

**Status:** design approved 2026-11-18. Protocol 2 site list approved and **frozen 2026-11-19**; rated subset drawn
by seed the same day. Nothing has been measured yet. Approving the design and list does not approve the findings
or Phase 2.

| File | What it is |
|---|---|
| `README.md` | This research plan: the design decisions, what is implementation detail, and what is only assumed |
| [`methodology.md`](methodology.md) | The protocol and the proposed list (generated: edit `methodology.head.md`, run `write_methodology.py`) |
| [`pick_sites.py`](pick_sites.py) | Builds the candidate pools from every source and proposes the site list. Selection only; it measures nothing |
| `proposed-sites.json` | Its output: the proposed sites, source composition and every exclusion with its reason |
| `proposed-sites.v1.json` | Protocol 1's proposal, kept unchanged for the audit trail |
| [`strikes.json`](strikes.json) | Category strikes made before freezing, each with reason, date and who asked |
| [`founded.json`](founded.json) | Founding years, with sources, for fintech candidates found only in the App Store Finance chart (criterion F) |
| [`draw_ratings.py`](draw_ratings.py) | Draws the human-rated subset by seed from the frozen list (methodology §9) |
| `rated-subset.json` | Its output, drawn at freezing before any measurement |
| `prechecks.json` | Every homepage pre-check: time, outcome, `lang`, writing systems, bot-protection flag |
| [`archive.py`](archive.py) | Audits each source's license, splits deposit from withheld, writes `archive-manifest.json`. Uploads nothing |
| `archive-manifest.json` | Every source file's SHA-256, source, terms and whether it is deposited, plus the deposit archive's checksum |
| `sources/` | Working cache of source snapshots. Not committed; deposited, privately kept or checksum-only per methodology §6 |

## Principle

**Appropriateness with intentional differentiation.** A typeface isn't slop by itself. Type fails in two
independent ways: **mismatch** (it doesn't fit the brand, audience or context) and **sameness** (it fits, but
everyone in the field already looks like this). Novelty is not the goal, and **diversity is not the optimization
target**: a varied industry is not proof of better type.

Each item below is marked **[D]** decided, **[I]** implementation detail (may change if a better way appears, as
long as the decision holds) or **[A]** assumption (expected, not required; the research can prove it wrong).

## Architecture this study feeds (built in Phase 2, not here)

- **[D]** Industry is read from the brief. Fonts get no industry tags.
- **[D]** Two libraries stay separate: the **catalog** (free, self-hostable, the only fonts the agent recommends;
  unchanged) and the **industry reference** (real companies and their type; evidence, never a pick).
- **[D]** `/taste` owns the brand-level reading: `DIRECTION.md` gains competitive differentiation (competitors,
  shared visual conventions, what this brand says differently, which conventions to adopt, challenge or avoid).
- **[D]** `find-font` adds a **Convention** line with n and date, follows `DIRECTION.md` when it exists, states the
  convention without deciding when run alone, and says "no data" for an unmeasured industry.
- **[D]** Convention data separates individual typefaces from classes (custom, commercial, OFL) and always sums
  to n; nothing is silently omitted.
- **[D]** The avoid list is a warning. An override needs an external reason: the user names the font, the brand
  already uses it, or the product ships inside a platform with its own type system (Apple HIG, Material, IBM
  Carbon, a host app's design system). Industry convention is never a reason. The reason is quoted verbatim and the
  best catalog alternative is still shown. **[I]** Avoid entries gain `license` and `url`.

## Phase 1: this research (PR 1)

- **[D]** Real sites: 8 industries × 15 (5 leaders + 10 source-balanced samples, kept as separate strata;
  editorial in five strata of 1 + 2). Several independent discovery sources per industry. The list is approved and
  **frozen before measurement**. A site that fails to load is recorded as a failure, never replaced.
- **[D]** No site is excluded for its language or writing system. Writing systems are recorded, and the
  measurement separates deliberate typography from script fallback.
- **[D]** AI prompts use one template; only the industry name changes. Every run keeps its exact prompt.
- **[D]** Raw sources stay out of git, in an immutable archive with SHA-256 checksums.
- **[D]** AI corpus: the same 8 industries, plain prompts, 3 models × 3 runs (72 pages). Each page records whether
  its type was explicitly chosen, inherited from system defaults, or loaded externally. Not choosing is a finding.
- **[D]** Measurement extends `../tools/detect.mjs` (no second renderer). Main document only; iframes and widget
  roots skipped. Per role, four layers: declared/computed family, loaded web font, actually rendered font
  (`CSS.getPlatformFontsForNode`), system fallback.
- **[D]** Fixed role rules on every page (headline, body, UI, code; see `methodology.md`). A missing role is
  recorded as absent.
- **[D]** Findings stay **per role**. A site with a custom headline face, Inter body, system UI and JetBrains
  Mono code is four observations, never collapsed into one site-level font count.
- **[I]** "Decorative oversized" and "logo" get fixed, testable rules, calibrated on fixture pages like the layout
  checks.
- **[I]** A hand-kept lookup classifies each family as custom, commercial or OFL, each with a source. Real sites
  are kept as dated font records plus screenshots, never as saved pages.
- **[D]** The automatic finding reports **prevalence** (which fonts, per role) and **convergence** (how
  concentrated the choices are) only, and says so. It makes no claim about **appropriateness** or **quality**.
- **[D]** Reproducibility: the sampling seed, Tranco list id, source hashes, model ids, exact prompts, Chrome and
  Playwright versions and the protocol version are stored with the findings.

## Human ratings

- **[D]** The rated subset (4 industries, about 5 pages per side) is drawn by seed when the list is frozen, before
  any result is seen.
- **[D]** A single-page scoring mode joins the existing pairwise mode in `../ratings/` (kept separate). Scored 1–5:
  contextual appropriateness, distinctiveness, typographic coherence (pairing is judged here), hierarchy, overall
  execution. Order randomized; real versus AI hidden. Raters judge the result, not the explanation.
- **[D]** Both full-page screenshots and typography-focused crops are tested. Neither is assumed better: full
  pages show type in context, crops reduce the pull of photography and product imagery.
- **[A]** Blinding is imperfect: real sites carry photography, product shots and real copy. The rating results
  state this limit.

## Phase 2: skills (PR 2, after the Phase 1 finding)

- **[D]** Override rule, Convention line, `conventions.json`, the `DIRECTION.md` section and new evals, each citing
  a finding. Approving this design does not approve Phase 1's findings or Phase 2's implementation.
- **[D]** Hybrid evals: same industry with different positioning must give different feel readings; different
  industries with the same positioning must share the primary feel; matching top picks are flagged for review, not
  failed; reasoning quality goes to human ratings. No LLM judge.
- **[A]** Those checks assume positioning shows up in feel tags. If the research shows feel is too coarse, the
  checks are redesigned.
- **[A]** Anything Phase 2 says about conventions (Inter or Geist in software, for example) comes from Phase 1,
  not from reported associations or expectation.

## Assumptions to test, not build in

- **[A]** AI converges more than real sites do. It may not.
- **[A]** 15 sites per industry shows a usable signal. Findings state n and don't generalize past it.
- **[A]** `CSS.getPlatformFontsForNode` is reliable on heavy production sites. Checked on a few sites first.
- **[A]** Several independent sources (YC, Wikidata, App Store charts, Altagamma, Michelin, Wikipedia lists) plus a
  traffic ranking produce a usable sample. Each skews differently; `methodology.md` records every source's bias and
  how many sites each contributed, per industry.
