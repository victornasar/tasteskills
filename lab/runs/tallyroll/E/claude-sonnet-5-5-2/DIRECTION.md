# Creative direction: Tallyroll
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, and the finance leads who sign off; they distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with revenue and send them to the docs or a demo — [client]

## 2. Values
- V1 Precision — "technical, calm, precise" — [client]
- V2 Traceability — "Every cent traces back to an event" — [client]
- V3 Show, don't sell — "They distrust marketing and want to see how it works" — [client]

## 3. Positioning
- Category: usage-based billing API / billing infrastructure — [inferred]
- Alternatives: building billing in-house; spreadsheets plus a payments API; other billing platforms (not named) — [inferred]
- Conventions:
  | Convention | Stance | Why |
  | Product UI / code snippet shown in hero | Adopt | Engineers act on seeing the real thing (V3) |
  | Blue as lead colour (finance-blue, engine) | Adopt, only as a small accent | Trust signal for finance readers |
  | Logo wall + testimonials | Avoid | Brief forbids added claims; audience distrusts marketing |
  | Centered headline over abstract gradient | Challenge | Replace with a working invoice line (V2) |
  | Big stat row | Avoid | No numbers allowed beyond brief |
  [agent]
- Intended perception — [inferred]
  - P1 Verifiable → check: an invoice line is on screen at first view and can be opened.
  - P2 Calm → check: one accent colour, no shadows or gradients, generous line spacing.
  - P3 Built by engineers → check: monospace for code and figures, API path visible above the fold.
- Sophistication: considered — B2B finance infrastructure, buyers signing off on revenue; no luxury signal — [inferred]
- Differentiate on: the invoice line itself is the hero; click it open to the 31 daily totals — [agent]

## 4. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference; fennel-street.md was not available, so read as "not warm, not decorative" — [agent]

## 5. References
None supplied. Open decision.

## 6. Directions explored
| Axis | A Ledger-as-hero | B Docs-first | C Diagram narrative |
| Composition | Split: copy left, live invoice line right — because V2 | Single reading column with code blocks — because V3 | Stacked full-width modules — because conventions Challenge |
| Scale | One big headline, rest small — because P2 | Flat even scale — because V3 | Several big moments — because pacing |
| Imagery | The real invoice line built in HTML — because P1 | Code only — because P3 | SVG flow diagram — because how-it-works |
| Signature device | Expandable ledger row with tick rule — because V2 | Endpoint path chip — because P3 | Event dots → line — because V2 |
| Colour proportion | Ground dominant, graphite band for engineering, blue on actions — because P2 | Ground and blue links — because P2 | Large graphite fields — because contrast |
| Surface | Flat, square, hairlines — because P2 | Same | Rounded soft — because approachable |
| House-style markers | 3: H3, H4, H5 | 5: H1, H2, H3, H4, H5 | 2: H4... see note |
| Distinct on | composition, imagery, signature | composition, imagery, scale | scale, surface, colour |
Other-client test: A fails for a non-billing client, because the hero is an invoice line with an expansion to daily event totals. [agent]
Direction colour and type engines are shared across directions (one engine run), so differences sit on axes only. [agent]

## 7. Selected direction
A Ledger-as-hero — origin: agent — [agent]
A working invoice line sits beside the headline and opens into 31 daily totals. It serves V2 and P1, and the flat calm surface serves P2.
The one memorable thing: you can open the invoice line and see where the money came from.
House style: 3 markers (H3, H4, H5); below the threshold of 4. — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Overpass (overpass), OFL, 600 weight. Engine's second-ranked headline pick; top pick Steps Mono was rejected because its caveats list missing code glyphs and two weights only — [engine pick, agent choice among returned]
- Body: IBM Plex Sans (ibm-plex-sans), OFL — [engine]
- Code and figures: Commit Mono (commit-mono), OFL — [engine]
- Loading: not embedded. The page names the families with system fallbacks; self-host woff2 files from the sources the engine returned. Open decision.
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal)
- Ground #F9FAFB · Figure #15181E · Accent #0E6EE6 · Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Tint-3 #B2B8C0 · Accent on ground 4.57:1
- Accent only for links, focus and the primary action (engine rule)
### Layout plan — [agent]
- Default avoided: centered hero, three feature cards, stat row, testimonials, CTA band.
- Visitor questions in order: what does it do, can I see it, how does it work, what do I get (finance/eng), what does it cost, where do I go.
- Only-this-brief artifact: the expandable invoice line.
- Cut: testimonials, logos, stats, any claim not in the brief.
- Axes as in Selected direction.
### Imagery plan — [agent]
- Job: make a buyer believe invoice lines are traceable — serves P1
- Kind: product interface built in HTML/CSS
- Ships now: invoice line with expandable 31-day table; request snippet for POST /v1/events; no photos
### Judgment tokens — [agent]
- Spacing: sections vary in padding (generous first, tighter after) so the page does not read as uniform
- Radii: 2px; no shadows
- Motion: row expand only, 150ms, off under reduced-motion

## 9. Constraints
- C1 Invoice line is visible in the first screen on desktop → check: line text readable above the fold — [agent]
- C2 Blue appears only on links, focus and primary button → check: no other blue — [agent]
- C3 No numbers or claims beyond the brief → check: every figure appears in brief — [agent]
- C4 P2 Calm: no gradients, shadows, emoji — [agent]
- C5 Phone width shows no horizontal scroll and the invoice line still opens — [agent]

## 10. Avoid
- Gradients, emoji icons, pill badges, three-card rows, logo walls — [agent]

## 11. Decisions log
| Chose direction A | agent | n/a | best serves the single page job | yes |
| Overpass over Steps Mono | engine top pick | n/a | caveats bite a billing page | until typography is approved |
Rejected: none

## 12. Open decisions
- Approve DIRECTION.md — decide at: next review — [inferred]
- Self-hosted font files and paths — decide at: build handoff — [inferred]
- Real docs and demo URLs — decide at: build handoff — [inferred]
- Reference sites — decide at: review — [inferred]
- The 31 daily totals are illustrative and sum to the stated amount; confirm the client is fine with a sample — [inferred]

## 13. Checkpoints
See round notes in the reply.
