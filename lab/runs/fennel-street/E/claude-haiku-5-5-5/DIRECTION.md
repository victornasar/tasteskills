# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; Gates 1–3 not confirmed) · Mode: fast · v1 · 2026-11-19

## 1. Context
- Product: neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries and a few seasonal cakes — [client]
- Audience: people within a few streets who walk in; people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked, when the shop is open and where it is, and make a cake order easy — [client]

## 2. Values
- V1 Handmade, by people you can name — "Ana bakes the bread. Rita does everything with custard." — [client]
- V2 Small and particular — "one oven and still only have one"; sells out by two — [client]
- V3 Warm without being twee; the register is "warm, local, handmade", the opposite of a slick product page — [inferred]

## 3. Positioning
- Category: neighbourhood bakery, the sourdough and custard-tart shop round the corner — [inferred]
- Alternatives: supermarket bread and packaged pastries; a chain bakery; ordering a cake through a large online marketplace (described by kind) — [inferred]
- Conventions:

  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Today's list with prices near the top | Adopt | Visitors come to check what's baked and what it costs — [agent] |
  | Opening hours and address near the top | Adopt | "Is it open?" is the first question on a phone — [agent] |
  | Hand-lettered script name | Avoid | Reads twee against V3 — [agent] |
  | Wheat-stalk or loaf line icon | Challenge | Makes every bakery look interchangeable — [agent] |
  | Kraft paper or gingham texture | Avoid | A generic "artisan" signal with no product fact behind it — [agent] |

- Intended perception:
  - P1 "Someone here makes this by hand." → check: both names and the one-oven fact appear before the cake section.
  - P2 "I can tell in a second whether it's open." → check: status line with hours is inside the first 844px on a 390px phone.
  - P3 "Warm and particular, not decorated." → check: one figure colour; no gradients, patterns, icons or pill badges. — [inferred]
- Sophistication: everyday — daily bakes £2.10–£5.60, whole cakes £28 — [inferred]
- Differentiate on: the day as a timeline. The shop sells out by two, so the page says when to come. — [agent]

## 4. Opening vocabulary
Not supplied beyond the brief. — [inferred]

## 5. References
None supplied. — [client]

## 6. Directions explored
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A · Bake clock | agent | The line "Bread at seven, tarts by nine, gone by two." | P2, P1 | Selected | — (non-interactive run) |
| B · Stamp and sack | agent | The name and the one-oven fact | P1 | Not selected | Its single huge statement is the house layout; the first screen doesn't answer P2 |

| Axis | A · Bake clock | B · Stamp and sack |
| --- | --- | --- |
| Composition | Day timeline under the headline, then short sections in visitor order: today, season, order, about, find us — because P2 and the visitor's questions come first | One huge name and a round stamp on the first screen, then a single reading column — because the name is the brand's one statement |
| Scale | Several big moments, one per section, in display type — because the list and the order are the content | One huge statement, everything else small — because a single slogan carries the page |
| Imagery | SVG illustration of the bake day plus type — because no photography is supplied and the timeline is a real product fact — [agent] | Type used as image — because the copy itself is the picture |
| Signature device | A ruled timeline, 7:00 · 9:00 · 14:00 — because "bread at seven, tarts by nine, gone by two" is the brand's one fact — [agent] | A round stamp — because a seal reads as handmade |
| Colour proportion | Linen ground; Rose Clay as a full band for cake orders and as timeline ink — because the order is the one action on the page | Ground almost everywhere, one Rose Clay figure — because one muted colour keeps it quiet |
| Surface | Soft 8px corners on the order card, hairline rules elsewhere — because "handmade" needs some give | Square, flat, no shadow — because flat reads as printed |
| House-style markers (H1–H6) | 1: H3 (ruled timeline) | 5: H1, H2, H4, H5, H6 |
| Distinct on | Composition, scale, imagery, signature device, colour proportion, surface (6) | Same six axes (6) |

Other-client test (A): the day-as-timeline is specific to a bakery that sells out by a set time; a cafe or florist could not use the same line. — [agent]

