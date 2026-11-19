# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; Gates 1–3 not confirmed by the user) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8, run by two sisters; sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: people within a few streets who walk in; people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked today, whether the shop is open and where it is, and make a cake order easy — [client]
- Brief's "opposite of tallyroll.md": tallyroll.md is not in the project folder, so the contrast could not be read. The warm/local/handmade register from the brief is used as given — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Made by hand, by two people, on one oven — "Ana bakes the bread. Rita does everything with custard… still only have one." — [client]
- V2 Time-bound: it's gone by two — "Bread at seven, tarts by nine, gone by two." — [client]
- V3 Neighbourly ease: walk in, or order a cake 48 hours ahead by phone — "Most customers walk in; some order cakes ahead." — [client]

## 3. Positioning
- Category: neighbourhood bakery, the one you walk to — [inferred]
- Alternatives: supermarket sliced bread; a coffee-shop bakery counter; a bakery farther away that you'd have to plan a trip for — described by kind, no named competitors — [inferred]
- Conventions (observable in bakery sites):
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Hero photo of loaves or pastries | Challenge | No client photos supplied; the page leads with the day's timeline as the one fact that differs (V2) |
  | Script or "artisan" display type | Avoid | Reads as generic craft pastiche; the sisters' plainness is the point (V1) |
  | Open/closed status and hours in the header | Adopt | The audience comes to check whether the shop is open (audience) |
  | Cake order as a clear contact block | Adopt | Cake orders are a stated job; 48 hours' notice must be visible (V3) |
  | Testimonials and star ratings | Avoid | None supplied; the brief forbids invented reviews |
- Intended perception: three qualities a stranger reports after five seconds — [inferred]
  - P1 Made by hand, by two people → check: the sisters' names and the one-oven line are visible in the first two screens
  - P2 Open now or not, at a glance → check: on a 390px phone first screen, the open/closed status line is visible without scrolling
  - P3 A small, particular shop, not a chain → check: no stock imagery, no gradients, no icons; the only visual is the bake timeline and a labelled photo slot
- Sophistication: considered — prices from £2.10 to £28, handmade and seasonal; the price range is the signal — [inferred]
- Differentiate on: a day that runs on a clock — bread at seven, tarts by nine, gone by two — [agent]

