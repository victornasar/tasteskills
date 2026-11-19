# Creative direction: Tallyroll
Status: draft (non-interactive fast run; Gate 1 and Gate 3 approvals not given) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies (integrate), and the finance leads who sign off and reconcile — [client]
- The page must: make a careful buyer trust Tallyroll with revenue, then send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceable: every cent on an invoice opens into the events behind it — "Every cent traces back to an event." — [client]
- V2 Checkable: finance can reconcile each line; the arithmetic is shown, not claimed — "reconcile line by line" — [client]
- V3 Calm and precise: no hype, no decoration; the register is technical, calm, precise — [client]
- V4 Plain terms: pricing stated in full, no platform fee — "0.5% of billed revenue, no platform fee" — [client]

## 3. Positioning
- Category: usage-based billing (invoices generated from metered usage) — [inferred]
- Alternatives (described by kind, no names given): building the invoice run in-house from event logs and spreadsheets; a subscription-billing platform that treats usage as an add-on; finance rebuilding usage invoices by hand from exports — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Centered hero with a slogan and two buttons | Challenge | V1: the first screen must show the invoice line, not a slogan. Perception P1 |
  | Pricing as tiers with "contact sales" | Challenge | V4: the price is one stated sentence the buyer can act on |
  | Demo as the only call to action | Challenge | Audience acts on docs first; docs is the primary action per the brief |
  | Security or compliance link in the footer | Adopt | Finance leads look for it before signing; the brief lists Security in the footer |
  | Testimonial or customer-logo rows | Avoid | Brief supplies no testimonials; V2 requires the mechanism, not social proof |
  — [agent]
- Intended perception:
  - P1 "I can trace any total on this invoice back to its events." → check: the expanded invoice line is visible on the first two screens.
  - P2 "The people who wrote this read invoices, not ads." → check: no gradients, glows, emoji or decorative imagery; figures are real arithmetic.
  - P3 "The arithmetic checks out." → check: "1,204,388 calls × $0.0004 = $481.76" renders exactly as the brief gives it.
  — [inferred] (derived from V1–V3; not stated by the client as perceptions)
- Sophistication: considered — signal: a usage-priced buyer with a finance sign-off, price stated as a rate on billed revenue — [inferred]
- Differentiate on: the invoice line opens into the events and daily totals behind it, on the page itself — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md." (fennel-street.md is not in the project; its content is not read) — [client]
Reading: the opposite of an ornate, warm, editorial register: few ornaments, mechanical rhythm, tabular figures — [inferred]

## 5. References (0–5)
None supplied.

## 6. Directions explored (2)
Font and colour choices are engine results. Positions on axes are [agent].

| Axis | A · Trace (selected) | B · Ledger paper |
| --- | --- | --- |
| Headlines font | Overpass (`overpass`) — find-font headlines pick #2 | Steps Mono (`steps-mono`) — find-font headlines pick #1 |
| Body font | IBM Plex Sans (`ibm-plex-sans`) — find-font body pick #2 | IBM Plex Serif (`ibm-plex-serif`) — find-font body pick #1 |
| Colour | Graphite and Signal (`lib.graphite-and-signal`) — find-color pick #1 | Bottle Green Ledger (`lib.bottle-green-ledger`) — find-color rank #2 |
| Composition | Asymmetric: headline left, live invoice line right on the first screen; then ordered steps as a sequence, not cards — because P1, V1 | One reading column, printed-document order — because a convention-matching document feel |
| Scale | One big moment (headline), then the expanded invoice as a second, mid-size moment — because P1 | Flat, even scale from top to bottom — because a single document |
| Imagery | The real product interface, built in HTML from the brief's own facts (invoice line, expansion, 31-tick day strip) — because P1 | Type only — because P2 |
| Signature device | Ruled ledger leader lines and a trace line from invoice total to events — because V1 | Hairline rules with small uppercase labels — because a ledger page |
| Colour proportion | Ground almost everywhere; Graphite for structure; Signal Blue at most a few percent for links, focus and the trace line — because V3 | Cream ground with Bottle Green figure throughout — because the category's expected palette |
| Surface | Flat, square, 2px radius only on the invoice sheet; no shadows — because V3 | Flat, square, no shadows — because V3 |
| House-style markers (H1–H6), on the direction as written | 2: H2 (pale ground, one dark figure), H4 (flat and square) | 6: H1, H2, H3, H4, H5, H6 |
| Distinct on | Composition, scale, imagery, signature device, colour proportion (5 axes) | — |

