# Creative direction: Tallyroll
Status: draft (non-interactive fast run; no approval gate passed) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies (integrate); finance leads who sign off and reconcile — [client]
- The page must: send a careful buyer to the docs or to book a demo, having seen how a single invoice line traces back to its events — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Traceability: every invoice figure is explained by the events behind it — "Every cent traces back to an event." — [client]
- V2 Reconcilability: finance can check each line — "reconcile line by line" — [client]
- V3 Proof over promise: buyers distrust marketing and want to see how it works — "They distrust marketing and want to see how it works." — [client]

## 3. Positioning
- Category: usage billing for metered products (events in, invoices out) — [inferred]
- Alternatives: building metering and invoicing in-house from event logs and spreadsheets; the billing module of a payments platform; reconciling exported usage by hand each month — described by kind, not named — [inferred]
- Conventions:

  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Centered hero with two buttons | Challenge | V3: the first screen shows the invoice line, not a slogan — [agent] |
  | Blue as the lead brand colour | Challenge | Blue is context-only in the engine; Graphite leads, Signal Blue marks action only — [agent] |
  | Row of three feature cards | Avoid | The brief's three steps are sequential; cards imply equal parallel items — [agent] |
  | Stats row of large numbers | Avoid | No figures beyond the brief's pricing and example; V3 — [agent] |
  | Logo wall or testimonials | Avoid | None supplied; the brief forbids invented proof — [agent] |
  | Docs and demo as the two exits | Adopt | Buyers act on the facts and the docs; the brief names both actions — [agent] |

- Intended perception:
  - P1 "I could trace one invoice line to the events behind it" → check: an invoice line is visible with its expansion (31 daily totals) on the first desktop screen or one scroll below it
  - P2 "This was built by people who reconcile for a living" → check: figures are right-aligned with tabular numerals, and labels are exact copy from the brief with no adjectives added
  - P3 "Nothing here is selling to me" → check: no decoration, gradients, or icons; primary action is "Read the docs"
  — [inferred]
- Sophistication: considered — pricing as a percentage of billed revenue and a finance sign-off audience — [inferred]
- Differentiate on: the invoice line itself, expandable into the events that produced it — [inferred]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md" (brief register)
Reading: deliberate preference — the register is the user's words; `fennel-street.md` is referenced by the brief but is not in this project, so the contrast is read from the brief alone — [agent]

## 5. References (0–5)
None supplied. — [inferred]

## 6. Directions explored (2)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A · Ledger paper | agent | Category convention (finance-leaning) | P2 | Not selected | Follows the finance convention; little differentiation |
| B · Invoice as instrument | agent | P1, Differentiate on, V1 | P1, P2, P3 | **Selected** | Departs most from the category's shared layout |

Engine results (copied from scripts):
- Typography: headlines `technor` (Technor, FFL); body `ibm-plex-serif` (IBM Plex Serif, OFL) — [engine]
- Colour: `lib.graphite-and-signal` "Graphite and Signal" (Light, Neutral) — [engine]
- Direction A colour: `lib.bottle-green-ledger` "Bottle Green Ledger" (Ledger Cream / Bottle Green), follows finance-blue convention — [engine]

| Axis | A · Ledger paper | B · Invoice as instrument |
| --- | --- | --- |
| Composition | One reading column, headline then numbered spec list — because P2 | Asymmetric two-column grid: rules and steps left, a live invoice panel right — because P1 |
| Scale | Flat, even scale — because V2 restraint | One large headline, invoice figures set large — because P1 |
| Imagery | Type only — because V3 | The real product interface, built in HTML from the brief's facts — because P1 |
| Signature device | Ruled ledger line — because V2 | A trace: the invoice total connected to its 31 daily cells — because V1 |
| Colour proportion | Cream ground almost everywhere, green figure as structure — engine colours | Ground almost everywhere; Graphite as one solid invoice panel; Signal Blue only on action and trace — because P3 |
| Surface | Flat, square, hairline rules — because V2 | Flat, square, hairline rules; one solid panel — because P3 |
| House-style markers (H1–H6) | 6: H1, H2, H3, H4, H5, H6 | 2 (H3, H4); the panel and product mock break H1, H2, H5, H6 |
| Distinct on | Composition, Imagery, Signature, Colour proportion, Surface (5 axes) | Same five axes |

Other-client test (B): could this belong to another client? Not as drawn: the expanding invoice line, the 31-cell trace and the copy are specific to usage billing.

## 7. Selected direction
Invoice as instrument — origin: agent — [agent]
The page leads with one invoice line that opens into its events, so a buyer checks the claim before reading any pitch. It serves V1 and V2 through the invoice itself, and P1 through P3 through restraint.
The one memorable thing: the invoice line opens into 31 days of cells.
House style: 2 markers (H3, H4) — below 4; no exception needed.

