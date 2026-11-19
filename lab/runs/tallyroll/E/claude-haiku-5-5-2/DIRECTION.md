# Creative direction: Tallyroll
Status: draft (non-interactive fast run; Gate 1–3 approvals not given, see Open decisions) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies decide and integrate; finance leads sign off and reconcile line items monthly — [client]
- The page must: send a careful buyer to the docs or to book a demo, having seen how a line item traces back to events — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceable: every figure can be opened into the events behind it — "Every cent traces back to an event." — [client]
- V2 Precise: the arithmetic is shown, not implied — "quantity × rate = total" — [client]
- V3 Unhyped: distrust of marketing; the page shows how it works — "They distrust marketing and want to see how it works." — [client]

## 3. Positioning
- Category: usage-based billing for software that charges by usage — [inferred]
- Alternatives: a finance team rebuilding invoices from spreadsheets exported from the product; an in-house usage-to-invoice script; a general billing platform sold on plans — described by kind, not named — [inferred]
- Conventions (3–5):
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Docs as the primary action | Adopt | Engineers evaluate by reading; V3 — [agent] |
  | Centered hero with a gradient glow | Avoid | Reads as marketing, against V3 — [agent] |
  | Row of three feature cards | Challenge | Equal-weight cards hide the line-to-events link that V1 needs — [agent] |
  | Row of big numbers / logo wall | Avoid | No figures or customers supplied; V3 — [agent] |
  | Pill badge above the headline | Avoid | No news supplied — [agent] |
- Intended perception: three qualities a stranger reports after five seconds on the page — [inferred]
  - P1 Precise → check: the example line shows quantity × rate = total on one row, every figure legible
  - P2 Traceable → check: the line's expansion into 31 daily totals is visible in the static render
  - P3 Unhyped → check: no gradients, badges, emoji or stat rows anywhere on the first screen
- Sophistication: considered — B2B billing for finance teams; no price signal beyond 0.5% of billed revenue — [inferred]
- Differentiate on: the invoice line itself opens into its events, and finance can read it without asking engineering — [agent]

