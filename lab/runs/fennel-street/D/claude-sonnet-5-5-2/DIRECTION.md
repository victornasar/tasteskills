# Creative direction: Fennel Street Bakery
Status: draft · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery, Ana and Rita Duarte; sourdough, Portuguese pastries, seasonal cakes — [client]
- Audience: locals within a few streets; people who heard about the custard tarts; mostly on phones, often checking if open — [client]
- The page must: show what's baked, when it's open and where, make cake orders easy — [client]

## 2. Values
- V1 Warm, local, handmade — "warm, local, handmade" — [client]
- V2 Honest: no claims, reviews or prices beyond the copy — "don't add claims, reviews or prices" — [client]
- V3 Answers "is it open?" before anything else — "often checking whether the shop is open" — [client]
- V4 Small and unfussy, like one oven — "still only have one" — [inferred]

## 3. Opening vocabulary
"warm, local, handmade. The opposite of tallyroll.md"
Reading: hypothesis — tallyroll.md is not in the project, so "opposite" is read as non-corporate, non-dashboard, no stats/feature-grid language — [inferred]

## 4. References
None supplied. [inferred] Hand-lettered shop price boards and chalkboard hours signs are the model for the menu and hours.

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome |
| --- | --- | --- | --- | --- |
| A Price board: Synonym + Sentient, Club Cream (lib.club-cream), hours and menu as ruled lists | agent | tarts "gone by two", price list is the content | V1 V3 | Selected |
| B Soft linen: same fonts, Clay and Linen (lib.clay-and-linen), photo-led | agent | no photos exist | — | Not chosen: relies on photography we don't have |
| C Quiet paper: Parchment and Ink (lib.parchment-and-ink) | agent | typographic | — | Not chosen: reads colder, less like custard |
Other-client test (A): the hours line "Bread at seven, tarts by nine, gone by two" and the one-oven price list belong to this shop only.
Fonts: Synonym (synonym) + Sentient (sentient) [engine]. Colors [engine]. Combination [agent].

## 6. Selected direction
Price board — origin: agent — [agent]
A cream page with burgundy type, set like a shop's board: a live open/closed line first, then ruled price lists with dotted leaders.
The one memorable thing: the page opens with whether the shop is open right now.

## 7. Design system
### Typography — [engine]
- Headlines: Synonym (synonym), FFL, self-host only; weights 200–700, no italics
- Body: Sentient (sentient), FFL, self-host only
### Color — [engine]
- Direction: Club Cream (lib.club-cream), Two-Tone, figure on ground 10.37:1
- Ground #F5E7C3 · Figure #5B1D26 · Text #37342E · Muted #67645D · Tint-1 #90474E · Shade-1 #48161D · no separate accent
### Layout plan — [agent]
- Default avoided: centered hero, 3 feature cards, stats, testimonials, CTA band.
- Visitor order: open now? → what's baked → where → order a cake → story.
- Only-this-brief: hours board with live open/closed state; priced menu.
- Cut: testimonials, stats, newsletter (no copy to support them).
### Judgment tokens — [agent]
- Spacing varies with content: tight in lists, large between sections.
- Radius 0 everywhere except none; rules and dotted leaders group things, no boxes.
- Imagery: one labelled photo placeholder, striped CSS, clearly marked.
- Motion: none.

## 8. Constraints
- C1 First phone screen shows name, the line, and open/closed with hours → check: visible without scroll at 390×844 — [agent]
- C2 Every price shown is in the brief and none are added → check: compare against copy — [agent]
- C3 No cards or boxed containers; grouping by rules/space → check: render — [agent]
- C4 Body text ≥17px, tap targets (phone, links) ≥44px high on phone → check: render — [agent]
- C5 Hours, address and phone reachable without scrolling past the menu on phone via nav links or order — [agent]
- C6 Only colors from the engine output → check: CSS — [agent]

## 9. Avoid
- Centered hero headline — [agent]
- Row of three cards — [agent]
- Gradients, emoji icons, pill badges — [agent]
- Row of big numbers — [agent]
- Fake photos or stock-looking imagery — [client]

## 10. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | n/a (non-interactive) | fits page job | until review |

## 11. Open decisions
- Font files: Synonym and Sentient woff2 must be downloaded from fontshare.com and placed in ./fonts/; page falls back to system fonts until then — decide at: deploy — [engine]
- "Message us": no Instagram handle, email or WhatsApp given; link points to #order/phone — decide at: client supplies handle — [inferred]
- Footer Instagram link has no URL — decide at: client supplies handle — [inferred]
- Opening times use the visitor's London clock; bank holidays not covered — decide at: client — [inferred]
- tallyroll.md not available — [inferred]
- Photo of the bakery — decide at: client supplies — [client]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| Round 1 phone | C1 | pass | — | — |
| Round 1 phone | C2, C3, C6 | pass | — | — |
| Round 1 phone | C4 | pass | — | — |
| Round 1 phone | C5 | pass (nav + footer links) | — | — |
| Round 1 | hero lost side padding, nav wrapped | fail → fixed | bug | padding and nowrap fixed; check-layout: none of nine patterns |
