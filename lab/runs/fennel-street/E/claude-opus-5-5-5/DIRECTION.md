# Creative direction: Fennel Street Bakery
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade" / "neighbourhood bakery" — [client]
- V3 Handmade, small on purpose — "one oven and still only have one" — [inferred]
- V4 Honest about selling out — "or until we sell out", "gone by two" — [inferred]

## 3. Positioning
- Category: "the bakery round the corner" / local bakery — [inferred]
- Alternatives: the supermarket bakery aisle; a chain café with pastries; another independent bakery a bus ride away — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | --- | --- | --- |
  | Full-bleed hero photo of bread with the name over it | Challenge | No photos supplied; phone visitors want "open now?" before mood (audience) |
  | Hours and address buried in the footer | Avoid | The audience's first question is whether it's open (audience) |
  | Menu as a priced list | Adopt | Visitors act on what's baked and what it costs (page job) |
  | "Order online" checkout flow | Avoid | Orders are by message or phone with 48h notice (client fact, V3) |
  | Script/handwritten logotype on cream | Challenge | Reads as every artisan bakery; interchangeable (V2) |
- Intended perception — [inferred]
  - P1 It's open (or not) right now → check: open/closed status with today's hours is visible in the first phone screen
  - P2 Small and handmade → check: drawn bakes (SVG), the "one oven" line, no stock imagery or slick UI chrome
  - P3 Easy to order a cake → check: a tappable phone number appears within two scrolls on phone
- Sophistication: everyday — prices £2.10–£28, walk-in neighbourhood trade — [inferred]
- Differentiate on: the shape of the day — bread at seven, tarts by nine, gone by two — shown as a live timeline — [agent]

## 4. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md" (tallyroll.md not present in the project) — [client]
Reading: deliberate preference — the register line is explicit — [agent]

## 5. References
None supplied (tallyroll.md is a negative reference but the file is missing) — [client]

## 6. Directions explored
Fonts [engine]: find-font recommend --role headlines --role body --feel warm --script latin-ext → pair synonym + sentient; alternates alpino, author, plein.
Colors [engine]: find-color recommend --domains food-and-beverage,restaurants (+bakeries) --foundation light → clay-and-linen (pick), parchment-and-ink, porcelain-and-indigo, club-cream.

| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| --- | --- | --- | --- | --- | --- |
| A "The day's clock" — Synonym/Sentient, Club Cream | agent | "Bread at seven, tarts by nine, gone by two" | P1, P3, V4 | Selected | Leads with the live open/closed + timeline the audience checks |
| B "Shop window" — Synonym/Sentient, Clay and Linen | agent | engine pick; photo-led chooseIf | P2 | Not chosen | Its chooseIf needs food photography we don't have |
| C "Chalkboard menu" — Alpino/Plein, Parchment and Ink | agent | menu-first | page job | Not chosen | Typographic and quiet = house style (5 markers) |

| Axis | A Day's clock | B Shop window | C Chalkboard menu |
| --- | --- | --- | --- |
| Composition | Phone-first stack: status board, then bakes, then order, then find us — because P1 | Full-bleed photo slot + split text — because convention "hero photo" (Adopt) | One reading column, menu then hours — because page job |
| Scale | Big moments per section (status, season band, phone number) — because P1/P3 | One huge hero, rest small | Flat even scale |
| Imagery | Drawn SVG bakes in burgundy line, beside each item — because P2 | Commissioned photography | Type only |
| Signature device | 7:00→14:00 timeline with "now" marker — because Differentiate on | Recurring round crop | Dotted price leaders |
| Colour proportion | Cream ground with full burgundy bands for season + order — because V1, P3 | Linen almost everywhere, clay accents | Paper almost everywhere, brown ink |
| Surface | Soft: rounded seal/stamp, rounded buttons, no hairline grid — because V3 | Soft photo edges | Flat, square, ruled |
| House-style markers | 1: H3 (price leaders) | 2: H2, H6 | 5: H1–H5 |
| Distinct on | imagery, colour proportion, signature, scale | composition, imagery, scale | imagery, surface, colour, scale |

