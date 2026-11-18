# Creative direction: Tallyroll
Status: draft (non-interactive run, not approved) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API; turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, plus the finance leads who sign off; they distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with revenue, and send them to the docs or a demo — [client]

## 2. Values
- V1 Traceable: every number opens up to its source — "Every cent traces back to an event" — [client]
- V2 Calm and precise — "technical, calm, precise" — [client]
- V3 Shows, doesn't sell — "distrust marketing, want to see how it works" — [client]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference. fennel-street.md was not provided, so "opposite" is read as: no warmth or ornament, no persuasion devices — [inferred]

## 4. References
None given — [inferred]

## 5. Directions explored
| Direction | Origin | Grounded in | Outcome |
| A Ledger: left-aligned, invoice line is the hero, rules not boxes; Overpass + IBM Plex Sans + Iosevka; Graphite and Signal | agent | the expanding invoice line | Selected |
| B Spec sheet: Steps Mono headings, Bottle Green Ledger | agent | API-doc register | Not chosen: Steps Mono lacks = { } [ ] and accents, which bites a page that shows code |
| C Statement: Cabin Navy, IBM Plex Serif body | agent | finance sign-off | Not chosen: reads as generic bank; serif body works against "engineering" |
Other-client test (A): the hero is Tallyroll's own invoice line with its 31 day rows; no other client has it.

## 6. Selected direction
Ledger — origin: agent — [agent]
A quiet light page set like a statement: hairline rules, tabular figures, one blue used only for links and focus. The first screen is the headline plus an openable invoice line. Serves V1–V3.
The one memorable thing: the invoice line opens into the 31 daily totals that sum to it.

## 7. Design system
### Typography — [engine]
- Headlines: Overpass (overpass), OFL
- Body: IBM Plex Sans (ibm-plex-sans), OFL
- Code and figures: Iosevka (iosevka), OFL
- Font files are not bundled; CSS names ./fonts/*.woff2 with system fallbacks. Self-host from the engine urls.
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light / Neutral, engine default pick
- Ground #F9FAFB · Figure #15181E · Accent #0E6EE6 · Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Tint-3 #B2B8C0 (rules)
- Accent on ground 4.57:1: links and focus only, per engine
### Layout plan — [agent]
- Default dropped: centered hero, three cards, stats band, testimonials, CTA band.
- Visitor order: what is it → can I trust a number → how does it work → does it fit my stack and finance process → cost → go.
- Only-this-brief artifact: expandable invoice line, in the first screen.
- Cut: testimonials, stats, logos (none in the copy).
### Judgment tokens — [agent]
- Radius 2px, only on buttons and the invoice object. Spacing varies: tight inside lists, wide between ideas. No images or icons; numerals label steps. Motion: none beyond the native details toggle.

## 8. Constraints
- C1 Headline left-aligned and at least 4× body size → render
- C2 First screen contains the invoice line with its toggle → desktop shot
- C3 Accent blue only on links, focus and the toggle; buttons graphite → render
- C4 No cards, gradients, pills or emoji; grouping by rules → render
- C5 No claim, number or testimonial outside the brief copy (daily totals labelled illustrative) → text
- C6 At 390px no horizontal scroll → phone shot

## 9. Avoid
- Centered hero; row of three cards; gradients; pill badges; big-number stat row; purple buttons — [agent]

## 10. Decisions log
| Direction A chosen automatically (non-interactive) | agent | – | best serves "show how it works" | until Gate 3 |

## 11. Open decisions
- Approve direction, set Status to agreed — decide at: Gate 3
- Host font files in ./fonts — decide at: deploy
- Docs, demo and footer link targets (currently #) — decide at: launch
- Daily totals are illustrative; replace with real sample data — decide at: content review
- Reading of fennel-street.md and references — decide at: Gate 1
