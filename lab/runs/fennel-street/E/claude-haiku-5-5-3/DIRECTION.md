# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; not approved at Gate 1 or Gate 3) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: people within a few streets who walk in; people who heard about the custard tarts; mostly on phones, checking whether it is open — [client]
- The page must: tell a visitor whether the shop is open, where it is, what is baked, and how to order a cake — [client]

## 2. Values (user-owned, 2–5)
- V1 Handmade and run by people: two sisters, one oven — "Ana bakes the bread. Rita does everything with custard… still only have one." — [client]
- V2 Small and local: a few streets, walk-in first — "Most customers walk in" — [client]
- V3 Sells out, so it's a daily rhythm, not a catalogue — "Bread at seven, tarts by nine, gone by two." — [client]

## 3. Positioning
- Category: neighbourhood bakery — [inferred]
- Alternatives: supermarket bread; a chain or high-street bakery; ordering a cake from an online-only baker — [inferred] (described by kind; none named by the client)
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Hero photo of loaves with a slogan and one "Order" button | Challenge | No photos are supplied; the line and the day's timeline carry the first screen (V3, P2) |
  | Opening hours and address in the footer only | Avoid | The visitor's first question is "is it open" (P2) |
  | Product grid of cards, each with an icon or emoji | Avoid | Prices in a plain ruled list read like the shop's board (P3) |
  | "Our story" with founder portrait | Adopt, in text only | Visitors want to know who makes it (V1, P1) |
  | Price-first menu with names and £ values | Adopt | Prices are the facts people came to check |
- Intended perception:
  - P1 "A real shop, run by two people who bake it themselves" → check: the sisters' names and the About line appear within the first two screens on a phone
  - P2 "Open now, and I can walk in" → check: status line, hours and address are visible without scrolling on a 390px screen
  - P3 "Made by hand, sold out by two" → check: the day's rhythm is shown as a timeline, and nothing on the page looks like a stock-photo or SaaS template
