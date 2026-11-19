# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; no approval gate passed) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries, a few seasonal cakes. — [client]
- Audience: people within a few streets who walk in; people who heard about the custard tarts; mostly on phones, often checking whether the shop is open. — [client]
- The page must: tell a visitor whether the shop is open and what's baked, show where it is, and make a cake order easy. — [client]

## 2. Values (user-owned, 2–5)
- V1 Neighbourhood: a shop for the streets around it, not a chain — "neighbourhood bakery" — [client]
- V2 Handmade and small: two people, one oven, bread and custard made by hand — "Ana bakes the bread. Rita does everything with custard… still only have one [oven]" — [client]
- V3 Time-of-day: the bakes have a schedule and sell out — "Bread at seven, tarts by nine, gone by two." — [client]

## 3. Positioning
- Category: neighbourhood bakery (sourdough and Portuguese pastries) — [client]
- Alternatives: the supermarket loaf; a chain bakery; the bakery across the road; ordering a cake from a marketplace — described by kind — [inferred]
- Conventions (3–5):
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Hero photo of loaves on a wooden board | Avoid | No photography supplied; a fake or stock image would claim things the brief doesn't (V2) — [agent] |
  | Centred slogan hero with two buttons | Challenge | The visitor's first question is "open now?", so the timing leads, not the slogan (P2) — [agent] |
  | Opening hours tucked in the footer | Challenge | Hours are the reason most phone visitors arrive (P2, audience) — [agent] |
  | Warm, unhurried cream-and-brown palette | Adopt | Matches a handmade, daytime shop (V2) — [agent] |
  | Online cart for cakes | Avoid | Brief says cakes are ordered by message or phone with 48 hours' notice — [client] |
- Intended perception: three qualities a stranger reports after five seconds on the page — [inferred]
  - P1 Made by hand, by two named people → check: Ana and Rita's names and "one oven" sit on the first screen or directly below it on a 390px phone.
  - P2 Open now, and here's what's left → check: the open/closed line and the bake times are visible without scrolling at 390px.
  - P3 A shop on your street, not a chain → check: the address appears above the fold.
- Sophistication: everyday — prices £2.10–£6.40 and a walk-in shop — [inferred]
- Differentiate on: the bake schedule itself: when each thing comes out and when it's gone. The alternatives don't tell you this. — [agent]

## 4. Opening vocabulary
Not supplied. — [inferred]
Reading: none recorded. Working vocabulary from the brief: "warm, local, handmade." — [agent]

## 5. References (0–5)
None supplied. — [inferred]

## 6. Directions explored (2)
Engine results: find-font `recommend --role headlines --role body --feel warm --feel editorial` returned Synonym (headlines, id `synonym`) and Sentient (body, id `sentient`). find-color `recommend --domains food-and-beverage` returned "Clay and Linen" (`lib.clay-and-linen`, rank 3) and "Espresso and Milk" (`lib.espresso-and-milk`, pick). — [engine]

| Axis | A: Bake board (selected) | B: Espresso shopfront |
| --- | --- | --- |
| Composition | Bake-times board first, then one reading column — because P2 and V3 put timing before story | Stacked full-bleed bands, each a section — because a product sheet reads as a set of facts |
| Scale | One large line in the board; everything else flat and small — because the brief's line is the one moment | One huge heading per band — because the shop name carries the page |
| Imagery | SVG timeline board drawn from the brief's times; no photos — because P2 and no supplied images | Type only, price lists — because nothing to show but the list |
| Signature device | A ruled timeline with 7:00, 9:00, 14:00 marks — because V3 |  A ruled price ledger — because the menu is the product |
| Colour proportion | Linen ground almost everywhere; Rose Clay as one solid field for the board only — because P2 needs the board to stand out | Espresso ground covers almost everything; Caramel for prices — because a dark shopfront |
| Surface | Flat, 12px radius on the board only, no shadows — because V2 handmade | Flat, square, no shadows — because a printed menu |
| House-style markers (H1–H6) | 1: H2 (pale ground, one muted figure) | 5: H1, H3, H4, H5, H6 |
| Distinct on | Composition, scale, imagery, signature device, colour proportion, surface (6) | Differs on at least 3 from A |

Other-client test (A): could this belong to another client? A timeline built from one shop's own hours and bake times cannot be reused for another shop. — [agent]
Engine pick note: Espresso and Milk was the engine's default, but its chooseIf is "a cafe or coffee product." The brief is a daytime bakery with a warm register, so A uses rank 3, Clay and Linen, whose chooseIf ("food or product photography leads") also does not match: no photography exists. This is a judgement call. — [agent]

