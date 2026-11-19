# Creative direction: Tallyroll
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate it) and the finance leads who sign off with them (reconcile line items monthly); they distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability — "Every cent traces back to an event" — [client]
- V2 Precision — "technical, calm, precise" — [client]
- V3 Calm — "technical, calm, precise" — [client]
- V4 Show, don't sell — "They distrust marketing and want to see how it works" — [inferred]

## 3. Positioning
- Category: "billing / metering API for usage-based pricing" — [inferred]
- Alternatives: building metering and invoicing in-house; a general subscription-billing platform with usage add-ons; spreadsheets reconciled by finance at month end — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Split hero: headline left, a code snippet or abstract product shot right | Challenge | The hero shows the actual invoice line opening into its 31 daily totals (V1, V4) |
  | Code samples for the API call | Adopt | Engineers came to check exactly this (audience) |
  | Pricing as a grid of plan tiers | Avoid | There is one price; a single sentence is more precise (V2) |
  | Logo wall / customer quotes under the hero | Avoid | Brief supplies none; inventing them breaks trust (V4) |
  | One audience addressed (developers only) | Challenge | Finance signs off; the page speaks to both, side by side |
- Intended perception — [inferred]
  - P1 Traceable → check: on the first screen an invoice line is visibly broken down into daily totals
  - P2 Engineered, not marketed → check: no adjectives-only section; every section shows an endpoint, rule, line or number from the brief
  - P3 Calm → check: one accent-free dark ground, no gradient, no motion beyond the expand toggle
- Sophistication: considered — B2B infrastructure that handles revenue; price 0.5% of billed revenue — [inferred]
- Differentiate on: the invoice is inspectable — a line opens into the events behind it — [client]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference — register given explicitly; fennel-street.md was not provided, so "opposite" is read only through the three words — [agent]

## 5. References (0–5)
None supplied (fennel-street.md not present in project) — [inferred]

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A Console trace — Technor + IBM Plex Serif + Commit Mono; Slate Press (lib.slate-press) | agent | product is an API whose output is an auditable document | P1, P2, P3 | selected [agent] | — |
| B Graphite desk — Technor + IBM Plex Serif; Graphite and Signal (lib.graphite-and-signal) | engine pick | engine default for saas/fintech | P2 | not selected | engine warns "easy to make indistinguishable from every other product" |
| C Ledger paper — Technor + IBM Plex Serif; Concrete and Brass (lib.concrete-and-brass) | agent | invoices as physical documents | P1 | not selected | gray ground domain is architecture; reads material, less "API" |

| Axis | A Console trace | B Graphite desk | C Ledger paper |
| --- | --- | --- | --- |
| Composition | product as layout: the invoice is the hero's main object, steps hang off a trace line — because Challenge "split hero with snippet" | one reading column, headline then lists — because V3 | centred paper sheet on a desk, sections as annotations — because P1 |
| Scale | three big moments: headline, invoice total, the 0.5% — because P1 + pricing is the deciding fact | one huge headline, rest small — because V3 | flat, document scale — because V2 |
| Imagery | real product interface (invoice) + data drawn as picture (31-day bar chart, event trace) — because V4 | product mock alone — because V2 | type as image (the invoice line set large) — because P1 |
| Signature device | the trace line: a thin vertical line that runs from event → rule → invoice line — because V1 | hairline rules | brass margin markers |
| Colour proportion | Slate Night ground everywhere, Cold Paper as type and the primary button fill, panels stepped up in lightness — because P3 | white ground, graphite text, 3% blue — engine area | concrete ground, white sheet, 4% brass |
| Surface | layered panels, 6px radius, subtle depth via lighter surfaces, no shadows-as-decoration, no grain — because P3 | flat, square | paper sheet with real shadow |
| House-style markers | 2: H1? no (interface + chart + diagram); H2 no (dark ground); H3 yes (invoice rules); H4 no; H5 yes-ish (left headline); H6 no | 6: all | 4: H1, H2, H3, H6 |
| Distinct on | colour, composition, imagery, surface, scale | composition, colour, surface | colour, surface, imagery |

Other-client test (A): the trace line and expandable invoice line come from Tallyroll's own claim ("each line opens up into the events that produced it"); it would not fit a non-billing product.

