# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; Gate 3 approval not obtained) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: Local walk-in customers within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: tell a visitor whether the shop is open now, where it is, what's baked today, and how to order a cake — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "a neighbourhood bakery… people who live within a few streets" — [client]
- V3 Handmade, one oven — "still only have one" — [client]
- V4 Practical on a phone — "often checking whether the shop is open" — [client]

## 3. Opening vocabulary
"Warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — tallyroll.md is not in this project, so the contrast is read from the brief's words alone — [agent]

## 4. References (0–5)
None supplied. — [inferred]

## 5. Directions explored (2–4)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Linen and rose clay, serif body, sans headline (selected) | agent | find-font pair + find-color pick | V1, V3, V4 | Selected in non-interactive run | — |
| B. Paper and bitter-brown ink, typographic menu | agent | find-color "Parchment and Ink" | V1, V4 | Not built; alternative | — |
| C. Matcha green single-hue system | agent | find-color "Matcha Field" | V1 | Not built; reads as tea brand | — |

Other-client test for A: could this belong to another client? Yes, any warm café with a clay palette. It is grounded in the brief's own words (handmade, one oven, custard), not in the palette alone, so it is kept.

## 6. Selected direction
Clay and Linen with a humanist headline face and a readable serif body — origin: agent — [agent]
A printed-bakery-list page: the day's bake reads as a list with prices, not a set of cards. It serves V1 (warmth from paper-like ground), V3 (the one oven, a plain list of what's made) and V4 (the status line is the first thing seen).
The one memorable thing: the day's bake written out like a chalk-and-paper board, with prices aligned to the right. — [agent]

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), Fontshare FFL, self-host only — [engine]
- Body: Sentient (sentient), Fontshare FFL, self-host only — [engine]
- Fallback stacks: system-ui sans for headlines; Georgia serif for body — [engine]
- Font files are not downloaded in this run; @font-face points at ./fonts/*.woff2 and falls back until they are added — [agent]

### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen), Light + Muted, Chromatic — [engine]
- Ground: Linen #F5EDE4 — [engine]
- Figure: Rose Clay #8D5951 (4.92:1 on Linen; headings and links only) — [engine]
- Text: #3D3832 (10.00:1 on Linen) — [engine]
- Text muted: #6C6761 (4.83:1 on Linen) — [engine]
- Accent: none supplied by the engine for this pair — [engine]

### Layout plan — [agent]
- Default: nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer. Rejected.
- Visitor's questions, in order: is it open? where is it? what's baked today and at what price? can I order a cake?
- The one thing only this brief has: the day's bake list with prices, under a live open/closed line. Leads the page.
- Cut: testimonials, stats row, map embed (external), newsletter, feature cards.

### Judgment tokens — [agent]
- Spacing: generous between the bake list and the about text, tight inside a list group — tied to V4 (scan fast on a phone).
- Radii: none on the bake list; a single small radius on the cake-order button only, because it is the one action.
- Imagery: one labelled photo placeholder for the custard tart; no external images.
- Motion: none.

## 8. Constraints (pass/fail on a screenshot)
- C1 First phone screen (390×844) shows the name, the open/closed line and the address without scrolling → check: the three are visible in the 390px screenshot — [agent]
- C2 Headline is the largest type on the page and nothing else competes in size → check: headline at least 4× body size — [agent]
- C3 Every price in the brief appears in the bake list, exactly as given; no other prices appear → check: text search for £ values — [client]
- C4 Cake ordering shows the phone number as a tap-to-call link and the 48-hour notice, reachable from the first screen or the footer → check: tel: link present and notice visible — [client]
- C5 Body and muted text meet 4.5:1 and 4.5:1 respectively against the ground → check: computed colours on the render — [engine]
- C6 No external requests: no remote images, scripts, fonts or map embeds → check: source has no http(s) URLs other than links — [client]

## 9. Avoid (≤6, each observable)
- Pill badge above the headline — [agent]
- Row of three feature cards — [agent]
- Centered hero headline with two buttons — [agent]
- Emoji used as icons or bullets — [agent]
- Decorative gradient backgrounds — [agent]
- Row of big numbers (for example "2019" as a stat) — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A (Clay and Linen) | A | not asked (non-interactive) | Engine pick fits warm/handmade and a photo-light page | until Gate 3 approval |
| Font pair Synonym + Sentient | engine top pair | not asked | Warm humanist sans with a readable serif for body | until Gate 3 approval |

Rejected (final): none in this run.

## 11. Open decisions
- Font files: download Synonym and Sentient woff2 from fontshare.com and place in ./fonts/ — decide at: deployment — [agent]
- Instagram URL: not supplied; footer shows the label without a link — decide at: content review — [inferred]
- Cake order email: not supplied; phone only — decide at: content review — [inferred]
- Live open/closed line uses the visitor's clock in Europe/London; confirm this is wanted — decide at: Gate 3 — [inferred]
- Photo: placeholder for a custard tart photo — decide at: Gate 3 — [inferred]
- Direction approval (Gate 3) not obtained in this non-interactive run — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 0 render (390 and 1440) | C1 | Pass: name, open/closed line and address visible in the 390×844 first screen | none | none |
| Round 0 render | C2 | Pass: headline 72px+ (4.5rem min) vs body 18px | none | none |
| Round 0 render | (pattern) uniform spacing | Fail: 5 of 6 sections shared padding | bug (code) | Fix round 1: spacing set per section by content (today tight, about short, cakes roomier) |
| Round 1 render (1440) | (pattern) centered hero | Fail: name centred in a centred column | bug (code) | Fix round 2: column on a fixed 8vw left edge at ≥900px; phone gutter kept at 16px |
| Round 2 render (390 and 1440) | all patterns | Pass: no overused patterns on phone; desktop clean | none | Stop; two fix rounds used |
| Not run | C3, C4, C6 | Text and source checked by reading, not by render | none | Prices, phone link and no external URLs confirmed in source |
| Not run | C5 | Computed contrast from find-color values (10.00:1, 4.83:1) | none | Pass on engine values; not re-measured on render |
