# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte: sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade"; "people who live within a few streets" — [client]
- V3 Handmade, small on purpose — "one oven and still only have one" — [inferred]
- V4 Honest about running out — "gone by two", "or until we sell out" — [inferred]

## 3. Positioning
- Category: "the local bakery" / "the place with the custard tarts" — [inferred]
- Alternatives: a supermarket in-store bakery; a chain café-bakery; a Portuguese café elsewhere in London — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Full-screen food photo hero with the name over it, hours buried in the footer | Challenge | Audience comes to check "open?" — status and hours lead instead (P1) |
  | Opening hours as a small table near the bottom | Avoid | The phone visitor's first question; it gets the biggest field on screen |
  | Menu as a priced list | Adopt | The facts people act on; prices from the brief only |
  | "Order online" checkout flow | Avoid | Brief says message or call; a tap-to-call number is the whole flow |
  | Story/about section with founder portraits first | Challenge | Two sentences about one oven carry it; it comes after the facts |
- Intended perception — [inferred]
  - P1 "I can tell if it's open right now" → check: phone first screen shows today's open/closed state and today's hours without scrolling
  - P2 "Made by hand, by two people, in one oven" → check: drawn (not photo-stock) illustrations and the about line are visible; nothing reads corporate
  - P3 "Warm and a bit Portuguese, not themed" → check: custard-cream ground with burgundy fields; no tile pastiche, no flags
- Sophistication: everyday — tarts at £2.10, loaves at £5.20, walk-in neighbourhood trade — [inferred]
- Differentiate on: the baking day itself — bread at seven, tarts by nine, gone by two — shown as a live clock of the day — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md" (tallyroll.md not present in the project) — [client]
Reading: deliberate preference — the brief pairs it with a cheap, walk-in, sell-out business — [agent]

## 5. References
None supplied. tallyroll.md referenced as the opposite but not found — see Open decisions.

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A. The baking day | agent | "Bread at seven, tarts by nine, gone by two" + hours | P1, V4 | Selected | Leads with the visitor's first question |
| B. Shop-window card | agent | walk-in trade, one oven | P2 | Not selected | Prettier, but hours sit lower |
| C. Paper bag stamp | agent | handmade, local | P2, P3 | Not selected | Leans to house style (pale ground, type only) |

Font pair for all: Synonym (synonym) + Sentient (sentient) — [engine]. Colour: A Club Cream (lib.club-cream), B Clay and Linen (lib.clay-and-linen), C Parchment and Ink (lib.parchment-and-ink) — [engine]

| Axis | A. The baking day | B. Shop-window card | C. Paper bag stamp |
| --- | --- | --- | --- |
| Composition | status board beside the name on first screen, then an asymmetric menu with drawings — because P1 | centred window "card" stack — because walk-in | one reading column — because handmade note |
| Scale | several big moments: status, prices, phone number — because each answers a question | one big name | one big headline, rest small |
| Imagery | drawn SVG tart, loaf, single oven — because P2 | photo placeholders for client shots | type only |
| Signature device | the day-bar 7 · 9 · 14 with a live "now" mark; fluted (tart-tin) edge on fields — because Differentiate | window lettering | rubber stamp |
| Colour proportion | burgundy as large solid fields alternating with cream bands — because P3 | linen almost everywhere, clay accents | paper everywhere, ink figure |
| Surface | soft, fluted edges and rounded panels, flat colour, no hairlines — because V1 | soft shadows | flat, square, ruled |
| House-style markers | 0 | 2: H2, H6 | 5: H1 H2 H3 H4 H5 |
| Distinct on | composition, imagery, device, colour, surface | composition, colour, imagery | all six |

Other-client test (A): the day-bar is built from this bakery's own line and hours; it wouldn't fit a bakery that bakes all day.

