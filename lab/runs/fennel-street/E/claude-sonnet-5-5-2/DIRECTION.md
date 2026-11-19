# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run, not approved) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people living within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 The opposite of tallyroll.md — "The opposite of tallyroll.md" — [client] (file not available to this run; read as "not a cold product-SaaS look" — [inferred])
- V3 Facts first for a phone in the street — "often checking whether the shop is open" — [inferred]

## 3. Positioning
- Category: local bakery / "bakery near me" — [inferred]
- Alternatives: a supermarket in-store bakery; a trendy café-bakery with a polished brand site; an Instagram page with no hours — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | Hours, address, menu with prices near the top | Adopt | the audience's job is checking these (V3) — [agent] |
  | Photo-grid hero of bread | Challenge | no photos available; and a drawn, clock-based hero is more handmade (V1) — [agent] |
  | Pale minimal "artisan" look, thin serif | Challenge | reads as polished brand, not neighbours (V1) — [agent] |
  | Cart / online shop | Avoid | brief: walk-ins, cake orders by message or phone — [agent] |
- Intended perception:
  - P1 "I can see if it's open right now" → check: open/closed status line visible on a 390px first screen
  - P2 "Two people make this by hand" → check: sisters named in About; hand-drawn SVG marks, not stock icons
  - P3 "It sells out, go early" → check: the 7 / 9 / 14 day-strip is the hero's artifact — [inferred]
- Sophistication: everyday — prices £2–£6 for loaves/pastries, a £28 cake — [inferred]
- Differentiate on: the line "Bread at seven, tarts by nine, gone by two" drawn as a working day-clock — [agent]

## 4. Opening vocabulary
"warm, local, handmade"
Reading: deliberate preference — stated as register — [agent]

## 5. References
None supplied except tallyroll.md (unreadable; treated as avoid) — [inferred]

## 6. Directions explored
| Axis | A Day-clock (chosen) | B Chalkboard menu | C Quiet paper |
| --- | --- | --- | --- |
| Composition | left-aligned, hero strip then hours/address slab then ledger menu — because V3 | single dark board column — because handmade | one reading column — because calm |
| Scale | one huge line, rest small — because P3 | several mid-size — | flat — |
| Imagery | SVG drawn pastry/loaf marks — because P2 | none, chalk type | none |
| Signature device | 7/9/14 time strip + street-sign address | chalk underline | rule |
| Colour proportion | cream ground ~70%, burgundy fields ~30% | dark ground | cream ground ~95% |
| Surface | flat, slightly rounded sign, dashed leaders | grain | flat square |
| House-style markers | 1 (H5) | 3 | 5 |
| Distinct on | imagery, device, colour, composition | | |
Other-client test: A rests on this bakery's own tagline and hours; no other client has it — [agent]
Fonts and colours per direction are the same engine picks (below) — the directions differ in layout. [agent]

## 7. Selected direction
A Day-clock — origin: agent — [agent]
The page opens on the tagline as three clock times, then the status and hours, then a priced ledger. Serves P1, P3 and V3.
The one memorable thing: the tagline as a time strip, with a live open/closed line above it.
House style: 1 marker — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200–700, no italics. Self-host only.
- Body: Sentient (sentient), FFL, weights 200–700, italics. Self-host only.
- Pair from find-font `pair`: synonym + sentient. Files expected at ./fonts/Synonym.woff2 and ./fonts/Sentient.woff2, not embedded; Georgia / system-ui fallbacks.
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, 78/22
- Ground #F5E7C3 · Figure #5B1D26 · text #37342E (10.1:1) · muted #67645D (4.8:1) · figure on ground 10.37:1
- Tints #90474E #C4757C #EDAEB1; shades #48161D #360E14 #26080C
- Watch out (engine): don't add gold or faux-aged texture; keep layout contemporary.
### Layout plan — [agent]
- Default avoided: centred hero + three cards + stats + testimonials.
- Visitor questions in order: open? where? what's baked and how much? how do I order a cake? who are you?
- Only-this-brief artifact: tagline as day-clock; hours board; street-sign address.
- Cut: testimonials, stats, newsletter, blog (no copy for them).
### Imagery plan — [agent]
- Job: make a visitor believe it's made by hand by two people — serves P2
- Kind: SVG illustration (pastel de nata top view, loaf with score marks) + type as image
- Shot list (client photography, not shipped): Ana scoring loaves at the oven; a tray of tarts with burnt tops, side light; the shop front on Fennel Street
- Treatment: single-colour burgundy line on cream; no photos faked
- Ships now: two inline SVG marks; time strip; street sign
### Judgment tokens — [agent]
- Radii 4px on sign and buttons only (object-like); big vertical gaps between subjects, tight inside lists; no motion except none (phone, glanceable).

## 9. Constraints
- C1 Status line (open/closed) visible without scrolling at 390×844 → check: screenshot — [agent]
- C2 Hours, address and phone appear above the cake section → check: order in render — [agent]
- C3 Every price from the brief and none invented; no reviews or stats → check: text diff vs brief — [agent]
- C4 Tagline is the largest text, ≥3× body size → check: computed sizes — [agent]
- C5 No horizontal scroll at 390px; tap targets ≥44px → check: phone render — [agent]
- C6 P2: no emoji, no stock-style icons, no empty image frames → check: screenshot — [agent]

## 10. Avoid
- Row of three equal cards — [agent]
- Pill badges, emoji, gradients — [agent]
- Centred hero headline — [agent]
- Empty photo placeholder boxes — [agent]
- Invented prices, reviews, or claims — [client]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | n/a (non-interactive) | best serves page job | until review |
| Club Cream over engine pick Clay and Linen | Club Cream | n/a | Clay and Linen is the pale muted pair (H2); Club Cream has strong contrast on phones in daylight | until review |
Rejected (final): none

## 12. Open decisions
- Instagram handle and message channel for cake orders (footer links are placeholders) — decide with client — [inferred]
- Font files: Fontshare files must be downloaded and placed in ./fonts/ — decide at deploy
- tallyroll.md was not readable; read of "opposite" is inferred — [inferred]
- Direction approval — decide at review

## 13. Checkpoints
See critique notes in the final reply.
