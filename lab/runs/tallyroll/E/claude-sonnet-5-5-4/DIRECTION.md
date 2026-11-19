# Creative direction: Tallyroll
Status: draft · Mode: fast · v1

## 1. Context
- Product: usage-based billing API; turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, and the finance leads who sign off. They distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or a demo — [client]

## 2. Values
- V1 Traceable — "Every cent traces back to an event" — [client]
- V2 Calm, precise — "technical, calm, precise" — [client]
- V3 Shows, doesn't sell — "distrust marketing… want to see how it works" — [client]

## 3. Positioning
- Category: billing API / usage metering and invoicing — [inferred]
- Alternatives: building billing in-house; a general subscription-billing product; spreadsheets at month end — [inferred]
- Conventions:
  | Convention | Decision | Why |
  | Dark dev-tool hero with code window | Challenge | V3: finance signs off too; light ledger paper reads as accounting — [agent] |
  | Blue as lead colour | Avoid | find-color lists finance-blue as the category norm — [engine/agent] |
  | Endpoint shown on the page | Adopt | Engineers check it first — [agent] |
  | Docs + demo as the two actions | Adopt | Brief's actions — [agent] |
  | Logo wall / testimonials | Avoid | None in brief; none invented — [agent] |
- Intended perception — [inferred]
  - P1 Exact → check: figures, `×`/`=` arithmetic and monospace appear above the fold
  - P2 Calm → check: one ground, one ink green, no decoration
  - P3 Inspectable → check: invoice line expands on the first screen
- Sophistication: considered — B2B revenue infrastructure, careful buyers — [inferred]
- Differentiate on: the invoice line that opens into its events — [client]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street." Reading: deliberate preference — [agent]

## 5. References
None given — [inferred]

## 6. Directions explored
| Axis | A Ledger | B Terminal | C Spec sheet |
| Composition | left-aligned, ruled ledger with label margin — V1 | dark full-bleed hero | docs-style sidebar layout |
| Scale | one large mono headline, small rest — V2 | huge type | uniform |
| Imagery | live invoice line built in HTML — P3 | code window | none |
| Signature device | expanding invoice line | typed request | sidebar nav |
| Colour proportion | 84/16 ground/ink — P2 | inverse | 90/10 |
| Surface | rules, no boxes | glow panels | flat |
| House-style markers | 1 | 4 | 2 |
| Distinct on | composition, imagery, surface | | |
Fonts (find-font, engine): Steps Mono + IBM Plex Serif + Commit Mono. Colour (find-color, engine): lib.bottle-green-ledger (A); lib.graphite-and-signal (B/C).
Other-client test: the expanding invoice line is Tallyroll's own artifact.

## 7. Selected direction
A Ledger — origin: agent — [agent]
Ruled ledger paper, mono headline, invoice line as the hero artifact. Serves V1–V3, P1–P3.
The one memorable thing: the first screen contains an invoice line you can open down to its daily totals.
House style: 1 — [agent]
Chosen because it best serves the page job and departs furthest from the dark dev-tool layout.

## 8. Design system
### Typography — [engine]
- Headlines: Steps Mono (steps-mono, OFL, 400 only; lacks `= @ [ ] { |` so never used for code)
- Body: IBM Plex Serif (ibm-plex-serif, OFL, variable)
- Code / figures: Commit Mono (commit-mono, OFL)
- Fonts must be self-hosted; the single file uses local() plus fallback stacks. [agent]
### Color — [engine] Bottle Green Ledger (lib.bottle-green-ledger), 9.82:1 figure on ground
- Ground #F6F2E7 · Figure #194430 · Text #3D3B34 (10.01:1) · Muted #6D6A63 (4.82:1) · tint-1 #417058 · tint-3 #9ED0B4
- No accent in this direction; actions are figure-filled buttons.
### Layout plan — [agent]
- Default: centred hero, three cards, stats, testimonials, CTA band. Visitor questions: what is it, how does it work, can I trust it, what does it cost, how do I act.
- Order: header, hero + invoice line, how it works, finance / engineering, pricing, closing actions, footer. Cut: testimonials, logos, stats.
### Imagery plan — [agent]
- Job: prove traceability — serves P1, P3. Kind: product interface, built in HTML/CSS.
- Shots: invoice line with expandable day table; `POST /v1/events` line.
- Ships now: both. Daily totals are illustrative, generated to sum to the stated 1,204,388 calls, and labelled so.
### Judgment tokens — [agent]
- Spacing follows content; radius 0 (ledger rules); no motion beyond the native details toggle.

## 9. Constraints
- C1 Headline ≥ 3× body size, left-aligned — [agent]
- C2 Invoice line visible without scrolling at 1280×800 — [agent]
- C3 Only engine colours and tints; no gradients — [agent]
- C4 No claims, numbers or names beyond the brief (illustrative rows labelled) — [agent]
- C5 P1, P2, P3 observable in the screenshot — [agent]

## 10. Avoid
- Centered hero, three-card rows, pill badges, gradients, emoji icons, stat rows — [agent]

## 11. Decisions log
| Direction A selected | agent | – | best serves job | yes |

## 12. Open decisions
- Spec approval — non-interactive run — decide at: review
- Font files self-hosted, not embedded — decide at: deploy
- Docs/demo URLs unknown (links are #) — decide at: deploy
- Audience and competitor readings are inferred — decide at: review

## 13. Checkpoints
Scored after build in the run report.