## 7. Selected direction
A "The day's clock" — origin: agent — [agent]
A phone-first page that answers "open?" first with a live status and a timeline of the bakery's day, then the bakes as a drawn, priced list, a burgundy season band and a burgundy cake-order band with a big phone number. Serves V1, V4, P1, P3.
The one memorable thing: the day drawn as a line from seven to two, with a dot for "now".
House style: 1 marker — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200–700, no italics. Self-host only; keep files out of public repos.
- Body: Sentient (sentient), FFL, weights 200–700, italics.
- Fallbacks: system-ui stack / Georgia. Files not in project yet → Open decision.
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, Light
- Ground #F5E7C3 oklch(0.93 0.05 90) · Figure #5B1D26 oklch(0.33 0.09 15) · Text #37342E · Muted #67645D
- Tints #90474E / #C4757C / #EDAEB1 · Shades #48161D / #360E14 / #26080C
- Contrast: text/ground 10.1, muted/ground 4.8, figure/ground 10.37
- Engine watch-out: easy to tip into pastiche; keep type and layout contemporary; no gold, no faux-aged texture.
- Chosen over engine pick Clay and Linen because its chooseIf requires photography — [agent]
### Layout plan — [agent]
- Default: nav, centered hero photo + two buttons, three feature cards, testimonials, CTA, footer with hours.
- Visitor questions: open now? → where? → what's baked / price → can I order a cake? → who are they.
- Only this brief has: the shape of the day (7 / 9 / 14) and "until we sell out".
- Cut: testimonials (none allowed), feature cards, stats, newsletter.
- Axis positions as in table column A.
### Imagery plan — [agent]
- Job: make the bakery feel small and handmade (P2).
- Kind: SVG line illustration (nata, loaf, bun, focaccia slice, cake), because no photos supplied.
- Shot list for later commission: Rita filling nata cases, overhead, window light, beside "Daily"; the one oven door open, tight crop, beside About; the shopfront on Fennel Street at 7am, beside Find us.
- Treatment: burgundy line drawings on cream; cream on burgundy in bands.
- Ships now: SVG drawings + timeline. No empty photo frames.
### Judgment tokens — [agent]
- Radii: 999px on buttons and the seal (soft, held objects, V3); 0 elsewhere.
- Spacing: tight inside lists, generous before bands; bands break the rhythm.
- Motion: none beyond the "now" dot; respect reduced motion.

## 9. Constraints
- C1 Phone 390×844: open/closed status and today's hours visible without scrolling → check screenshot — [agent]
- C2 Phone number is a tel: link and is the largest text in its section → check — [agent]
- C3 Every price on the page matches the brief exactly; no added claims/reviews → check copy — [agent]
- C4 (P2) At least four drawn bakes visible; no stock photo, no empty image box → check full screenshot — [agent]
- C5 No horizontal scroll at 390px — [agent]

## 10. Avoid
- Script/handwritten logotype — [agent]
- Gold or faux-aged paper textures — [engine]
- Row of three cards — [agent]
- Testimonials or star ratings — [client]
- Hours only in the footer — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A Day's clock | — (non-interactive) | Best serves "is it open" job | until review |
| Color | Club Cream over Clay and Linen | — | No photography | until review |

## 12. Open decisions
- Font files: Synonym.woff2 / Sentient.woff2 must be downloaded from Fontshare into ./fonts — decide at: deploy — [agent]
- "Message us" channel and Instagram handle not given; links point to #instagram placeholder — decide at: client review — [inferred]
- Open status uses Europe/London clock and cannot know when stock sells out — decide at: client review — [inferred]
- tallyroll.md reference missing — decide at: client review
- Whole spec unapproved (Gate 1–3 skipped, non-interactive) — decide at: client review

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Render 1 (1440 / 390) | — | — | Bug | Order + About lost side gutter (padding shorthand); timeline dots off track → fixed |
| Render 2 (390) | C2 | fail→pass | Bug | Order grid didn't stack on phone → added breakpoint |
| Final | C1 status + hours in first phone screen | pass | — | — |
| Final | C2 tel: link, largest text in section | pass | — | — |
| Final | C3 prices match brief, no added claims | pass | — | — |
| Final | C4 (P2) ≥4 drawn bakes, no empty frames | pass (7 drawings) | — | — |
| Final | C5 no horizontal scroll at 390 | pass | — | — |
| Final | check-layout nine patterns | 0 hits desktop + phone | — | — |
| Final | House style on render | H1 no (drawings) · H2 no (burgundy bands) · H3 no (no hairlines/small caps; one rule above Find us) · H4 no (rounded board, pill buttons) · H5 no (status board beside headline) · H6 no (season band, big phone number) = 0 | — | — |