## 7. Selected direction
A · Bake clock — origin: agent — [agent]
Serves V1, V2 and P2: the day's bake and the opening hours sit on the first phone screen, with names and the one-oven fact directly under them. The order band is the only full colour field.
The one memorable thing: the day as a ruled line from 7:00 to 14:00.
House style: 1 marker (H3). No `House style kept because` note needed. — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Bagnard (id `bagnard`), OFL, display only, one weight (400). Self-hosted from `./fonts/Bagnard.woff2` — [engine]. The engine's top headline pick was Recursive (id `recursive`), which reads playful mono; Bagnard is the carved, editorial alternative from the same result — [agent]
- Body: Source Sans 3 (id `source-sans-3`), OFL, variable 200–900. Self-hosted from `./fonts/SourceSans3.woff2` — [engine]
- Notes from engine: Fontshare fonts dropped because the repo is public (`--public-repo` assumed) — [engine]. Bagnard lacks ß, Ø, Ł, Š, Ž and # % * + = [ ] { }; the copy uses none of them — [engine]
- Font files are not bundled in this run. Until they are added to `./fonts/`, the fallback stacks (Georgia, system-ui) render — [agent]

### Color — [engine]
- Direction: Clay and Linen (id `lib.clay-and-linen`), food-and-beverage, Light · Chromatic · Muted — [engine]
- Ground: Linen `#F5EDE4` · Figure: Rose Clay `#8D5951` · Text: `#3D3832` · Muted text: `#6C6761` — [engine]
- Contrast: Rose Clay on Linen 4.92:1; body text 10:1; muted text 4.83:1 — [engine]
- Engine avoid note: do not push the clay toward orange terracotta — [engine]

### Layout plan — [agent]
- Default: nav, centred hero with two buttons, three feature cards, stats, testimonials, CTA band, footer. Cut: stats, testimonials, cards.
- Visitor's questions in order: is it open? what's baked and what does it cost? where is it? how do I order a cake?
- The one thing only this brief has: the day as a timeline (7:00 bread · 9:00 tarts · 14:00 gone by two).
- Axis positions: as in §6, column A.

### Imagery plan — [agent]
- Job: make the bakery feel real and made by hand — serves P1
- Kind: illustration (SVG timeline) and type. No photography supplied.
- Shot list: none on the page. Photography of loaves, tarts and the shop is a client commission (Open decisions).
- Treatment: SVG in Rose Clay on Linen, 1.5px strokes, inset to the grid.
- Ships now: SVG bake timeline; the copy set as type; the daily and seasonal lists. No empty frames.

### Judgment tokens — [agent]
- Spacing: 8px base. 12px inside list rows, 48px between sections, 96px before the order band. Section gaps follow content, not a fixed scale.
- Radii: 8px on the order button only. Everything else square.
- Motion: none.

## 9. Constraints
- C1 Open status and hours sit inside the first 844px on a 390px-wide phone → check: phone screenshot, first screen shows open/closed and 7:00–14:00 — [agent]
- C2 Ana and Rita, and the one-oven fact, appear before the cake section → check: full-page screenshot order — [agent]
- C3 Every item shows its price; body text at least 16px on phone; prices align in one column → check: phone screenshot — [agent]
- C4 The cake order action (phone number, 48-hour note) is reachable from the header without scrolling → check: header link in the phone first screen — [agent]
- C5 Fewer than 4 of H1–H6 house-style markers on the screenshots; no gradients, pill badges, emoji or icons → check: marker count written per screenshot — [agent]
- C6 No empty image frames or grey placeholder boxes → check: full-page screenshot has no empty rectangles — [agent]

## 10. Avoid
- Hand-lettered script name
- Kraft paper or gingham texture
- Wheat-stalk or loaf line icons
- Pill badges or "New" banners
- Emoji as icons
- Stock bread photography

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A · Bake clock | A (non-interactive) | Answers "is it open" on the first screen; B scores 5 house markers | yes |

Rejected (final): B · Stamp and sack — 5 of 6 house-style markers, and its first screen answers the name, not the visitor's question.

## 12. Open decisions
- Photography of bakes and the shop — decide at: client commission; the page works without it — [inferred]
- Instagram URL for the footer and "Message us" — no handle was given; links are `#` placeholders — decide at: client handover — [inferred]
- Bagnard and Source Sans 3 `.woff2` files to be added to `./fonts/` — decide at: build handover — [agent]
- Open state: the page computes open/closed in Europe/London time from the stated hours; "or until we sell out" can't be known by the page, so the status says "or sold out" — [inferred]
- Gate 1 and Gate 3 approval not obtained (non-interactive run); status stays draft — [inferred]
- Sophistication "everyday" rests on price points only — [inferred]
- Contrast against tallyroll.md not checked: that file is not in the project — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
