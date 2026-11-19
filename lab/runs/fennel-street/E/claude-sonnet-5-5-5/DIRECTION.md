# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run, no gate approvals) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: locals within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where, and make cake orders easy — [client]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 The opposite of tallyroll.md — "The opposite of tallyroll.md" — [client] (file not available to read; reading: not a tool/dashboard, no data-product look — [inferred])
- V3 Plain honesty: only the supplied copy, no invented claims, reviews or prices — "don't add claims, reviews or prices" — [client]

## 3. Positioning
- Category: "the bakery near me", the place for custard tarts — [inferred]
- Alternatives: supermarket in-store bakery; chain coffee-and-pastry shops; other independent bakeries with a pastel Instagram-style site — [inferred]
- Conventions:
  | Convention | Decision | Why |
  | Opening hours and address near the top | Adopt | Audience checks "is it open" on a phones — [agent] |
  | Menu as list with prices | Adopt | Visitors came to see what's baked — [agent] |
  | Big food photo hero | Challenge | No photos supplied; the line "Bread at seven, tarts by nine, gone by two" is the hero — V3 [agent] |
  | Pale cream + sage/pastel "artisan" palette | Challenge | Interchangeable with other indie bakeries; use deep burgundy fields — [agent] |
  | Order form / online shop | Avoid | Brief asks for message or phone only — V3 [agent] |
- Intended perception (check on screenshot) — [inferred]
  - P1 Open and findable right now → check: open/closed status and hours are visible on the first phone screen without scrolling
  - P2 Made by two people by hand → check: hand-lettered display type, drawn tart, no stock-style imagery
  - P3 Small, honest, sells out → check: day timeline 7 / 9 / 14 and "gone by two" appear as content
- Sophistication: everyday — prices £2–£6, walk-in trade — [inferred]
- Differentiate on: the baking day itself (7 / 9 / 14) as the page's spine, with live open status — [agent]

## 4. Opening vocabulary
"warm, local, handmade"
Reading: deliberate preference — stated as the register — [agent]

## 5. References
| Reference | Admire | Borrow | Avoid | Just interesting |
| tallyroll.md | — | — | Whatever it is (negative reference) — [client] | — |

## 6. Directions explored
Font pair and colours from engines. Combination [agent].
| Direction | Origin | Grounded in | Outcome |
| A "Bake day" — Bagnard + Source Sans 3; Club Cream | agent | P1, P3 | Selected |
| B "Shop sign" — Red Hat Display + Source Sans 3; Clay and Linen | agent | P2 | Not selected: pale ground, muted figure, closest to category default |
| C "Recipe card" — Recursive + Source Sans 3; Parchment and Ink | agent | V1 | Not selected: mono-style headlines read technical |

| Axis | A Bake day | B Shop sign | C Recipe card |
| Composition | Asymmetric: status + line left, tart drawing right, then timeline — because P1 | Centered hero, card grid — because category | One reading column — because V1 |
| Scale | Several big moments, one per section — because P3 | One big moment, rest small | Flat |
| Imagery | CSS/SVG drawn tart and bread — because P2 | Placeholder photo frames | Type only |
| Signature device | Day timeline 7/9/14 and street-sign plate — because P3 | Hand-drawn underline | Ruled list |
| Colour proportion | Burgundy as full-width fields alternating with cream — because P2 | Ground almost everywhere | Ground almost everywhere |
| Surface | Scalloped edge, soft corners, no shadows — because V1 | Rounded cards | Flat square |
| House-style markers | 1 (H4 no; H1 no; H2 no; H3 partial: price leaders) | 4 | 5 |
| Distinct on | composition, scale, imagery, colour, surface | | |
Other-client test: the 7/9/14 timeline and Ana/Rita copy belong only to this bakery.

## 7. Selected direction
A "Bake day" — origin: agent — [agent]
Left-aligned page led by live open status and the line, with a drawn tart; the day timeline and burgundy fields carry the handmade warmth. Serves P1–P3, V1, V3.
The one memorable thing: the page is organised like the bakery's day, 7, 9, 14.
House style: 1 marker.

## 8. Design system
### Typography — [engine]
- Headlines: Bagnard (bagnard), OFL, single weight 400, Latin only; caveat: missing # % * + = [ ] { } and ß Ø Ł Š Ž; display only — used for name, line, section heads, never for prices. Third-ranked headline pick; chosen over rank 1 Recursive (mono) for handmade character — [agent]
- Body: Source Sans 3 (source-sans-3), OFL, weights 200–900 — engine top body pick
- Delivery: self-hosted `./fonts/Bagnard.woff2`, `./fonts/SourceSans3.woff2` per engine CSS; not bundled in this file (see Open decisions)
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, Light
- Ground #F5E7C3 · Figure #5B1D26 · Text #37342E · Muted #67645D · tint-1 #90474E · tint-3 #EDAEB1 · shade-2 #360E14
- Engine watch-out: easy to tip into pastiche; keep type and layout contemporary
### Layout plan — [agent]
- Default dropped: centered hero, three cards, testimonials, stats.
- Visitor questions: open now? → what's baked and cost → where → how to order a cake.
- Only-this-brief: the baking-day timeline and the price list.
- Cut: testimonials, stats, newsletter, gallery.
- Order: header, hero (status + line + tart), timeline, menu (daily / season), about, cake orders band (burgundy), hours + address, footer.
### Imagery plan — [agent]
- Job: make visitors believe two people bake this by hand — P2
- Kind: SVG illustration (pastel de nata) + CSS timeline; no photos supplied
- Shot list (future photography, Open decision): Rita's tarts straight from the oven, overhead, window light; Ana's loaves on the cooling rack
- Treatment: engine colours only, flat shapes
- Ships now: SVG tart in hero; timeline; street-sign plate. No empty frames.
### Judgment tokens — [agent]
- Radius 4px on buttons, scalloped band edges; no shadows; spacing varies by section (tight in lists, wide between sections); no motion except none.

## 9. Constraints
- C1 First phone screen (390×844) shows open/closed status, hours and the line → check: visible without scroll — P1 [agent]
- C2 Every price and fact matches the brief; no added claims → check: compare to copy — [client]
- C3 Section headlines ≥ 3× body size → check: render — [agent]
- C4 Tart is drawn, no empty image frame → check: no grey boxes — P2 [agent]
- C5 Timeline shows 7 / 9 / 14 → check: visible — P3 [agent]
- C6 Cake order phone number is a tap-to-call link and ≥44px tall button → check: render — [agent]
- C7 Body text contrast ≥ 4.5:1 → check: engine pairs only — [agent]

## 10. Avoid
- Three-card rows; stat rows; gradient backgrounds; emoji icons; pill badges; centered hero; stock-photo placeholders — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | (non-interactive) | best serves page job and departs from category layout | until review |
Rejected: none.

## 12. Open decisions
- Font files not bundled; add woff2 files to ./fonts or approve a different delivery — decide at: deploy — [agent]
- "Message us" channel not given; linked to Instagram placeholder `#` — decide at: client handover — [inferred]
- Instagram URL missing — decide at: client handover
- Photography — decide when client supplies it
- Spec approval (Gate 3) not given — status stays draft

## 13. Checkpoints
(see end of run report)
