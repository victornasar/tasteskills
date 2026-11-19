# Creative direction: Tallyroll
Status: draft · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing, plus the finance leads who sign off with them; they distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability — "Every cent traces back to an event" — [client]
- V2 Legibility — "rules you can read", "reconcile line by line" — [client]
- V3 Calm precision — "Register: technical, calm, precise" — [client]
- V4 Show, don't sell — "They distrust marketing and want to see how it works" — [inferred]

## 3. Positioning
- Category: usage-based billing / metering API — [inferred]
- Alternatives: building metering and invoicing in-house; a general subscription-billing platform with usage add-ons; spreadsheets reconciled by finance each month — [inferred]
- Conventions:
  | Convention | A / C / Avoid | Why |
  | --- | --- | --- |
  | Split hero: headline left, abstract dashboard screenshot right | Challenge | V4: the hero shows one real, working invoice line instead of a decorative dashboard |
  | Code snippet of the API call near the top | Adopt | Engineers check the integration shape first (V4) |
  | Logo wall / customer counts under the hero | Avoid | No such facts in the brief; inventing them breaks trust |
  | Pricing hidden behind "Contact sales" | Challenge | Brief gives a plain rate; showing it serves P3 |
  | Feature grid of icons + one-line claims | Avoid | Interchangeable; replace with the event → rule → line trace (V1) |
- Intended perception — [inferred]
  - P1 It shows its working → check: on the first screen an invoice line with an arithmetic expression is visible and expands into dated daily totals
  - P2 Calm, not salesy → check: no exclamation marks, no badges, no gradients, at most two button styles; one accent colour, used only for actions and the trace thread
  - P3 Nothing hidden → check: the price (0.5%, free under $10,000/mo) is readable as a sentence without clicking
- Sophistication: considered — B2B infrastructure bought by eng + finance leads; rate is a percentage of revenue — [inferred]
- Differentiate on: the invoice line that opens into the events behind it — [client]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference — register stated as a requirement; fennel-street.md not present in the project, so "opposite" is read only through the three stated words — [agent]

## 5. References (0)
None supplied (fennel-street.md referenced but absent) — [inferred]

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A "Ledger book" — Plex Serif + Plex Sans; Bottle Green Ledger (lib.bottle-green-ledger) | agent | finance reconciliation | V2, V3 | not selected | 5 house-style markers; follows finance convention flagged by engine |
| B "Audit trail" — Plex Serif (headlines) + Plex Sans (body) + Commit Mono (data); Graphite and Signal (lib.graphite-and-signal) | agent | V1 "every cent traces back" | V1, V4, P1 | **selected** | Leads with the product's own artifact |
| C "Terminal" — Technor + Commit Mono; Atelier Black (lib.atelier-black) | agent | engineering audience | V3 | not selected | Technor reads sci-fi/retro (engine note), fights "calm"; all-dark loses finance readers |

| Axis | A Ledger book | B Audit trail | C Terminal |
| --- | --- | --- | --- |
| Composition | one reading column, headline then lists — because V2 | the working invoice is the hero and the page follows its expansion: event → rule → line — because Differentiate on | full-width console panes stacked — because engineers |
| Scale | one big headline, rest small | three moments: headline, the $481.76 line total, the 0.5% rate — because P1, P3 | flat, even mono scale |
| Imagery | type only | product interface (invoice) + data drawn as picture (31-day bar strip) + real API payload — because P1 | code only |
| Signature device | ruled ledger lines, small caps | a signal-blue trace thread that connects a total to its sources — because V1 | blinking cursor/status line |
| Colour proportion | cream ground almost everywhere, green figure | paper ground ~65%, one inverted graphite band ~30% (engineering + pricing), signal blue <5% for actions/thread — because P2 | black ground everywhere |
| Surface | flat, square | flat page; the invoice alone is an object with 6px radius and soft shadow — because it is the thing you hold | flat, square |
| House-style markers | 5: H1 H2 H3 H4 H5 | 2: H1 (product mock + chart, counted on hesitation), H3 (invoice table hairlines) | 4: H1 H4 H5 H6 |
| Distinct on | Composition, Imagery, Colour, Signature | Composition, Scale, Imagery, Colour, Surface | Colour, Scale, Signature |

Other-client test (B): the trace thread only makes sense for a product whose claim is that totals decompose into events.

