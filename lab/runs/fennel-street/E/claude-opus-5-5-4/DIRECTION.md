# Creative direction: Fennel Street Bakery
Status: draft (not approved — non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking if it's open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade" / "a few streets" — [client]
- V3 Handmade, small on purpose — "one oven and still only have one" — [inferred]
- V4 Honest about selling out — "gone by two", "or until we sell out" — [inferred]

## 3. Positioning
- Category: "the bakery round the corner" / "where to get pastéis de nata in E8" — [inferred]
- Alternatives: a supermarket in-store bakery; a chain café-bakery; another independent bakery a bus ride away — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Full-bleed hero photo of bread, hours and address buried in the footer | Challenge | Audience is checking whether it's open; status and address go first |
  | Menu as a PDF or image, or no prices | Avoid | Brief gives prices; phone users need text |
  | Hours as a 7-row weekday table | Challenge | The day's rhythm (7 / 9 / 2) is the brand line; show it as a day line |
  | Cake orders via a long web form | Avoid | Brief says message or call; one tap to call |
  | Founder story with portrait | Adopt (short) | Two sisters, one oven is the differentiator; keep it to the brief's three sentences |
  — [agent]
- Intended perception — [inferred]
  - P1 It's open right now (or exactly when it opens) → check: open/closed status readable in the first phone screen without scrolling
  - P2 Made by hand by two people → check: hand-drawn illustrations of the actual bakes; no stock-photo look; sisters named
  - P3 Go early → check: the 7 / 9 / 14 day line is visible as a graphic, not only text
- Sophistication: everyday — £2.10 tarts, £5.20 loaves, walk-in neighbourhood shop — [inferred]
- Differentiate on: the shape of the day — bread at seven, tarts by nine, gone by two — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — the brief states register plainly. tallyroll.md was not in the project, so "opposite" is read only as "not a cool, corporate product page" — [agent]

## 5. References (0–5)
None supplied (tallyroll.md referenced but absent). — [client]

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A. The day line — Synonym + Sentient; Club Cream (lib.club-cream) | agent | the line "Bread at seven, tarts by nine, gone by two" | P1, P3, V4 | Selected | best serves the open-check job; departs from photo-hero layout |
| B. Shop window — Alpino + Plein; Clay and Linen (lib.clay-and-linen) | agent | warm food photography | P2 | Not selected | needs photography the client hasn't supplied |
| C. Chalkboard list — Author + Author; Parchment and Ink (lib.parchment-and-ink) | agent | the price list | P2 | Not selected | reads as house style (4 markers) |

| Axis | A. The day line | B. Shop window | C. Chalkboard list |
| --- | --- | --- | --- |
| Composition | status band first, then day-line graphic, then menu as large-name list — because P1 | full-bleed photo modules, hours overlaid — because P2 | one column, price list — because convention "menu with prices" |
| Scale | several big moments: status, bake names, phone number — because the page has three jobs | one huge photo per section | flat, even |
| Imagery | hand-drawn SVG line drawings of each bake — because P2 | photography of bakes in morning light | type only |
| Signature device | the 7→14 day line with a live "now" marker — because P3 / V4 | the shop-window frame crop | dotted price leaders |
| Colour proportion | burgundy as large solid bands (status, cakes, footer) alternating with cream — because Club Cream is two-tone | ground almost everywhere, clay accents | paper almost everywhere, ink type |
| Surface | crimped (tart-tin scallop) band edges, rounded drawings, no shadows — because V3 | soft, photographic | flat, square, ruled |
| House-style markers | 1: H3 (dotted price leaders) | 1: H3 | 5: H1, H2, H3, H4, H5/H6 |
| Distinct on | imagery, signature, colour proportion, surface, composition | imagery, composition, surface | all |

Other-client test (A): the day line is built from this bakery's own line and hours; another shop's day has a different shape.

## 7. Selected direction
A. The day line — origin: agent — [agent]
Cream and deep burgundy in big alternating bands; the opening status and today's day line lead, then the bakes drawn by hand with prices, then cake orders with a one-tap phone number. Serves V1, V4, P1, P3.
The one memorable thing: a line across the morning — bread at 7, tarts at 9, gone at 14 — with a dot showing where today is.
House style: 1 marker — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200–700, no italics — https://www.fontshare.com/fonts/synonym
- Body: Sentient (sentient), FFL, weights 200–700, italics — https://www.fontshare.com/fonts/sentient
- Fallbacks: `system-ui, -apple-system, "Segoe UI", sans-serif` / `Georgia, "Times New Roman", serif` — [engine]
- Self-hosted from `./fonts/Synonym.woff2`, `./fonts/Sentient.woff2`, `./fonts/Sentient-Italic.woff2`; files not yet in the project — [agent]
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, light foundation, area 78/22
- Ground Club Cream #F5E7C3 / oklch(0.93 0.05 90); Figure Club Burgundy #5B1D26 / oklch(0.33 0.09 15)
- Text #37342E (10.1:1), muted #67645D (4.8:1), figure on ground 10.37:1, button label ground on figure 10.37:1
- Tints/shades: tint-1 #90474E, tint-2 #C4757C, tint-3 #EDAEB1, shade-1 #48161D — decorative strokes only, never text
### Layout plan — [agent]
- Default: nav, photo hero with two buttons, three product cards, testimonials, contact form, footer.
- Visitor questions: Is it open now? → Where is it? → What's baked and how much? → How do I order a cake?
- Only this brief has: the day line (7 / 9 / 14) and a priced daily list.
- Cut: testimonials, stats, form, gallery, newsletter.
- Axes as in §6 column A.
### Imagery plan — [agent]
- Job: make a visitor believe these are made by hand by two people — serves P2
- Kind: SVG line illustration now; photography later
- Shot list (to commission): Ana scoring loaves at the single oven, tight on hands, early blue light; a tray of natas just out, top-down, scorched tops; the shop window at 13:50 with an empty shelf, street level
- Treatment: drawings in burgundy stroke on cream, cream stroke on burgundy bands; inline with each bake name
- Ships now: SVG drawings (loaf, rye, nata, bun, focaccia, cake, fig loaf), the day-line graphic. No empty photo frames.
### Judgment tokens — [agent]
- Crimp edge: scalloped 14px band edges (tart tin) — V3
- Radii: none on boxes; roundness lives in the drawings and the crimp — avoids rounded-boxes default
- Motion: none except the "now" dot; nothing that delays the status — P1

## 9. Constraints
- C1 On a 390×844 screen, the open/closed status and address are visible without scrolling → check phone screenshot — [agent]
- C2 The day line shows 7:00, 9:00 and 14:00 as a graphic with labels → check render — [agent]
- C3 Every price on the page matches the brief; no added claims, reviews or prices → check copy — [agent]
- C4 The cake phone number is a tap-to-call link at ≥ 28px on phone → check render — [agent]
- C5 No photo placeholders or empty frames; each bake has a drawing → check render (P2) — [agent]
- C6 Burgundy covers at least two full-width bands → check full-page screenshot — [agent]

## 10. Avoid
- Stock-style hero photograph or empty image box — [agent]
- Rows of three rounded product cards — [agent]
- Testimonial quotes or star ratings — [client]
- Gold, faux-aged paper textures — [engine]
- Emoji as icons — [agent]
- A web form for cake orders — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. The day line | — (non-interactive) | best serves the open-check job; departs most from photo-hero layout | until client review |
| Colour | Club Cream over engine pick Clay and Linen | — | Clay and Linen's chooseIf is "photography leads"; there is no photography | until client review |
| Fonts | engine top pair Synonym + Sentient | — | top pick, caveat (no italics) doesn't bite headlines | until client review |
Rejected (final): none.

## 12. Open decisions
- Spec approval — decide at: client review — [agent]
- Font files: download Synonym and Sentient from Fontshare into `./fonts/`; until then the page renders in fallbacks. Fontshare FFL: keep files out of public repos. If the site must be one file with no font folder, re-run find-font with `--public-repo` (OFL) and embed — decide at: deploy — [agent]
- Instagram handle / URL ("Message us" and footer link currently `#`) — decide at: client review — [inferred]
- Bank holidays and sell-out notices: status is computed from the regular hours only — decide at: client review — [inferred]
- Values V3, V4 and all Positioning are agent readings — decide at: client review — [inferred]
- tallyroll.md not found in the project — decide at: client review — [inferred]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| R1 render 1440 + 390 (closed state, Thu after 14:00) | C1 status + address in first phone screen | pass | — | — |
| R1 | C2 day line 7/9/14 graphic | pass | — | — |
| R1 | C3 copy and prices match brief | pass | — | — |
| R1 | C4 tap-to-call ≥ 28px on phone (~32px) | pass | — | — |
| R1 | C5 drawings, no empty frames | pass | — | — |
| R1 | C6 ≥ 2 burgundy bands (header, season, footer) | pass | — | — |
| R1 | check-layout: none of nine patterns found | pass | — | — |
| R1 | House style on screenshot: H1 no (drawings), H2 no (burgundy bands), H3 yes (hairlines between bakes), H4 no (crimp edges), H5 no, H6 no → 1 | pass | — | — |
| R1 | Phone: nav hidden, so no route to cake orders in first screen | — | bug | added "Order a cake" link to status band |
| R1 | Renders in fallback fonts (Synonym/Sentient files absent) | — | open | see Open decisions |
