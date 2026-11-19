# Creative direction: Tallyroll
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing, and the finance leads who sign off — [client]
- The page must: make a careful buyer trust Tallyroll with revenue; send them to the docs or a demo — [client]

## 2. Values
- V1 Calm — "technical, calm, precise" — [client]
- V2 Traceable — "Every cent traces back to an event" — [client]
- V3 Unmarketing — "They distrust marketing and want to see how it works" — [client]

## 3. Positioning
- Category: billing API / usage metering and invoicing — [inferred]
- Alternatives: building billing in-house; other billing APIs (none named in brief); spreadsheets for reconciliation — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | Dark, glowing developer-tool first screen | Challenge | V1 calm, finance readers; light ledger paper reads as accounting |
  | Code snippet beside the headline | Adopt | engineers verify by reading the API call |
  | Logo wall and testimonials | Avoid | brief supplies none; no invented claims |
  | Feature grid | Challenge | replaced by a numbered sequence plus two plain lists |
  | Pricing stated plainly | Adopt | finance sign-off needs the number |
  All [agent]
- Intended perception:
  - P1 Precise → check: a real invoice line with arithmetic is visible in the first screen
  - P2 Calm → check: one accent family, no gradients, generous measure, no motion beyond expand
  - P3 Auditable → check: the line expands to 31 daily totals on the page
  [inferred]
- Sophistication: considered — B2B finance purchase, careful buyers — [inferred]
- Differentiate on: the invoice line you can open down to the events — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: hypothesis — fennel-street.md was not provided; read as "not warm/playful" — [agent]

## 5. References
None given.

## 6. Directions explored
Fonts engine: headlines Steps Mono (steps-mono), body IBM Plex Serif (ibm-plex-serif), code Iosevka (iosevka) — [engine]
Colors engine: Graphite and Signal (lib.graphite-and-signal, pick), Bottle Green Ledger (lib.bottle-green-ledger), Cabin Navy (lib.cabin-navy) — [engine]

| Axis | A Ledger | B Console | C Spec sheet |
| --- | --- | --- | --- |
| Composition | left-aligned, invoice as hero — because P1 | split, dark code panel — convention | single column, text first |
| Scale | modest headline, tabular figures large — V1 | large headline | uniform |
| Imagery | built invoice UI — V2 | terminal mock | none |
| Signature device | expandable ledger line — P3 | request/response | rules |
| Colour proportion | cream 90 / green 10 — V1 | dark 85 / signal 15 | white / navy |
| Surface | paper, hairline rules, no boxes — V1 | glass panels | flat |
| House-style markers | 1 (H: monospace headline) | 4 | 2 |
| Distinct on | composition, colour, surface, imagery | | |
All [agent]. Other-client test: the expandable line and ledger paper are specific to billing.

## 7. Selected direction
A Ledger — origin: agent — [agent] (chosen: best serves the page job and departs most from the dark console convention)
Cream ledger paper, bottle green, hairline rules; the invoice line is the hero. Serves P1–P3.
The one memorable thing: you can open an invoice line down to its 31 daily totals on the first screen.
House style: 1.

## 8. Design system
### Typography — [engine]
- Headlines: Steps Mono (steps-mono), OFL, weight 400; caveat: no = @ [ ] { | } ~, so never used for code or the arithmetic.
- Body: IBM Plex Serif (ibm-plex-serif), OFL.
- Figures/code: Iosevka (iosevka), OFL, tabular figures. (Departure Mono, the engine's top code pick, is a pixel font; rejected as too decorative for finance. [agent])
- Delivery: @font-face with local() then ./fonts/*.woff2 and system fallbacks. Files are not bundled, so the page falls back to system mono/serif until they are added. [agent]
### Color — [engine]
- Direction: Bottle Green Ledger (lib.bottle-green-ledger), Light + Muted
- Ground #F6F2E7, figure #194430, text #3D3B34 (10.01:1), muted #6D6A63 (4.82:1), tint-1 #417058, tint-3 #9ED0B4, shade-1 #123524. Figure on ground 9.82:1.
- Engine gives no accent; the figure green is the action color.
### Layout plan — [agent]
- Default: nav, centered hero, three cards, stats, testimonials, CTA. Cut: cards, stats, testimonials.
- Questions: what is it → how does it work → can I check it → fit for me (finance/eng) → cost → act.
- Order: headline + invoice line, how it works (numbered rows), finance/engineering as two plain lists, pricing sentence, closing action, footer.
- Axes as table A.
### Imagery plan — [agent]
- Job: prove traceability — P1, P3. Kind: product interface built in HTML/CSS. Shot list: invoice with expandable line; request snippet. Ships now: both.
### Judgment tokens — [agent]
- Radius 0–2px (ledgers are square). Spacing varies: tight in groups, wide between sections. Motion: only the expand.

## 9. Constraints
- C1 Invoice line with arithmetic visible without scrolling at 1280×800 and 390×844 → check: screenshot — [agent]
- C2 Headline ≥ 4× body size, left-aligned — [agent]
- C3 No gradients, emoji, pill badges, or cards in rows of three — [agent]
- C4 Exactly two actions in hero, docs primary — [agent]
- C5 Every claim, number comes from brief → check: copy diff — [agent]
- C6 Perception P2 calm: one accent hue family — [agent]

## 10. Avoid
- Dark glowing console hero; testimonials/logo wall; gradients; boxed card grids; invented stats — [agent]

## 11. Decisions log
| Direction A chosen | agent | n/a | non-interactive | until approval |

## 12. Open decisions
- Direction approval — decide at: Gate 3 — [inferred]
- Font files to self-host — decide at: deploy — [inferred]
- fennel-street.md contents — decide at: client — [inferred]
- Docs, demo, footer link targets — decide at: client — [inferred]

## 13. Checkpoints
See report in chat.
