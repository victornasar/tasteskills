# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run, no approval) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery, two sisters; sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: locals within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where, and make cake orders easy — [client]

## 2. Values
- V1 Handmade, small — "run by two sisters", "one oven" — [inferred]
- V2 Local and warm — "neighbourhood", "register: warm, local, handmade" — [client]
- V3 Honest — "don't add claims, reviews or prices" — [client]

## 3. Positioning
- Category: the bakery on my street / where the tarts are — [inferred]
- Alternatives: supermarket bakery aisle; other independent bakeries and cafés, by kind — [inferred]
- Conventions:
  | Convention | Decision | Why |
  | Hero photo of bread, full-bleed | Challenge | No photos supplied; V3; a drawn tart is ours |
  | Hours and address visible fast | Adopt | Audience checks "is it open" on a phone |
  | Menu as a price list | Adopt | Audience acts on prices |
  | Cursive script logo, wheat icons | Avoid | Reads generic, not two specific sisters |
- Intended perception:
  - P1 "I can tell if it's open in a second" → check: open/closed status and today's hours in the first phone screen
  - P2 "Small, handmade, someone's shop" → check: drawn illustration, first-person copy, no stock feel
  - P3 "Warm" → check: cream/burgundy dominate, no cool or grey fields
- Sophistication: everyday — prices £2–£6, walk-in trade — [inferred]
- Differentiate on: a live open/closed line and a menu board — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md" (tallyroll.md not available; read as opposite of a cool, digital product). Reading: deliberate preference — [agent]

## 5. References
None given. [inferred]

## 6. Directions explored
| Axis | A Shop sign | B Recipe card | C Menu board (chosen) |
| Composition | centered poster stack | one narrow column | asymmetric: status + line left, tart right; menu as ruled-dot list — because P1 |
| Scale | one huge name | flat | status and line big, rest small — because P1 |
| Imagery | type only | type only | SVG tart and loaf drawn in palette — because P2 |
| Signature device | scalloped awning | stamp | dot-leader price lines + live status — because Adopt price list |
| Colour proportion | ground everywhere | ground everywhere | ground ~60%, full burgundy band for hours/orders ~30% — because P3 |
| Surface | flat | flat, square | soft round corners on the illustration, 6px buttons, no shadows |
| House-style markers | 5 | 6 | H3 only → 1 (dot leaders count as rules) |
| Distinct on | | | composition, imagery, colour proportion, surface |
Other-client test: the hours board, the one oven and the tart are this shop's alone.
Palette A/B would have used Clay and Linen (engine pick, pale muted, H2); not chosen.

## 7. Selected direction
Menu board — origin: agent — [agent] (non-interactive; best serves the page job, departs from photo-hero convention)
A cream page with a burgundy hours-and-orders band; status first, prices as a board.
The one memorable thing: the page tells you whether the oven is on right now.
House style: 1 marker — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Red Hat Display (red-hat), OFL, weights 300–900
- Body: Sentient (sentient), serif, weights 200–700 (Fontshare, FFL; self-host only)
- Not embedded: no network in this run; CSS uses local() then Georgia / system sans fallbacks. Open decision.
### Color — [engine]
- Direction: Club Cream (lib.club-cream)
- Ground #F5E7C3 · Figure #5B1D26 · Text #37342E (10.1:1) · Muted #67645D (4.8:1) · figure on ground 10.37:1
- Tints #90474E #C4757C #EDAEB1; shades #48161D #360E14 #26080C
### Layout plan — [agent]
- Default dropped: centered hero, 3 cards, testimonials, CTA band.
- Visitor order: open now? → where → what's baked → cake order → who.
- Only-this-brief: live status + price board. Cut: reviews, stats, gallery.
### Imagery plan — [agent]
- Job: make it feel hand-made (P2). Kind: SVG illustration. Shot list: custard tart top view beside status; loaf in about. Treatment: palette colours only. Ships now: both SVGs; no photo frames.
### Judgment tokens — [agent]
- Spacing varies: tight in lists, large between sections. Radii 6px buttons. No motion.

## 9. Constraints
- C1 Status line and today's hours visible on a 390px first screen → P1 — [agent]
- C2 Every price matches the brief; no review, stat or claim not in the copy — [agent]
- C3 Cake order phone link and message path reachable without scrolling past more than one section — [agent]
- C4 Burgundy is the only strong colour; no cool or grey fields → P3 — [agent]
- C5 Name headline at least 4× body size on desktop — [agent]

## 10. Avoid
- Wheat icons, script fonts — [agent]
- Row of three cards — [agent]
- Gradients — [agent]
- Empty photo boxes — [agent]

## 11. Decisions log
| Chose Club Cream over engine pick Clay and Linen | engine pick | agent | avoid pale-muted house style, closer to custard/crust | yes |

## 12. Open decisions
- Instagram handle and message channel (brief gives none; links are "#") — decide at launch
- Fonts to embed as woff2 — decide at launch
- Real photos to replace SVGs — decide at launch
- Approval of this spec — missing

## 13. Checkpoints
See final report.