## 7. Selected direction
Audit trail — origin: agent — [agent]
The page is built around one real invoice line that opens into its 31 daily totals; everything after it explains how that line was produced (events, rules, invoice) and who checks it. Serves V1, V4, P1, P3.
The one memorable thing: you click the invoice line and the month unfolds into its days.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: IBM Plex Serif (ibm-plex-serif) 500, OFL — engine body pick #1, uses include headlines
- Body / UI: IBM Plex Sans (ibm-plex-sans) 400/600, OFL — engine body pick #2
- Numbers & code: Commit Mono (commit-mono) 400, OFL — engine code pick #1
- Engine headline pick #1 Technor (FFL) not used: note "sci-fi and industrial" conflicts with V3; FFL cannot be loaded from a public CDN — [agent]
- Loading: @fontsource packages via cdn.jsdelivr.net (download needed approval in this run) — see Open decisions — [agent]
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light / Neutral, figure on ground 17.01:1, body 10.09:1
- Ground Paper White #F9FAFB (oklch 0.985 0.002 250) · Figure Graphite #15181E (oklch 0.21 0.012 260) · Accent Signal Blue #0E6EE6 (oklch 0.56 0.2 258)
- Engine watch-out: "Brand character has to come from type and layout" — answered by the invoice-led composition — [agent]
- Muted text and tints: derived by mixing figure into ground with color-mix (not engine output; checked visually) — [agent]
### Layout plan — [agent]
- Default: nav, centered hero + 2 buttons, logo wall, 3 feature cards, stats, testimonials, pricing tiers, CTA band, footer.
- Visitor questions: what is it → show me a real line → how does data get in and become that line → can finance audit it / can eng integrate it → what does it cost → where do I start.
- Only-this-brief: the expandable invoice line with its 31 daily totals. Lead with it.
- Cut: logo wall, stats, testimonials, feature cards, CTA band, pricing tiers.
- Composition: headline left on a 12-col grid, invoice spans cols 6–12, first screen.
- Scale: 3 big moments (headline, line total, rate).
- Imagery: invoice UI, bar strip, JSON event payload.
- Signature: 2px signal-blue trace thread linking line → days, and step 1 → 2 → 3.
- Colour: one graphite band (engineering + pricing).
- Surface: only the invoice is raised.
### Imagery plan — [agent]
- Job: make a visitor believe every total decomposes into events (P1)
- Kind: product interface + data drawn as picture
- Ships now: HTML invoice with expandable line; 31-bar daily strip (example data, labelled); JSON event payload; pricing rule shown as readable text
- Treatment: engine colours only; bars in figure tint, hovered/selected bar in accent
### Judgment tokens — [agent]
- Spacing: tight (8–16px) inside the invoice, wide (120px+) between questions — density changes where the subject changes
- Radius: 6px on the invoice and buttons only; everything else square
- Motion: one 180ms height/opacity transition on the expanding line; respects prefers-reduced-motion

## 9. Constraints
- C1 First screen (1440×900) shows the headline, both actions and the invoice line with "1,204,388 calls × $0.0004 = $481.76" — [agent]
- C2 Clicking the invoice line reveals 31 dated rows/bars whose sum is stated as 1,204,388 — [agent]
- C3 Signal blue appears only on actions, focus, the trace thread and selected data; nowhere decorative — [agent]
- C4 (P3) Pricing reads as a sentence with 0.5% and $10,000 visible without interaction — [agent]
- C5 (P2) No badge, gradient, emoji, stat row, testimonial or logo wall anywhere — [agent]
- C6 Phone 390px: no horizontal scroll; invoice expression wraps legibly — [agent]

## 10. Avoid
- Pill badges above the headline — [agent]
- Rows of three icon cards — [agent]
- Gradients or glow — [agent]
- Invented customer logos, numbers or quotes — [client]
- Small-caps letter-spaced eyebrow labels — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | B Audit trail | — (non-interactive) | Best serves page job; departs most from category's split-hero layout | until user review |
| Headline font | Plex Serif over Technor | — | Technor's sci-fi note conflicts with "calm" | until user review |
| Invoice line open by default on desktop | open ≥981px, collapsed on phone | — | first screen must prove P1 | until user review |
Rejected (final): none by user.

## 12. Open decisions
- Spec approval (Gate 3) not given; built against draft — decide at: user review — [inferred]
- Self-host fonts instead of jsdelivr CDN (GDPR) before launch — decide at: pre-launch — [agent]
- Daily totals in the invoice are illustrative example data summing to the brief's 1,204,388 — confirm label wording — decide at: user review — [inferred]
- Footer link targets and demo-booking destination — decide at: integration — [inferred]
- fennel-street.md not found; "opposite" register unverified — decide at: user review — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| R1 desktop | C1 | fail: expression wrapped mid-sum | bug | nowrap expression; invoice widened to cols 6–12 |
| R1 desktop | C2 | pass on click; first screen didn't show days | lesson | line opens by default ≥981px (logged; user to confirm) |
| R1 phone | C6 | fail: figure default margin inset the invoice | bug | margin 0 |
| R1 all | brief copy rule | fail: descriptions under finance/eng items added claims | bug | removed; items are brief copy only |
| R2 desktop | C2 | fail: days list cut a row in half | bug | max-height fits 8 whole rows |
| R2 all | C3, C4, C5 | pass | — | check-layout: none of nine patterns found (desktop + phone) |
| R2 render | House style | 3: H1 yes (invoice + chart only), H2 no (graphite band ~25%), H3 yes (hairline lists), H4 no (raised invoice), H5 yes on hesitation (finance/eng are lists), H6 no (pricing scale jump) | — | under threshold |
