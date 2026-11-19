# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run, not approved) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte: sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked, when the shop is open and where it is, and make cake orders easy — [client]
- Primary job in one line: a phone visitor learns "open or not, until when, where" in the first screen — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade"; "people who live within a few streets" — [client]
- V3 Handmade, small on purpose — "warm, local, handmade"; "one oven and still only have one" — [client]
- V4 Honest about scarcity — "gone by two", "or until we sell out" — [inferred]

## 3. Positioning
- Category: "the bakery on Fennel Street" / local bakery and pastry shop — [inferred]
- Alternatives: a supermarket in-store bakery; a chain coffee shop with pastries; another independent bakery further away — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Opening hours buried in the footer | Challenge | Audience checks "is it open" first; hours lead the page — [agent] |
  | Full-bleed hero photo of bread with a centred slogan | Challenge | No photos supplied; a slogan over a photo makes bakeries interchangeable — [agent] |
  | Menu with prices as a plain list | Adopt | Visitors act on it; prices are in the copy — [agent] |
  | Tap-to-call phone number | Adopt | Cake orders by phone is the client's channel — [agent] |
  | Rustic kraft-paper textures, chalkboard fonts | Avoid | Reads as pastiche (engine watch-out for this palette) — [agent] |
- Intended perception — [inferred]
  - P1 It's a real, small shop with its own day → check: the 7:00–14:00 day ruler with bread/tarts/gone marks is visible on the first phone screen
  - P2 I know right now whether it's open → check: a status line ("Open now" / "Closed now, opens …") sits in the first 600px at 390px width
  - P3 Warm, not slick → check: the burgundy and cream fields, a hand-drawn line illustration of a tart, no stock UI chrome (pills, gradients, card grids)
- Sophistication: everyday-considered — prices £2.10–£28, walk-in neighbourhood trade — [inferred]
- Differentiate on: the shop's day itself (bread at seven, tarts by nine, gone by two) shown as a live timeline — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — repeated in copy tone and the one-oven line. tallyroll.md was not present in the project, so "opposite" is read only from the words given — [agent]

## 5. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
| tallyroll.md (named, not found in project) | — | — | everything it stands for, per the brief | — |

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. The Day Ruler | agent | "Bread at seven, tarts by nine, gone by two"; phone visitors checking hours | P1, P2, V4 | Selected [agent] | — (non-interactive) |
| B. Shop-window board | agent | menu with prices, V2 | P3 | Not selected | — |
| C. Photo-led linen | agent | custard tarts are the draw | P3 | Not selected: needs photography that doesn't exist yet | — |

Engines: A = Synonym + Sentient (find-font pair `synonym`/`sentient`), Club Cream `lib.club-cream` (find-color) — [engine]. B = Author + Plein, Parchment and Ink `lib.parchment-and-ink` — [engine]. C = Alpino + Author, Clay and Linen `lib.clay-and-linen` — [engine]. Combinations — [agent].

| Axis | A. Day Ruler | B. Shop-window board | C. Photo-led linen |
| --- | --- | --- | --- |
| Composition | phone-first stack in the visitor's order: status → day → menu → cakes → find us — because P2 | one long menu board, everything else small — because convention "menu list" Adopt | full-bleed photo modules alternating with text — because tarts are the draw |
| Scale | one big moment: the line "Bread at seven, tarts by nine, gone by two", then mid-size section heads — because P1 | flat, even scale — because V3 small on purpose | several big photo moments |
| Imagery | SVG line drawing of a pastel de nata + the day ruler as a picture — because P1, no photos supplied | type only | photography (needs a commission) |
| Signature device | the 7→14 day ruler with a live "now" marker — because V4 and P2 | ruled price leaders | recurring round crop |
| Colour proportion | burgundy as large solid bands (status, cakes, footer) alternating with cream — because P3 warm | paper almost everywhere, ink thin | linen ground, clay accents |
| Surface | soft: 18px radius on the status board only, hand-drawn strokes, no shadows — because V3 handmade | square, flat, ruled | soft, photographic |
| House-style markers | 1: H5? no; H1 no (SVG drawing + ruler); H2 no (burgundy fields); H3 partial → count 1 (H3) | 5: H1 H2 H3 H4 H6 | 1: H2 |
| Distinct on | composition, imagery, signature, colour proportion, surface | scale, imagery, surface, colour | composition, imagery, signature |

Other-client test (A): the ruler encodes this shop's own hours and sell-out times; it wouldn't transfer to a bakery with different hours — [agent]

