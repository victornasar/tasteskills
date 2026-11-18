# Creative direction: Fennel Street Bakery
Status: draft · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery (sourdough, Portuguese pastries, seasonal cakes) run by sisters Ana and Rita Duarte — [client]
- Audience: locals within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open, where it is, and make cake orders easy — [client]
- Visitor's first question is "is it open right now?" — [inferred]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 Opposite of tallyroll — "The opposite of tallyroll.md" — [client]. The file is not in the project; read only as "not a data/SaaS look" — [inferred]
- V3 Honest: no added claims, reviews or prices — "don't add claims, reviews or prices" — [client]
- V4 Phone-first, answers fast — [inferred]

## 3. Opening vocabulary
"warm, local, handmade"
Reading: deliberate preference; repeated in register and About copy — [agent]

## 4. References
None supplied. See Open decisions.

## 5. Directions explored
| Direction | Origin | Grounded in | Outcome |
| A Price board: menu as a typeset shop price list, live open-status line on top | agent | Daily/Season price copy and hours | Selected [agent] |
| B Sisters' letter: About-led narrative column | agent | the About copy | Not chosen: delays hours and menu on a phone |
| C Poster: huge slogan, photo-led | agent | the Line | Not chosen: no photos exist |
Fonts: Red Hat Display + Source Sans 3 [engine]. Colour: Clay and Linen [engine pick]. Combination [agent].
Other-client test (A): a price board with a live open/closed line only suits a shop with a short fixed menu and fixed hours.

## 6. Selected direction
Price board — [agent]. The page reads like the shop's own paper price list: an open/closed line, then the list with prices, then how to order a cake. Serves V1, V3, V4.
The one memorable thing: the hours line says "Open now" or when the shop next opens, computed on the visitor's phone.

## 7. Design system
### Typography — [engine]
- Headlines: Red Hat Display (red-hat), OFL, 300–900, latin-ext
- Body: Source Sans 3 (source-sans-3), OFL, 200–900, latin-ext
- find-font ranked Recursive first for headlines; not used because it is a monospace-based family and would read technical — [agent]
### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen), Light + Muted
- Ground #F5EDE4 · Figure #8D5951 · Text #3D3832 · Muted #6C6761 · Tints #B4786E #CBA199 #E1CAC6 · Shades #6A423C #4A2D28 #2B1815
- Figure on ground 4.92:1; text on ground 10:1; muted 4.83:1; button label on figure 4.92:1
### Layout plan — [agent]
- Default dropped: centered hero, three cards, stats, testimonials, CTA band
- Visitor's questions in order: open now? → what's baked and cost → cake order → where → who
- Only-this-brief thing: price list with dotted leaders and live hours line
- Cut: testimonials, stats, gallery (no assets or claims supplied)
### Judgment tokens — [agent]
- Left-aligned; single column on phone, two columns from 760px
- Radii 0, buttons 2px: paper, not app UI
- Imagery: one labelled placeholder, no invented photos
- Spacing: tight inside lists, large between sections, dark cake band as the change of subject
- Motion: none

## 8. Constraints
- C1 Open/closed line and hours visible without scrolling at 390×844 → check: phone screenshot — [agent]
- C2 Phone number is a tap-to-call link; cake section reachable from the top in one tap — [agent]
- C3 Every price and claim on the page is in the brief → check: text compare — [agent]
- C4 Headline at least 4× body size, left aligned — [agent]
- C5 Text colours are engine tokens, ≥4.5:1 — [agent]
- C6 No horizontal scroll at 390px — [agent]

## 9. Avoid
- Centered hero with two buttons; row of three cards; gradients as decoration; emoji icons; pill badges; invented photos — [agent]

## 10. Decisions log
| Fonts referenced via local() then ./fonts/*.woff2; files not bundled (no network) | agent | n/a | single-file constraint | until files added |
Rejected (final): Recursive for headlines — monospace-based.

## 11. Open decisions
- Instagram link and message channel (copy says "message us" but names none): links are placeholders — decide at: client review — [inferred]
- Real photos — decide at: client review
- tallyroll.md missing; contrast read is inferred — [inferred]
- Direction and spec not approved (non-interactive run) — decide at: client review

## 12. Checkpoints
| Checkpoint | Constraint | Result | Action |
| Round 1, 390px render | C1–C6 | all pass; check-layout found none of the nine patterns | none |
| Round 1 | copy | "Closed now" followed by "or until we sell out" read oddly | Bug: hours line reworded in code |
