# Creative direction: Fennel Street Bakery
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: neighbourhood bakery, two sisters, sourdough, Portuguese pastries, a few seasonal cakes — [client]
- Audience: people living within a few streets, plus people who heard about the custard tarts; mostly on phones, often checking if the shop is open — [client]
- The page must: show what's baked, when it's open and where, and make cake orders easy — [client]

## 2. Values
- V1 Warm — "warm, local, handmade" — [client]
- V2 Local / personal — "run by two sisters", "within a few streets" — [client]
- V3 Honest, no puffery — "don't add claims, reviews or prices" — [client]
- V4 Practical first — "checking whether the shop is open" — [inferred]

## 3. Positioning
- Category: the local bakery / the place for custard tarts — [inferred]
- Alternatives: a supermarket in-store bakery; a bigger café-bakery chain; another independent bakery nearby (described by kind, none named) — [inferred]
- Conventions:
  | Convention | Decision | Why |
  | Full-bleed food photo hero | Challenge | No photos supplied; V3 forbids stock posing as the shop; the line is the hero — [agent] |
  | Hours and address findable at once | Adopt | Audience checks "is it open" on a phone (V4) — [agent] |
  | Menu as a priced list | Adopt | Prices are in the brief; people scan to decide — [agent] |
  | Cream/kraft + script "artisan" type | Avoid | Reads as generic artisan pastiche; V2 wants this shop's own voice — [agent] |
  | Order form with many fields | Challenge | Brief gives phone/message only; no invented form — [agent] |
- Intended perception — [inferred]
  - P1 Open today or not, in under five seconds → check: a live open/closed line sits in the first screen
  - P2 Small, handmade, two people → check: hand-scaled shapes, the sisters' names and "one oven" in plain sight
  - P3 Sells out → check: the day timeline "7 / 9 / 2" is visible as the page's signature
- Sophistication: everyday — prices £2–£6 for loaves and pastries — [inferred]
- Differentiate on: a day laid out by the clock (bread at seven, tarts by nine, gone by two) with a live open status — [agent]

## 4. Opening vocabulary
"warm, local, handmade"
Reading: deliberate preference — stated as the register, opposite of the tallyroll brief — [agent]

## 5. References
| Reference | Admire | Borrow | Avoid | Just interesting |
| tallyroll.md (named in brief) | — | nothing | Everything: it is the stated opposite. File was not available to read, so "opposite" is taken only as cool/technical vs warm/handmade — [inferred] | — |

## 6. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| A Day Clock | agent | the tagline | P1, P3 | Selected [agent] | non-interactive |
| B Price Board (chalkboard-dark ground, menu as the layout) | agent | Daily list | P2 | Not chosen | — |
| C Loaf Poster (big CSS bread shapes, one huge word per section) | agent | handmade | P2 | Not chosen | — |

Fonts: Recursive (headlines, [engine] id recursive) + Source Sans 3 (body, id source-sans-3), from find-font recommend `--feel warm --public-repo`. Colours: Butter and Chocolate (lib.butter-and-chocolate), the engine's alternatives were Clay and Linen, Club Cream, Porcelain and Indigo. [engine]

| Axis | A Day Clock | B Price Board | C Loaf Poster |
| Composition | asymmetric: statement left, hours board right on desktop; one column on phone — because V4 | one catalogue column | stacked full-bleed modules |
| Scale | one big moment (the line), rest small — because P3 | several mid | several big |
| Imagery | CSS/SVG loaf and tart, labelled photo frames — because V3 | none | CSS shapes |
| Signature device | a timeline bar 7 → 9 → 14 with a live "now" mark — because the tagline | chalk rules | scored-loaf cut |
| Colour proportion | butter ground ~75%, chocolate figure ~20% incl. one inverted band, tints for fills — because V1 | chocolate ground | split halves |
| Surface | soft: big radii on food shapes only, flat elsewhere, no shadows — because V1/V2 | grain | grain |
| House-style markers | 2 (H3 small labels, H5 left headline) | 4 | 2 |
| Distinct on | composition, signature, surface, colour | | |

Other-client test: the 7/9/14 timeline and live open status come from this shop's tagline and hours; no other bakery shares them.

