# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; no approval gate passed) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: People within a few streets who walk in; people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: tell a visitor whether the shop is open now, what's baked today, where it is, and how to order a cake — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 Answers "is it open, where, what's baked" first — "Bread at seven, tarts by nine, gone by two." — [client]
- V3 Cake orders are easy — "Whole cakes with 48 hours' notice. Message us or call…" — [client]
- V4 Two sisters, one oven, no inflated claims — "still only have one" — [client]

## 3. Opening vocabulary
"Warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — the brief's contrast with tallyroll.md is read as: no tech-brand chrome, no cool palette, no dashboard grid; the page should feel like a paper sign in a shop window — [agent]
tallyroll.md was not in the project folder, so the contrast is read from the brief alone — [inferred]

## 4. References (0–5)
None supplied. — [inferred]

## 5. Directions explored (2–4)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Clay and Linen: linen ground, rose-clay figure | agent | engine: lib.clay-and-linen (food-and-beverage domain, rank 1) | warm, handmade, food-led | Selected | — (non-interactive; selected by agent) |
| B. Parchment and Ink: warm paper, bitter-brown ink | engine | engine: lib.parchment-and-ink (rank 3) | typographic, quiet | Not built | — |
| C. Matcha Field: one green family | engine | engine: lib.matcha-field (rank 2) | single hero product | Not built; a single green would fight "warm" and "custard" | — |

Pairs: A uses Cormorant + Source Sans 3 (engine: find-font, headlines + body). Combining them is [agent].
Other-client test (A): could this belong to another client? Possibly any food brand with a cream ground. What makes it this one: the two-sister, one-oven, custard-led copy and the rose-clay echo of baked crust. — [agent]

## 6. Selected direction
Clay and Linen — origin: agent — [agent]
A paper-and-clay page: linen ground, rose-clay headings and links, dark warm text. Set like a printed bakery card: product list as the main content, hours and address in plain text near the top, cake order as one clear block. Serves warmth (V1), the visitor's first questions (V2) and cake orders (V3).
The one memorable thing: the daily bake list reads like a handwritten board, with prices set flush right in the same figure colour.

## 7. Design system
### Typography — [engine]
- Headlines: Cormorant (cormorant), OFL, self-hosted; weights 400–600 used — [engine]
- Body: Source Sans 3 (source-sans-3), OFL, self-hosted; weights 400 and 600 used — [engine]
- Fallback stacks: Georgia / system-ui — [engine]
- Files: not bundled in the single HTML file. Expected at ./fonts/Cormorant.woff2 and ./fonts/SourceSans3.woff2. Until added, the fallbacks render. — [agent]

### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen) — [engine]
- Ground / figure / accent: ground #F5EDE4 (Linen); figure #8D5951 (Rose Clay); no accent — [engine]
- Text #3D3832 on ground: 10:1 — [engine]
- Text-muted #6C6761 on ground: 4.83:1 — [engine]
- Figure on ground: 4.92:1 (headings, links, button fill with ground label) — [engine]
- Tints/shades (tint-1 #B4786E, tint-3 #E1CAC6, shade-2 #4A2D28) used only for hover and rules — [engine]

### Layout plan — [agent]
- Default section list rejected: centered hero, three feature cards, stats, testimonials, CTA band.
- Visitor's questions in order: open now and hours → what's baked today → where → cake order → about.
- The one thing only this brief has: the daily bake list with real prices.
- Cut: testimonials and stats (none supplied); the About text stays short.

### Judgment tokens — [agent]
- Spacing: one base unit of 8px with generous gaps between groups; tight inside product rows. Tied to "handmade" paper-card feel.
- Radii: 0 on the page; 2px on the button only. Tied to printed-card look, not rounded-box default.
- Imagery: no external images. A labelled photo placeholder for the hero. Tied to "Where a photo would go" rule.
- Motion: none beyond a hover underline. Tied to a quiet shop, not an app.

## 8. Constraints (4–8, each pass/fail on a screenshot)
- C1 Open status: the hours line (Wednesday to Sunday, 7:00 to 14:00; closed Monday and Tuesday) is visible on the first screen at 390×844 without scrolling → check: hours text is above the fold on the phone screenshot — [agent]
- C2 Cake order: the "Order a cake" action and the 48-hour notice line are visible on the first screen or one tap away from it → check: an order link sits in the nav or hero at phone width — [agent]
- C3 Headlines at least 4× body size; nothing else competes in size → check: largest heading vs body text size in the render — [agent]
- C4 All text meets 4.5:1 against its ground; body uses the text token → check: no grey or light text on linen below 4.5:1 — [agent]
- C5 All five daily items and two seasonal items appear with the prices given, with no added prices or claims → check: product list matches the copy — [client]
- C6 No external images or external font requests; a labelled photo placeholder stands in for photography → check: no network image URLs in the file; placeholder is visibly labelled — [agent]
- C7 No horizontal page scroll at 390px width → check: phone screenshot has no clipped content or sideways scroll — [agent]

## 9. Avoid (≤6, each observable)
- Centered hero headline with a gradient background — [agent]
- A row of three feature cards with emoji icons — [agent]
- Pill badge above the headline ("New", "Open now" badges) — [agent]
- Purple, indigo or violet button — [agent]
- Row of big numbers ("since 2019", "1 oven") presented as stats — [agent]
- Orange terracotta pushed into the rose clay — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A, Clay and Linen | A | not asked (non-interactive) | Engine rank 1 for food-and-beverage; warm, earthy, quiet beside food | until review |
| Cormorant + Source Sans 3 | this pair | not asked | Engine's top pair with warm/literary feel; public-repo flag not set, so Fontshare fonts not dropped by engine | until review |

Rejected (final): none.

## 11. Open decisions
- Photograph for the hero (real photo of the bake) — decide at: owner, before launch — [inferred]
- Font files: whether to bundle woff2 in the page or keep them in ./fonts — decide at: deploy — [agent]
- Instagram handle or URL — none supplied; footer link is a labelled placeholder — decide at: owner — [inferred]
- Find-us map link — no map provider or URL supplied; address printed as text only — decide at: owner — [inferred]
- Order channel: message and phone are given; no email or order form — decide at: owner — [client]
- Holiday or sold-out notices — not supplied; not built — decide at: owner — [inferred]
- Approval of this direction (Gate 2 and Gate 3) — not run in non-interactive mode — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Phone render, first screen (390×844) | C1, C2 | pass: hours and "Order a cake" above the fold | — | — |
| Round 1 (layout checker: centered hero, uniform spacing) | — | 2 patterns hit | Fix: two-column desktop layout, section spacing varied | Applied |
| Round 2 (checker re-run, phone + desktop) | — | 0 patterns hit; spacing review by eye | Fix: desktop section gaps restored | Applied |
| Final critique | C3 | fail: h1 about 2.8× body on phone (48px vs 17px); h2 about 2× | Lesson: C3 at 4× is stricter than a warm bakery page needs. Reopen with user; constraint not edited | Open |
| Final critique | C4 | pass: text 10:1, muted 4.83:1, figure 4.92:1 | — | — |
| Final critique | C5 | pass: all copy prices present, no additions | — | — |
| Final critique | C6 | pass: no external images or font URLs; placeholder labelled | — | — |
| Final critique | C7 | not verified: checker does not measure horizontal scroll | — | Check at 390px before launch |
