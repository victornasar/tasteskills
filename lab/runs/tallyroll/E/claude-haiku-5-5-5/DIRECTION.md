# Creative direction: Tallyroll
Status: draft (non-interactive fast run; no user approval yet) · Mode: fast · v1

Note: `fennel-street.md` is referenced by the brief as the register to oppose, but it is not present in the project. The opposite register is taken from the brief's own words: technical, calm, precise. [inferred]

## 1. Context
- Product: usage-based billing API. It turns raw usage events into invoices. — [client]
- Audience: engineering leads at usage-priced software companies (integrate); finance leads who sign off and reconcile line items. — [client]
- The page must: send a careful buyer to the docs or to book a demo, having seen how a line on an invoice traces back to events. — [client, job wording inferred]

## 2. Values (user-owned, 2–5)
- V1 Traceable: every figure can be followed back to its source events — "Every cent traces back to an event." — [client]
- V2 Precise: numbers, endpoints and rules are shown exactly, not described — "reconcile line by line" — [client]
- V3 Calm: no urgency, no selling tone; the buyer distrusts marketing — "They distrust marketing and want to see how it works." — [client]

## 3. Positioning
- Category: billing for metered usage, bought by engineering and signed off by finance. — [inferred]
- Alternatives: in-house scripts that turn event logs into spreadsheets; billing platforms built around seats or plans rather than metered usage. Described by kind; no competitor named by the client. — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Blue as the lead colour (find-color `technology-blue` / `finance-blue`, context) | Challenge | Makes pages interchangeable. Accent is held to 3% of area so blue means "act here" (V3). — [agent] |
  | Code sample or endpoint as the first proof | Adopt | Engineers judge integration from the endpoint; the brief gives `POST /v1/events`. — [agent] |
  | Customer logo strip | Avoid | The brief names no customers; invented logos would break V1 and the honesty rule. — [agent] |
  | Public pricing hidden behind "contact sales" | Avoid | The brief states the price (0.5%, free to $10,000 a month); showing it fits V2 and the finance reader. — [agent] |
  | Dark developer-tool theme with a glowing accent | Challenge | Reads as a product showcase rather than a record a finance team can file. — [agent] |
- Intended perception:
  - P1 Every figure traces to its source → check: the example invoice line and its arithmetic are visible without scrolling on desktop, and the line's expansion is shown.
  - P2 Written for someone who will check it → check: arithmetic is shown in full (quantity × rate = amount); no adjective-only claims in the body.
  - P3 Quiet, not sold to → check: one accent colour; no gradients, shadows, motion or superlatives in the render.
  — [inferred]
- Sophistication: considered — signal: finance sign-off, line-level audit trail, and pricing stated as a single percentage with no platform fee. — [inferred]
- Differentiate on: the invoice line that opens into the daily totals behind it, shown on the page rather than described. — [agent]

## 4. Opening vocabulary
"Technical, calm, precise. The opposite of fennel-street.md." (brief register line, as given)
Reading: deliberate preference — the brief's register words are the direction; fennel-street.md was not available to confirm the opposite. — [agent]

## 5. References (0–5)
None supplied. [client]

## 6. Directions explored (2)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A · Graphite ledger | agent | V1, V2, P1; challenges blue convention | Engineers and finance reading a record | Selected (non-interactive) | — |
| B · Cream ledger | agent | V2, P2; adopts the finance-ledger look | Finance reader; slower, print-like read | Not selected | — |

Direction A engines: headlines Technor (`technor`); body IBM Plex Sans (`ibm-plex-sans`); colour `lib.graphite-and-signal` (Graphite and Signal). — [engine]
Direction B engines: headlines Trench Slab (`trench-slab`); body IBM Plex Serif (`ibm-plex-serif`); colour `lib.bottle-green-ledger` (Bottle Green Ledger). — [engine]

