# Creative direction: Tallyroll
Status: draft · Mode: fast · v1
(Non-interactive run. No approval gate was passed. Everything below is built against as draft; unconfirmed items are tagged `inferred` or listed under Open decisions.)

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies (integrate); finance leads who sign off and reconcile line items monthly — [client]
- The page must: send a careful buyer to the docs or to book a demo, having believed that every invoiced amount traces to its events — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceable: every invoiced figure can be followed back to the events that produced it — "Every cent traces back to an event." — [client]
- V2 Calm and precise: no hype, measured tone, technical register — "technical, calm, precise" (register line) — [client]
- V3 Shown, not claimed: the buyer sees how it works rather than being told it is trustworthy; they "distrust marketing" — [client]

## 3. Positioning
- Category: software that bills metered usage and produces invoices a finance team can reconcile — [inferred]
- Alternatives: a spreadsheet or in-house script that totals usage each month; a billing suite that bills subscriptions first and usage as an add-on — described by kind, not named — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Blue as the lead colour across SaaS and fintech (engine: `finance-blue`, `technology-blue`, context) | Challenge | Blue makes it interchangeable with every other product; V2 wants precision, not signalling — [agent] |
  | Gradient hero behind a centred headline and two buttons | Avoid | Reads as launch-page marketing; V3 — [agent] |
  | Row of big numbers ("10k+ users") | Avoid | No such figures in the brief; V3 — [agent] |
  | Testimonials and logo wall | Avoid | None supplied in the brief, and the copy adds no testimonials; V3 — [agent] |
  | Concrete, checkable detail near the top (code, arithmetic, documentation links) | Adopt | The audience checks facts before acting; V1 — [agent] |
- Intended perception: three qualities a stranger reports after five seconds, each checkable on a screenshot — [inferred]
  - P1 Traceable → check: the invoice line with its arithmetic is visible in the first screen on desktop
  - P2 Calm, unhurried → check: no gradient, no shadow, no competing large element beside the headline
  - P3 Written by people who have reconciled invoices → check: the example line shows real arithmetic and named export targets, with no adjectives standing in for them
- Sophistication: considered — signal: "0.5% of billed revenue, no platform fee" and a finance sign-off step imply a considered purchase, not an impulse one — [inferred]
- Differentiate on: the invoice line that opens into the events and daily totals behind it, on the page itself — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md" (brief register line)
Reading: deliberate preference — the register is the brief's own words; "the opposite of fennel-street.md" is a pointer to a file not present in this project, so it is not used as a reference — [agent]

## 5. References (0–5)
None supplied in the brief. — [inferred]

## 6. Directions explored (3)
Each direction answers the same brief. Font pairs and colour directions are engine results.

| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Overcast | agent | V1, V2; convention blue challenged | P1, P2, P3 | **Selected** | — (non-interactive: agent selection, see §11) |
| B. Graphite and Signal | agent | Engine's default pick (`lib.graphite-and-signal`) | P2 | Not selected | — |
| C. Concrete and Brass | agent | V2 materiality | P1 | Not selected | — |

Engine inputs shared by all directions:
- Typography [engine]: Switzer (`switzer`) headlines; IBM Plex Serif (`ibm-plex-serif`) body
- Code [engine]: Iosevka (`iosevka`) — see §8 for why not the top pick
- Colour [engine]: A = Overcast (`lib.overcast`); B = Graphite and Signal (`lib.graphite-and-signal`); C = Concrete and Brass (`lib.concrete-and-brass`)

