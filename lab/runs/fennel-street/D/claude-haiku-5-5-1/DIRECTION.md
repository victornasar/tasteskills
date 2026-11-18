# Creative direction: Fennel Street Bakery
Status: draft (non-interactive run; no user approval yet) · Mode: fast · v1

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8. Sourdough, Portuguese pastries, a few seasonal cakes; cakes ordered ahead — [client]
- Audience: Walk-in neighbours within a few streets, people who heard about the custard tarts, and cake orderers. Mostly on phones, often checking whether the shop is open — [client]
- The page must: let a visitor see whether the shop is open now and what is on the counter today, and find the address — [inferred; the brief lists these as three musts, so the primary job is the first two]

## 2. Values (user-owned, 2–5)
- V1 Local: the neighbourhood, the few streets around it — "neighbourhood bakery", "live within a few streets" — [client]
- V2 Handmade: one oven, bread by hand, custard by hand — "warm, local, handmade"; "still only have one" — [client]
- V3 Honest about limits: sells out, closes at two, cakes need 48 hours — "or until we sell out", "gone by two" — [inferred]

## 3. Opening vocabulary
"Warm, local, handmade. The opposite of tallyroll."
Reading: deliberate preference — the brief sets the register by contrast with a reference page; read as: unhurried, paper-and-clay, not product-marketing — [agent]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
| --- | --- | --- | --- | --- |
| tallyroll.md (named in brief, not read) | — | — | Its register is the opposite of this one | — |

## 5. Directions explored (3)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Linen and Clay: Clay and Linen (`lib.clay-and-linen`) + Synonym / Sentient | agent | Warm, muted, earthy; "handmade" and the counter as the product | V1, V2 | **Selected** | Non-interactive pick: engine rank 1 for food-and-beverage, light ground, warm-muted |
| B. Parchment and Ink (`lib.parchment-and-ink`) + Author / Author | agent | Typographic, quiet, product carries colour | V2 | Alternative | Pick A carries more warmth; B is the fallback if the page reads too cool |
| C. Club Cream (`lib.club-cream`) + Synonym / Sentient | agent | Heritage cream and burgundy | V1 | Alternative | Risks pastiche ("heritage" tips into antique); not chosen |

Other-client test (Direction A): could this belong to another client? A linen ground with a rose-clay figure is common in food brands. What makes it this bakery's is the daily bake list as the first content, and the tarts and loaves as the only things on the page. — [agent]

Font pairs for every direction come from the same engine run: headlines Synonym, Author, Alpino; body Sentient, Author, Plein (find-font, see section 7).

## 6. Selected direction
Linen and Clay — origin: agent — [agent]
A paper ground, one rose-clay figure, and a counter list as the main content. The page reads like the card on the counter, not like an app. Serves V1 (local, a page the neighbourhood checks) and V2 (handmade type, no ornament).
The one memorable thing: today's bake list, set as a ruled menu with prices, is the first thing on the page.

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (`synonym`), FFL, weights 200–700, variable, latin + latin-ext. No italics. Fontshare, self-host only.
- Body: Sentient (`sentient`), FFL, weights 200–700, variable, latin + latin-ext, italics. Fontshare, self-host only.
- Files: `./fonts/Synonym.woff2`, `./fonts/Sentient.woff2` (not bundled; see Open decisions). Fallback stacks: system-ui and Georgia.

### Color — [engine]
- Direction: Clay and Linen (`lib.clay-and-linen`), Light · Chromatic, Light + Muted, contrast tag high
- Ground: Linen `#F5EDE4` (oklch 0.95 0.015 75)
- Figure: Rose Clay `#8D5951` (oklch 0.52 0.07 30) — figure on ground 4.92:1; button label on fill 4.92:1
- Text: `#3D3832` on ground 10:1 · Muted text: `#6C6761` on ground 4.83:1
- Accent: none (engine returned no accent). Rose Clay is the only colour, used for headings, links, the status line and the cake button.

