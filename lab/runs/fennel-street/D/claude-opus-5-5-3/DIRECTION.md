# Creative direction: Fennel Street Bakery
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people within a few streets, and people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked, when the shop is open and where it is, and make cake orders easy — [client]
- Most customers walk in; some order cakes ahead, so walk-in info outranks ordering on the page — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade" / "a neighbourhood bakery" — [client]
- V3 Handmade, small — "one oven and still only have one" — [client]
- V4 Honest about scarcity (things sell out) — "gone by two", "or until we sell out" — [inferred]

## 3. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md"
Reading: deliberate preference — the register is stated as three words plus a contrast reference — [agent]
tallyroll.md was not present in the project, so "the opposite" is read only as: not a product/SaaS page — [inferred]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
| tallyroll.md (not found in project) | — | — | Whatever it is; read as anti-reference only | — |

## 5. Directions explored (2–4)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| A "Shop window card": Synonym + Sentient, Club Cream (lib.club-cream), page reads like a hand-lettered window board: open/closed status first, then a price list with leaders | agent | the brief's hours line and price list; phone visitors checking if open | V1, V2, V4 | selected [agent] | non-interactive |
| B "Linen counter": Synonym + Sentient, Clay and Linen (lib.clay-and-linen), photo-led layout with large image placeholders | agent | engine pick for food & beverage | V1 | not selected | its chooseIf is "photography leads"; brief forbids external images |
| C "Paper bag": Alpino + Plein, Parchment and Ink (lib.parchment-and-ink), pure typographic menu | agent | paper-and-ink menus | V3 | not selected | quietest; risks reading cold against "warm" |
Other-client test (A): a live open/closed board plus a price list with "gone by two" only fits a sell-out bakery with fixed short hours; a café or restaurant would not lead with it.

## 6. Selected direction
Shop window card — origin: agent — [agent]
Cream ground with burgundy type, like a painted shopfront or a cake-box label. First screen answers "open now?" with a live status from the real hours, then the address; the day's bake is a priced list, not cards.
The one memorable thing: the hero line "Bread at seven, tarts by nine, gone by two." set large, directly above a live "Open now / Closed" status.

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), humanist sans with stroke contrast, weights 200–700, no italics, FFL — [engine]
- Body: Sentient (sentient), robust serif, weights 200–700 with italics, FFL — [engine]
- CSS stacks: "Synonym", system-ui, -apple-system, "Segoe UI", sans-serif · "Sentient", Georgia, "Times New Roman", serif — [engine]
- Fontshare FFL: self-host only, keep files out of public repos; files expected at ./fonts/Synonym.woff2 and ./fonts/Sentient.woff2 — [engine]
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Light / Two-Tone — [engine]
- Ground Club Cream #F5E7C3 oklch(0.93 0.05 90) · Figure Club Burgundy #5B1D26 oklch(0.33 0.09 15) · no accent — [engine]
- Text #37342E (10.1:1) · Muted #67645D (4.8:1) · Figure on ground 10.37:1 · Button label (ground on figure) 10.37:1 — [engine]
- Tints/shades: tint-1 #90474E, tint-3 #EDAEB1, shade-1 #48161D, shade-2 #360E14 — [engine]
- Engine's default pick was Clay and Linen; switched because its chooseIf (photography leads) does not hold — [agent]
### Layout plan — [agent]
- Default: nav, centered hero with two buttons, three product cards, about, testimonials, CTA band, footer.
- Visitor questions in order: is it open now? → where is it? → what's baked today / this season? → how do I order a cake? → who are they?
- Only this brief has: fixed short hours that sell out ("gone by two") and a short priced list; lead with a live hours status and the price list.
- Cut: testimonials (none given; no added claims), stats, feature cards, second hero button, newsletter.
### Judgment tokens — [agent]
- Spacing: tight inside the price list (rows ~0.6rem), generous between subjects; the page changes density at the menu — [agent]
- Radii: 0 on everything except the round "status dot"; shop-sign feel is square-edged — [agent]
- Rules: 1px burgundy rules and dotted price leaders group content instead of boxes — [agent]
- Imagery: one labelled photo placeholder (the counter / tarts) and a labelled map placeholder; no stock illustration — [agent]
- Motion: none beyond the status text updating each minute — [agent]

## 8. Constraints (4–8, each pass/fail on a screenshot)
- C1 On a 390px phone, the first screen shows the open/closed status and today's hours without scrolling → check: status line and hours visible above the fold — [agent]
- C2 Prices are in a list with name left, price right on one baseline; no cards → check: no repeated boxed items in the menu — [agent]
- C3 The phone number is a tappable tel: link and appears in the cake-order section and in the first screen or nav → check: number visible twice, styled as a link — [agent]
- C4 Only engine colors appear (cream, burgundy, its text/muted/tints/shades); no gradient → check: no other hues in the render — [agent]
- C5 Headline (the line) is at least 3× body size on desktop and set on a left edge, not centered → check: measure — [agent]
- C6 Every copy claim on the page is in the brief → check: no invented reviews, prices or dates — [client]

## 9. Avoid (≤6, each observable)
- Rounded cards or pill badges — [agent]
- Emoji or icon-font food icons — [agent]
- Gold, faux-aged paper textures (engine avoid) — [engine]
- Centered hero with two buttons — [agent]
- Testimonials or star ratings (none supplied) — [client]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction | A, Shop window card | — (non-interactive) | Serves "is it open / where / what's baked" first; no photography available | until user review |
| Color | Club Cream over engine pick Clay and Linen | — | Clay and Linen's chooseIf is photography-led | until user review |
| Fonts | engine top pair Synonym + Sentient | — | top picks, no caveat bites (headlines short; body has italics) | until user review |

## 11. Open decisions
- Spec approval (Gate 1–3 skipped; non-interactive run) — decide at: first user review — [inferred]
- Font files: Synonym/Sentient .woff2 must be downloaded from Fontshare into ./fonts/; until then the page falls back to system sans/Georgia — decide at: deploy — [engine]
- Instagram handle and "message us" channel not given; links are placeholders (#) — decide at: content review — [inferred]
- Real photo of counter/tarts and a map embed — placeholders labelled — decide at: content review — [inferred]
- Public holiday hours and sell-out notifications — not in brief — decide at: content review — [inferred]
- Dark mode — not requested; not built — [agent]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| Round 1 (1440 + 390 renders; checker: none of 9 patterns) | C1 status + hours on first phone screen | pass | — | — |
| Round 1 | C2 price list, no cards | pass | — | — |
| Round 1 | C3 tel: link twice (hero, cake orders) | pass | — | — |
| Round 1 | C4 engine colors only, no gradient | pass (placeholder hatch uses figure at 5% to mark placeholders only) | — | kept |
| Round 1 | C5 headline ≥3× body, left edge | pass | — | — |
| Round 1 | C6 no invented claims | pass | — | — |
| Round 1 | polish | — | bug: about ::first-line bolded mid-sentence; order lead floated to bottom; hours rules broke at cell gap | fixed in code |
| Round 1 | fonts | — | render used fallback stack (no font files in project) | Open decision: add ./fonts/ |
