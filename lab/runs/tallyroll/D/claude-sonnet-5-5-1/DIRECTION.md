# Creative direction: Tallyroll
Status: draft · Mode: fast · v1 (non-interactive run; nothing approved)

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, and the finance leads who sign off; both distrust marketing — [client]
- The page must: make a careful buyer trust Tallyroll with revenue; send them to the docs or a demo — [client]

## 2. Values
- V1 Calm, precise, technical register — "technical, calm, precise" — [client]
- V2 Show the mechanism, don't assert it — "they … want to see how it works" — [client]
- V3 Opposite of fennel-street — [client]. fennel-street.md is not in the project; reading: no warmth-by-decoration, no playful voice — [inferred]
- V4 No claims, numbers or testimonials beyond the copy — [client]

## 3. Opening vocabulary
"technical, calm, precise"
Reading: deliberate preference — stated as the register and contrasted with another brand — [agent]

## 4. References
None supplied. fennel-street.md is cited but absent; used only as Avoid-by-contrast — [inferred]

## 5. Directions explored
| Direction | Origin | Grounded in | Outcome |
|---|---|---|---|
| A Ledger: Overpass + IBM Plex Sans/Mono, Bottle Green Ledger (paper, deep green) | agent | the invoice line is a ledger entry; finance reads ledgers | **selected** |
| B Console: Mona Sans, Graphite and Signal (cool white, blue) | agent | dev-tool default | not chosen: reads as any API product; Mona is GitHub-coded (engine caveat) |
| C Terminal mono: Steps Mono headlines | agent | engineering audience | not chosen: engine caveat (no `= [ ] { }`), cold to finance |

Other-client test (A): paper-and-green ledger comes from the audit-trail promise, not from "API". — [agent]

## 6. Selected direction
Ledger — origin: agent — [agent]
A page that reads like a well-kept ledger: paper ground, green ink, monospace for every figure. Serves V1, V2.
The one memorable thing: the example invoice line opens into the 31 daily totals behind it, on the first screen.

## 7. Design system
### Typography — [engine]
- Headlines: Overpass (overpass), OFL, no caveats
- Body: IBM Plex Sans (ibm-plex-sans), OFL — engine rank 2 for body; rank 1 Plex Serif passed over for a tabular, UI feel — [agent]
- Figures/code: IBM Plex Mono (ibm-plex-mono), OFL
- Loading: self-hosted `./fonts/*.woff2` with system fallbacks; font files are not bundled in the single HTML — [agent]
### Color — [engine]
- Direction: Bottle Green Ledger (lib.bottle-green-ledger), Light + Muted
- Ground #F6F2E7 · Figure #194430 · Text #3D3B34 (10.01:1) · Muted #6D6A63 (4.82:1) · Figure on ground 9.82:1
- Tints #417058 #6E9F84 #9ED0B4 · Shades #123524 #0B2719 #06190F
- Engine returned no accent; the green figure carries actions; tint-3 for hover/rules only — [agent]
### Layout plan — [agent]
- Default: nav, centered hero, 3 cards, stats, testimonials, CTA. Cut: stats, testimonials (none in copy), card row.
- Visitor order: what is it → can I verify it → how does it work → who is it for → cost → go.
- Only-this-brief artifact: the expandable invoice line, in the hero; headline left, artifact right.
- Finance and engineering as two ruled lists, not cards.
### Judgment tokens — [agent]
- Radius 2px on the invoice object only; 1px rules group everything else (ledger = lines).
- Spacing varies: tight in lists, large between ideas. Motion: none beyond expand.
- Imagery: none; the invoice is built in HTML.

## 8. Constraints
- C1 Headline left-aligned, ≥4× body size; invoice line on first screen → check: desktop screenshot
- C2 Invoice line expands to exactly 31 rows summing to 1,204,388 → check: open details
- C3 No numbers/claims outside the copy (day split labelled illustrative) → check: read text
- C4 Figures in mono; paper + green only, no gradients → check: screenshot
- C5 390px: no horizontal scroll, invoice line legible → check: phone screenshot
- C6 Docs primary, demo secondary, repeated at the end → check: both visible

## 9. Avoid
- Centered hero; row of three cards; pill badges; gradients; emoji; rounded boxes on every section; row of big numbers

## 10. Decisions log
| Decision | Recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction A | agent | n/a (non-interactive) | fits audit-trail promise | until approval |

## 11. Open decisions
- Approval of this draft — decide at: user review
- fennel-street.md contents — decide at: user supplies file — [inferred]
- Docs and demo URLs — placeholders `#docs`, `#demo`
- Font files to self-host — decide at: deploy
- Daily split numbers are illustrative; swap for real sample data — [inferred]

## 12. Checkpoints
Filled after critique (see final report).
