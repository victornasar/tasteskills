# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery, sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: people living within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where, and make cake orders easy — [client]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 Honest: no added claims, reviews or prices — "don't add claims, reviews or prices" — [client]
- V3 Answer "is it open?" first on a phone — "often checking whether the shop is open" — [client]
- V4 Small and modest, one oven — "still only have one" — [inferred]

## 3. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md"
Reading: hypothesis — tallyroll.md was not provided; read as "not a slick, data-heavy product page" — [agent]

## 4. References
None supplied. Open decision.

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| A. Cormorant + Source Sans 3, Clay and Linen (lib.clay-and-linen) | agent | warm feel, soft earthy palette, no photos yet | V1 V3 | Selected | Best fit for warm/handmade; muted rose clay is not the overused orange terracotta — [agent] |
| B. Cormorant + Source Sans 3, Parchment and Ink (lib.parchment-and-ink) | agent | typographic, prices read like a chalk/paper menu | V2 | Not chosen | Quieter, relies on photography for colour; none exists yet — [agent] |
| C. Red Hat + Atkinson, Matcha Field (lib.matcha-field) | agent | engine alternates | — | Not chosen | Green has no basis in the bakery's facts — [agent] |
Other-client test (A): the hours board, the "gone by two" line and the price list with leaders come from this shop's facts.

## 6. Selected direction
A — origin: agent — [agent]
A paper-menu page: left-aligned, price list with dot leaders, a hours board that says open/closed right now. Serves V1, V3.
The one memorable thing: the hours board at the top tells you, live, whether the ovens are still giving out bread.

## 7. Design system
### Typography — [engine]
- Headlines: Cormorant (cormorant), OFL, 300–700 variable, latin-ext
- Body: Source Sans 3 (source-sans-3), OFL, 200–900 variable, latin-ext
- Cormorant is thin: used only at large sizes, weight 500+. Never for body.
### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen), Light + Muted
- Ground #F5EDE4 · Figure (Rose Clay) #8D5951 (4.92:1 on ground) · Text #3D3832 (10:1) · Muted #6C6761 (4.83:1) · tint-3 #E1CAC6 · shade-2 #4A2D28
- No accent returned; action buttons use figure fill with ground label (4.92:1).
### Layout plan — [agent]
- Default avoided: centered hero, 3 cards, stats, testimonials, CTA band.
- Visitor's questions in order: open now? → what's baked and cost → where → order a cake.
- Only-this-brief artifact: hours board with live status, and the priced list.
- Cut: testimonials, stats, newsletter, feature cards.
### Judgment tokens — [agent]
- Spacing: tight in lists, large gaps between sections; sections not equal.
- Radii: 0 on content; a single 2px on buttons. Handmade = paper and rules, not boxes.
- Imagery: one labelled placeholder (oven/bread photo); no stock, no emoji.
- Motion: none.

## 8. Constraints
- C1 First phone screen (390×844) shows name, line and the open/closed status with hours → check: all three visible without scroll — [agent]
- C2 Every price in the copy appears, no price or claim not in the brief → check: compare to copy — [agent]
- C3 Body text ≥16px, tap targets (phone, nav) ≥44px tall → check: inspect — [agent]
- C4 No horizontal scroll at 390px → check: render — [agent]
- C5 Headline at least 3× body size; one headline typeface only → check: render — [agent]
- C6 No cards in a row of three, no gradients, no emoji → check: render — [agent]

## 9. Avoid
- Centered hero headline with two buttons — [agent]
- Rounded-corner card grid — [agent]
- Gradient backgrounds — [agent]
- Emoji or icon decoration — [agent]
- Orange terracotta — [engine, from lib.clay-and-linen avoid]

## 10. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | — | non-interactive | until user review |

## 11. Open decisions
- Direction/spec approval — decide at: user review — [agent]
- Font files: woff2 for Cormorant and Source Sans 3 not bundled (no download in this run); page falls back to Georgia / system-ui until `fonts/` is added — decide at: deploy — [agent]
- "Message us" channel and Instagram/Find us URLs not supplied; links point to #order/#find/Instagram placeholder — decide at: client reply — [inferred]
- Real photography (placeholder shown) — decide at: client reply
- Opening-hours status uses London time; "or until we sell out" can't be live — [inferred]

## 12. Checkpoints
See end of run report.
