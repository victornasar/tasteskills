# Creative direction: Tallyroll
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate), and finance leads who sign off and reconcile monthly — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability — "Every cent traces back to an event" — [client]
- V2 Show how it works, no marketing — "They distrust marketing and want to see how it works" — [client]
- V3 Calm precision — "technical, calm, precise" — [client]
- V4 Readability for non-engineers — "rules you can read", "reconcile line by line" — [inferred]

## 3. Positioning
- Category: billing / metering API for usage-based pricing — [inferred]
- Alternatives: building metering and invoicing in-house; a general subscription-billing platform with usage add-ons; spreadsheets reconciling exports by hand — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Code snippet in the hero | Adopt (moved below) | Engineers rely on seeing the API surface (V2) |
  | Dashboard screenshot with charts as hero | Challenge | Shows "analytics", not reconciliation; the invoice line is the proof (V1) |
  | Logo wall and big-number stats | Avoid | No such claims in the brief; audience distrusts them (V2) |
  | Blue/purple gradient glow backgrounds | Avoid | Reads as marketing, not calm (V3) |
  | Pricing as three tier cards | Challenge | Pricing is one sentence; say it as one (V3) |
  — [agent]
- Intended perception — [inferred]
  - P1 "I can see where the number came from" → check: first screen shows the invoice line with its arithmetic and an open control for daily totals
  - P2 "It's for engineers and finance equally" → check: two parallel columns of equal weight, one per audience, above the fold-out of pricing
  - P3 "Calm, not hyped" → check: no gradients, no badges, one accent colour used only on links/primary action
- Sophistication: considered — B2B infrastructure handling revenue; 0.5% fee signals mid-market+ — [inferred]
- Differentiate on: the invoice line opens into the events behind it — [client]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md" (fennel-street.md not present in project)
Reading: deliberate preference — the register is stated as a constraint — [agent]

## 5. References
None supplied (fennel-street.md referenced but missing) — [inferred]

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A. Open ledger | agent | the expanding invoice line | V1, V2, P1 | Selected | Puts the product's own proof on the first screen |
| B. Event stream terminal | agent | `POST /v1/events` | V2 | Not chosen | Engineering-first; finance lead sees nothing they reconcile |
| C. Statement paper | agent | monthly statement | V3, V4 | Not chosen | House style (5 markers); reads as a printed spec |

Fonts (engine): A = IBM Plex Serif (ibm-plex-serif) headlines + IBM Plex Sans (ibm-plex-sans) body + IBM Plex Mono (ibm-plex-mono) figures; B = Technor (technor) + IBM Plex Mono; C = Trench Slab (trench-slab) + Source Sans 3 (source-sans-3). Colour (engine): A, C = Graphite and Signal (lib.graphite-and-signal); B = Atelier Black (lib.atelier-black). Combinations — [agent]

| Axis | A. Open ledger | B. Event stream | C. Statement paper |
| --- | --- | --- | --- |
| Composition | asymmetric two-column hero: copy left, live invoice object right; then a full-width ledger — because P1 | one terminal column, events scroll — because V2 | one reading column like a statement — because V4 |
| Scale | two big moments: headline, then the invoice amount in mono — because V1 | flat, mono at one size — because V3 | one huge headline, rest small |
| Imagery | the real product interface in HTML (invoice, daily bars, pricing rule, event payload) — because P1 | streaming JSON log | none |
| Signature device | the trace line: a thin vertical rule linking invoice line → daily totals → event — because V1 | blinking cursor | ruled ledger lines |
| Colour proportion | ground ~80%, one graphite band (~15%) for engineering detail, Signal Blue ≤3% on actions — because P3 | black ground everywhere | ground everywhere, figure only |
| Surface | objects (invoice, code) get 6px radius and one soft shadow; page itself flat — because "opens up" is an object you handle | flat, square | flat, square, hairlines |
| House-style markers | 2: H1 (product mock only), H2 (pale ground) | 3: H1, H4, H6 | 5: H1–H5 |
| Distinct on | composition, imagery, signature, colour proportion, surface | colour, composition, scale | composition, imagery, surface |

Other-client test (A): the trace from invoice line to daily totals to an event only exists for a billing ledger product — [agent]