Agent-originated rows also answer: Other-client test: the invoice line that expands into its events is a fact about this product's billing model; a generic billing vendor's page could not show this exact arithmetic — [agent]

Direction B is not selected because it scores 6 house-style markers with no Positioning that requires the house style. Direction A challenges three conventions and scores 2.

## 7. Selected direction
A · Trace — origin: agent — [agent]
A product page that is the invoice. The first screen shows a real invoice line with its arithmetic; the reader opens it and sees the 31 daily totals behind it. Serves V1, V2 and P1, P3.
The one memorable thing: a line on an invoice that opens into its events, drawn on the page.
House style: 2 markers on direction (H2, H4); recheck on render in Phase 5.

## 8. Design system
### Typography — [engine]
- Headlines: Overpass (`overpass`), weights 500–700, OFL, variable; self-host — find-font
- Body: IBM Plex Sans (`ibm-plex-sans`), weights 400 and 600, OFL, variable; self-host — find-font
- Code and invoice figures: Iosevka (`iosevka`), OFL — find-font code role, pick #2. Departure Mono (pick #1) is a pixel face whose lo-fi vibe conflicts with V3, so it is not used — [agent]
- Font files: self-hosted only, from `./fonts/`. This file does not bundle them; until they are added, the page falls back to the system sans and monospace stacks — [engine] + [agent]
- The find-font CSS templates and file names: `./fonts/Overpass.woff2`, `./fonts/IBMPlexSans.woff2`, `./fonts/Iosevka.woff2` — match to the downloaded files — [engine]

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), find-color pick, Light foundation, Neutral structure — find-color
- Ground: Paper White `#F9FAFB` (OKLCH 0.985 0.002 250) — find-color
- Figure: Graphite `#15181E` (OKLCH 0.21 0.012 260) — find-color; figure on ground 17.01:1 — find-color
- Accent: Signal Blue `#0E6EE6` (OKLCH 0.56 0.2 258) — find-color; used only for focus, the trace line and link underlines, never for body text — [agent]
- Text: `#3C3F46` on ground, 10.09:1 — find-color; muted text `#6B6F76`, 4.82:1 — find-color
- Button: Graphite fill, Paper White label, 17.01:1 — find-color
- Convention note: find-color ran with `--convention mix`; the Blue-as-lead-colour convention is recorded as context. The accent is kept below the lead role, so the page does not follow it — [agent]

### Layout plan — [agent]
- Default section list (what check-layout expects a template to be): nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Cut: stats row, testimonials, three feature cards. None answers the visitor's questions.
- Visitor's questions, in order: what does it do (headline + invoice line) → how does it work (three ordered steps, with the POST line) → can finance check it (the expanded line and the finance and engineering facts) → what does it cost (one sentence) → how do I start (docs, demo).
- Lead with the one thing only this brief has: the invoice line that expands into events.
- Axis positions: Composition asymmetric two-column hero; scale one big moment plus the expanded invoice; imagery is the real product interface; signature is the ruled trace line; colour is ground-dominant with Signal Blue at a few percent; surface is flat and square.

### Imagery plan — [agent]
- Job: make the buyer believe the total is checkable — serves P1, P3.
- Kind: product interface built in HTML and CSS, plus a diagram of the trace line.
- Shot list (built, not photographed):
  1. Invoice line, first screen, right of the headline: "API calls, March: 1,204,388 calls × $0.0004 = $481.76".
  2. The same line open: 31 daily-total ticks in a single row, each tick a daily total, joined by the trace line to the line above. Ticks carry no invented values: they show count only, labelled "31 daily totals".
  3. Event row: a sample `POST /v1/events` request in the code face, sitting under step 1.
