# Creative direction: Tallyroll
Status: draft (not approved — non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate it) and finance leads who sign off and reconcile line items monthly — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability — "Every cent traces back to an event" — [client]
- V2 Calm precision — "technical, calm, precise" — [client]
- V3 Show, don't sell — "They distrust marketing and want to see how it works" — [client]

## 3. Positioning
- Category: billing / metering API for usage-based pricing — [inferred]
- Alternatives: building metering and invoicing in-house; a general subscription-billing platform with usage add-ons; spreadsheets between the data warehouse and the accounting system — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Abstract dashboard mock-up or gradient hero art | Avoid | V3: buyers want the mechanism, not atmosphere |
  | Rows of big numbers / logo walls | Avoid | Brief forbids added claims; V3 |
  | Code snippet near the top for developers | Adopt (endpoint only) | Engineers check integration surface first |
  | Pricing hidden behind "contact sales" | Challenge | Price is published in the brief; stating it plainly builds trust |
  | Blue as lead colour | Adopt, as action colour only | Engine pick; blue reserved for actions keeps it from decorating |
- Intended perception — [inferred]
  - P1 Auditable → check: the first screen shows a real invoice line with the arithmetic and its daily totals
  - P2 Calm → check: one accent colour, used only on actions; no gradients, no animation beyond the expand
  - P3 Built by engineers for finance too → check: engineering and finance claims sit side by side at equal weight
- Sophistication: considered — B2B infrastructure sold to leads, priced as % of revenue — [inferred]
- Differentiate on: the invoice line that opens into its events, shown working on the page — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference — register stated plainly; fennel-street.md not present in project, so the contrast is unread — [agent]

## 5. References (0–5)
None supplied (fennel-street.md referenced but missing) — [inferred]

## 6. Directions explored
Fonts from find-font (`--role headlines body code --feel technical neutral`); colours from find-color (`fintech, saas, enterprise-software, finance`, light). Combination is [agent].

| Axis | A. Working ledger (selected) | B. Mint statement | C. Bottle-green annual report |
| --- | --- | --- | --- |
| Fonts [engine] | Overpass / IBM Plex Serif / Commit Mono | Technor / IBM Plex Sans / Commit Mono | Trench Slab / IBM Plex Serif / Iosevka |
| Colour [engine] | Graphite and Signal | Mint Ledger | Bottle Green Ledger |
| Composition | Split hero: claim left, live invoice right; product as layout — because P1 | One reading column, statement-style — because V2 | Report spreads, wide margins — because "established" reading |
| Scale | One big headline + one big figure ($481.76); sections vary density — because V1 | Flat even scale — because V2 | Several big moments, one per section |
| Imagery | The real product object (invoice + 31 daily bars) built in HTML — because V3 | Type only | Data drawn as charts |
| Signature device | Trace rule: "↳" lines from a total down to the events behind it — because V1 | Tinted statement ground | Ruled ledger with folios |
| Colour proportion | Paper ground ~80%, a full graphite band for engineering ~15%, blue ~3% on actions only — because P2, P3 | Mint ground everywhere, navy figure | Cream ground, green on rules/headings |
| Surface | Invoice is a raised object (shadow, 6px radius); rest flat — because the invoice is the one thing you can hold | Flat, square | Flat paper, hairlines |
| House-style markers | 2: H1 (product mock only), H5 partly | 5: H1–H5 | 5: H1–H4, H6 |
| Distinct on | Composition, imagery, colour proportion, surface | Scale, colour, surface | Signature, imagery, composition |

Other-client test (A): the trace rule and the expanding invoice line only make sense for a billing product whose promise is "every cent traces back to an event".

