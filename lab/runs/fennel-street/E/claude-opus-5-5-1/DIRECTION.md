# Creative direction: Fennel Street Bakery
Status: draft (not approved — non-interactive fast run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "a neighbourhood bakery… people who live within a few streets" — [client]
- V3 Handmade, small on purpose — "one oven and still only have one" — [client]
- V4 Honest about running out — "gone by two", "or until we sell out" — [inferred]

## 3. Positioning
- Category: "the local bakery" / "where to get pastéis de nata" — [inferred]
- Alternatives: a supermarket bakery aisle; a chain café's pastry counter; a bigger artisan bakery further away — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Hours and address hidden in the footer | Challenge | Audience checks "is it open" on phones; status goes in the first screen |
  | Cream/kraft/brown "rustic" palette | Challenge | Makes every bakery interchangeable; the Portuguese side is the difference |
  | Full-bleed hero photo of bread | Avoid | No photos available; never fake one (honesty rule) |
  | Menu with prices | Adopt | The facts visitors came to check |
  | Order form with many fields | Avoid | Brief says "message us or call"; a tap-to-call is easier |
- Intended perception — [inferred]
  - P1 "It's open / closed right now, and I know when" → check: status line with today's state visible above the fold on a 390px phone
  - P2 "Portuguese, handmade, by people" → check: tile pattern and the sisters' names visible without scrolling past the menu
  - P3 "Small, local, not a chain" → check: no stock-photo hero, no testimonials, single short page
- Sophistication: everyday — pastries £2.10–£5.60, walk-in neighbourhood trade — [inferred from client prices]
- Differentiate on: the day's rhythm (bread at seven, tarts by nine, gone by two) told with the shop's Portuguese roots — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — register words are explicit; tallyroll.md was not present in the project, so "the opposite" could not be read — [agent]

## 5. References
| Reference | Admire | Borrow | Avoid | Just interesting |
| tallyroll.md (missing) | — | — | its register (unknown) | — |

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A Azulejo morning | agent | Portuguese pastries → blue-and-white tile | P1 P2 V1 V2 | Selected | [agent] best ties look to the brief's own fact |
| B Custard ledger | agent | "Rita does everything with custard" | P2 V3 | Not chosen | warmer, but drifts to heritage pastiche (engine watchOut) |
| C Clay and linen | engine pick | food photography | V1 | Not chosen | chooseIf "photography leads" — we have no photos |

Engines: A = Synonym + Sentient, lib.porcelain-and-indigo; B = Alpino + Author, lib.club-cream; C = Red Hat + Plein, lib.clay-and-linen — [engine]

| Axis | A Azulejo morning | B Custard ledger | C Clay and linen |
| --- | --- | --- | --- |
| Composition | asymmetric stack, status first, menu as list — because P1 | one centred reading column like a shop card — because V3 | photo grid with captions — because V1 |
| Scale | one big line set on a 7→14 timeline — because Differentiate | huge price numerals — because Adopt menu | even, photos carry scale |
| Imagery | SVG tile pattern + 2 art-directed photo frames — because P2, honesty | type as image | photography (needs client shots) |
| Signature device | azulejo tile + the day timeline — because P2, Differentiate | dotted price leaders | rounded photo crops |
| Colour proportion | porcelain ground, indigo as full bands (cake orders, season) ~30% — because watchOut "needs real presence" | cream everywhere, burgundy type | linen everywhere, clay accents |
| Surface | square tiles, flat glaze, no shadows | flat paper | soft rounded |
| House-style markers | 2: H3 partial, H4 | 5: H1 H2 H3 H5 H6 | 2: H2, H6 |
| Distinct on | imagery, colour proportion, signature, scale | composition, scale, imagery | composition, imagery, surface |

Other-client test (A): the tile only belongs to a Portuguese-rooted shop; the timeline only to one with "bread at seven, tarts by nine, gone by two".

## 7. Selected direction
A Azulejo morning — origin: agent — [agent]
Porcelain ground with indigo tile bands; the shop's day drawn as a timeline from 7:00 to 14:00 with a live "open now" marker. Serves P1 (status), P2 (Portuguese, by two sisters), V1–V4.
The one memorable thing: the day's line set on its own clock, with a dot that tells you where in the day the shop is right now.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, 200–700, no italics. Fontshare: self-host only, keep files out of public repos.
- Body: Sentient (sentient), FFL, 200–700, italics. Fontshare: self-host only.
- Fallbacks: system-ui sans / Georgia serif (from engine CSS). Font files not yet downloaded (download not approved this run) — see Open decisions.
### Color — [engine]
- Direction: Porcelain and Indigo (lib.porcelain-and-indigo)
- Ground #F8F7F2 · figure #1E339B · text #403D37 · muted #706D66 · tints #405FCF #7893DE #B5C4EC · shades #16267A #0D1A5B #060F3E
- Contrast: text/ground 10.08, muted/ground 4.81, figure/ground 9.77, button label 9.77
### Layout plan — [agent]
- Default reached for: nav, centred hero + 2 buttons, 3 product cards, about, testimonials, CTA, footer.
- Visitor questions: open now? → where? → what's baked, how much? → can I order a cake? → who are they?
- Only this brief has: the day's rhythm + hours; the one oven; custard tarts six for £11.
- Cut: testimonials, stats, features cards, newsletter.
- Order: status strip (open/closed, address, call) → timeline hero → menu (daily list + seasonal indigo panel) → cake orders band → about + photo frames → find us (week hours, address) → footer.
### Imagery plan — [agent]
- Job: make "Portuguese, handmade" believable without photos — serves P2
- Kind: SVG azulejo tile pattern (agent-drawn, honest) + art-directed photo frames
- Shot list: (1) Rita's hands pressing pastry into tart tins, overhead, morning window light, 4:5, beside About; (2) the single oven door open with loaves, eye level, warm low light, 4:5, beside About
- Treatment: frames sit in a tile border; captions are the shot-list line; square edges
- Ships now: tile pattern bands, timeline, hours board; frames await (1) and (2)
### Judgment tokens — [agent]
- Radii 0 (tiles are square) except 2px on buttons; no shadows (glaze is flat)
- Spacing: tight inside lists (menu rows 0.6rem), generous between subjects (5–7rem), indigo bands break rhythm
- Motion: only the "now" dot pulses once; respects reduced motion

## 9. Constraints
- C1 On a 390×844 phone, the open/closed status and the address are visible in the first screen → check: phone screenshot — [agent]
- C2 Every price matches the brief exactly; no added claims, reviews or prices → check: text diff — [agent]
- C3 Cake ordering offers a tap-to-call link to 020 7946 0381 and states 48 hours' notice → check: band visible, tel: link — [agent]
- C4 (P2) The tile pattern appears above the menu and at least twice on the page, and indigo covers at least one full-width band → check: full screenshot — [agent]
- C5 No photo placeholder is the main visual of the first screen → check: desktop + phone first screen — [agent]

## 10. Avoid
- Centred hero with two buttons — [agent]
- Row of three product cards — [agent]
- Cream/kraft-brown rustic palette, wood textures — [agent]
- Stock-style bread photo or fake map screenshot — [agent]
- Testimonials or star ratings — [client: no reviews]
- Emoji as icons — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A Azulejo morning | (non-interactive) | best serves P1/P2; engine pick C needs photos we don't have | until review |
| Colour | Porcelain and Indigo over engine pick Clay and Linen | — | Clay's chooseIf is photo-led; Indigo's chooseIf "step away from warm category colours" matches Challenge | until review |
| Fonts | Synonym + Sentient (engine pair) | — | engine default for warm | until review |

## 12. Open decisions
- Spec, values and perception qualities unapproved — decide at: client review — [inferred]
- "Message us" channel (Instagram DM? SMS? email?) and the Instagram handle — decide at: client review; placeholder links to #instagram — [inferred]
- Font files: download Synonym and Sentient from fontshare.com into ./fonts/ — decide at: deploy
- Live open/closed status uses Europe/London time and the stated hours; "sold out early" can't be known — decide at: client review (manual "sold out" toggle?)
- tallyroll.md not found; "opposite of" reading unverified — decide at: client review
- Photos for frames (1) and (2) — decide at: photo shoot

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| R1 render | C1 status + address in phone first screen | pass | — | — |
| R1 render | C2 prices match brief | pass | — | — |
| R1 render | C3 tel: link + 48 hours | pass | — | — |
| R1 render | C4 tile ≥2×, indigo full band | pass | — | — |
| R1 render | C5 no placeholder in first screen | pass | — | — |
| R1 render | Photo frames' border-image rendered as broken fragments | fail | bug | rebuilt as a tile mat with an inset frame; passes R2 |
| R1 check-layout | Centred hero flagged (desktop) | kept | — | the lines are staggered onto the 7/9/14 ticks, not centred; the phone check is clean |
| R2 render | House-style markers on render | 2 (H3 partial, H4) | — | matches direction |
| Note | Fonts | — | — | font files not in ./fonts yet, so the renders used fallbacks; re-check once they're added |
