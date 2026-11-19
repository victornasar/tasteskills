# Creative direction: Fennel Street Bakery
Status: draft (non-interactive fast run; not approved) · Mode: fast · v1

Brief source: written brief in this run. The brief names `tallyroll.md` as the opposite register; that file is not in
this project, so the direction is set against the brief's own words only. [inferred]

## 1. Context
- Product: Neighbourhood bakery on Fennel Street, E8: sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: people within a few streets who walk in; people who heard about the custard tarts; mostly on phones, often checking whether the shop is open — [client]
- The page must: show what's baked, when the shop is open and where it is, and make cake orders easy — [client]

## 2. Values (user-owned, 2–5)
- V1 Made by hand, in one shop, by two people — "Ana bakes the bread. Rita does everything with custard… still only have one [oven]." — [client]
- V2 Honest about limits: a daily bake that sells out — "Bread at seven, tarts by nine, gone by two." — [client]
- V3 Local and unhurried: a neighbourhood shop, not a brand — "walk in", "a few streets" — [inferred]

## 3. Positioning
- Category: neighbourhood bakery, filed under "bakery near me" and "custard tarts near me" — [inferred]
- Alternatives: a supermarket or chain bread counter; a larger patisserie that takes cake orders online; a delivery app for bread. Described by kind; no competitor is named by the client — [inferred]
- Conventions (as the category commonly does them; not from research):

  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
  | --- | --- | --- |
  | Hero photograph of loaves or pastries filling the first screen | Challenge | Photos not supplied; the first screen should answer open / where / what, which is what phone visitors check (V2, audience) |
  | Script or ornate wordmark, "artisan" lettering | Avoid | Reads as pastiche; V1 says the bakery is plain and handmade |
  | Pastel palette, cream and sage | Avoid | Colour set comes from find-color's Clay and Linen pick instead |
  | Prices in a menu list, opening hours in the footer | Challenge | Visitors check hours first, so hours move to the first screen (audience) |
  | "Our story" section near the top | Adopt | The About copy is short and carries V1; it stays, placed after the menu |
  | Cake enquiry as a contact form | Challenge | Brief says message or call; a phone link and a short note are enough (audience) |

- Intended perception: three qualities a stranger reports after five seconds on the page — [inferred]
  - P1 Plainly made in one place by named people → check: the About text naming Ana and Rita is visible in the full-page render, with no ornamental lettering above it
  - P2 Open or not, and where, is answered at once → check: the status line, hours and address sit inside the first 844px phone screen
  - P3 Specific, not decorated → check: the page has no gradients, badges, emoji or stock imagery
- Sophistication: everyday — prices run £2.10 to £28 whole cake, no luxury signals in the brief — [inferred]
- Differentiate on: the shop tells you, within a glance, whether today's bake is still on, and how to order a cake. — [agent]

## 4. Opening vocabulary
"Bread at seven, tarts by nine, gone by two."
Reading: deliberate preference — the line already states the daily rhythm; the page builds around that rhythm — [agent]

## 5. References (0–5)
None supplied. [client]

## 6. Directions explored (2)

| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Bake board | agent | V2, P2 | P1, P2 | **Selected** (non-interactive pick) | Puts the day's status and the bake list first |
| B. Tile book | agent | Portuguese pastries (brief); P1 | P1, P3 | Not selected | Would make the first screen a decorative pattern, delaying hours and address |

Engine results (copied from scripts):
- Typography `find-font recommend --role headlines --role body --feel warm --feel literary`: headlines **Synonym** (`synonym`, FFL, Fontshare); body **Sentient** (`sentient`, FFL, Fontshare). Engine top headline pick Switzer was ranked first only because of a `--replaces Inter` flag; the project does not use Inter, so that flag was dropped and Synonym (warm, editorial, no italics) is used. — [engine] + [agent]
- Colour `find-color recommend --domains food-and-beverage --foundation light`: **Clay and Linen** (`lib.clay-and-linen`), pick by engine. Alternative: Club Cream (`lib.club-cream`, burgundy on cream) — [engine]