## 7. Selected direction
A. The baking day — origin: agent — [agent]
The first screen answers "open?" with a burgundy status field driven by the real hours, beside the name and the line. Below, the day-bar shows when things come out; the menu and cake orders follow at large, tappable sizes. Cream and burgundy alternate as full bands with fluted edges like a nata tin.
The one memorable thing: a live bar of the baking day — seven, nine, two — with where "now" sits on it.
House style: 0 markers planned — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200–700, no italics
- Body: Sentient (sentient), FFL, 200–700 with italics
- Fallbacks from engine: Synonym → system-ui, -apple-system, "Segoe UI", sans-serif; Sentient → Georgia, "Times New Roman", serif
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, light foundation
- Ground #F5E7C3 / oklch(0.93 0.05 90) · Figure #5B1D26 / oklch(0.33 0.09 15) · Text #37342E · Muted #67645D
- Tints #90474E, #C4757C, #EDAEB1 · Shades #48161D, #360E14, #26080C
- Contrast: text on ground 10.1:1, muted 4.8:1, figure on ground 10.37:1; ground label on figure button (inverse) 10.37:1
- Engine avoid: no gold, no faux-aged textures
### Layout plan — [agent]
- Default: nav, centred photo hero + two buttons, three product cards, story, testimonials, CTA band, footer
- Visitor questions: 1 open now? 2 where? 3 what's baked and when? 4 how to order a cake?
- Only this brief: the day line + hours → live status and day-bar
- Cut: testimonials, stats, feature cards, separate CTA band, newsletter
- Order: name + line + status field (hours, address) → day-bar → daily & seasonal menu → cake orders (tap to call) → about (one oven) → find us → footer
### Imagery plan — [agent]
- Job: make "handmade by two people, one oven" believable — P2
- Kind: SVG illustration in the two engine colours now; photography later
- Shot list (to commission): a tray of pastéis de nata from above, tight crop, morning window light, beside the menu; Ana scoring a loaf, hands only, side light, beside the about line; the single oven door open, full-bleed band above Find us
- Treatment: two-tone (ground + figure tints/shades), cut-out, no frames
- Ships now: SVG nata (top view, fluted case, caramel spots), SVG scored loaf, SVG oven; no empty photo frames
### Judgment tokens — [agent]
- Fluted edge (scallop) between colour bands, from the nata tin — V1
- Radius 18px on panels, 999px only on the status dot — soft object, not app UI
- Spacing changes with content: tight within menu rows, wide between questions
- Motion: none beyond the live status text — the page is checked, not browsed

## 9. Constraints
- C1 Phone first screen (390×844) shows open/closed state, today's hours and the address without scrolling → check phone screenshot — [agent]
- C2 Phone number is a tel: link at least 28px tall in the cake section → check render — [agent]
- C3 Every price on the page matches the brief exactly; no extra claims/reviews → check text — [agent]
- C4 At least two burgundy full-width bands alternate with cream; no third colour hue → check full screenshot (P3) — [agent]
- C5 Drawn illustrations visible in the menu and about; no grey placeholder boxes → check (P2) — [agent]

## 10. Avoid
- Full-bleed stock photo hero — [agent]
- Azulejo tile patterns or Portuguese flag colours — [agent]
- Row of three equal product cards — [agent]
- Hairline rules + letter-spaced small caps as the structure — [agent]
- Gold, faux-aged paper texture — [engine]
- "Order now" pill buttons or checkout flow — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. The baking day | — (non-interactive) | Best serves the page job (open? where?) and departs most from the photo-hero category layout | until review |
| Colour | Club Cream over engine pick Clay and Linen | — | Clay and Linen's chooseIf needs photography to lead; we have none yet. Club Cream supports solid fields; watchOut (pastiche) handled by contemporary type | until review |
| Fonts | engine top pair Synonym + Sentient | — | warm/retro feel, no caveat bites (headlines don't need italics) | until review |
| Font delivery | self-host (find-font rule) | — | Font files couldn't be downloaded in this run (network needs approval); page links Fontshare CSS as a stopgap, which find-font forbids for production | no — Open |

## 12. Open decisions
- Self-host Synonym + Sentient (download from fontshare.com, `Fonts/WEB/fonts/*.woff2`) and remove the api.fontshare.com link — decide at: before launch — [agent]
- "Message us" channel (Instagram DM? WhatsApp? email?) — brief gives none; page points to Instagram — decide at: client review — [inferred]
- Instagram URL/handle not given — link is a placeholder — decide at: client review — [inferred]
- Live status uses London time and the stated hours; can't know a sell-out — page says "or until we sell out" — decide at: client review — [agent]
- tallyroll.md not found; reading of "the opposite" unverified — decide at: client review — [inferred]
- Values V3, V4, Positioning and Sophistication unconfirmed — decide at: client review — [inferred]
- Spec approval (Gate 3) missing — decide at: client review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1 (1440 full, 390×844) | C1 status, hours, address on phone first screen | pass | — | — |
| Round 1 | C2 tel link ≥28px | pass (≈60px button) | — | — |
| Round 1 | C3 no added claims | fail: "one batch" heading, "collect it" instruction were agent copy | bug | cut both |
| Round 1 | C4 burgundy bands alternate | pass (menu, about, footer) | — | — |
| Round 1 | C5 drawn imagery, no grey boxes | pass; nata drawing left a hole under the list | bug | moved nata to the side column |
| Round 1 | check-layout nine patterns | none found, desktop and phone | — | — |
| Round 1 | House style H1–H6 on render | H1 no (drawings) · H2 no (burgundy ≈40%) · H3 no (dotted price leaders only; no small caps) · H4 no (rounded panels, fluted edges) · H5 no (two-column status hero) · H6 no (sizes change per section) = 0 | — | — |
| Round 2 | re-render after fixes | pass, no new findings | — | stopped |