| Axis | A. Overcast | B. Graphite and Signal | C. Concrete and Brass |
| --- | --- | --- | --- |
| Composition | One reading column; the invoice line sits as a ruled table in the second column — because V1 | Single column with a product panel above the fold — because the engine's default fits working interfaces | Two columns, one drawing-like plate — because V2 materiality |
| Scale | One large headline, then one flat text scale — because P2 | Large headline plus a bold blue CTA row — because a conventional SaaS reading | Large headline, brass rules as the only secondary emphasis — because V2 |
| Imagery | The invoice line and the expand state built in HTML and CSS — because P1 | Product interface panel — because the category shows the app | Ruled diagrams built in SVG — because V2 |
| Signature device | Ruled ledger lines, with the expanded daily totals hanging under each invoice line — because V1 | A blue focus-ring and link system — because the engine's accent use | A brass hairline marker per item — because V2 |
| Colour proportion | Ground almost everywhere; figure for type and rules; no accent — because the blue convention is Challenged | Ground almost everywhere; blue at about 3% — because the engine's area split | Ground and figure with brass at about 4% — because V2 |
| Surface | Flat paper, square edges, no shadows — because V2 and "printed" reconciliation records | Flat, square, no shadows — because the engine's default | Flat with a warm ground — because V2 |
| House-style markers (H1–H6) | 3: H1 (type and built product only), H4 (square and flat), H5 (left headline then a printed spec) | 5: H1, H2 (pale ground, one muted figure), H4, H5, H6 | 4: H1, H3 (hairlines carry hierarchy), H4, H5 |
| Distinct on | Imagery, signature device, colour proportion, surface, scale | Imagery, signature device, colour proportion, composition | Imagery, colour proportion, ground lightness, signature device |

Other-client test (agent-originated directions): A could not belong to a generic SaaS billing product because its figure-only palette and ruled ledger device are built around the invoice line, which only Tallyroll's own example shows.

## 7. Selected direction
Overcast — origin: agent — [agent]
A printed-ledger page on a cool gray ground: the one invoice line in the brief is the page, its arithmetic checkable at a glance, and every other element stays quiet. It serves V1 (traceable) and V2 (calm, precise), and P1–P3. It is the direction that challenges the blue-lead convention without giving up legibility; Graphite and Signal is the engine's default and was passed over because it reads as the category, and Concrete and Brass was passed over because its brass accent leans toward premium signalling the brief does not ask for.
The one memorable thing: the invoice line that opens into the days behind it, printed like a ledger.
House style: 3 markers — under the threshold, no house-style justification required. — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Switzer (`switzer`), FFL, self-host only, keep files out of public repos. Fallback: `system-ui, -apple-system, "Segoe UI", sans-serif` — [engine]
- Body: IBM Plex Serif (`ibm-plex-serif`), OFL. Fallback: `Georgia, "Times New Roman", serif` — [engine]
- Code (invoice arithmetic, the `POST /v1/events` line): Iosevka (`iosevka`), OFL, prebuilt web package. Switched from the top pick Departure Mono (`departure-mono`): its pixel-only sizing in 11px steps and single weight bite on a ruled table of numbers, and its lo-fi retro feel works against V2. Fallback: `ui-monospace, "SF Mono", Menlo, Consolas, monospace` — [engine] for the pick, [agent] for the switch
- Font files are not bundled in the single HTML file; they must be self-hosted under `./fonts/`. Until then the fallback stacks render — [inferred]

### Color — [engine]
- Direction: Overcast (`lib.overcast`) — Neutral, Light foundation, Neutral structure
- Ground: Overcast #D1D9DF — oklch(0.88 0.012 240)
- Figure: Wet Slate #161B20 — oklch(0.22 0.012 245)
- Text: #252B30 — contrast 10.02:1 on ground
- Text muted: #545B60 — contrast 4.83:1 on ground
- Tints (engine): #444A50, #788086, #B1B9C0
- No accent. Links and focus are marked by underline and figure weight, not colour — [agent]

### Layout plan — [agent]
- Default (what the template would reach for): nav, centred hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor's questions, in order: (1) What does it do to my usage? (2) Can I trace a line to its events? (3) How does it work? (4) What do finance and engineering get? (5) What does it cost? (6) Where do I go next: docs or demo?
- The one thing only this brief has: the invoice line `API calls, March: 1,204,388 calls × $0.0004 = $481.76`, which opens into the daily totals behind it. It is the first thing after the headline, as content, not decoration.
- Cut: the stats row, testimonials, logo wall, three-card feature grid (the brief has two audiences, not three parallel items, so finance and engineering sit as a two-column split), and the CTA band (the actions are in the hero and the footer repeats the links).
- Six axis positions: see the Overcast column of the §6 table.