| Axis | A. Bake board (selected) | B. Tile book | |
| --- | --- | --- | --- |
| Composition | Two columns from tablet up: a status panel (open today, hours, address) beside the bake list; one column on phone — because P2 and V2 | One wide grid of tiles, each a product — because P3 | |
| Scale | One large statement (the line), then small text with prices set heavier — because P2 needs the status readable at a glance | Flat even scale — because P3 "unfussy" | |
| Imagery | Type as image: the daily line set large, plus one inline SVG tile motif — because V2, P3 | Pattern as image across every section — because Portuguese pastries | |
| Signature device | A ruled "today's bake" list with a status line at its head — because V2 | Azulejo-derived tile motif — because pastries | |
| Colour proportion | Linen ground almost everywhere; Rose Clay for headings, the status line and the cake button — [agent] | Rose Clay field tiles alternating with Linen — [agent] | |
| Surface | Soft 14px corners on panels, no shadows, no gradients — because P3 | Square tiles, flat — because the motif | |
| House-style markers (H1–H6) | 2: H2 (pale ground, one muted figure), H3 (ruled list as structure). H1 no (the SVG motif is an illustration), H4 no (rounded panels), H5 no (two columns), H6 no (prices and status change scale) | 4: H1, H2, H4, H6 — house style by the count | |
| Distinct on | Composition, Scale, Imagery, Signature device, Surface — 5 axes | — | |

Other-client test (A): could this belong to another bakery? Only if the bake list and the status panel were
copied elsewhere; the daily line and the two-person About copy are this shop's own text. — [agent]

Difference rule: A and B differ on 5 axes; B challenges the hero-photo convention and A also challenges it
(Challenge row). Directions answer the same brief. The house-style check passes: A scores 2, B scores 4 and was
not chosen.

## 7. Selected direction
Bake board — origin: agent — [agent]
A two-part first screen: the status of today's bake and where to find it, followed by a plain priced list. It serves V2 and P2 first, then P1 through the About copy. Both are set in Synonym and Sentient on Linen with Rose Clay as the single figure colour.
The one memorable thing: the status line says whether today's bake is still on — "Open today until 14:00" — and it is the only moving element. — [agent]
House style: 2 markers. — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Synonym (`synonym`) — FFL, self-host only. Files: `fonts/Synonym-*.woff2`, downloaded from fontshare.com, not included here. Fallback: system-ui.
- Body: Sentient (`sentient`) — FFL, self-host only. Files: `fonts/Sentient-*.woff2`, same source. Fallback: Georgia, serif.
- Notes: until the font files are placed, the page renders in the system fallbacks. Never load from Google Fonts or Fontshare's API (GDPR).

### Color — [engine]
- Direction: Clay and Linen (`lib.clay-and-linen`), Light + Muted.
- Ground: Linen `#F5EDE4` · Figure: Rose Clay `#8D5951` · Text: `#3D3832` (10:1 on Linen) · Muted text: `#6C6761` (4.83:1) · Figure on ground: 4.92:1 (used for headings, the status line and the cake button label, where contrast is ≥4.5).
- Tints/shades: engine tokens are available if needed (tint-1 `#B4786E`, tint-3 `#E1CAC6`).

### Layout plan — [agent]
- Default would have been: nav, centered hero photo with two buttons, three feature cards, stats, testimonials, CTA band, footer. Not used.
- Visitor's questions, in order: is it open today and what's left? where is it? what's baked? how do I order a cake? who makes it?
- The one thing only this brief has: the daily line and the bake list with prices.
- Cut: the stats row, the testimonials (none supplied), the three-card row, the hero photo.
- Axis positions: see §6 table, column A.

### Imagery plan — [agent]
- Job: make a visitor believe the bakery is real, made by hands, and today — serves P1, P2.
- Kind: type as image + one SVG tile motif (illustration, derived from pattern). Photography is not supplied and is not faked.
- Shot list (for the client to commission later, not shipped now):
  - Ana's sourdough on the bench after the morning bake, tight crop, raking window light, full-bleed under the status panel.
  - Rita's custard tarts, overhead, caramelised tops, on the counter, inset beside the menu list.
  - The shop front at 07:00, the door sign visible, placed in the About section.
- Treatment: colour treatment from engine colours only (Linen, Rose Clay); photos would sit inset with 14px corners.
- Ships now: the daily line set large; the status panel; the SVG tile motif in the cake-order band (Rose Clay on Linen); the wordmark in Synonym. No empty image frames. No photos are shown until supplied.
- Honesty: no stock imagery; no invented customers, reviews or claims.