- Treatment: the invoice sits on a 2px-radius sheet, 1px hairline border, no shadow; the trace line uses Signal Blue; no image is cropped.
- Ships now: all three above. No photographs, no stock images, no client logos.
- Honesty: no fake customers, no invented per-day values, no claims beyond the brief.

### Judgment tokens — [agent]
- Spacing: 8px base; section gaps differ by content (large between the hero and steps, tight inside the invoice) — ties to V3.
- Radii: 0 on text and rules; 2px only on the invoice sheet — ties to V3, flat and checkable.
- Motion: one transition, the invoice expansion, 150ms ease-out — ties to V1, the expansion is the product's behaviour. No other motion.
- Shadows: none.

## 9. Constraints (8, each pass/fail on a screenshot)
- C1 Headline is at least 4× body size; no other element competes at that size → check: computed sizes in check_layout output; visual in shot. — [agent]
- C2 The invoice line with its arithmetic is fully visible on the desktop first screen (1440×900), reading "1,204,388 calls × $0.0004 = $481.76" → check: first-screen screenshot. — [agent]
- C3 The expanded line shows 31 daily-total ticks linked to the line by a visible trace → check: open state screenshot. — [agent]
- C4 Perception P1: a viewer reports after five seconds that totals trace to events → check: the invoice and its expansion are in the first two screens, above any section heading. — [agent]
- C5 "Read the docs" is visibly the stronger action than "Book a demo" → check: the primary button is filled, the secondary is outlined, both above the fold. — [agent]
- C6 No gradients, glows, emoji, pill badges, rounded boxes beyond 2px, or shadows → check: check_layout report shows none of the nine patterns except rounded boxes and centered hero, both removed. — [agent]
- C7 Phone 390px: no horizontal scroll; the invoice line wraps without splitting any figure from its unit → check: phone screenshot and scrollWidth. — [agent]
- C8 Body text contrast at least 4.5:1 on Paper White → check: #3C3F46 on #F9FAFB, 10.09:1 by find-color. — [engine]

## 10. Avoid (6, each observable)
- Gradient or glow backgrounds
- Rows of three feature cards
- Stat rows of large numbers
- Pill badges above the headline
- Testimonial or customer-logo rows
- A "contact sales" pricing tier

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A · Trace | A | not confirmed (non-interactive) | Only direction that serves P1 and avoids house style | until Gate 2 confirmation |
| Body face: IBM Plex Sans over Plex Serif | Sans | not confirmed | Serif is the engine's #1 body pick; the UI-like sans fits the technical register and matches the headline family | until Gate 3 |
| Code face: Iosevka over Departure Mono | Iosevka | not confirmed | Departure's pixel look conflicts with V3 | yes |
| Signal Blue limited to focus, links and trace | Limited | not confirmed | Keeps blue from reading as decoration | yes |
| Rejected (final): Direction B · Ledger paper | — | not chosen | 6 house-style markers, no Positioning requiring the house style | yes |

## 12. Open decisions
- Gate 1: Positioning readings (alternatives by kind, conventions, perceptions P1–P3) — decide at Gate 1 — [inferred]
- Gate 3: spec approval; status stays draft until then — decide at Gate 3 — [inferred]
- Fennel-street contrast: fennel-street.md is not in the project, so the "opposite" reading is inferred from the brief's words — decide at Gate 1 — [inferred]
- The 31 daily totals: shown as unlabelled ticks with no values, since the brief gives no per-day numbers. Decide at the client-data checkpoint whether real values replace them — [inferred]
- Docs URL, demo booking URL, Status, Security, Contact and © links: placeholders (`#`) until the client gives URLs — decide at the client-data checkpoint — [inferred]
- Font files: the three find-font picks must be downloaded to `./fonts/`; until then the fallbacks show — decide at build hand-off — [inferred]
- Wordmark: no logo supplied; "Tallyroll" set in the headline face — decide at Gate 3 — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| (filled in Phase 5) | | | | |