### Imagery plan — [agent]
- Job: make a visitor believe the numbers trace to events — serves P1
- Kind: product interface, built in HTML and CSS. No photography: the brief supplies no images, and the trust claim rests on checkable numbers, not on pictures — [agent]
- Shot list (built, not photographed):
  1. The example invoice line, full width of the reading column, with the arithmetic in the figure colour.
  2. The same line expanded into its daily totals: a ruled table with the 31 rows labelled by day. Values are not invented; each row reads "daily total · from event log" with the value left as a dash, since no daily figures are in the brief.
  3. The three steps as numbered ruled rows (send events, define pricing, invoice).
  4. The `POST /v1/events` line as a code block in the code font.
- Treatment: figure and ground only, no tints beyond the engine's three. The invoice mock sits on the page ground with rules, not in a card. Nothing is cropped; there are no images to crop.
- Ships now: all four frames above are built in full. No frame awaits a client asset.

### Judgment tokens — [agent]
- Radius: 0. Square edges match V2 and the ledger device. Focus outlines use the figure colour at 2px.
- Hairlines: 1px in the engine's tint-3 (#B1B9C0), to draw ledger rules without boxes.
- Spacing: one vertical rhythm of 8px steps; sections separated by a hairline rule, not by spacing alone, so the page reads as one document.
- Motion: none beyond a 150ms opacity transition on the expand control. No parallax, no entrance animation (matches V2).
- Shadows: none.

## 9. Constraints (8, each pass/fail on a screenshot)
- C1 Headline is the largest text on the page, at least 4× body size, and nothing else competes at that size → check: first-screen screenshot at 1280×800; measure headline against body. — [agent]
- C2 The example invoice line is visible in the first screen on desktop and shows its arithmetic (1,204,388 × $0.0004 = $481.76) → check: first-screen screenshot. — [agent]
- C3 P1 Traceable: the expanded daily-total table is reachable from the invoice line, by a visible control, without leaving the page → check: click the control in a render and see the 31-row table. — [agent]
- C4 No gradients, shadows, rounded corners or blue anywhere; only the Overcast ground, figure and tints appear → check: computed styles and the screenshot. — [agent]
- C5 P2 Calm: no element other than the headline is larger than 1.25× body size above the fold → check: first-screen screenshot. — [agent]
- C6 Primary action "Read the docs" and secondary "Book a demo" both visible in the first screen, with the docs action visibly stronger → check: first-screen screenshot. — [agent]
- C7 Body and muted text use only the two engine pairs (10.02:1 and 4.83:1) and pass 4.5:1 → check: computed colours against the engine values. — [engine]
- C8 At 390px width there is no horizontal page scroll, and the invoice line stays readable (wraps or stacks rather than clipping) → check: phone screenshot and the checker's overflow report. — [agent]

## 10. Avoid (≤6, each observable)
- Gradient backgrounds or gradient text
- A testimonial, logo wall or "trusted by" row
- A row of big numbers such as "10k+" or "99.9%"
- Blue, or any accent hue, on links, buttons or the hero
- Rounded cards with shadows
- Emoji or icon-font glyphs used as feature icons

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | Overcast | — (non-interactive; no pick given) | Challenges the blue convention, scores 3 house markers, and carries V1 through the invoice line. Graphite and Signal is the engine default but scores 5 markers and sits with the category. | Settled = until the user confirms at Gate 2 |
| Body font | IBM Plex Serif (engine top pick) | — | Top pick; "printed" register suits Overcast | yes |
| Code font | Iosevka (switched from Departure Mono) | — | Departure Mono's caveats (11px steps, single weight) and retro feel bite the calm, ruled table | yes |
| Accent colour | None | — | Ledger register; the engine's own do/avoid says do not add an accent to rescue the calm | yes |

Rejected (final): none.

## 12. Open decisions
- Gate 1 and Gate 2 confirmations (Context, Values, Positioning, direction choice) — decide at: user review — [inferred]
- Font files: self-host Switzer, IBM Plex Serif and Iosevka under `./fonts/`; the Switzer licence bars public repos — decide at: delivery — [inferred]
- Docs, Demo, Pricing, Status, Security and Contact targets: placeholders (`#`) until the client supplies URLs — decide at: delivery — [inferred]
- Sophistication "considered" is an inference from price and buyer type — decide at: Gate 1 — [inferred]
- Whether the period-specific copy "March" is the right example month, and whether the expanded table should show real figures from a client account — decide at: client review — [inferred]
- Positioning Challenge on blue: confirm the client wants to move off the category colour — decide at: Gate 2 — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| (filled in at critique) | | | | |