## 7. Selected direction
A Console trace — origin: agent — [agent]
A dark, cool slate page where the product's own invoice is the hero and the explanation is a trace from event to line. Serves V1, V4 and P1 directly; the cool dark ground and absence of accent colour keep it calm (V3).
The one memorable thing: the March API-calls line opens into its 31 daily totals right on the first screen.
House style: 2 planned (H3, H5) — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Technor (technor), FFL, Fontshare, weights 200–900, no italics — self-host only, keep files out of public repos
- Body: IBM Plex Serif (ibm-plex-serif), OFL, github.com/IBM/plex
- Code / figures: Commit Mono (commit-mono), OFL, commitmono.com
- Loading: self-hosted @font-face from ./fonts/ (Technor.woff2, IBMPlexSerif.woff2, CommitMono.woff2) with engine fallback stacks; no font CDN — [engine/agent]
### Color — [engine]
- Direction: Slate Press (lib.slate-press), Dark / Neutral, area 82/18
- Ground: Slate Night #121921 oklch(0.21 0.02 255) · Figure: Cold Paper #E6ECF2 oklch(0.94 0.01 250)
- Text #BEC4CB (10.06:1) · Muted #81868D (4.82:1) · Button: Cold Paper fill, Slate Night label 14.86:1
- No accent; engine note: "Step surfaces up in lightness from Slate Night rather than adding new hues." Raised surfaces are colour-mix of ground and figure — [agent]
### Layout plan — [agent]
- Default: nav, split hero + code, logo wall, 3 feature cards, stats, testimonials, pricing tiers, CTA band, footer.
- Visitor questions: what is it → can I see a real line traced → how does data get in and become a line → what does finance get / what does engineering get → what does it cost → where do I go next.
- Only-this-brief thing: the invoice line that expands into 31 daily totals. Leads the page.
- Cut: logo wall, stats, testimonials, feature cards, pricing tiers, CTA band (actions live in hero and pricing).
- Axis positions: as table column A.
### Imagery plan — [agent]
- Job: make a visitor believe every amount is traceable — serves P1
- Kind: real product interface (HTML invoice) + data (bar chart of daily totals) + trace diagram (event → rule → line)
- Shot list: none; no photography needed
- Treatment: panels on stepped slate surfaces, Commit Mono for every figure
- Ships now: invoice panel, 31-bar chart, step code panels. Daily totals are illustrative and labelled "example".
### Judgment tokens — [agent]
- Radius 6px on panels only; buttons 4px; nothing pill-shaped (V2)
- Spacing: tight inside panels (12–16px), wide between sections, but section padding varies with content
- Motion: only the expand/collapse of the invoice line (≤180ms height), respects reduced motion (V3)

## 9. Constraints
- C1 First desktop screen shows the invoice line with its daily breakdown visible → check: bars and "1,204,388 calls × $0.0004 = $481.76" above the fold at 1440×900 — [agent]
- C2 No colour outside the engine tokens and their mixes; no gradient → check: render shows only slate/paper tones — [agent]
- C3 Every section contains a concrete artefact (endpoint, rule, line, figure) from the brief → check P2 — [agent]
- C4 No claim, number or testimonial beyond the brief; example data labelled as example → check copy — [agent]
- C5 Phone (390px): no horizontal scroll; invoice line readable, chart fits — [agent]

## 10. Avoid
- Logo walls, testimonials, star ratings — [agent]
- Pill badges above the headline — [agent]
- Three equal feature cards — [agent]
- Gradient or glow backgrounds — [agent]
- Pricing tier cards — [agent]
- Emoji or decorative icon sets — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A Console trace | — (non-interactive) | Best serves "see how it works"; departs most from split-hero category layout | until user review |
| Colour | Slate Press over engine pick Graphite and Signal | — | pick's watchOut: indistinguishable; Slate Press chooseIf matches "technical product, cool deliberate cast" | until user review |
| Fonts | engine top picks | — | no caveat bites | until user review |

## 12. Open decisions
- Gate 1–3 approvals (Context, Values V4, Positioning, spec) — decide at: user review — [inferred]
- Font files: Technor is Fontshare (FFL); files must be downloaded into ./fonts/ and kept out of a public repo — decide at: deploy
- Dark-only vs light theme — decide at: user review — [agent: dark only]
- Real illustrative data for the invoice breakdown (daily totals are generated examples) — decide at: before launch
- fennel-street.md reference not available — decide at: user review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1 render (1440, 390) | C1 | pass — bars and formula above the fold | — | — |
| Round 1 | C2 | pass — slate/paper tokens only, no gradient | — | — |
| Round 1 | C3 | pass — endpoint, rule, line, feature names, price in every section | — | — |
| Round 1 | C4 | pass — example data labelled "Example" / "illustrative" | — | — |
| Round 1 | C5 | pass — no page scroll; code blocks scroll inside their panel | — | — |
| Round 1 | House style | 3: H1 no, H2 no (dark), H3 yes (list rules), H4 yes (hesitated: no shadows), H5 yes, H6 no (0.5% moment) | — | kept, ≤3 |
| Round 1 | check-layout | none of nine patterns, desktop and phone | — | — |
| Round 1 | polish | chevron glyph rendered like a caron | bug | replaced with SVG chevron; right column padding |