## 7. Selected direction
A. The Day Ruler — origin: agent — [agent]
The page is the shop's day. The first screen says if it's open now and draws the day from bread at seven to gone by two. Below that come the board of what's baked, the cake-order band with a tap-to-call number, and the address. Serves V1, V2 and V4, and P1–P3.
The one memorable thing: a burgundy day ruler with a dot showing where "now" falls between bread and gone.
House style: 1 marker (H3, the small labels on the ruler) — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (`synonym`), FFL, weights 200–700, no italics. Stack: "Synonym", system-ui, -apple-system, "Segoe UI", sans-serif
- Body: Sentient (`sentient`), FFL, weights 200–700, italics. Stack: "Sentient", Georgia, "Times New Roman", serif
- License: Fontshare, self-host only, keep the files out of public repos — [engine]
### Color — [engine]
- Direction: Club Cream (`lib.club-cream`), Two-Tone, light foundation
- Ground #F5E7C3 / oklch(0.93 0.05 90) · Figure Club Burgundy #5B1D26 / oklch(0.33 0.09 15) · no accent
- Text #37342E (10.1:1) · Muted #67645D (4.8:1) · Figure on ground 10.37:1 · Button ground-on-figure 10.37:1
- Tints #90474E #C4757C #EDAEB1 · Shades #48161D #360E14 #26080C
- Engine watch-out: easy to tip into pastiche; no gold, no faux-aged texture
### Layout plan — [agent]
- Default I'd reach for: nav, centred hero over a bread photo with two buttons, three feature cards, about, testimonials, CTA band, footer
- Visitor questions in order: is it open now / until when → where is it → what's baked and what does it cost → can I order a cake and how → who are you
- Only this brief has: the day ("bread at seven, tarts by nine, gone by two") and the one oven. It leads, as a live ruler
- Cut: feature cards, testimonials, stats, separate CTA band (cake band does it), nav menu beyond a call link
- Axes: as column A above
### Imagery plan — [agent]
- Job: make a visitor believe it's a real, small, handmade shop (P1, P3)
- Kind: line illustration (SVG, one tart) + data as picture (the day ruler). No photography ships
- Shot list for later commission: (1) a tray of natas just out of the oven, top-down, morning window light, beside the menu; (2) Ana's hands scoring a sourdough loaf, tight crop, side light, in the About section; (3) the shopfront on Fennel Street with the door open at 7:00, street level, in Find us
- Treatment: the drawing uses Club Burgundy strokes on cream only; it overlaps the hero's right edge on desktop and sits above the line on phones
- Ships now: SVG tart drawing, the day ruler, the street-sign address block. No empty image frames
### Judgment tokens — [agent]
- Spacing: tight inside the menu (rows 14px), generous between sections (72–120px); the status band is denser than the rest, because it's a tool
- Radii: 18px on the status board and cake band only (objects you hold); everything else square
- Motion: none, except the now-dot, which updates each minute without animating

## 9. Constraints
- C1 At 390×844, the status line (open/closed + today's hours) and the day ruler are both visible without scrolling → check: phone screenshot, first screen — [agent]
- C2 Every price in the brief appears, exactly as written, with nothing added → check: compare the menu text with the brief — [agent]
- C3 The phone number is a tap-to-call link and appears in the cake section and the footer/find-us → check: `tel:` hrefs present, visible in the screenshot — [agent]
- C4 (P3) No pill badges, gradients, emoji or three-card rows; burgundy covers at least two full-width bands → check: check-layout report + full screenshot — [agent]
- C5 Mon/Tue closed is stated in words, not only by colour → check: hours list shows "Closed" text — [agent]

## 10. Avoid
- Kraft paper, wood or chalkboard textures — [agent]
- Gold anywhere — [engine]
- Testimonials, star ratings, "since 2019" badges — [client: no added claims]
- Centred slogan over a placeholder photo box — [agent]
- Pill-shaped tags on menu items ("NEW", "BESTSELLER") — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. Day Ruler | — (non-interactive) | best serves "is it open / where / what's baked" on phones | until user review |
| Palette | Club Cream over engine pick Parchment and Ink | — | chooseIf "specialty brand… established feel" fits; burgundy fields avoid H2; Parchment's chooseIf needs photography | until user review |
| No photo placeholders | SVG drawing + ruler instead | — | brief allows placeholders, but the skill forbids empty frames and the drawing does the job | until photos exist |

## 12. Open decisions
- Gates 1–3 not confirmed by the client; all `[inferred]` and `[agent]` lines stand unconfirmed — decide at: client review
- Font files: Synonym and Sentient are declared but not embedded (the download needed approval in a non-interactive run). The page falls back to system sans / Georgia until `fonts/Synonym-Variable.woff2` and `fonts/Sentient-Variable.woff2` are added — decide at: before launch
- Instagram handle not given; the footer and "Message us" links point to a placeholder `#instagram` — decide at: client supplies handle
- "Message us" channel (Instagram DM vs WhatsApp vs email) is inferred as Instagram — decide at: client review
- Bank-holiday and sell-out overrides: the live status only knows the weekly hours — decide at: client review
- tallyroll.md was referenced but not present — decide at: client review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Render r1 (1440 full, 390 first screen) | C1 | pass: status board and ruler end at ~535px on 390×844 | — | — |
| Render r1 | C2 | pass: all 9 prices match the brief; nothing added | — | — |
| Render r1 | C3 | fail: tel link in header and cake band, but not in Find us | bug | added tel link beside "Open in maps" |
| Render r1 | C4 | pass: check-layout found 0 of 9 patterns; cake band and footer are full-width burgundy | — | — |
| Render r1 | C5 | pass: "Closed" in words for Mon/Tue; today marked with "· today" text | — | — |
| Render r1 | copy | closed-state sub-line repeated the hours twice | bug | shortened to "Back <day> at 7:00…" |
| Render r1 | layout | desktop cake band: heading sank to the bottom left | bug | aligned to top |
| Render r2 (390 full) | C1–C5 | all pass; check-layout 0 patterns | — | stop (cap 2) |
| House style on render | H1 no (tart drawing, ruler, sign) · H2 no (burgundy bands) · H3 yes (dashed rules group the menu and hours) · H4 no (18px radii) · H5 yes, hesitant (left headline then lists) · H6 no (cake band and About change scale) → 2 | | | under 4; kept |
