# Creative direction: Tallyroll
Status: draft (non-interactive fast run; Gates 1–3 unconfirmed) · Mode: fast · v1

## 1. Context
- Product: Usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies (integrate); finance leads who sign off and reconcile line items monthly (decide). They distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with revenue, then send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceable: every amount resolves to the events behind it — "Every cent traces back to an event." — [client]
- V2 Precise: numbers, arithmetic and rules are shown, not described — "written as rules you can read" — [client]
- V3 Calm: no hype; the page states what the product does — "The opposite of fennel-street.md" (file not present in project; read from brief only) — [inferred]

## 3. Opening vocabulary
"Technical, calm, precise. The opposite of fennel-street.md."
Reading: deliberate preference — the brief names the register directly; the referenced file is absent, so the contrast is taken from the brief's own words — [agent]

## 4. References (0–5)
None supplied. No reference sites were named. — [inferred]

## 5. Directions explored (3)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Graphite and Signal: light Paper White ground, Graphite figure, Signal Blue for links/focus only; Supreme headlines + IBM Plex Sans body | agent (engine pick #1 for color) | Engine rank 1 for fintech + enterprise-software; "reserve blue for actions" | Calm, precise, dense-readable | **Selected** (non-interactive choice) | — |
| B. Slate Press: dark blue-black ground, Cold Paper figure, no accent; same type | agent (engine rank 2) | Technical-product dark interface | Engineers; weaker for finance readers | Not selected | Finance sign-off reads better on light paper |
| C. Bottle Green Ledger: cream ground, bottle-green figure | agent (engine rank 3) | Finance convention | Trust through restraint | Not selected | Engine flags it as category convention, differentiates little |

Other-client test (direction A): a graphite-on-white page with one blue link colour could belong to many SaaS tools. What is specific here is the structural idea below (the invoice line as the hero object), which comes from the product's own line→events relation.
Structural idea (agent): lead with a real-looking invoice line built in HTML, expandable to its daily totals, beside a left-aligned headline. The page is a document about one invoice, not a feature grid.

## 6. Selected direction
Ledger Hairline — origin: agent — [agent]
A quiet, document-like page on paper-white with graphite type and hairline rules. The invoice line is the only object drawn as a box; everything else is typeset and ruled. Serves V1 (traceability shown on the first screen) and V2 (the arithmetic is on the page).
The one memorable thing: the invoice line that opens into its 31 days.

## 7. Design system
### Typography — [engine]
- Headlines: Supreme (id `supreme`, FFL, self-host only, keep files out of public repos), weights 500–700 — [engine] ; the engine's top pick for headlines was Mona Sans, but its caveat ("strongly associated with GitHub") bites for a developer-tool brand, so Supreme is used — [agent]
- Body: IBM Plex Sans (id `ibm-plex-sans`, OFL), weights 400/500/600 — [engine]
- Monospace for `POST /v1/events` and figures: not in the requested roles; IBM Plex Mono is the obvious pairing (noted, not used unless the page needs it) — [agent]
- Font files: fonts/Supreme-Variable.woff2 and fonts/IBMPlexSans-Variable.woff2 are referenced but not supplied in this run. Stack falls back to system-ui. — [inferred]
### Color — [engine]
- Direction: Graphite and Signal (id `lib.graphite-and-signal`) — [engine]
- Ground: Paper White #F9FAFB — [engine]
- Figure: Graphite #15181E — [engine]
- Accent: Signal Blue #0E6EE6 — [engine]
- Text: #3C3F46 (contrast 10.09:1 on ground) — [engine]; Muted text: #6B6F76 (4.82:1) — [engine]
- Figure on ground 17.01:1 — [engine]. Accent use is restricted to links, focus rings and the expansion marker. Primary button uses the engine's button pair (Graphite fill, Paper White label, 17.01:1) rather than Signal Blue fill — [agent]
### Layout plan — [agent]
- Default: nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor questions in order: what is it and does it take my revenue seriously → how does one line become an invoice → what does finance get / what does engineering get → what does it cost → where do I start.
- Lead object: the invoice line (content, not decoration), beside a left-aligned headline; stacks below on phone.
- Cut: centered hero, card row, stats row, testimonials (none supplied), CTA band (replaced by a closing action row).
### Judgment tokens — [agent]
- Spacing: one 8px base; section gaps differ by content density (hero generous, how-it-works tight). Not a fixed scale across sections.
- Radii: 0 on text blocks; 4px only on the invoice exhibit and buttons. Radius is not used as decoration.
- Imagery: none. No external images. The exhibit is HTML/CSS.
- Motion: none beyond focus transitions. The expand is shown open in static form; no animation required.

