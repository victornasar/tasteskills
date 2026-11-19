# Creative direction: Tallyroll
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate it) and the finance leads who sign off with them (reconcile line items monthly) — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability — "Every cent traces back to an event" — [client]
- V2 Show, don't sell — "They distrust marketing and want to see how it works" — [client]
- V3 Calm precision — "Register: technical, calm, precise" — [client]
- V4 Readable rules — "written as rules you can read" — [inferred: elevated from a step description to a value]

## 3. Positioning
- Category: "billing / metering API for usage-based pricing" — [inferred]
- Alternatives: building metering and invoicing in-house; a general subscription-billing platform with usage add-ons; spreadsheets reconciled by finance each month — [inferred, none named in brief]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Code snippet near the top (curl / SDK call) | Adopt | Engineers rely on it to judge integration effort (V2) |
  | Abstract dashboard screenshot as hero art | Challenge | Shows "a product", not proof; replace with the one invoice line that opens into its events (V1) |
  | Sans-serif geometric type, blue accent, everything on white | Challenge | Makes alternatives interchangeable; set the page like a document finance would sign (serif + mono) |
  | Pricing as a three-tier table | Avoid | Tallyroll has one price; a tier table would invent structure (V2) |
  | Logo wall / customer counts | Avoid | Brief supplies none; adding them breaks the copy rule (V2) |
- Intended perception — [inferred]
  - P1 "I can audit this" → check: the first screen shows an invoice line with its arithmetic and its daily breakdown, numbers in tabular mono
  - P2 "Engineers built this for engineers" → check: real endpoint `POST /v1/events` and a code sample visible within the first two screens
  - P3 "Calm, not salesy" → check: no badges, stats rows, gradients or exclamation; one accent colour used only on links/focus
- Sophistication: considered — B2B infrastructure priced at 0.5% of billed revenue, bought by leads who sign off together — [inferred]
- Differentiate on: the invoice is the demo — the line expands into the events behind it, on the page — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference — register stated as a contrast; fennel-street.md not present in project — [agent]

## 5. References (0)
None supplied. fennel-street.md referenced but not found — [client/inferred]

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A Working ledger | agent | V1, P1 | page job: trust → docs | Selected | Product artifact carries the page |
| B Audit book | agent | V3, finance audience | P3 | Not chosen | House style (5 markers); reads as a document, underserves engineers |
| C Terminal | agent | P2 | engineering audience | Not chosen | Dark full-page code look alienates finance co-signer |

Fonts (all): IBM Plex Serif (`ibm-plex-serif`) + Commit Mono (`commit-mono`) — [engine]. Colours: A `lib.graphite-and-signal`, B `lib.bottle-green-ledger`, C `lib.atelier-black` — [engine]. Combinations — [agent].

| Axis | A Working ledger | B Audit book | C Terminal |
| --- | --- | --- | --- |
| Composition | headline left, live invoice object filling the right/below; then a pipeline of three steps with code; then a two-column finance/engineering ledger — because P1 | one centred reading column like a printed report — because V3 | full-width console panes stacked — because P2 |
| Scale | three big moments: headline, the $481.76 total, "0.5%" — because V1 (the numbers are the point) | one huge headline, all else small — because V3 | flat even mono scale — because P2 |
| Imagery | the product interface (expandable invoice) + a 31-bar chart of daily totals drawn in HTML — because V2 | type only — because V3 | code blocks only — because P2 |
| Signature device | the trace: a mono arithmetic line `calls × rate = amount` that recurs in hero, steps and pricing — because V1 | ruled ledger lines | blinking prompt line |
| Colour proportion | Paper White ground; one full Graphite band for "How it works" and its code (moved from the engineering list at build: code needs the band more); Signal Blue only on links/focus — because engine do-rule | cream ground, green figure only | black ground everywhere |
| Surface | invoice is a raised sheet (shadow, 6px radius); rest flat — because the invoice is an object you hold | flat paper, square | flat, square |
| House-style markers | 2: H3 (invoice rules), H5 (left headline) | 5: H1 H2 H3 H4 H5 | 4: H1 H4 H5 H6 |
| Distinct on | composition, scale, imagery, colour, surface | | |

Other-client test (A): the expanding invoice line and the `× $0.0004 =` trace only make sense for a billing product.

