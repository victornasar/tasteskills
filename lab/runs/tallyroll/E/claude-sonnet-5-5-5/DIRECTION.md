# Creative direction: Tallyroll
Status: draft (non-interactive run, no approval gate) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API; turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing; finance leads who sign off with them; they distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, then send them to the docs or a demo — [client]

## 2. Values
- V1 Calm, precise — "technical, calm, precise" — [client]
- V2 Show, don't claim — "They distrust marketing and want to see how it works" — [client]
- V3 Traceability — "Every cent traces back to an event" — [client]
- V4 Opposite of fennel-street.md — [client] (file not supplied; read only as "not warm/decorative") — [inferred]

## 3. Positioning
- Category: usage-based billing API / billing infrastructure — [inferred]
- Alternatives: building billing in-house; another billing platform (not named) — [inferred]
- Conventions:
  | Convention | Adopt / Challenge / Avoid | Why |
  | Dark developer-tool look, glowing accents | Challenge | V1; finance readers sign off, they need paper not neon [agent] |
  | Blue as lead colour (engine convention: finance-blue, technology-blue) | Challenge | Interchangeable with alternatives; green ledger ties to V3 [agent] |
  | Code snippet / endpoint visible on first screens | Adopt | Engineers verify how it works (V2) [agent] |
  | Logo wall and testimonials | Avoid | No such material in brief; none may be invented [agent] |
  | Hero headline then product screenshot | Adopt, with the artifact being the invoice line itself | V3 [agent] |
- Intended perception — [inferred]
  - P1 "It shows its working" → check: a real invoice line with its arithmetic and 31 days is visible in the first screen
  - P2 "Calm, nothing shouting" → check: one accent hue, no gradients, no badges, body text ≥ 16px
  - P3 "Built for both engineers and accountants" → check: endpoint in mono and a ledger-style total both appear above the fold or in the next screen
- Sophistication: considered — B2B revenue infrastructure, buyers sign off on revenue — [inferred]
- Differentiate on: the invoice line opens up into the days behind it, on the page — [client] (copy)

## 4. Opening vocabulary
"technical, calm, precise" — Reading: deliberate preference — [agent]

## 5. References
None supplied. fennel-street.md named as opposite, not available.

## 6. Directions explored
| Direction | Origin | Fonts (engine) | Colour (engine) |
| A Ledger sheet | agent | Mona Sans + IBM Plex Mono | Bottle Green Ledger |
| B Console | agent | Mona Sans + IBM Plex Mono | Graphite and Signal |
| C Spec document | agent | IBM Plex Serif + Plex Mono | Cabin Navy |

| Axis | A Ledger sheet | B Console | C Spec document |
| Composition | asymmetric: headline left, live invoice sheet right; later sections as ledger rows — V2 | dark docs-style sidebar layout | one reading column |
| Scale | big moment per section (headline, total, 0.5%) — V1 | flat | one big, rest small |
| Imagery | product interface built in HTML: invoice + 31-day grid — P1 | terminal mock | type only |
| Signature device | the ruled total line (dotted leader to amount) — V3 | blinking cursor | footnote numbers |
| Colour proportion | cream ground, one full-width inverted green band — P2 | dark ground | white ground, navy figure |
| Surface | invoice sheet has paper depth, rest flat — V2 | rounded panels | flat |
| H-markers | 2 (H3, H5-partial no): H2, H3 | 3 | 5 |
| Distinct on | composition, imagery, surface, colour | | |

## 7. Selected direction
A Ledger sheet — origin: agent — [agent] (chosen: best serves page job and departs most from category layout)
The page is a working invoice. Serves P1, P3.
The one memorable thing: the invoice line opens into the 31 days behind it.
House style: 2 markers (H2, H3).

## 8. Design system
### Typography — [engine]
- Headlines and body: Mona Sans / Hubot Sans (mona-sans), OFL, variable 200–900
- Code, figures: IBM Plex Mono (ibm-plex-mono), OFL
- Not embedded; `@font-face` points to ./fonts/*.woff2 with system fallback. Self-host, no third-party requests.
### Color — [engine]
- Bottle Green Ledger (lib.bottle-green-ledger)
- Ground #F6F2E7 · figure #194430 · text #3D3B34 (10.01:1) · muted #6D6A63 (4.82:1) · tints #417058 #6E9F84 #9ED0B4 · shades #123524 #0B2719 #06190F
- Figure on ground 9.82:1. Hairlines/sheet whites derived by mixing in CSS from these tokens — [agent]
### Layout plan — [agent]
- Default: centered hero, three cards, stats, testimonials, CTA band. Cut: testimonials, stats, logos (none in brief).
- Visitor questions: what is it → how does it work → can I check it → what does it do for me (finance / eng) → cost → act.
- Only-this-brief thing: the expandable invoice line.
- Order: header · hero+invoice · how it works (inverted band, vertical sequence) · for finance / for engineering · pricing · footer.
### Imagery plan — [agent]
- Job: make the visitor believe every figure is traceable — P1
- Kind: product interface built in HTML/CSS (invoice sheet, 31-day grid as bars)
- Ships now: invoice sheet; day grid. Daily values are generated to sum to 1,204,388 and labelled illustrative.
### Judgment tokens — [agent]
- Radii 2px; shadow only on the invoice sheet; spacing varies: tight in ledgers, wide between ideas; no motion except details toggle.

## 9. Constraints
- C1 Invoice line with arithmetic and day grid visible on desktop first screen → check: screenshot
- C2 Headline ≥ 4× body size → check: computed sizes
- C3 Only the green hue plus neutrals; no gradients, badges, emoji → check: render
- C4 Primary and secondary action visible in first screen; docs is the visually stronger → check: render
- C5 No claim, number or testimonial beyond brief (illustrative days labelled) → check: copy diff
- C6 Phone 390px: no horizontal scroll → check: render

## 10. Avoid
- Gradients; pill badges above headline; rows of three cards; stat rows; emoji icons; logo walls.

## 11. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction A | A | — | non-interactive | until review |
| Fonts not embedded | fallback stack | — | single file, no external requests | until review |

## 12. Open decisions
- Approve direction/spec — decide at: review — [agent]
- Illustrative daily totals: replace with real example data — decide at: client data
- fennel-street.md contents — read as unknown — [inferred]

## 13. Checkpoints
| Round 1 | C1–C6 | pass (desktop 1440, phone 390; check-layout: none of nine patterns) | bug: h2 line-height 1.6 and one added dd line | fixed |
House-style markers on render: H2 yes, H3 yes (hairlines), others no = 2.