## 7. Selected direction
A. Working ledger — origin: agent — [agent]
The page is built around the product's own artifact: an invoice line whose arithmetic is visible and that opens into the 31 daily totals behind it. Serves V1, V3 and P1; the inverted engineering band and equal-weight finance column serve P3.
The one memorable thing: you can click the invoice line and see where $481.76 came from.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Overpass (`overpass`, OFL) — open, legible, a little civic
- Body: IBM Plex Serif (`ibm-plex-serif`, OFL) — "a serif with an engineer's precision"
- Code / figures: Commit Mono (`commit-mono`, OFL)
- Engine's top headline pick was Technor (Fontshare FFL, self-host only); dropped via `--public-repo` because a single shared HTML file cannot carry FFL files — [agent]
### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), area 86/11/3
- Ground Paper White #F9FAFB · figure Graphite #15181E · accent Signal Blue #0E6EE6
- Text #3C3F46 (10.09:1) · muted #6B6F76 (4.82:1) · tints #44484F / #797E85 / #B2B8C0
- Inverted band: #B2B8C0 on #15181E measured 8.89:1 (classify) — [engine]
### Layout plan — [agent]
- Default: nav, centred hero + 2 buttons, 3 feature cards, stats, testimonials, CTA band, footer
- Visitor questions: what is it → can I see where a number comes from → how do I integrate → does finance get what it needs → what does it cost → where next
- Only this brief: the invoice line that expands into 31 daily totals — leads, beside the headline
- Cut: stats, testimonials, logo wall, repeated CTA band, feature cards
### Imagery plan — [agent]
- Job: prove traceability (P1)
- Kind: product interface built in HTML — the invoice with its expanding line and daily bars
- Ships now: invoice object; 31-day bar strip with values; `POST /v1/events` endpoint
- Daily figures are illustrative (sum to 1,204,388) and labelled "Example invoice"
### Judgment tokens — [agent]
- Radius 6px on the invoice and buttons only; everything else square
- One shadow, on the invoice only
- Spacing: tight inside the invoice (ledger density), wide between sections; engineering band denser
- Motion: the line expands (160ms); nothing else moves

## 9. Constraints
- C1 First screen shows headline, both actions and the invoice line with its arithmetic → check: desktop 1440×900 screenshot — [agent]
- C2 Signal Blue appears only on links/actions/focus → check: no blue on headings, rules or decoration — [agent]
- C3 No copy, number or claim outside the brief, except labelled example daily totals → check: diff text against brief — [agent]
- C4 (P3) Finance and engineering lists sit side by side at equal width on desktop → check: full screenshot — [agent]
- C5 Phone (390px) has no horizontal scroll and the invoice math stays legible → check: phone screenshot — [agent]

## 10. Avoid
- Gradients, glows, or mesh backgrounds — [agent]
- Pill badge above the headline — [agent]
- Row of big stat numbers or logos — [client: no added claims]
- Emoji or decorative icons — [agent]
- Blue used as decoration — [engine]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. Working ledger | — (non-interactive) | Best serves the page job: shows the mechanism | until review |
| Headline font | Overpass over Technor | — | FFL can't ship in a single shared file | until review |

## 12. Open decisions
- Approval of this whole spec (Gates 1–3 skipped, non-interactive) — decide at: first review — [inferred]
- Fonts are loaded from jsDelivr (Fontsource); self-host before launch for GDPR — decide at: production build — [agent]
- Commit Mono has no Fontsource package assumed; falls back to system mono — decide at: production build — [agent]
- Docs / demo / footer link targets (placeholders `#`) — decide at: handoff — [inferred]
- fennel-street.md not found; contrast reading unverified — decide at: first review — [inferred]
- Example daily totals are illustrative; replace with a real export if available — decide at: first review — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Render 1 | C1–C5 | pass | — | check-layout: none of nine patterns |
| Render 1 | (order) | — | bug: pricing actions sat before the price; mono "0.5%" slashed zero read oddly | moved actions under price; headline font for 0.5% |
| Render 2 | C1–C5 | pass | — | stop (1 of 2 rounds used) |
| Render 2 | House style | 3 markers: H1 yes (product mock only), H2 yes (pale ground + graphite), H5 yes (left headline then lists); H3 no (no small caps), H4 no (raised invoice, inverted band), H6 no (density changes per section) | — | kept |