## 8. Constraints (pass/fail on a screenshot)
- C1 Headline is left-aligned and the invoice line is fully visible in the first screen at 1440×900 → check: headline left edge aligned with nav; invoice line legible without scrolling — [agent]
- C2 Signal Blue appears only on links, focus rings and the expansion marker → check: no blue fills or blue decoration elsewhere — [agent]
- C3 No bordered cards; how-it-works, finance and engineering are ruled lists/columns → check: no item sits in its own box except the invoice exhibit — [agent]
- C4 No gradients, emoji, pill badges, icon glyphs used as decoration, purple → check: visually absent — [agent]
- C5 Headline at least 4× body size on desktop and 2.5× on phone; body at least 16px; nothing else competes with the headline in size → check: computed sizes at 1440 and 390 widths — [agent]
- C6 Primary action "Read the docs" is filled; "Book a demo" is outlined; both visible in first screen → check: style difference — [agent]
- C7 Phone width 390px: no horizontal scroll; exhibit stacks below headline, 16px side gutter → check: checker reports no overflow — [agent]
- C8 Every number on the page appears in the copy or is arithmetic on it (1,204,388 × $0.0004 = $481.76) → check: no added figures — [client]

## 9. Avoid (≤6, observable)
- Centered hero headline — [agent]
- Row of three feature cards — [agent]
- Decorative gradient backgrounds or gradient text — [agent]
- Emoji or decorative icons — [agent]
- Stats row of large numbers or invented metrics, logos or testimonials — [agent]
- Blue used as a fill or background colour — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Direction A (Graphite and Signal) | A | not confirmed (non-interactive) | Engine rank 1; fits calm/precise and finance readability | Settled = until user review |
| Headline font: Supreme instead of engine top pick Mona Sans | Mona Sans | not confirmed | Mona Sans caveat: GitHub association for a dev-tool brand | Settled = until user review |
| Primary button = Graphite fill, not Signal Blue fill | Graphite | not confirmed | Engine's verified button pair; keeps blue reserved | Settled = until user review |
Rejected (final): none.

## 11. Open decisions
- Font files for Supreme and IBM Plex Sans: supply them in ./fonts/ or accept system fallback — decide at: Phase 4 handoff — [inferred]
- Docs URL and demo booking URL: placeholders "#docs" and "#demo" until supplied — decide at: Phase 4 handoff — [inferred]
- Whether a monospace face is needed for code samples (IBM Plex Mono) — decide at: user review — [agent]
- Gate 1/2/3 approval of this direction — decide at: user review — [inferred]
- Whether the file fennel-street.md exists elsewhere and should refine the "opposite" reading — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
| Critique round 1 (check-layout, 1440 + 390) | C1 | Pass | — | None |
| Critique round 1 | C2 | Pass | — | Blue only on caret, links and focus |
| Critique round 1 | C3 | Pass | — | How it works is a ruled sequence, not boxed cards |
| Critique round 1 | C4 | Pass | — | None |
| Critique round 1 | C5 | Pass (4.1× desktop, 2.5× phone, at the limit) | — | None |
| Critique round 1 | C6 | Pass | — | None |
| Critique round 1 | C7 | Pass (checker: no overflow at 390) | — | None |
| Critique round 1 | C8 | Pass | — | Day labels 1–31 only; no daily values invented |
| Critique round 1 | Pattern: row of three cards (flagged) | Kept | The three steps are an ordered sequence the brief numbers (check-layout: "a sequence when order matters") | Kept, reason logged here |
| Critique round 1 | Pattern: same padding (flagged) | Fixed | Sections shared 80px padding | Varied: 48px (finance/engineering), 112px (pricing) |
| Critique round 2 | — | Not needed | Round 1 fixes resolved the only actionable finding | Stopped; 1 of 2 rounds used |
| Open | Font files | Not verified | Fonts/ not supplied; render used system-ui fallback, so Supreme and IBM Plex Sans were not seen in the screenshot | Supply files to verify typography |