## 7. Selected direction
Day Clock — origin: agent — [agent]
The page is organised around the shop's day. Opening status first, then the clock strip, then what's baked, then cakes. Serves V1, V4, P1, P3.
The one memorable thing: a live open/closed line above a 7 / 9 / 2 day strip.
House style: 2 markers — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: Recursive (recursive), variable 300–900, used with its casual/sans axes; license OFL. Source: github.com/arrowtype/recursive
- Body: Source Sans 3 (source-sans-3), variable 200–900, OFL. Source: github.com/adobe-fonts/source-sans
- Not embedded: font files were not available offline in this run, so the page names the families, tries local(), and falls back to system fonts (see Open decisions).
### Color — [engine]
- Direction: Butter and Chocolate (lib.butter-and-chocolate)
- Ground #F4E9B4 · Figure #45281A · text #37352E · muted #66645D · tint-1 #775242 · tint-2 #A98271 · tint-3 #DFB5A2 · shade-1 #371F14
- Contrast from engine: figure on ground 10.92:1, text 10.02:1, muted 4.83:1
### Layout plan — [agent]
- Default dropped: centred hero, 3 cards, stats, testimonials (none are in the brief).
- Visitor questions: open now? → where? → what's baked and cost? → how do I order a cake?
- Only-this-brief: the day strip + live open status.
- Cut: testimonials, stats, newsletter, long about.
- Axes as table above.
### Imagery plan — [agent]
- Job: make a visitor believe it is a small hand-run oven, not a chain — serves P2
- Kind: SVG illustration (loaf, tart) + labelled photo frames
- Shot list: Ana scoring loaves, side light, 4:5, beside About; tray of pastéis de nata, overhead, 1:1, by Daily; orange and almond cake whole, 3/4 view, 4:3, by Season
- Treatment: tint-3 fills and chocolate line; frames inset, same radius as food shapes
- Ships now: SVG loaf in hero, CSS day strip; the three photo frames are labelled placeholders below the first screen
### Judgment tokens — [agent]
- Spacing: tight within a group, large between ideas; sections not identical
- Radii: 999px / 28px for food shapes and frames only; 0 on text blocks and buttons use 10px
- Motion: none beyond a gentle pulse on the open dot, off under reduced-motion

## 9. Constraints
- C1 Open/closed line visible without scrolling at 390×844 → check: P1 — [agent]
- C2 Hours and address both readable by one scroll from the top on phone → check: V4 — [agent]
- C3 No price, claim or review beyond the brief → check: compare copy — [agent]
- C4 Headline at least 4× body size on desktop → check: scale — [agent]
- C5 Call link tappable (≥44px) → check: cake section — [agent]
- C6 Page passes P2 with photo frames empty → check: first two screens — [agent]

## 10. Avoid
- Centred hero with two buttons — [agent]
- Row of three equal cards — [agent]
- Gradients and emoji icons — [agent]
- Script "artisan" fonts and kraft textures — [agent]
- Photo frames pretending to be photos — [agent]

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | n/a (non-interactive) | best serves "is it open" | until approval |
| Butter and Chocolate | engine alt, warm/retro | n/a | highest contrast of warm options | until approval |
Rejected (final): none

## 12. Open decisions
- Font files: embed woff2 for Recursive and Source Sans 3 — decide at: delivery — [inferred]
- Instagram link target and handle (not in brief; footer link is a placeholder) — decide at: client reply
- Message channel for cakes (brief says "message us" with no channel; page offers phone only) — decide at: client reply
- Real photos for three frames — decide at: shoot
- Whether bank holidays change hours (not in brief) — decide at: client reply

## 13. Checkpoints
| Round | Constraint | Result | Type | Action |
| 1 | C1 status line in first screen | pass (phone + desktop) | | |
| 1 | C2 hours+address one scroll | fail: they sit at the foot; only a top-bar link reaches them | lesson | kept; link in top bar and footer, status line carries hours. Reopen with client |
| 1 | C3 no added claims | pass | | |
| 1 | C4 headline >=4x body | pass (83px vs 18px) | | |
| 1 | C5 tap target | pass (56px) | | |
| 1 | C6 P2 with frames empty | pass | | |
| 1 | check-layout: rounded boxes (8 of 13) | kept: soft radii are the handmade surface; text blocks stay square | | |
| 1 | hero headline wrapped badly on desktop | fail | bug | fixed: nowrap lines, smaller clamp |
Markers on render: H3, H5 = 2.