## 4. Opening vocabulary
"A neighbourhood bakery run by two sisters" (brief, not the user's own words) — no opening vocabulary supplied by the user.
Reading: deliberate preference — the register is "warm, local, handmade" from the brief — [agent]

## 5. References (0–5)
No references supplied. None built in — [inferred]

## 6. Directions explored (2)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A — Ledger & Linen | agent | Brief register; V2 and P2 | P1, P2, P3 | **Selected** (non-interactive pick) | — |
| B — Cream & Burgundy | agent | Engine runner-up for heritage feel | P1 | Not selected | Pastiche risk per the engine's own watch-out |

Engine results for each direction (copied from the scripts):
- A typography: Synonym (headlines, `synonym`) + Sentient (body, `sentient`) — find-font `recommend` pair, [engine]
- A colour: Clay and Linen (`lib.clay-and-linen`), Linen #F5EDE4 ground / Rose Clay #8D5951 figure — find-color `recommend`/`apply`, [engine]
- B typography: Alpino (headlines, `alpino`) + Author (body, `author`) — find-font `recommend`, [engine]
- B colour: Club Cream (`lib.club-cream`), Club Cream #F5E7C3 ground / Club Burgundy #5B1D26 figure — find-color `recommend`, [engine]

| Axis | A — Ledger & Linen | B — Cream & Burgundy |
| --- | --- | --- |
| Composition | Asymmetric: sticky status column left, day's list right; one reading column on phones — because V2 and P2 need the hours found first | Centred catalogue of tiles — because the category's sites lean on it (Adopt-marked in B only) |
| Scale | One big statement in the hero, everything else small — because V2 is the line the page is built on | Several medium moments, one per section — because P1 wants the names read as a set |
| Imagery | Type plus the bake timeline (SVG); one labelled photo slot — because P1 needs a real photo later, none supplied | Type plus tile placeholders — because no client photos |
| Signature device | Ruled bake-day timeline: 07:00 / 09:00 / 14:00 — because V2 "bread, tarts, gone" | Stamped seal — because P1 "made by hand" |
| Colour proportion | Linen ground almost everywhere; Rose Clay as one full band (cake orders) — because V3 makes the order the one loud moment | Burgundy used for type and labels only — because the engine notes heritage risk |
| Surface | Soft 12–14px corners on cards, flat paper, no shadows — because "handmade", object-like | Square, flat — because heritage labels |
| House-style markers (H1–H6) | 2: H2 (pale ground, one muted figure), H5 (headline then a list) | 4: H2, H3, H4, H5 |
| Distinct on | Composition, Scale, Signature device, Colour proportion, Surface (5 axes) | — |

Other-client test (A): the timeline device belongs to this bakery's day and its line; a different bakery has a different clock — [agent]

## 7. Selected direction
Ledger & Linen — origin: agent — [agent]
The page is a day on a ruled line: bread at seven, tarts by nine, gone by two. It serves P1 (names and one oven in the first two screens), P2 (open/closed status above the fold on a phone) and P3 (no stock, no icons, no gradients).
The one memorable thing: the bake-day timeline under the headline.
House style: 2 markers; no override needed — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (`synonym`), find-font FFL, weights 200–700 — self-host `./fonts/Synonym.woff2`
- Body: Sentient (`sentient`), find-font FFL, weights 200–700 — self-host `./fonts/Sentient.woff2`
- Fallbacks: system-ui for headlines, Georgia for body until the files are placed. No Google Fonts or Fontshare CDN links (the engine's privacy rule).

### Color — [engine]
- Direction: Clay and Linen (`lib.clay-and-linen`), Light + Muted
- Ground: Linen `#F5EDE4` · Figure: Rose Clay `#8D5951` · Text: `#3D3832` (10:1 on ground) · Muted text: `#6C6761` (4.83:1 on ground) · Figure on ground: 4.92:1 · Button label (ground on figure): 4.92:1
- Tints for hairlines only: `#CBA199` (tint-2), `#E1CAC6` (tint-3)

### Layout plan — [agent]
- Default structure (what we would reach for): nav, centred hero with two buttons, three feature cards, stats, testimonials, CTA band, footer. Cut: centred hero, three cards, stats, testimonials, pill badge.
- Visitor's questions in order: is it open → what's baked → where is it → can I order a cake → who makes it.
- The one thing only this brief has: the bake-day timeline and the daily list with prices.
- Cut: stats, testimonials, feature icons, the centred CTA.
- Axis positions: Composition asymmetric two-column (desktop), one column (phone); Scale one big statement; Imagery type + SVG + one labelled photo slot; Signature device ruled timeline; Colour proportion Linen ground, one Rose Clay band; Surface flat paper, 12–14px card corners, no shadows.

### Imagery plan — [agent]
- Job: this is a real bakery with two people who made the food — serves P1
- Kind: type as image + SVG diagram (the timeline) + one labelled photo placeholder
- Shot list: (1) Ana at the oven, bread on the peel, early light, 4:5, left of the About text; (2) a row of custard tarts on a tray, overhead, window light, 1:1, beside the Daily list; (3) the shop front at 7:00, 3:2, in the Find us section. Photos not supplied — all three are labelled frames.
- Treatment: no colour grading beyond the engine palette; frames inset in the grid, not full-bleed; corners 12px to match cards
- Ships now: the bake-day timeline (SVG), the headline composition, the daily list and season list as typography, three labelled photo frames

### Judgment tokens — [agent]
- Spacing: 8px base, 24px between list rows, 88px between sections (tighter inside groups, looser between ideas) — tied to V2's rhythm
- Radii: 12px cards and frames, 0 on rules — "soft like an object you hold", not blocks
- Motion: none beyond a colour change on link hover — the page is for reading and checking

## 9. Constraints (pass/fail on a screenshot)
- C1 First screen on a 390×844 phone shows the name, the open/closed status line and the hours, without scrolling → check: phone screenshot, top fold — [agent]
- C2 The headline "Bread at seven, tarts by nine, gone by two." is at least 4× body size and is the largest element on the page → check: desktop and phone screenshots — [agent]
- C3 P1: both sisters' names and "one oven" appear within the first two screens on desktop and phone → check: screenshot of the About section — [agent]
- C4 P3: no stock imagery, icons, emoji, gradients or shadows; the only photo slots are labelled placeholders → check: full-page screenshot — [agent]
- C5 V3: the cake-order block (tel link 020 7946 0381, "48 hours' notice") is reachable within one tap from the first screen → check: header or first-screen link — [agent]
- C6 Body text and muted text meet WCAG AA on the ground using only the engine text colours → check: computed colours in the render — [agent]

## 10. Avoid (≤6, each observable)
- Gradient backgrounds or gradient buttons — [agent]
- Emoji or icon-font icons in lists or buttons — [agent]
- Pill badges such as "New" above the headline — [agent]
- Stock or invented bakery photos — [agent]
- Star ratings, testimonials or reviews not in the brief — [agent]
- Script or "artisan" display type — [agent]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A, Ledger & Linen | A | — (non-interactive; no pick given) | Serves P1–P3 and V2; B's heritage risk | until user review |
| Fonts Synonym + Sentient | find-font top pair | — | Warm, legible at phone size | yes (engine) |
| Colour Clay and Linen | find-color pick | — | Warm, quiet, photo-friendly | until user review |

Rejected (final): none.

## 12. Open decisions
- Photos of Ana, Rita, the bread and the shop: placeholders ship; decide at: asset handoff — [inferred]
- Instagram handle or URL for the footer link: `href="#"` placeholder until given — decide at: copy review — [inferred]
- The messaging channel for "Message us": only the phone number was supplied; the page shows the phone and no other channel — decide at: copy review — [inferred]
- "Until we sell out": the page shows open status by clock time only; sell-out cannot be known to a static page — decide at: product decision — [inferred]
- Font files: Synonym and Sentient must be downloaded from Fontshare and placed in `./fonts/` — decide at: build handoff — [engine]
- Approval of this direction (Gates 1–3): not given in the non-interactive run; status stays draft — decide at: user review
- Sophistication and alternatives: inferred from the price range and category; confirm at Gate 1 — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