| Axis | A · Graphite ledger | B · Cream ledger |
| --- | --- | --- |
| Composition | Asymmetric two-column grid: rule-ledger prose on the left, the worked invoice line as the right-hand object — because P1 | One reading column, headline then a printed spec sheet — because P2 |
| Scale | One large headline, body text at one size in every section — because V3 (quiet) | Several mid-size moments, one per section — because P2 (written to be checked) |
| Imagery | Data drawn as a picture: an illustrative 31-bar schematic of daily totals, labelled as illustrative — because P1 | The invoice drawn as a ruled cream sheet, in SVG — because P1 |
| Signature device | Right-aligned tabular figures on a ruled line, so every amount lines up — because P1 | Leader lines from each invoice line to its events — because P1 |
| Colour proportion | Ground almost everywhere; Signal Blue ≤3% for links, focus and the primary action — because blue convention is Challenge | Bottle Green figure as a large solid band for the invoice section — because finance convention is Adopt |
| Surface | Square, flat, no shadows, corners 0–2px — because V3 | Paper ground, 4px corners, no shadows — because the printed-document reading |
| House-style markers (H1–H6) | 3: H2 pale ground with one figure colour; H3 ruled lines carry structure; H4 square and flat | 3: H2; H4; H5 headline then document |
| Distinct on | Imagery, Composition, Scale, Signature device, Colour proportion, Surface (6) | — |

Other-client test (A): a different billing API could not use the 31-bar schematic and the right-aligned invoice line as its signature without changing the example, since the example comes from this brief's own figures. — [agent]

## 7. Selected direction
Graphite ledger (Direction A) — origin: agent — [agent]
A record-like page: one large headline, body in a plain sans, and the worked invoice line set as the object the buyer checks. It serves V1 and P1 directly, and it departs most from the category's blue, card-led layout. Selected because it departs most from the convention and serves P1. Non-interactive: no user pick.
The one memorable thing: a right-aligned invoice line whose 31 daily bars sit directly beneath it.
House style: 3 markers (H2, H3, H4); under the threshold of 4. — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Technor (`technor`), Fontshare FFL; weights 400–600 used. Self-host only; keep files out of public repos. — [engine]
- Body: IBM Plex Sans (`ibm-plex-sans`), OFL; weights 400, 500, 600. — [engine]
- Monospace for the endpoint and arithmetic: none returned by find-font for this brief; system monospace stack, flagged for a later `find-font` run with role `code`. — [inferred]

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), Light foundation, Neutral structure.
- Ground / figure / accent: `#F9FAFB` (Paper White) / `#15181E` (Graphite) / `#0E6EE6` (Signal Blue). Text `#3C3F46` (10.09:1 on ground); muted text `#6B6F76` (4.82:1 on ground); figure on ground 17.01:1; button label on figure 17.01:1. — [engine]
- Tints from `find-color apply`: figure tint-1 `#44484F`, tint-2 `#797E85`, tint-3 `#B2B8C0`. — [engine]
- Engine area split: 86/11/3 (ground / figure / accent). — [engine]

### Layout plan — [agent]
- Default: nav, centred hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor's questions in order: (1) what does it do; (2) how does a line trace back to events; (3) can finance export and reconcile it; (4) how do engineers integrate it; (5) what does it cost; (6) where do I go next (docs or demo).
- The one thing only this brief has: the invoice line that expands into its daily totals, placed high on the page.
- Cut: centred hero, feature cards, stats row, testimonials (none supplied), customer logos (none supplied), CTA band (one closing action row in the footer area instead).
- Axis positions: Composition — asymmetric two-column; Scale — one large headline, flat body scale; Imagery — data as picture (labelled illustrative) and the worked line; Signature device — right-aligned tabular figures on ruled lines; Colour proportion — ground dominant, accent ≤3%; Surface — flat, square, no shadows.

### Imagery plan — [agent]
- Job: a finance reader believes each total is a sum of dated events. — serves P1
- Kind: data drawn as a picture (illustrative schematic) + the real product interface built in HTML from the brief's facts.
- Shot list:
  1. The March API-calls line, set as a ruled row: "API calls, March: 1,204,388 calls × $0.0004 = $481.76", right-aligned amount, placed in the first viewport.
  2. Beneath that row, 31 thin bars (one per day) in Signal Blue on a ruled baseline, labelled "Illustrative shape of daily totals. Not real data." Placed directly under the line it explains.
  3. A code block with `POST /v1/events` in the Send-events step, on the figure colour ground, in the integration section.
- Treatment: no crops or photography; bars and rules use colour tokens only; visuals meet the grid inside the column, not full-bleed.
- Ships now: all three items above are built in HTML/SVG. No empty frames.

### Judgment tokens — [agent]
- Spacing: 8px base; section gaps 96px desktop, 56px phone, because the page is read in long sessions, not scanned.
- Radii: 0 on surfaces, 2px on the primary button; no other rounding.
- Motion: none; focus rings only, in Signal Blue.
- Imagery: as above.

