# Creative direction: Fennel Street Bakery
Status: draft (not approved — non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking if it's open — [client]
- The page must: show what's baked, when it's open and where it is, and make cake orders easy — [client]
- Most visits are walk-in; cake orders are the only "conversion" — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm" — [client]
- V2 Local — "local", "neighbourhood", "within a few streets" — [client]
- V3 Handmade — "handmade", "one oven and still only have one" — [client]
- V4 Honest / small — the opposite of a polished product site; no invented claims — [inferred]

## 3. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference for the register; the tallyroll.md reference file was not present in the project, so "the opposite of" is read as: not a SaaS/fintech page (no cards, gradients, stats, product polish) — [inferred]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
|---|---|---|---|---|
| tallyroll.md (missing from project) | — | — | Its register, whatever it is; read as SaaS polish — [inferred] | — |

## 5. Directions explored (2–4)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
|---|---|---|---|---|---|
| A. Shop window: Synonym + Sentient, Clay and Linen, the day as a timeline (7 bread → 9 tarts → 14 gone) | agent | The brief's own line "Bread at seven, tarts by nine, gone by two" and the open-now question | V1, V2, V3 | Selected — [agent] | non-interactive |
| B. Chalkboard price list: Synonym + Sentient, Parchment and Ink, menu leads the page | agent | Daily price list | V3, V4 | Not selected; Parchment and Ink's chooseIf assumes photography carries colour — [agent] | — |
| C. Heritage cream: Alpino + Author, Club Cream | agent | Portuguese pastry tradition | V1 | Not selected; engine watch-out "easy to tip into pastiche"; shop opened 2019 — [agent] | — |
Other-client test (A): the timeline is built from this shop's own hours and bake times; no other bakery has this line — [agent]

## 6. Selected direction
A. Shop window — origin: agent — [agent]
A plain, warm, typographic page that answers "is it open?" in the first screen, then the price list, then cake orders. Rose clay on linen, a humanist sans for the shop's voice, a book serif for prices and prose.
The one memorable thing: a day bar from 7:00 to 14:00 marking bread, tarts and "gone", with a live "you are here" marker in London time.

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, weights 200–700, no italics — [engine]
- Body: Sentient (sentient), FFL, weights 200–700, italics — [engine]
- CSS stacks: "Synonym", system-ui, -apple-system, "Segoe UI", sans-serif / "Sentient", Georgia, "Times New Roman", serif — [engine]
- Self-hosted from ./fonts/*.woff2 (Fontshare: self-host only, keep files out of public repos); falls back to system stacks until files are added — [engine]
### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen) · Light + Muted — [engine]
- Ground Linen #F5EDE4 oklch(0.95 0.015 75) / figure Rose Clay #8D5951 oklch(0.52 0.07 30) / no accent — [engine]
- Text #3D3832 (10:1), muted #6C6761 (4.83:1), figure on ground 4.92:1, button label ground on figure 4.92:1 — [engine]
- Tints #B4786E #CBA199 #E1CAC6, shades #6A423C #4A2D28 #2B1815 — [engine]
- Chosen over engine alternatives although its chooseIf mentions photography: no option fit a no-photo page better; mitigated by keeping body copy in --color-text — [agent]
### Layout plan — [agent]
- Default: nav, centered hero + two buttons, three product cards, testimonials, CTA band, footer.
- Visitor's questions: Is it open now? → Where is it? → What's baked today (and price)? → How do I order a cake? → Who are they?
- Only this brief has: the day timeline and the price list. Lead with open status + timeline + address; menu as a dot-leader list.
- Cut: testimonials, stats, feature cards, nav menu beyond a single "Order a cake" link.
### Judgment tokens — [agent]
- Spacing: tight within the price list (it's one object), wide between subjects; hero denser than the rest — ties to phone-checking visitors.
- Radii: 0 everywhere except the round "you are here" dot — handmade print, not app UI.
- Imagery: one labelled photo placeholder (the counter/oven); no stock, no illustrations.
- Motion: none beyond focus/hover states.

## 8. Constraints (4–8, each pass/fail on a screenshot)
- C1 Open/closed status and today's hours visible in the first phone screen (390×844) → check: status text above the fold — [agent]
- C2 Address and a tap-to-call number reachable within the first two phone screens → check: tel: link and address visible — [agent]
- C3 Every daily and seasonal item shown with its exact brief price; no added claims/prices → check: diff against brief — [agent]
- C4 Headline left-aligned, not centered → check: hero text left edge — [agent]
- C5 No card grid: menu is a list with rules/dot leaders → check: no boxed items — [agent]
- C6 Only engine colors used; body copy in --color-text → check: CSS — [agent]
- C7 Photo placeholder clearly labelled as such → check: visible label — [agent]

## 9. Avoid (≤6, each observable)
- Rounded cards or pill badges — [agent]
- Gradients — [agent]
- Emoji or icon sets — [agent]
- Centered hero with two buttons — [agent]
- Stars, reviews or stats not in the brief — [client]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction | A. Shop window | — (non-interactive) | Best serves "is it open / where / what's baked" | until user review |
| Color | Clay and Linen (engine pick) | — | Warmest; others' chooseIf no better fit | until user review |
| Fonts | Synonym + Sentient (engine pair) | — | Top warm pair, no caveat bites (body has italics) | until user review |

| Critique round 1 | Restore section side gutter; show Bread/Tarts/Gone labels on phone | — | Bug: menu touched phone edge; timeline lost its meaning | yes |
| Critique round 2 | Two-line price rows on phone for nata and orange cake; drop duplicate "48 hours' notice" kicker | — | Bug: price wrapped word by word at 390px | yes |

Critique result (1440 and 390 renders): C1–C7 pass; check-layout found none of the nine patterns, on desktop or phone — [agent]

## 11. Open decisions
- Direction, fonts, colors and this spec are unapproved (non-interactive run) — decide at first user review.
- tallyroll.md was not in the project; "opposite of" reading is inferred — confirm at review.
- Instagram handle / "Message us" destination not given; links point to "#instagram" placeholder — client to supply.
- Font files (Synonym.woff2, Sentient.woff2) must be downloaded from Fontshare into ./fonts/; page falls back to system fonts until then — before launch.
- Real photo for the placeholder — client to supply.