## 7. Selected direction
A. Open ledger — origin: agent — [agent]
The first screen carries the example invoice line, its multiplication and a control that opens the 31 daily totals; the rest of the page follows the same trace downward (events → rules → invoice). Serves V1, V2, P1, P3.
The one memorable thing: you click the invoice line and the month unfolds into days.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: IBM Plex Serif (ibm-plex-serif), OFL, https://github.com/IBM/plex — returned as body pick #1 with `headlines` use; chosen over engine headline pick Technor (technor) because its "retro / sci-fi" feel contradicts V3 calm, and Technor is FFL (self-host only) — swap is [agent]
- Body: IBM Plex Sans (ibm-plex-sans), OFL — [engine]
- Figures and code: IBM Plex Mono (ibm-plex-mono, via `get`), OFL — [engine]; engine `code` picks (departure-mono, iosevka, sligoil) passed over: pixel / huge download / micro — [agent]
- Loading: Fontsource via jsdelivr CDN (exact version) for this single-file deliverable — [agent]; see Open decisions
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light / Neutral, area 86/11/3
- Ground #F9FAFB · oklch(0.985 0.002 250) · Figure #15181E · oklch(0.21 0.012 260) · Accent Signal Blue #0E6EE6 · oklch(0.56 0.2 258)
- Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Accent on ground 4.57:1 · Tints #44484F #797E85 #B2B8C0
- Dark band: #B2B8C0 on #15181E measured 8.89:1 via `classify` — [engine]; #F9FAFB on #15181E 17.01:1
- Engine watch-out: "Brand character has to come from type and layout." Signal Blue only for links, focus, primary action.
### Layout plan — [agent]
- Default: nav, centered hero + two buttons, three feature cards, stats, testimonials, three pricing cards, CTA band, footer.
- Visitor questions: what is it → show me a number traced → how does data get in and rules apply → what does finance get / what does engineering get → what does it cost → where are the docs.
- The one thing: the invoice line that expands into 31 daily totals.
- Cut: stats, testimonials, logos, three-card features, tiered pricing cards, CTA band duplicate.
- Order: header · hero (copy + invoice object) · How it works as a numbered trace with the artifact of each step (payload, rule, line) · graphite band: For finance | For engineering as two columns · pricing as one sentence + worked example from the brief's numbers only · footer.
### Imagery plan — [agent]
- Job: make P1 true — the visitor sees where a number came from.
- Kind: the real product interface, built in HTML from brief facts.
- Ships now: invoice line with expandable 31-day table and bar column (illustrative daily values summing exactly to 1,204,388, labelled "example data"); event payload for `POST /v1/events`; a readable pricing rule. No photography frames needed.
### Judgment tokens — [agent]
- Radius 6px only on objects you can open (invoice, code panels); 0 elsewhere — because "opens up".
- Spacing: tight inside the invoice (8px rows), 128px between ideas, graphite band changes density.
- Motion: the expansion animates height in 180ms, no other motion; respects reduced motion.

## 9. Constraints
- C1 First screen at 1440×900 shows the headline and the invoice line with "1,204,388 calls × $0.0004 = $481.76" and a visible control to open it → check: desktop first-screen shot — [agent]
- C2 Signal Blue appears only on links, focus and the primary button → check: no blue in decoration — [agent]
- C3 (P3) No gradients, pill badges, emoji, stat rows or logo walls anywhere → check: full-page shot + check-layout report — [agent]
- C4 Every claim/number on the page is in the brief's copy, except example daily totals labelled as example data → check: read the render — [agent]
- C5 Phone (390px) has no horizontal page scroll; invoice table scrolls inside itself if needed → check: phone shot — [agent]

## 10. Avoid
- Gradient or glow backgrounds — [agent]
- Pill badge above the headline — [agent]
- Rows of three equal cards — [agent]
- Big-number stat row — [agent]
- Blue used as decoration — [engine]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. Open ledger | — (non-interactive) | Best serves "trust with revenue" by showing the trace | until user review |
| Headline font | IBM Plex Serif over Technor | — | Technor's retro feel fights "calm" | until user review |
Rejected (final): none.

## 12. Open decisions
- Gate 1–3 approvals not given (non-interactive run) — decide at: first user review
- Self-host Plex fonts instead of jsdelivr CDN before launch (GDPR) — decide at: pre-launch — [agent]
- Docs / demo / footer link targets (currently `#` placeholders) — decide at: integration — [inferred]
- Contents of fennel-street.md (referenced but missing) — decide at: first user review
- Example daily totals are illustrative; replace with a real anonymised month if one exists — decide at: content review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1 render | C1 | partial: line shown collapsed, hero right half empty | bug | Line opens by default; 10 daily rows visible, rest scroll inside |
| Round 1 render | C5 | pass, JSON panel cramped at 390px | bug | Smaller mono size and padding on phone |
| Round 2 render | C4 | fail: trace note mentioned "the dashboard" (not in brief) | bug | Sentence removed |
| Round 2 render | C1, C2, C3, C5 | pass; check-layout found none of nine patterns, desktop + phone | — | Stop. House-style markers on render: 2 (H1, H2), H3 partial (mono labels in band) |