### Layout plan — [agent] (check-layout step 1)
- Default (not used): nav, centred hero with two buttons, three feature cards, stats, testimonials, CTA band, footer.
- Visitor's questions in order: (1) Is it open, and until when? (2) What's on the counter today, and what does it cost? (3) Where is it? (4) Can I order a cake, and how?
- The one thing only this brief has: the bake list with real prices and the day's hours, set as a menu.
- What to cut: testimonials, stats, feature cards, badges, a centred hero, a gradient. No reviews or claims exist in the copy, so none are added.
- Structure: name and line at top-left; status line; today's list; seasonal cakes; cake orders; about; find us; footer. One column on phone; two columns from 760px only for hours and address.

### Judgment tokens — [agent]
- Spacing: 4px base, with large gaps between sections (96px desktop, 56px phone) and tight gaps inside the list. Varies with content, not one scale.
- Radii: 0 on everything except the cake button (2px). Paper, not cards.
- Imagery: no external images. One labelled photo placeholder beside the bake list ("Photo: the day's bread on the board"). No illustrations.
- Motion: none. The open/closed status is computed on load, nothing animates.

## 8. Constraints (each pass/fail on a screenshot)
- C1 First screen on a 390×844 phone shows the name, the line "Bread at seven, tarts by nine, gone by two.", and the open or closed status → check: all three visible without scrolling. — [agent]
- C2 All five daily items and their prices are visible within the first two phone screens → check: Country sourdough £5.20 through Olive oil focaccia £2.80 all visible, no card or carousel. — [agent]
- C3 Headline size is at least 4× body size, and nothing else on the page is larger than the name → check: computed font sizes. — [agent]
- C4 Body and muted text meet contrast on Linen (≥4.5:1 for body, the muted value for secondary labels only) → check: computed colours vs. the engine values. — [agent]
- C5 "Order a cake" is reachable in one tap from the top (a link in the header) and the phone number is a `tel:` link → check: DOM. — [agent]
- C6 No network requests except the local fonts; no external images or scripts → check: network log in the render. — [agent]

## 9. Avoid (≤6, each observable)
- Rounded cards around items or sections — [agent]
- A pill badge or "New" tag above the headline — [agent]
- A row of three equal feature cards or a stats row — [agent]
- Any gradient background or decorative blob — [agent]
- Emoji or icon-font glyphs as bullets — [agent]
- Purple, indigo or other off-palette button colour — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A (Clay and Linen + Synonym/Sentient) | A | (none; non-interactive) | Engine rank 1, warm-muted fits "warm, local, handmade" | until owner review |
| Primary page job | Open status + today's bake list | (none) | The brief's three musts; the order follows the visitor's questions | yes |

Rejected (final): none.

## 11. Open decisions
- Instagram URL for the footer and cake-order message link — decide at: owner, before launch — [inferred placeholder `#instagram`]
- Cake-order channel: the brief says "message us or call". Only the phone number is given; no messaging address. Page links the phone and an Instagram placeholder — decide at: owner — [inferred]
- Font files: Synonym and Sentient are Fontshare FFL, self-host only, and must stay out of public repos. Files are not bundled in index.html; they must be downloaded to `./fonts/`. Confirm the repo is private, or switch to a different font — decide at: owner — [inferred]
- Photo for the counter placeholder — decide at: when photos exist — [inferred]
- Sold-out signal: the page shows "or until we sell out" as text; no live stock — decide at: owner — [inferred]
- Bank-holiday hours and seasonal menu changes not in the brief — decide at: owner — [inferred]
- Gate 3 approval of this spec not given (non-interactive). Build proceeds against this draft — decide at: owner review — [agent]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Critique round 1, phone 390×844 | C1, C2 | Pass: name, line and status on first screen; all five daily prices visible in first two screens | none | none |
| Critique round 1, desktop 1440 | C3 | Pass: headline ~5.5rem vs 1.06rem body; nothing else larger | none | none |
| Critique round 1, check-layout | Avoid: spacing rule | Fail → fixed: About and Cake orders given their own top padding; check now clean on phone | Lesson: uniform section spacing | Changed in code (no constraint edited) |
| Critique round 1, check-layout desktop | Avoid: centred hero | Flagged; the heading is left-aligned full-width masthead, not centred text. Kept. | Checker false positive (heading box spans the column) | Left as is; reason recorded here |
| Not yet measured | C4 contrast, C5 tel link, C6 network | Not run in this pass: contrast values come from the engine; tel link and fonts are in the DOM; no network request is made except the local fonts | — | Noted; not verified by render |