## 8. Design system
### Typography — [engine]
- Headlines: Technor (`technor`), weights 400–700, self-hosted — 
- Body: IBM Plex Serif (`ibm-plex-serif`), weights 400/500/600, self-hosted
- Code strings (`POST /v1/events`, `$0.0004`): set in the body family; no third family is added
- Font files are not yet in the project; the page falls back to system-ui and Georgia until `fonts/Technor.woff2` and `fonts/IBMPlexSerif.woff2` are placed (see Open decisions)

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`)
- Ground: `#F9FAFB` (Paper White) · Figure: `#15181E` (Graphite) · Accent: `#0E6EE6` (Signal Blue)
- Text: `#3C3F46` (10.09:1 on ground) · Muted text: `#6B6F76` (4.82:1 on ground)
- Tints of figure (rules, cell fills): `#44484F`, `#797E85`, `#B2B8C0`
- Figure on ground 17.01:1; button label on figure 17.01:1

### Layout plan — [agent]
- Default avoided: centered hero, three cards, stats row, testimonial strip, CTA band
- Visitor's questions in order: what does it do (headline + subhead); how does one number get checked (the invoice line); how is it integrated and how is it priced (steps, then the two columns)
- The one thing only this brief has: the expandable invoice line — it is the hero, as content
- Cut: stats, testimonials, logos, feature cards, a second hero
- Axis positions as set in §6 (B)

### Imagery plan — [agent]
- Job: make a visitor believe any figure can be checked — serves P1
- Kind: product interface (built in HTML) + one diagram (the trace)
- Shot list:
  1. The invoice line, collapsed, with its arithmetic: "API calls, March: 1,204,388 calls × $0.0004 = $481.76" — top of the invoice panel, right column
  2. The same line expanded: 31 daily cells (Mar 1–31) with a sum footer "31 daily totals" — directly below, same panel
  3. The trace connector from the line to the cell grid — thin Signal Blue rule
- Treatment: no values are invented for the daily cells; cells show date labels only and a fill that marks the day; panel is a solid Graphite field with Paper White type; images meet the grid by being the grid
- Ships now: all three (HTML/CSS). No photography is used.

### Judgment tokens — [agent]
- Spacing: 8px base; section gaps differ by content (large between the hero and steps, tight inside the invoice) — avoids same-padding-everywhere
- Radii: 0 on all surfaces; the invoice panel stays square to read as a document
- Rules: 1px, figure tint 2 (`#797E85`)
- Motion: none beyond a 150ms expand on the invoice line; respects reduced motion

## 9. Constraints (pass/fail on a screenshot)
- C1 Headline is the largest type on the page and at least 4× body size; nothing else competes in size → check: measured font sizes in render
- C2 P1: the invoice line with its arithmetic is fully visible on a 1440×900 first screen, and its "31 daily totals" expansion is one click away → check: screenshot shows the line and the toggle without scrolling
- C3 Signal Blue appears only on the primary action, links, focus and the trace rule; no blue fills or gradients → check: screenshot and CSS
- C4 P2: invoice figures are right-aligned with tabular numerals and the copy matches the brief verbatim (no added claims or numbers) → check: diff copy against the brief
- C5 No centered hero, no card row, no gradient, no icon glyphs, no pill badge → check: screenshot
- C6 P3: "Read the docs" is visually stronger than "Book a demo" → check: screenshot
- C7 Phone width 390px: no horizontal scroll; the invoice line stays legible without zoom → check: phone screenshot

## 10. Avoid (≤6)
- A centered hero headline or a hero centred over a button pair — [agent]
- A row of three cards or equal feature tiles — [agent]
- Gradient backgrounds or gradient buttons — [agent]
- Emoji or decorative icons — [agent]
- A row of large statistics or a logo/testimonial strip — [agent]
- Blue used as a decorative fill — [agent]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | B · Invoice as instrument | (no user; non-interactive run) | Fast-mode Gate 2 rule: the direction that departs most from the category's shared layout while serving the page job | Settled = until the user reviews |
| Colour | Graphite and Signal (engine pick #1) | — | Engine pick for enterprise software and finance; no convention followed | yes |
| Fonts | Technor + IBM Plex Serif (engine top pair) | — | Engine top pair for technical + neutral | yes |
Rejected (final): none.

## 12. Open decisions
- Font files: woff2 not yet downloaded or placed in `fonts/`; the page uses fallbacks until they are — decide at: before launch — [agent]
- Technor is Fontshare FFL: self-host only, keep the font files out of any public repo — decide at: launch — [engine]
- Sophistication "considered" rests on inferred pricing and audience signals — decide at: Gate 1 confirmation — [inferred]
- Docs, demo and footer link targets are not given; they are `#` placeholders — decide at: launch
- Direction B was chosen without user approval; Status stays draft — decide at: Gate 3 review
- Layout of the daily cells after 31 days: no values shown; the user may want real daily figures — decide at: build review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1 (desktop + phone) | C5 | fail (uniform spacing) | Bug: `section.block` padding overrode per-section rules | Fixed: per-section padding; check-layout now clean |
| Round 2 (phone) | C7 | fail (headline flush to left edge) | Bug: `.hero` padding shorthand removed the side gutter | Fixed: gutter restored; check-layout clean |
| Round 2 | C1–C4, C6 | pass on desktop screenshot | — | — |
| Round 2 | Fonts | open | Lesson: Technor and IBM Plex Serif woff2 files are not in `fonts/`, so the render uses system fallbacks | Open decision; placing the files is the fix |
Two critique rounds used (cap reached). Status stays draft.