### Judgment tokens — [agent]
- Spacing: 8px base; 24px between panels; 48px between sections. Tied to P2: the status panel must have room to breathe.
- Radii: 14px for panels and the button; 0 for the tile motif. Tied to V1 (soft, handmade).
- Motion: none except the open/closed status updating on load. Tied to P3 (no decoration).

## 9. Constraints (pass/fail on screenshots)
- C1 Opening status, hours and address are all visible in the first 390×844 phone screen → check: the phone screenshot's first screen contains "Open today" or "Closed", "Wednesday to Sunday, 7:00 to 14:00", and "14 Fennel Street, London E8" — [agent]
- C2 Cake ordering is one tap away on a phone → check: a `tel:` link to 020 7946 0381 and an "Order a cake" link are visible within the first two phone screens — [agent]
- C3 The About copy naming Ana and Rita is visible on the full-page render, and no ornamental lettering sits above it → check: full-page screenshot; the wordmark is in Synonym, no script — [agent]
- C4 Visual restraint: no gradient backgrounds, no pill badges, no emoji, no card row of three, no stock imagery → check: full-page screenshot and the DOM check from check-layout — [agent]
- C5 Only engine colours appear (Linen, Rose Clay, the two text colours and the tints if used) → check: the computed colours on the page match the DIRECTION.md values — [agent]
- C6 No external requests and no empty image frames → check: no `<img>`, no `src` pointing off-page, and no box without content — [agent]

## 10. Avoid (≤6, each observable)
- Gradient backgrounds or gradient text — [agent]
- A hero photograph of bread or pastries filling the first screen — [agent]
- Script or ornate lettering in the wordmark — [agent]
- Pill badges, emoji, or stat rows like "10k customers" — [agent]
- Stock imagery of people or bakeries — [client] (no images supplied; invented imagery would misrepresent the business)
- Any review, testimonial or price not in the brief — [client]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction | A. Bake board | (non-interactive: agent chose) | Serves the page's job; departs from the hero-photo convention | Settled = until a reviewer finds the status panel unreadable on phone |
| Headline font | Synonym (engine #2 after the --replaces flag was dropped) | (non-interactive) | Warm, editorial, fits V1 | yes |
| Colour | Clay and Linen (engine pick) | (non-interactive) | Engine pick; soft, earthy, works without photos | yes |
| Photography | None shipped | (non-interactive) | No assets supplied; the brief allows HTML/CSS in place of photos | Settled = until assets arrive |
Rejected (final): Direction B, Tile book — heavy pattern as the first screen delays hours and address (P2).

## 12. Open decisions
- Photography: whether to commission the shot list — decide at: client review — [inferred]
- Instagram handle or URL: the brief gives the word only; footer link is a placeholder anchor — decide at: client review — [inferred]
- Whether the status line uses the visitor's clock (computed on load) or a static line — decide at: critique round 1 — [agent]
- Font files: Synonym and Sentient must be downloaded and placed in `fonts/`; page uses system fallbacks until then — decide at: build handoff — [engine]
- Approval of this spec: non-interactive run, Status stays draft — decide at: client review — [inferred]
- Whether to add a Club Cream variant of the palette — decide at: client review — [agent]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Round 1, phone 390×844 | C1 | Pass (status, hours, address within first screen) | none | — |
| Round 1, phone 390×844 | C2 | Pass (Order a cake, tel link in first screen) | none | — |
| Round 1, phone full page | C3 | Pass (About naming Ana and Rita; wordmark in Synonym, no script) | none | — |
| Round 1, phone full page | C4 | Pass (checker: none of nine patterns) | none | — |
| Round 1, phone full page | C5 | Pass (only Linen, Rose Clay, engine text colours) | none | — |
| Round 1, phone full page | C6 | Pass (no img elements, no external requests) | none | — |
| Round 1, render | Gutter bug: `padding` shorthand on `.line` and `.section` removed the side gutter on phone | Fail → fixed | bug | Code fixed (padding-top/bottom); tile motif arcs redrawn |
| Round 1, render | Font files missing | Fail (open) | bug, environmental | Page falls back to system-ui / Georgia; listed in Open decisions |
| Round 2, phone full page | Gutter after fix | Pass | — | Stopped; two-round cap reached |
| Note | Checker's "body" font reads the first `<p>`, which is the status line in Synonym | Not a page fault | — | Body paragraphs are Sentient |