## 7. Selected direction
A: Bake board — origin: agent — [agent]
A daytime bakery page that opens on the day's schedule: when bread, tarts and buns come out and when they're gone, with the open status beside it. It serves P2 and V3 first, and P1 and V2 through the names and the single oven. Everything reads in a warm linen ground with one rose-clay board.
The one memorable thing: the bake timeline, drawn from the shop's own times.
House style: 1 marker (H2). No `House style kept because` needed.

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (id `synonym`), Fontshare, FFL. Self-host only; keep files out of public repos. Weights 200–700, variable.
- Body: Sentient (id `sentient`), Fontshare, FFL. Self-host only. Weights 200–700, variable, italics available.
- Files: `./fonts/Synonym.woff2`, `./fonts/Sentient.woff2` — **not bundled**. Downloads needed before the page shows the intended faces. Until then the fallback stacks (`system-ui` / `Georgia`) render.

### Color — [engine]
- Direction: Clay and Linen (`lib.clay-and-linen`) — [engine]
- Ground: Linen #F5EDE4 — [engine]
- Figure: Rose Clay #8D5951 — [engine]
- Text: #3D3832 (10.00:1 on Linen) — [engine]
- Text muted: #6C6761 (4.83:1 on Linen) — [engine]
- Figure on ground: 4.92:1 (headings and links only, not long body) — [engine]

### Layout plan — [agent]
- Default: nav, centred hero, three feature cards, stats, testimonials, CTA band, footer. Cut: stats, testimonials, cards. Nothing in the brief supports them.
- Visitor's questions in order: is it open and what's on → where is it → what's baked and what it costs → how to order a cake → who makes it.
- The one thing only this brief has: the bake schedule (7:00, 9:00, 14:00, "until we sell out").
- Cut: anything not in the supplied copy.
- Axis positions: see §6, column A.

### Imagery plan — [agent]
- Job: make a visitor believe the bakes are real, timed and limited today — serves P2.
- Kind: illustration (inline SVG timeline) + type. No photography supplied.
- Shot list (for the client to commission later, not shipped): Ana's loaves on the bench, first light, tight crop, sits above the bread list. Rita's custard tarts, cut open on a tray, tight crop, sits beside the tart price. — [agent]
- Treatment: flat Rose Clay field for the board; Linen elsewhere; images (when supplied) meet the grid inset, never full-bleed over text.
- Ships now: the bake timeline SVG (7:00 bread, 9:00 tarts, 14:00 gone, sold out marker); the line set large as type.

### Judgment tokens — [agent]
- Spacing: 8px base, larger gap between sections than within lists.
- Radius: 12px on the board only; 0 elsewhere. Ties to V2.
- Motion: none beyond a colour change on link hover; respect reduced motion.

## 9. Constraints (pass/fail on a screenshot)
- C1 Open status and bake times visible without scrolling at 390px width → check: phone screenshot shows the open/closed line and at least the bread time above the fold. — [agent]
- C2 Headline is at least 4× body size; nothing else competes in size → check: computed font sizes. — [agent]
- C3 Only Linen, Rose Clay, and the two text values are used for colour → check: CSS custom properties and rendered colours. — [engine]
- C4 No external requests, no external images → check: no http(s) URLs for src, href to assets, or font links except none. — [agent]
- C5 Address and "Order a cake" are visible above the fold on phone (P3, ordering) → check: phone screenshot. — [agent]
- C6 Perception P1 holds: Ana and Rita are named within the first screen or directly below → check: rendered text order. — [inferred]

## 10. Avoid (≤6)
- Centred slogan hero with two buttons
- Rows of three cards
- Placeholder image frames or stock photos
- Testimonials, star ratings or review counts (none supplied)
- Pill badges and emoji icons
- Decorative gradients

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A: Bake board | A | — (non-interactive, no pick) | Serves P2 and V3; B is a dark cafe-style look the brief doesn't ask for | Settled = until approval |
| Engine font pair Synonym + Sentient | Engine top pair | — | Warm, editorial, same family as engine's top picks | Settled |
| Colour Clay and Linen over Espresso and Milk | Clay and Linen | — | Warm daylight register; see §6 note | Settled = until approval |

Rejected (final): none recorded.

## 12. Open decisions
- Spec approval (Gate 3): build runs against draft — decide at: user review — [inferred]
- Fonts: download Synonym and Sentient woff2 into `./fonts/` (self-hosted) — decide at: before publish — [engine]
- Instagram account URL: footer link is a placeholder `#` until supplied — decide at: before publish — [inferred]
- Cake order channel: phone 020 7946 0381 and "message us" with no email given; the message link is a placeholder — decide at: client — [inferred]
- Photography: none supplied; shot list in §8 is for the client to commission — decide at: client delivery — [agent]
- Tallyroll contrast: `tallyroll.md` is not in this project, so the "opposite of" reference could not be read. Direction A avoids the brief's listed opposites, but this is unchecked — decide at: Gate 3 — [inferred]
- Sophistication "everyday" — based on prices and walk-in setting — decide at: Gate 3 — [inferred]