## 4. Opening vocabulary
"Calm, precise, technical. The opposite of [fennel-street.md]." (fennel-street.md is not in the project; the contrast is taken from the brief's wording only.)
Reading: deliberate preference — brief register words — [agent]

## 5. References (0–5)
None supplied. — [inferred]

## 6. Directions explored (2)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A · Ledger sheet | agent | P1, P2; the house-style default | P1 | Not selected | Scores house style; reads as a printed spec, the default for this brief family |
| B · Live reconciliation | agent | P1, P2, P3; V1 | P1–P3 | **Selected** | Makes the traceable line the page's main object |

Engine rows (both directions use the same engine picks, so the difference is composition and surface, not font):
- Typography [engine]: Technor (`technor`, FFL) headlines; IBM Plex Serif (`ibm-plex-serif`, OFL) body
- Colour [engine]: Graphite and Signal (`lib.graphite-and-signal`), rank 1 of find-color recommend, Light foundation, Neutral structure

| Axis | A · Ledger sheet | B · Live reconciliation |
| --- | --- | --- |
| Composition | One reading column, headline then printed sections — because V3 and "how it works" | Two columns: headline and actions left, the invoice line object right, same first screen — because V1, P2 |
| Scale | One large statement, flat scale below — because V3 | Several moments: headline, the invoice total, the three steps — because P1 needs the figures to read as objects |
| Imagery | Type only — because V3 | Product interface built in HTML: the invoice line and its daily strip — because V1 |
| Signature device | Hairline ledger rules — because P1 | Expanding invoice row that opens into its events — because V1, P2 |
| Colour proportion | Ground everywhere, figure text, accent in links only — because V3 | Ground for text; one inverted figure band for the invoice object; accent on links and focus only (primary action is figure fill) — because P1 |
| Surface | Flat, square, no shadow — because V3 | Object-like panel, 8px radius, 1px border, no shadow — because the invoice is a thing finance holds |
| House-style markers (H1–H6) | 6: H1, H2, H3, H4, H5, H6 | 2: H1 (product mock allowed), H2 — H3–H6 no because composition is split, density varies, radius 8px |
| Distinct on | — | Composition, scale, imagery, signature device, colour proportion, surface (≥3) |

Agent-originated rows also answer: Other-client test: a billing page could show any product's invoice; this one shows the line-to-event expansion, which only a usage-billing API has to show — [agent]

## 7. Selected direction
B · Live reconciliation — origin: agent — [agent]
The page is a working object: the invoice line, opened into its events, sits beside the headline so the first screen answers "does it add up?" as well as "what is it?". It serves V1, V2 and P1–P3.
The one memorable thing: the invoice line that opens into 31 daily totals.
House style: 2 markers (H1, H2); below 4, no override needed — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Technor (`technor`) — FFL, self-host only, keep files out of public repos. Files: `./fonts/Technor.woff2` — [engine]
- Body: IBM Plex Serif (`ibm-plex-serif`) — OFL. Files: `./fonts/IBMPlexSerif.woff2` — [engine]
- Fallbacks: system-ui for headlines, Georgia for body until the files are placed — [agent]

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`)
- Ground: Paper White #F9FAFB · Figure: Graphite #15181E · Accent: Signal Blue #0E6EE6
- Text: #3C3F46 (contrast 10.09:1 on ground) · Muted text: #6B6F76 (4.82:1 on ground)
- Figure on ground 17.01:1 · Accent used only for links, focus and the primary action — [engine values, agent use]

### Layout plan — [agent]
- The default: nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer. Cut: centered hero, feature cards, stats row, testimonials (none supplied), CTA band.
- Visitor's questions in order: what is it → does an invoice line add up → how does it work (3 steps) → how do engineers integrate (API, SDKs, webhooks) → what does it cost → where do I go (docs / demo).
- The one thing only this brief has: the invoice line that opens into its events, leading the first screen.
- Cut: anything that answers none of the six questions.
- Axis positions: Composition two columns; Scale several moments; Imagery product interface in HTML; Signature device expanding invoice row; Colour proportion ground for text, inverted figure band for the invoice object, accent on actions; Surface 8px radius, 1px border, no shadow.

### Imagery plan — [agent]
- Job: a finance reader believes each figure is traceable and adds up — serves P1, P2
- Kind: product interface built in HTML — the invoice line and its daily strip
- Shot list: (1) the line "API calls, March: 1,204,388 calls × $0.0004 = $481.76" on the first screen, right column; (2) the same line expanded to a 31-cell strip, days 01–31, no per-day values invented — right column, below the line; (3) a 3-row event excerpt "POST /v1/events" beside the steps — invented event fields not shown.
- Treatment: no photography; panel in figure band for the invoice object; panel meets the grid inset, not full-bleed.
- Ships now: all three above, built in HTML from the brief's copy. No empty frames, no stock images.

### Judgment tokens — [agent]
- Spacing: 8px base; section gap 120px desktop, 64px phone — the first screen and the steps differ in density, so spacing is not uniform.
- Radii: 8px on the invoice panel only; 0 elsewhere — the invoice is a held object; the rest is a page.
- Motion: none beyond the expand/collapse of the invoice row (150ms) — calm, no decoration.

## 9. Constraints (pass/fail on a screenshot)
- C1 P1 Precise: the example line shows quantity × rate = total on one row, all numbers legible without interaction → check: "1,204,388 calls × $0.0004 = $481.76" fully visible in the desktop and 390px screenshots — [agent]
- C2 P2 Traceable: the expanded daily strip (31 cells, days 01–31) is visible in the first full-page render → check: 31 cells present, labelled — [agent]
- C3 P3 Unhyped: no gradient, pill badge, emoji, stat row or testimonial anywhere → check: full-page screenshot — [agent]
- C4 Accent only on actions: Signal Blue appears only on "Read the docs", links and focus rings → check: blue used on no other element — [agent]
- C5 Scale: headline is at least 4× body size and no other element exceeds it → check: visual and computed sizes — [agent]
- C6 Phone 390px: no horizontal scroll; invoice numbers wrap or scale without clipping → check: 390px screenshot — [agent]

## 10. Avoid (≤6)
- Gradient backgrounds or glow behind the headline — [agent]
- Row of three feature cards — [agent]
- Row of big numbers or a logo wall — [agent]
- Pill badge above the headline — [agent]
- Emoji used as icons — [agent]
- Purple or indigo buttons — [agent]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction B over A | B | (non-interactive: agent chose) | B makes the traceable line the main object; A scores 6 house-style markers | yes — [agent] |
| Engine pick top-1 colour (Graphite and Signal) | Graphite and Signal | (agent) | Rank 1; quiet, high contrast, accent for action only | yes — [engine + agent] |
| Font pair top picks | Technor + IBM Plex Serif | (agent) | Engine top picks; body serif kept per skill rule | until critique — [engine] |
Rejected (final): Direction A (Ledger sheet) — scores 6 house-style markers, the default for this brief family.

## 12. Open decisions
- Docs URL and demo booking URL — decide at: launch; placeholders `#docs`, `#demo` — [inferred]
- Font files: Technor (Fontshare, self-host) and IBM Plex Serif must be downloaded into `./fonts/`; fallbacks until then — decide at: before launch — [engine]
- Body serif vs sans (IBM Plex Sans is the engine's second body pick) — decide at: critique round — [agent]
- Gate 1/2/3 approvals not given (non-interactive run); the direction is built as a draft — decide at: client review — [inferred]
- fennel-street.md is not in the project; the "opposite of" register is taken from the brief text — decide at: review — [inferred]
- Dark mode: not requested; light only — decide at: client review — [inferred]
- Pricing copy, footer links and © line are as supplied; no legal or security claims added — decide at: none — [client]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