## 9. Constraints (pass/fail on a screenshot)
- C1 P1 trace: the March invoice line, with its full arithmetic and its amount, is visible in the first 900px of the desktop render → check: text "1,204,388 × $0.0004 = $481.76" visible without scrolling. — [agent]
- C2 Type scale: the headline is at least 4× the body size, and no other element competes in size → check: headline font-size ≥ 4× body font-size in computed styles and in the screenshot. — [agent]
- C3 P3 quiet: Signal Blue appears only on the primary action, links and focus; no gradients, shadows or motion → check: blue appears only on those three roles in the render; no `box-shadow` or `gradient` in computed styles. — [agent]
- C4 Honest data: the 31-bar schematic is labelled illustrative, and no number appears that is not in the brief → check: the label is visible next to the bars; every figure matches the brief's copy. — [agent]
- C5 Mobile: at 390px wide, the invoice line wraps without horizontal scroll and the arithmetic stays readable → check: no horizontal scrollbar; the line's full text is visible on the phone render. — [agent]
- C6 Actions: "Read the docs" is the primary action and "Book a demo" the secondary, both visible in the first viewport → check: both buttons present, and "Read the docs" is visually stronger. — [agent]

## 10. Avoid (≤6)
- Gradient or glow backgrounds
- Rounded cards with shadows
- A customer logo strip or testimonial block
- A three-card feature row
- A row of large statistics
- Blue used as decoration rather than for an action

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A · Graphite ledger | — (non-interactive) | Departs most from the category's blue, card-led layout; serves P1 | Until client review |
| Accent | Signal Blue ≤3% | — | Challenge blue convention; V3 | Until client review |
| Fonts | Technor + IBM Plex Sans | — | Engine top pick for the brief's feel | Until client review |

Rejected (final): none.

## 12. Open decisions
- Real daily totals for the March line, replacing the illustrative bars — decide at: client review — [inferred]
- Docs, Status, Security, Contact, Pricing and demo-booking URLs; placeholders `#` in the build — decide at: client review — [inferred]
- Wordmark or logo: none supplied; the build uses the text "Tallyroll" in the headline face — decide at: client review — [inferred]
- Dark theme: not requested; the build is light only — decide at: client review — [inferred]
- Monospace face for code and arithmetic: not picked by find-font for this brief; a `code` role run is needed — decide at: build follow-up — [inferred]
- Font files: Technor and IBM Plex Sans woff2 files are not bundled (no approved download in this run); the page declares them and falls back to system stacks — decide at: build follow-up — [inferred]
- Approval of this spec: non-interactive run, Status stays draft — decide at: Gate 3 with the user — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Render 1, desktop | C3 quiet | Fail: bars were Signal Blue | Bug | Bars changed to figure tint-1; blue kept for links, focus, hover |
| Render 1, desktop | House style | 4 markers (H2, H3, H4, H5) | Bug | Moved H3 (rules no longer carry hierarchy) and H5 (steps become a three-column row, not a printed list). Recount: 3 (H2, H4, H6 hesitation) |
| Render 1, desktop | check-layout | Uniform section spacing flagged | Bug | Section paddings varied (128 / 48 / 80 / 96px) |
| Render 2, desktop + phone | C1 | Pass | — | Line "1,204,388 calls × $0.0004 = $481.76" visible at y≈298px. Spec wording said "1,204,388 ×"; page follows the brief's copy, so C1 text in this file is loose |
| Render 2, desktop | C2 type scale | Pass | — | 68px headline vs 16px body = 4.25× |
| Render 2, phone | C2 type scale | Fail: 44px vs 16px = 2.75× | Lesson | Not fixed. Phone headline at 4× would be ~64px and wrap to five lines. Decide at client review whether C2 is desktop-only |
| Render 2, desktop + phone | C4 honest data | Pass | — | Bars labelled illustrative; figures match the brief |
| Render 2, phone | C5 mobile | Pass (visual) | — | Screenshot shows no overflow and the invoice line fits; no measured scrollWidth |
| Render 2, desktop | C6 actions | Pass | — | Filled "Read the docs", outlined "Book a demo" |
| Stop | Two-round cap | Used one fix round | — | Stopped at one round because the remaining failures were checkpoint lessons, not bugs |
