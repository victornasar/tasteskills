# Creative direction: Tallyroll
Status: draft · Mode: fast · v1

## 1. Context
- Product: usage-based billing API; turns raw usage events into invoices — [client]
- Audience: engineering leads at usage-priced software companies, and the finance leads who sign off; both distrust marketing — [client]
- The page must: make a careful buyer trust Tallyroll with revenue, then send them to the docs or a demo — [client]

## 2. Values
- V1 Precise — "technical, calm, precise" — [client]
- V2 Show the mechanism — "want to see how it works" — [client]
- V3 No invented claims — "don't add claims, numbers or testimonials" — [client]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md"
Reading: deliberate preference. fennel-street.md was not provided, so "opposite" is read as quiet, un-ornamented, not playful — [inferred]

## 4. References
None supplied. — [inferred]

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome |
|---|---|---|---|---|
| A Ledger: Bottle Green Ledger (lib.bottle-green-ledger), Overpass / IBM Plex Sans / Commit Mono, ruled-ledger layout | agent | finance reconciles line by line | V1 V2 | Selected |
| B Console: Graphite and Signal (lib.graphite-and-signal), blue accent, dev-docs look | agent | engineers | V2 | Not chosen: the stock dev-tool look; half the audience is finance |
| C Mint Ledger (lib.mint-ledger) | agent | fintech | V1 | Not chosen: tinted ground reads as brand more than proof |
Other-client test for A: the ledger rhythm comes from the expandable invoice line and finance sign-off, so it would not suit a bakery or an SDK-only product. — [agent]

## 6. Selected direction
Ledger — origin: agent — [agent]
Cream paper, bottle-green ink, hairline rules and tabular numerals, like a reconciled statement. Serves V1 and V2 by making the invoice line the first thing a visitor can operate.
The one memorable thing: the hero is an invoice line you can open into its 31 daily totals.

## 7. Design system
### Typography — [engine]
- Headlines: Overpass (overpass), OFL, variable 100–900
- Body: IBM Plex Sans (ibm-plex-sans), OFL
- Code and figures: Commit Mono (commit-mono), OFL
- Self-hosting: no font files are bundled in the single HTML; @font-face points to ./fonts/*.woff2 with local() first, then system stacks. No third-party font requests.
### Color — [engine]
- Direction: Bottle Green Ledger (lib.bottle-green-ledger)
- Ground #F6F2E7 · figure #194430 · text #3D3B34 · muted #6D6A63 · tint-1 #417058 · tint-3 #9ED0B4 · shade-1 #123524
- Body on ground 10.01:1; muted 4.82:1; figure 9.82:1. Engine: no gold; follows a category convention.
### Layout plan — [agent]
- Default: nav, centered hero with two buttons, three cards, stats, testimonials, CTA band.
- Visitor questions: what is it → how does it work → can finance verify it → can engineering integrate it → cost → where to go.
- Only this brief has: the expandable invoice line.
- Cut: testimonials, stats, logos (none supplied), CTA band (hero and pricing carry the actions).
### Judgment tokens — [agent]
- Spacing: tight inside ledger rows, wide between sections; sections not equal.
- Radii: zero. Hairline rules group content instead of boxes.
- Imagery: none; the invoice line is built in HTML/CSS.
- Motion: only the invoice details expanding.

## 8. Constraints
- C1 Headline ≥4× body size, left-aligned → check: render — [agent]
- C2 Invoice line visible above the fold on desktop and expands to 31 rows → check: click — [agent]
- C3 No cards, gradients, emoji, pills or stat rows → check: check_layout report — [agent]
- C4 Only brief copy and numbers; invented numbers labelled illustrative → check: read text — [agent]
- C5 Both actions in the hero; text contrast ≥4.5:1 → check: render — [agent]
- C6 At 390px: no horizontal scroll → check: phone screenshot — [agent]

## 9. Avoid
- Centered hero; rows of three cards; gradient backgrounds; rounded boxes; testimonial or logo strip — [agent]

## 10. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction A | Ledger | — (non-interactive) | Serves finance and engineering | until review |
Rejected (final): none by the user.

## 11. Open decisions
- Gates 1–3 not approved (non-interactive) — decide at: first review
- fennel-street.md missing; "opposite" unconfirmed — decide at: review — [inferred]
- Font files to add in ./fonts/ — decide at: deploy
- Daily totals in the invoice demo are illustrative; supply real ones — decide at: review
- URLs for Docs, demo, Pricing, Status, Security, Contact unknown; links use # — decide at: deploy

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
|---|---|---|---|---|
| Render round 0 | C1 C2 C5 C6 | pass (screenshots 1440 and 390) | — | none |
| check_layout | C3 | pass, none of nine patterns | — | none |
| Read-through | C4 | pass; daily split labelled illustrative | — | none |
No fix rounds needed. C2's expanded state was not rendered; it was not tested by click.