## 7. Selected direction
A Working ledger — origin: agent — [agent]
The page is built around the brief's example invoice line, shown working: arithmetic in mono, 31 daily totals as a chart and table, collapsible. Serves V1, V2, P1, P2.
The one memorable thing: the invoice line that opens into the events that produced it.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines + body: IBM Plex Serif (`ibm-plex-serif`), OFL, https://github.com/IBM/plex — body pick #1 for feel technical; its `use` includes headlines
- Code, numbers, labels: Commit Mono (`commit-mono`), OFL, https://commitmono.com — code pick #1
- Not used: Technor (headline pick #1, "sci-fi and industrial", conflicts with calm — [agent]); Mona Sans (caveat: GitHub association bites a dev tool — [agent])
### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), Neutral, light foundation
- Ground #F9FAFB oklch(0.985 0.002 250) · Figure #15181E oklch(0.21 0.012 260) · Accent #0E6EE6 oklch(0.56 0.2 258)
- Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Tints #44484F #797E85 #B2B8C0
- Button: figure fill, ground label (17.01:1). Accent links on ground 4.57:1. Signal Blue never decorative.
### Layout plan — [agent] (check-layout step 1)
- Default: nav, centred hero + two buttons, three feature cards, stats row, testimonials, three-tier pricing, CTA band, footer
- Visitor questions: what does it do → show me the proof → how do I integrate → will finance accept it → what does it cost → where are the docs
- Only this brief has: the invoice line that expands into 31 daily totals — lead with it in the first screen
- Cut: stats row, testimonials, logo wall, tier table, duplicate CTA band
### Imagery plan — [agent]
- Job: make a visitor believe every amount is auditable — serves P1
- Kind: product interface built in HTML + data drawn as a picture (31 daily bars)
- Shot list: n/a (no photography)
- Treatment: invoice sheet sits on the grid's right 7 columns on desktop, full width on phone; bars in Figure tints
- Ships now: invoice line + daily chart/table, event payload, pricing rule, invoice JSON — all labelled as example data
### Judgment tokens — [agent]
- Spacing: tight (8–16px) inside the invoice; 120px+ between ideas; the graphite band changes density
- Radii: 6px only on the invoice sheet and buttons; everything else square
- Motion: the expand/collapse only, 180ms, respects reduced-motion

## 9. Constraints
- C1 First desktop screen shows headline, both actions and the invoice line with `1,204,388 calls × $0.0004 = $481.76` → check: all visible at 1440×900 — [agent]
- C2 (P1) Daily breakdown shows exactly 31 values that sum to 1,204,388, and the sum is printed → check: table footer — [agent]
- C3 (P2) `POST /v1/events` appears in a code sample within the first two screens on desktop — [agent]
- C4 (P3) Signal Blue appears only on links, focus rings and none of the decoration → check: no blue fills/bars — [agent]
- C5 No copy claims, numbers or testimonials beyond the brief; example data is labelled "Example" → check: read the render — [agent]
- C6 Phone 390px: no horizontal scroll; invoice readable without zoom — [agent]

## 10. Avoid
- Pill badge above headline — [agent]
- Row of big stat numbers — [agent]
- Three identical feature cards — [agent]
- Gradients or glows — [agent]
- Icons or emoji beside feature lists — [agent]
- Customer logos or quotes — [client: no testimonials beyond copy]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A Working ledger | — (non-interactive) | Best serves page job; departs most from category's shared layout | until user review |
| Fonts loaded from jsdelivr (@fontsource) rather than embedded | self-host | — | Network download for base64 embedding not available in this run; brief allows loading | until launch |

## 12. Open decisions
- Gates 1–3 not confirmed by the client; all `inferred` items stand — decide at: client review
- Self-host the two font families (find-font rule) instead of jsdelivr — decide at: before launch
- Dark theme: engine returned a light direction only — decide at: re-run find-color with `--foundation dark` if needed
- Docs, Status, Security, Contact and demo URLs — placeholders (`#`) — decide at: client supplies links
- Event payload field names and pricing-rule syntax are illustrative — decide at: engineering review against the real API
- fennel-street.md not found; contrast reading unverified — decide at: client review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1 (render) | C1 | fail → pass | bug | invoice line lacked "=" before $481.76; added |
| Round 1 | C5 | fail → pass | bug | caption implied daily totals open into events (beyond brief); reworded to a sum statement |
| Round 1 | C6 / layout | fail → pass | bug | section padding shorthand removed side gutters (hero, lists, pricing flush to edge on phone); switched to padding-block |
| Round 1 | C2, C3, C4 | pass | — | 31 values sum to 1,204,388 and print the sum; POST /v1/events in second desktop screen; blue only on links/focus |
| Render house-style count | — | 2 | — | H1 no (chart + product UI) · H2 no (graphite band) · H3 yes (ledger rules) · H4 no (shadowed sheet) · H5 yes · H6 no (band + 0.5% display) |
| check-layout | — | 0 of 9 patterns | — | desktop and 390px; no second round needed |
