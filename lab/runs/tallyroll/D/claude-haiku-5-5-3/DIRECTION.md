# Creative direction: Tallyroll
Status: draft (non-interactive fast run; Gate 3 approval not given) · Mode: fast · v1

## 1. Context
- Product: Usage-based billing API that turns raw usage events into invoices — [client]
- Audience: Engineering leads at usage-priced software companies decide and integrate; finance leads sign off and reconcile line items monthly. Both distrust marketing — [client]
- The page must: make a careful buyer trust Tallyroll with revenue, then send them to the docs or to book a demo — [client]

## 2. Values (2–5)
- V1 Traceability: every number on an invoice can be followed back to the events behind it — "Every cent traces back to an event." — [client]
- V2 Precision: exact arithmetic shown, not implied — "1,204,388 calls × $0.0004 = $481.76" — [client]
- V3 Restraint: no marketing theatre; the product explains itself — "They distrust marketing and want to see how it works." — [client]
- V4 Calm: nothing competes for attention; reading is the main activity — "technical, calm, precise" — [client]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md."
Reading: deliberate preference — fennel-street.md is not in this project, so the contrast is taken as stated: no warmth, no ornament, no display theatre — [inferred]

## 4. References
None supplied. [inferred]

## 5. Directions explored (3)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Graphite ledger: Switzer + IBM Plex Serif, Graphite and Signal | agent | Engine pair: Switzer (headlines), IBM Plex Serif (body); engine pick Graphite and Signal | V1, V2, V4 | **Selected** | Non-interactive: best fit for technical + calm + measurable contrast [agent] |
| B. Cream ledger: Bottle Green Ledger | agent | Engine pick #2 (finance domain) | V1, V3 | Not selected | Reads as established-finance convention; engine marks it as convention-following [agent] |
| C. Corporate navy: Cabin Navy | agent | Engine pick #3 | V3 | Not selected | Follows finance-blue convention; differentiates least [agent] |

Other-client test (A): Graphite and Signal's watch-out is "easy to make indistinguishable from every other product." Answer: the distinctiveness must come from the invoice-line artifact and type, not colour. [agent]

## 6. Selected direction
Graphite ledger — origin: agent — [agent]
A paper-white page, graphite type and one signal blue reserved for links and focus. The page reads like a technical document: left-aligned, ruled, numbered, with a working invoice line as the hero artifact. It serves V1 (the expandable line), V2 (exact figures in tabular numerals) and V4 (no decoration).
The one memorable thing: the invoice line in the hero opens into the events behind it.

## 7. Design system
### Typography — [engine]
- Headlines: Switzer (id `switzer`), FFL, Fontshare — self-host only, keep files out of public repos. Weights 400–700 used. — [engine]
- Body: IBM Plex Serif (id `ibm-plex-serif`), OFL, GitHub — self-host. Weights 400, 500 used. — [engine]
- Figures in the invoice line: system tabular numerals on the body face; no third family. — [agent]
- Engine notes: no mono role requested; a code font for the snippet uses the system monospace stack (not a catalog pick). — [agent]

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), Neutral, Light foundation — [engine]
- Ground: Paper White #F9FAFB · Figure: Graphite #15181E · Accent: Signal Blue #0E6EE6 — [engine]
- Text: #3C3F46 (10.09:1 on ground) · Muted text: #6B6F76 (4.82:1 on ground) — [engine]
- Figure on ground 17.01:1 · Accent on ground 4.57:1 (passes 4.5:1 for body text) — [engine]
- Tints for rules and the expanded event list: #B2B8C0, #797E85 — [engine]
- Accent use: links and focus only. The primary button is Graphite fill with Paper White label (17.01:1), per engine roles. — [engine]

### Layout plan — [agent]
- Default being avoided: nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor's questions in order: What is it? How does a line on an invoice trace back? Can finance reconcile it? How do engineers integrate? What does it cost? Then the two actions.
- The one thing only this brief has: the invoice line (1,204,388 calls × $0.0004 = $481.76) that expands to 31 daily totals. Leads the page as content in the first screen.
- Cut: testimonials (none supplied), stats row (no figures beyond the brief), three-card row, centered CTA band.

### Judgment tokens — [agent]
- Spacing: one vertical rhythm of 8px steps; section gaps vary by content (hero largest, pricing tight). Tied to V4.
- Radii: 0 on everything except the expanded invoice panel (2px). Boxes are reserved for the one separate object, the invoice. Tied to V1.
- Imagery: none; the invoice line is built in HTML/CSS. Tied to brief (no external images).
- Motion: none beyond a disclosure toggle. Tied to V4.

## 8. Constraints (pass/fail on screenshot)
- C1 Headline is the largest type on the page; at least 4× body size on desktop and at least 2.5× on phone → check: headline vs. body computed size at 1440 and 390 widths. — [agent] (phone threshold revised at build, see Decisions log)
- C2 Hero is left-aligned, not centred; the invoice line is visible in the first screen on desktop (1440×900) → check: screenshot. — [agent]
- C3 The invoice line expands to show 31 daily entries without invented values → check: expanded state shows 31 labelled days, no per-day numbers. — [client]
- C4 Accent blue appears only on links and focus rings; no decorative use → check: every blue element is a link or focus state. — [agent]
- C5 No rounded boxes except the invoice panel; no pill badges, emoji, gradients or purple → check: screenshot and source. — [agent]
- C6 Only the copy from the brief appears; no added claims, numbers or testimonials → check: text diff against brief. — [client]

## 9. Avoid (≤6)
- Centered hero with a slogan and two buttons only
- Rows of three cards with icons
- Pill badges or "New" banners
- Gradient or mesh backgrounds
- Stats rows of large numbers
- Emoji used as icons

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A: Graphite ledger | A | (non-interactive, [agent] selection) | Best fit for technical, calm, precise; avoids finance-blue convention | yes |
| Primary button Graphite fill | Graphite fill | — | Engine role mapping; accent kept for links/focus | yes |
| C1 phone threshold revised from 4× to 2.5× body size | — | — | At 390px a 4× headline does not fit the 16px gutter with a legible size; agent change at build, logged here for review | until checkpoint |

Rejected (final): none in this run.

## 11. Open decisions
- Gate 3 approval of this spec — decide at: user review — [inferred]
- Docs URL and Book a demo URL (the page uses placeholders `#docs` and `#demo`) — decide at: user review — [inferred]
- Font files: the page references `./fonts/Switzer.woff2` and `./fonts/IBMPlexSerif.woff2`. Not downloaded in this run (no approval for network fetch); system fallbacks render until the files are placed. — decide at: build hand-off — [inferred]
- Mono/code font for the endpoint snippet — decide at: user review — [inferred]
- Whether the Plex Serif body is preferred over Plex Sans (engine runner-up) for the technical register — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Render 1 (1440 and 390) | C2 | Pass | Bug: invoice figure indented by UA figure margin | Fixed (margin reset) |
| Render 1 (390) | C1 | Pass at 2.5× (revised threshold) | Bug: "How it works" paragraphs fell into the number column | Fixed (grid placement) |
| Render 2 (390) | C1, C2, C5 | Pass | None | Stopped; two fix rounds used |
| Render 2 (1440) | C2, C3, C4, C5, C6 | Pass | Fonts not loaded (files not downloaded): system fallbacks render | Open decision |