- Sophistication: considered — prices from £2.10 to £28 and a single-oven, cake-to-order shop — [inferred] (price signal from the brief's copy; no explicit tier given)
- Differentiate on: the daily rhythm — bread at seven, tarts by nine, gone by two — [agent]

## 4. Opening vocabulary
"Bread at seven, tarts by nine, gone by two."
Reading: deliberate preference — the line is the brand's own voice, so the page leads with time, not product photography — [agent]

## 5. References (0–5)
None supplied. [inferred]

## 6. Directions explored (3)
Engine picks (same in all three): Cormorant (headlines) + Source Sans 3 (body) [engine]; Clay and Linen colour direction [engine].

| Axis | A · Ruled daily board (selected) | B · Hand-set poster | C · Photo-led shop front |
| --- | --- | --- | --- |
| Composition | Hero name, then a single-column timeline and a ruled price list — because P2 (open/where first) | Full-bleed type stacked per section — because P1 | Hero image band, menu grid below — because Challenge convention on hero photo |
| Scale | One big moment (the name), then even small text — because P3 (quiet, handmade) | Several large statements, one per section — because the line is the voice | One large image, then body text — because photo carries it |
| Imagery | Type and an SVG day timeline; no photos shipped — because no client photos exist | Type as image (large lettering of the line) — because V3 | Photography of loaves, tarts, the oven — not supplied, so not shippable |
| Signature device | A ruled timeline with the three times — because V3 | A hand-set underline under each time — because V1 | A recurring crop — because photo |
| Colour proportion | Linen almost everywhere, Rose Clay as thin figure — because P3 | Rose Clay large fields alternating with Linen — because P1 | Linen ground, figure in captions — because photo leads |
| Surface | Flat paper, 6px corners, no shadows — because V1 | Flat paper with slight grain — because V1 | Layered cards with shadow — because product-shop convention |
| House-style markers (H1–H6) | 3: H1, H2, H3 | 2: H1, H2 | 1: H2 |
| Distinct on | Composition, Imagery, Signature device | Composition, Scale, Signature device | Imagery, Scale, Surface |

Other-client test (A): the daily timeline is built from this brief's three times and copy; another bakery would have different times and products, so it doesn't transfer. [agent]

## 7. Selected direction
A · Ruled daily board — origin: agent — [agent]
The page reads like the shop's day: the open status and where first, then the timeline of bread, tarts and sell-out, then a ruled price list and the cake order. It serves V1 and V3 through text and the timeline, and P2 through the first screen.
The one memorable thing: the day drawn as a single ruled line, bread at seven to gone by two. [agent]
House style: 3 markers (H1, H2, H3) — under the threshold of 4. [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Cormorant (cormorant), weights 300–700, OFL, self-hosted; url https://github.com/CatharsisFonts/Cormorant
- Body: Source Sans 3 (source-sans-3), weights 200–900, OFL, self-hosted; url https://github.com/adobe-fonts/source-sans
- Pairing: cormorant + source-sans-3 — [engine]
- Engine caveat: Cormorant is too thin for body text; used only at large sizes. [engine]
- Engine caveat: Cormorant is a sibling of Cormorant Garamond, a commonly overused face; kept because the engine returned it for the brief's warm/elegant reading. Reconsider if it reads as a template at render. [agent]

### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen), Light + Muted, Chromatic — [engine]
- Ground: Linen #F5EDE4 — [engine]
- Figure: Rose Clay #8D5951 — [engine]
- Text: #3D3832 (10:1 on Linen) — [engine]
- Text muted: #6C6761 (4.83:1 on Linen) — [engine]
- Figure on ground: 4.92:1 — used for headings and links only, never for body copy — [engine]
- Alternative noted by engine, not used: Parchment and Ink (Warm Paper #F7EFE3 / Bitter Brown #2D1D14) — [engine]

### Layout plan — [agent]
- Default (avoided): nav, centred hero with two buttons, three feature cards, stats, testimonials, CTA band, footer.
- Visitor's questions, in order: is it open and where → what is baked, when → what it costs → can I order a cake → who makes it.
- Lead with: the day timeline as content, not decoration.
- Cut: stats row, testimonials (none supplied), feature cards.
- Axis positions: Composition single column with a two-part hero; Scale one big moment then even text; Imagery type and SVG only; Signature device ruled timeline; Colour proportion Linen ground, Rose Clay figure; Surface flat, 6px corners, no shadows.

### Imagery plan — [agent]
- Job: make a visitor believe the shop runs on a daily rhythm made by hand — serves P3
- Kind: type as image + one SVG diagram — none of photography, because none is supplied
- Shot list: none. Photography (loaves, tarts, oven, the sisters at work) is left for the client to commission; the layout does not reserve space for it.
- Treatment: the timeline is drawn in Rose Clay on Linen; the times set in Cormorant at large sizes.
- Ships now: SVG day timeline (7:00, 9:00, 14:00) built from the brief's copy; the line set as a large headline.
- Honesty: no invented product images, customers or reviews.

### Judgment tokens — [agent]
- Spacing: 8px base; 4 steps only (8, 16, 32, 64) — ties to a calm, ruled list.
- Radius: 6px on the cake-order button only; everything else square. [agent]
- Motion: none. The shop is slow and handmade; a static page matches it. [agent]

## 9. Constraints (pass/fail on a screenshot)
- C1 Open status, hours and address are visible without scrolling on a 390px-wide phone render → check: the phone screenshot's first screen contains all three. — [agent]
- C2 The sisters' names (Ana and Rita) and the About line appear within the first two screens on phone → check: scroll once on the 390px render and find both. (P1) — [agent]
- C3 Every price in the brief appears, and no price, review or claim appears that the brief does not contain → check: text compared with the Copy list. — [agent]
- C4 Cake ordering is one tap away: a tel: link to 020 7946 0381 and the 48-hour notice are visible without scrolling past the menu → check: phone screenshot. — [agent]
- C5 No external images, no emoji, no gradient; the only figure colour on the page is Rose Clay → check: source has no img/url() to remote hosts; screenshot shows flat ground. — [agent]
- C6 Body text uses #3D3832 or #6C6761 only; Rose Clay is never used for body copy → check: computed colour of body text. — [engine values, agent rule]

## 10. Avoid (≤6)
- Hero photo of loaves or any stock image — [agent]
- Emoji or icons in the menu — [agent]
- Gradient backgrounds or shadowed cards — [agent]
- Product card grid for the menu — [agent]
- Testimonials, stat rows, or star ratings (none supplied) — [client: no claims beyond the brief]
- Pill badges above the headline — [agent]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A, Ruled daily board | A | (none: non-interactive run) | Best serves the page job (open, where, what's baked) and differs on three axes from the shared category layout | Settled = until the client reviews the render |
| Cormorant + Source Sans 3 | engine pair | (none) | Warm/elegant reading; serif at display sizes suits a handmade shop | Settled = until Gate 3 |
| Clay and Linen | engine pick | (none) | Engine's top pick for food and beverage, warm and quiet | Settled = until Gate 3 |

Rejected (final): none.

## 12. Open decisions
- Font files: Cormorant and Source Sans 3 are specified with @font-face to ./fonts/ but the .woff2 files are not bundled in this run; the page renders in Georgia / system-ui until they are added. — decide at: asset handoff — [inferred]
- Instagram URL for the footer link: none supplied; placeholder href="#". — decide at: client handoff — [inferred]
- Whether Cormorant reads as overused at render, or should swap to Happy Times at the IKOB (engine serif, Western European accents only). — decide at: Gate 3 — [agent]
- Photography (loaves, tarts, oven, the sisters): client to commission; not shipped. — decide at: client handoff — [inferred]
- Whether to show a map embed: not used; a plain address link only. — decide at: Gate 3 — [agent]
- Gate 1 and Gate 3 approvals: not obtained (non-interactive run). All [inferred] and [agent] tags remain until the client confirms. — decide at: Gate 3

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1, phone 390px | C1 | Pass | — | none |
| Round 1, phone 390px | C2 | Fail (About at page bottom) | Bug | Moved About section under the day timeline; re-render shows it at the first scroll |
| Round 1, phone 390px | Gutter | Fail (text touched screen edges) | Bug | `.hero` padding shorthand overrode `.wrap` side padding; fixed to top/bottom only |
| Round 1, phone 390px | C3, C4, C5, C6 | Pass on render and source review | — | none |
| Round 1, desktop | Layout check: centred hero flagged | Checker hit; h1 is left-aligned in a page-centred column | Checker false positive, kept | No change; the first screen is left-aligned, not centred |
| Round 1 | Layout check: no other patterns | Pass | — | Two-round cap: one round used, stopped |
| Open | Body font reported as Cormorant by checker | Not resolved | Lesson: checker reports the first @font-face family for body | Confirm in browser devtools when fonts are bundled |
