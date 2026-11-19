# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by Ana and Rita Duarte; sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: locals within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if it is open — [client]
- The page must: show what's baked, when it's open and where, and make cake orders easy — [client]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 Small and honest — "one oven and still only have one"; no added claims, reviews or prices — [client]
- V3 The opposite of tallyroll (no tool or SaaS feel) — [client]

## 3. Positioning
- Category: local bakery, "bakery near me" — [inferred]
- Alternatives: a supermarket in-store bakery; a café-bakery chain; another independent bakery down the road (by kind, none named) — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | Hours and address findable at once | Adopt | phone visitors check "open?" first (audience) — [agent] |
  | Menu as a list with prices | Adopt | visitors act on it (V2) — [agent] |
  | Cream or kraft pastel ground with script logo | Challenge | interchangeable with every bakery; use deep burgundy bands — [agent] |
  | Big food-photo hero | Challenge | no photos exist; the day's schedule is the real asset — [agent] |
  | Order form with fields | Avoid | cake orders are by phone or message with 48h notice (copy) — [agent] |
- Intended perception (5 seconds) — [inferred]:
  - P1 "I can tell if it's open right now" → check: open/closed line above the headline, legible on a 390px first screen
  - P2 "small and handmade, two people" → check: hand-built day strip, plain first-name voice, no corporate chrome
  - P3 "bread and tarts have a time" → check: tagline times 7 / 9 / 2 drawn as a timeline
- Sophistication: everyday — neighbourhood prices (£2 to £6), walk-in trade — [inferred]
- Differentiate on: the bakery's day as the layout (bread 7, tarts 9, gone by 2) — [agent]

## 4. Opening vocabulary
"warm, local, handmade"
Reading: deliberate preference — it is the stated register — [agent]

## 5. References
None supplied. tallyroll.md is a counter-reference (avoid the product-UI look) — [client]

## 6. Directions explored
| Direction | Origin | Fonts | Colour |
| A Day strip (selected) | agent | Synonym + Sentient [engine] | Club Cream [engine] |
| B Price board | agent | Synonym + Sentient [engine] | Parchment and Ink [engine] |
| C Soft and rosy | agent | Author + Plein [engine] | Clay and Linen [engine] |

| Axis | A Day strip | B Price board | C Soft and rosy |
| Composition | asymmetric: headline left, day strip right, stacked bands — because P1, phone-first | one centred menu column | catalogue grid of items |
| Scale | huge headline, mid-size prices, several moments — because the tagline is the voice | flat scale | one big moment |
| Imagery | CSS/SVG day strip — because P3, no photos | type only | photo placeholders |
| Signature device | the day strip (7 / 9 / 14) | ruled ledger | none |
| Colour proportion | burgundy fills two full bands, cream the rest — because V1 | cream almost everywhere, brown type | rose accents |
| Surface | rounded ends on the strip only, flat otherwise | flat, square | rounded cards |
| House-style markers | 1 (H4) | 5 (H1 H2 H3 H4 H5) | 2 (H2 H6) |
| Distinct on | composition, imagery, colour proportion, signature | | |
Other-client test: the day strip is built from this bakery's tagline times; no other client has it.

## 7. Selected direction
A Day strip — origin: agent — [agent]
Cream ground with two burgundy bands. The first screen states open or closed, then the tagline beside a drawn timeline of the day. Serves P1 to P3, V1, V2.
The one memorable thing: the tagline is drawn as the bakery's day.
House style: 1 marker (H4). Chosen because it departs most from the category's shared layout (Gate 2 rule) — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200 to 700, humanist sans, no italics
- Body: Sentient (sentient), FFL, weights 200 to 700, serif with italics
- Both are Fontshare: self-host only, keep files out of public repos. The page is one HTML file, so @font-face points to ./fonts/*.woff2 and falls back to system-ui and Georgia until the files are added.
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Light, Two-Tone
- Ground #F5E7C3 · figure #5B1D26 · text #37342E (10.1:1) · muted #67645D (4.8:1) · figure on ground 10.37:1
- Tints and shades from apply: tint-1 #90474E, tint-3 #EDAEB1, shade-1 #48161D
- On burgundy bands: ground colour for text and button label (10.37:1)
### Layout plan — [agent]
- Default: centred hero, three cards, stats, testimonials, CTA band. Cut: testimonials, stats, newsletter (no content for them).
- Visitor order: open now? → what's baked and prices → cake orders → where and when.
- Only-this-brief thing: the day strip and the hours.
- Axes as §6 column A.
### Imagery plan — [agent]
- Job: make visitors believe bread and tarts have a time of day — serves P3
- Kind: CSS/SVG day strip; no photography
- Shot list for the client to commission (not placed, no holes left): Ana scoring loaves, tight crop, window light; a tray of pastel de nata just out, raking light; the single oven.
- Ships now: the day strip.
### Judgment tokens — [agent]
- Spacing varies by section: tight in price lists, large between bands.
- Radii: 0 except the strip's bar ends.
- Motion: none beyond link underlines.

## 9. Constraints
- C1 Open/closed line is the first text on a 390px screen, above the headline — [agent]
- C2 Hours and address are visible within two phone screens; the phone number is a tap-to-call link — [agent]
- C3 Every price appears in the brief; no reviews, stats or invented claims — [client]
- C4 Headline is at least 4x body size — [agent]
- C5 No photo frames or empty placeholder boxes — [agent]
- C6 House-style markers on the render are 3 or fewer — [agent]
- C7 Burgundy covers two full-width bands — [agent]

## 10. Avoid
- Pastel ground with script wordmark — [agent]
- Row of three cards — [agent]
- Gradient backgrounds — [agent]
- Emoji icons — [agent]
- Centred hero — [agent]
- Order form with fields — [agent]

## 11. Decisions log
| Gate 2 pick | A | n/a (non-interactive) | departs most from the category layout | until approval |

## 12. Open decisions
- Instagram URL and message channel for cake orders: not in brief; links are placeholders — decide at: handover — [inferred]
- Real photography: commission per shot list — decide at: launch
- Font files: download Synonym and Sentient from Fontshare into ./fonts — decide at: deploy
- Direction not approved by the client — decide at: first review
