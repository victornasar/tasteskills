# Creative direction: Fennel Street Bakery
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery run by sisters Ana and Rita Duarte; sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people living within a few streets, and people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked, when the shop is open and where it is, and make cake orders easy — [client]
- Most customers walk in; cake orders are the only thing done ahead — [client]

## 2. Values (user-owned, 2–5)
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local — "warm, local, handmade" / "neighbourhood" — [client]
- V3 Handmade, small on purpose — "one oven and still only have one" — [inferred]
- V4 Plain-spoken, practical — copy reads like a shop sign ("gone by two") — [inferred]

## 3. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md."
Reading: deliberate preference — the brief gives a register and an anti-reference; tallyroll.md was not present in the project, so what "the opposite" excludes is unknown — [agent]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
|---|---|---|---|---|
| tallyroll.md (anti-reference) | — | — | whatever it is; file not found | — |

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
|---|---|---|---|---|---|
| A. Shop day — Synonym + Sentient (synonym, sentient), Clay and Linen (lib.clay-and-linen); page structured around the day "seven / nine / two" and a live open/closed line | agent | the client's own line and the "checking whether it's open" fact | V1, V2, V4 | selected | n/a (agent choice) |
| B. Menu card — Alpino + Author (alpino, author), Parchment and Ink (lib.parchment-and-ink); page as a printed price card, typographic, no colour | agent | the priced Daily list | V3, V4 | not selected: quietest option, less warm without photography | — |
| C. Old shopfront — Red Hat Display/Text (red-hat) + Sentient, Club Cream (lib.club-cream); burgundy sign-painted headings | agent | "specialty shops" use of the colour direction | V1 | not selected: engine warns of pastiche; shop opened 2019, not heritage | — |
Other-client test (A): a café could have hours, but "bread at seven, tarts by nine, gone by two" as the page's spine belongs only to this shop — [agent]

## 6. Selected direction
A. Shop day — origin: agent — [agent]
The page opens on whether the shop is open right now, then follows the day the client describes: bread at seven, tarts by nine, gone by two. Menu and prices read like the board on the counter; cake orders are one tap to call. Serves Warm, Local and Plain-spoken.
The one memorable thing: a live line at the top saying "Open now — until 14:00, or until we sell out" (or when it next opens), computed from the client's hours.

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (synonym) — FFL, Fontshare; weights 200–700; no italics; "humanist sans with visible stroke contrast" — [engine]
- Body: Sentient (sentient) — FFL, Fontshare; weights 200–700, italics; "robust serif… holds up at small sizes" — [engine]
- Stacks: "Synonym", system-ui, -apple-system, "Segoe UI", sans-serif / "Sentient", Georgia, "Times New Roman", serif — [engine]
- Fonts self-hosted only (no fontshare/google CDN), per find-font rules — [engine]
### Color — [engine]
- Direction: Clay and Linen (lib.clay-and-linen) · Light + Muted · area 80/20 — [engine]
- Ground Linen #F5EDE4 / oklch(0.95 0.015 75); Figure Rose Clay #8D5951 / oklch(0.52 0.07 30); no accent — [engine]
- Text #3D3832 (10:1); muted #6C6761 (4.83:1); figure on ground 4.92:1; button label ground on figure 4.92:1 — [engine]
- Tints #B4786E, #CBA199, #E1CAC6; shades #6A423C, #4A2D28, #2B1815 — [engine]
- Watch-out: moderate contrast; keep long copy in text colour; don't push clay toward orange terracotta — [engine]
### Layout plan — [agent]
- Default I'd reach for: nav, centered hero with two buttons, three cards (Bread / Pastries / Cakes), about with photo, testimonials, CTA band, footer.
- Visitor's questions in order: Is it open now? → Where is it / how do I call? → What's baked today and what does it cost? → Can I order a cake, how? → Hours for other days → Who are they.
- Only this brief has: the day as a rhythm (7:00 bread, 9:00 tarts, 14:00 gone) and a priced daily board. Lead with the open/closed status and the rhythm, as content.
- Cut: testimonials and stats (none supplied, adding is forbidden), feature cards, CTA band, two-button hero.
### Judgment tokens — [agent]
- Radii: 0 except the call button (4px) — the board is a list on paper, not cards (V3).
- Grouping by hairline rules in tint-3 and dot leaders between item and price, like a counter board (V4).
- Spacing: tight inside the menu list, generous between the day line and the menu; not one padding for all sections.
- Imagery: no external images; labelled hatched placeholders for photos (shop front, tarts) — [client constraint].
- Motion: none. Phone first: status, address and call reachable without scrolling at 390px.

## 8. Constraints (each pass/fail on a screenshot)
- C1 At 390×844, the first screen shows the open/closed status, the address and a tap-to-call for cake orders → check phone screenshot — [agent]
- C2 Every price in the brief appears, right-aligned against its item; no price or claim not in the brief → check menu vs. copy — [agent]
- C3 Only engine colours are used; Rose Clay is the only chromatic colour and fills only the call/order action → check render and CSS — [agent]
- C4 Hours show Wed–Sun 7:00–14:00 and closed Mon/Tue as a scannable list, with "or until we sell out" → check render — [agent]
- C5 Photo positions are visibly labelled placeholders, not fake imagery → check render — [agent]

## 9. Avoid (≤6, observable)
- Centered hero with two buttons — [agent]
- Row of three cards for Bread / Pastries / Cakes — [agent]
- Rounded boxed cards around menu items — [agent]
- Emoji or stock icons (croissant, wheat) — [agent]
- Gradients or orange terracotta — [engine]
- Reviews, star ratings, stats — [client]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction | A. Shop day | — (non-interactive) | serves "checking whether it's open" first | until user review |
| Colour | Clay and Linen (engine pick) | — | no other chooseIf matched better; warm, muted | until user review |
| Font pair | Synonym + Sentient (engine pair) | — | top pair for warm headlines/body | until user review |

## 11. Open decisions
- Spec approval (Gate 3) — decide at: first user review — [agent]
- Font files: Synonym.woff2 and Sentient.woff2 must be downloaded from fontshare.com and embedded (base64) or placed in ./fonts/; until then the fallback stacks render — decide at: before launch — [agent]
- Instagram handle and "message us" channel (assumed Instagram DM) — decide at: before launch — [inferred]
- Real photographs for the shop-front and tart placeholders — decide at: before launch — [inferred]
- Dark mode: engine returned light tokens only; page is light-only — decide at: user review — [agent]
- Bank-holiday / sell-out status: live line uses fixed hours only; can't know when they sell out — decide at: user review — [inferred]
- What tallyroll.md excludes (file not supplied) — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
|---|---|---|---|---|
| Round 1 (1440 + 390) | C1 first phone screen: status, address, call | pass | — | — |
| Round 1 | C2 prices match copy | fail → pass | bug: orange cake read "£4 slice · whole £28"; day-line label "Gone, or closed" added wording | price now "£28 whole · £4 a slice"; label "Gone" |
| Round 1 | C3 one chromatic colour, filled only on call action | pass | — | — |
| Round 1 | C4 hours list incl. sell-out note | pass | — | — |
| Round 1 | C5 labelled placeholders | pass; phone ordered tart placeholder above prices | bug | placeholder moved below the board on phone |
| check-layout | nine patterns | none found desktop or phone | — | stopped after round 1 |
