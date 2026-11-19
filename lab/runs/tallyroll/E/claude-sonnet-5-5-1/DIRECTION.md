# Creative direction: Tallyroll
Status: draft · Mode: fast · v1

## 1. Context
- Product: usage-based billing API; turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, and the finance leads who sign off — [client]
- The page must: make a careful buyer trust Tallyroll with revenue; send them to the docs or to book a demo — [client]

## 2. Values
- V1 Calm, precise — "technical, calm, precise" — [client]
- V2 Show, don't claim — "They distrust marketing and want to see how it works" — [client]
- V3 Traceability — "Every cent traces back to an event" — [client]

## 3. Positioning
- Category: billing API / usage metering and invoicing — [inferred]
- Alternatives: building billing in-house; a general subscription-billing tool; spreadsheets at month end (by kind, none named) — [inferred]
- Conventions:
  | Convention | Stance | Why |
  | Code snippet beside the hero | Adopt | engineers read the endpoint to judge the product (V2) |
  | Logo wall / testimonials | Avoid | brief supplies none; may not invent (V2) |
  | Row of big stat numbers | Avoid | would be invented claims |
  | Three feature cards | Challenge | the invoice line is the real artifact (V3) |
  | Dark gradient hero | Challenge | calm, not hype (V1) |
- Intended perception:
  - P1 "I can see how it works" → check: an interactive invoice line with its endpoint is visible in the first screen or just under it
  - P2 "Nothing is hidden" → check: every figure on the page is arithmetic the reader can verify
  - P3 "Calm and exact" → check: one accent colour, no gradients, aligned numerals
  — [inferred]
- Sophistication: considered — B2B finance infrastructure, sign-off by finance — [inferred]
- Differentiate on: the invoice line that opens into its 31 daily totals — [client]

## 4. Opening vocabulary
"technical, calm, precise" — Reading: deliberate preference — [agent]

## 5. References
None given. See Open decisions.

## 6. Directions explored
| Direction | Origin | Fonts | Colour | Outcome |
| A Ledger Instrument | agent | Overpass + IBM Plex Sans | Graphite and Signal | Selected |
| B Cream Ledger Book | agent | same | Bottle Green Ledger (engine rank 2) | Not selected: follows category convention, drifts to house style |
| C Dark Console | agent | same | dark (engine excluded for light run) | Not selected: contradicts "calm", dev-tool cliché |

| Axis | A | B | C |
| Composition | asymmetric; working invoice as layout — V3 | one reading column | full-bleed terminal |
| Scale | one big headline, rest small, numerals mid — V1 | flat | big |
| Imagery | product interface built in HTML — V2 | none | terminal |
| Signature device | the expandable ledger line with dotted leader — V3 | rules | prompt |
| Colour proportion | ground 86 / figure band 11 / accent 3 — engine area | cream 84 / green 16 | dark |
| Surface | flat, square, 1px rules, one inverted graphite band | same | glow |
| House-style markers | 3 (H3, H4, H5) | 5 | 1 |
| Distinct on | composition, imagery, signature, colour | | |

## 7. Selected direction
A Ledger Instrument — origin: agent — [agent]
The page is the product: an invoice line you can open. Serves P1–P3.
The one memorable thing: a billed amount that expands into the 31 days behind it.
House style: 3 markers.

## 8. Design system
### Typography — [engine]
- Headlines: Overpass (overpass), OFL, variable 100–900, caveats none
- Body: IBM Plex Sans (ibm-plex-sans), OFL, variable 100–700
- Code/numerals: no mono returned by the engine; system monospace stack (`ui-monospace`). Open decision.
### Color — [engine]
- Graphite and Signal (lib.graphite-and-signal), Light/Neutral
- Ground #F9FAFB · Figure #15181E · Accent #0E6EE6 · text #3C3F46 (10.09:1) · muted #6B6F76 (4.82:1) · tints #44484F #797E85 #B2B8C0
- Accent only for links, focus, primary action.
### Layout plan — [agent]
- Default avoided: centered hero, three cards, stats, testimonials, CTA band.
- Visitor order: what is it → show me → how does it work → who is it for → what does it cost → docs/demo.
- Only-this-brief artifact: the expandable invoice line, leading.
- Cut: testimonials, logos, stats, extra feature cards.
### Imagery plan — [agent]
- Job: make the traceability believable — P1, P2
- Kind: product interface (HTML/CSS)
- Ships now: invoice line + 31-day table, request snippet. No photos.
### Judgment tokens — [agent]
- Spacing varies by content: tight in the ledger, wide between ideas. Radii 0–2px. Motion: only the expand.

## 9. Constraints
- C1 Headline is ≥4× body size and left-aligned → [agent]
- C2 Invoice line is visible without scrolling on 1440×900 and is keyboard-operable → [agent]
- C3 Accent colour appears only on links, focus, primary action → [agent]
- C4 No claim, number or testimonial outside the brief (except the labelled illustrative daily table) → [agent]
- C5 P3: no gradients, no emoji, no shadows → [agent]
- C6 No horizontal scroll at 390px → [agent]

## 10. Avoid
- Gradients, pill badges, emoji icons, three-card rows, big-number stat rows, logo walls — [agent]

## 11. Decisions log
| Direction A chosen | Best serves page job (non-interactive) | Settled until review |

## 12. Open decisions
- Direction A not user-approved — decide at: first review
- Mono font for code/numerals — decide at: font review (engine returned none; Plex Mono is the sibling family but was not engine-returned)
- Fonts are referenced by name with system fallbacks; woff2 files not bundled in the single file — decide at: deploy
- Daily totals are illustrative, generated to sum to 1,204,388 — replace with real data
- Audience, values and positioning are inferred beyond the brief; no references supplied
- Docs/demo URLs are placeholders (#)

## 13. Checkpoints
See report in chat.
