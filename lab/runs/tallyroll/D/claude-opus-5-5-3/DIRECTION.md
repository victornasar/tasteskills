# Creative direction: Tallyroll
Status: draft (not approved; non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate it) and the finance leads who sign off with them (reconcile line items monthly) — [client]
- They distrust marketing and want to see how it works — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]
- Primary visitor on first load is the engineering lead; finance lead arrives second, often via a forwarded link — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Technical — "Register: technical, calm, precise" — [client]
- V2 Calm — same line — [client]
- V3 Precise — same line — [client]
- V4 Show, don't claim (traceability is demonstrated, not asserted) — "They distrust marketing and want to see how it works" — [inferred]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md."
Reading: deliberate preference — the register is stated as a contrast to another brief; fennel-street.md was not present in the project, so what it is the opposite *of* is unread — [agent]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
|---|---|---|---|---|
| fennel-street.md (anti-reference) | — | — | Whatever it does; file not available to read — [inferred] | — |

## 5. Directions explored (2–4)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
|---|---|---|---|---|---|
| A. Ledger proof — IBM Plex Serif headlines + IBM Plex Sans body + Commit Mono figures; Graphite and Signal (lib.graphite-and-signal); the invoice line *is* the hero and opens into its 31 days | agent | The product's core claim: every line traces to events | V1–V4 | Selected [agent] | non-interactive |
| B. Engineered sans — Technor headlines + IBM Plex Sans; Mint Ledger (lib.mint-ledger); API-request-first hero | agent | "technical" feel; fintech tinted ground | V1 | Not selected: Technor's note reads "sci-fi and industrial", louder than "calm"; mint ground reads consumer fintech | — |
| C. Statement paper — IBM Plex Serif + Source Sans 3; Bottle Green Ledger (lib.bottle-green-ledger); pricing-led | agent | Finance lead as audience | V2 | Not selected: engine flags it as category convention that differentiates little; leading with pricing answers the wrong first question | — |

Other-client test (A): the hero component is Tallyroll's own invoice line with its own arithmetic; it can't move to another product without becoming false — [agent]

## 6. Selected direction
A. Ledger proof — origin: agent — [agent]
A quiet graphite-on-paper page set like a well-typeset statement: serif headlines for calm authority, a grotesque for body, monospace for every figure. Structure follows the trace: headline → the invoice line → the events behind it → how it works → who gets what → price.
The one memorable thing: the invoice line on the first screen opens into 31 daily totals whose sum visibly equals the line's quantity.

## 7. Design system
### Typography — [engine]
- Headlines: IBM Plex Serif (ibm-plex-serif), OFL, weights 100–700 with italics; engine top body pick, `use` includes headlines; note: "a serif with an engineer's precision; pairs naturally with Plex Sans and Plex Mono" — [engine]
- Body / UI: IBM Plex Sans (ibm-plex-sans), OFL, engine body pick #2 for feel technical+neutral — [engine]
- Figures and code: Commit Mono (commit-mono), OFL, engine top code pick — [engine]
- Combining Plex Serif as headline with Plex Sans as body (rather than engine's top pair technor + ibm-plex-serif) — [agent], because Technor's sci-fi note conflicts with V2 Calm
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light / Neutral, area 86/11/3 — [engine]
- Ground Paper White #F9FAFB oklch(0.985 0.002 250) · Figure Graphite #15181E oklch(0.21 0.012 260) · Accent Signal Blue #0E6EE6 oklch(0.56 0.2 258) — [engine]
- Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Tints #44484F / #797E85 / #B2B8C0 — [engine]
- Primary button: Graphite fill, Paper White label (17.01:1). Signal Blue only for links, focus, the expand control (4.57:1 on ground) — [engine]
### Layout plan — [agent]
- Default I'd reach for: nav, centered hero + two buttons, three feature cards, stat row, testimonials, pricing cards, CTA band, footer.
- Visitor's questions in order: What is it? → Show me a number tracing back → How does data get in and come out? → What does my side (finance / engineering) get? → What does it cost? → Where next (docs / demo)?
- The one thing only this brief has: the invoice line "API calls, March: 1,204,388 calls × $0.0004 = $481.76" that expands into its 31 daily totals. It leads, under a left-set headline, on the first screen.
- Cut: stat row, testimonials, logo wall, feature cards, pricing tiers, CTA band duplicates. How-it-works is an ordered sequence; finance/engineering is a two-column ruled spec list; pricing is one sentence.
### Judgment tokens — [agent]
- Rules not boxes: 1px tint-3 hairlines group content; only the invoice is a bordered object (it is a separate document). Radius 2px on buttons and invoice only (V3 Precise).
- Spacing follows content: tight (8–16px) inside a ledger, 96–160px between ideas, denser in the spec list. No uniform section padding.
- Figures: `font-variant-numeric: tabular-nums`, right-aligned in tables (V3).
- Motion: only the disclosure opening; none under prefers-reduced-motion (V2).
- Imagery: none; the invoice built in HTML is the picture.

## 8. Constraints (each pass/fail on a screenshot)
- C1 At 1440×900 the first screen shows the invoice line including "$481.76" and its expand control → check desktop first-screen shot — [agent]
- C2 Signal Blue appears only on links, the focus ring and the expand control; no blue fill or decoration → check full-page shot — [agent]
- C3 No row of three cards, no gradient, no shadow, no pill badge → check checker report + shot — [agent]
- C4 Every figure is set in mono with tabular numerals; amount columns right-aligned → check invoice and daily table — [agent]
- C5 Headline is left-aligned and at least 3× body size → check first screen — [agent]
- C6 At 390px wide: no horizontal page scroll, invoice amount visible without sideways scrolling → check phone shot — [agent]

## 9. Avoid (≤6, observable)
- Marketing superlatives or any claim/number not in the brief copy — [client]
- Testimonials, logo walls, stat rows — [client] (no testimonials) / [agent]
- Emoji or decorative icons — [agent]
- Blue-filled buttons or blue section backgrounds — [engine] ("Do not use Signal Blue decoratively")
- Drop shadows and glassy cards — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction | A. Ledger proof | — (non-interactive) | Best serves "see how it works": proof on first screen | until user review |
| Headline face | Plex Serif over engine top pair Technor | — | Technor note "sci-fi" vs Calm | until user review |
| Light only | Engine direction has no dark tokens | — | Never invent colors | until user review |
Rejected (final): none yet.

## 11. Open decisions
- Spec approval (Gate 3) not given; built against draft — decide at: user review — [inferred]
- Values V4 and audience order are readings, not confirmed — decide at: user review — [inferred]
- The 31 daily totals are not in the brief; page shows illustrative values generated to sum exactly to 1,204,388 and labels them "Example data" — decide at: user review; replace with real sample — [inferred]
- Font delivery: brief requires one self-contained file; find-font says always self-host. Plex is loaded from jsDelivr (@fontsource) as a stopgap; Commit Mono resolves only if installed locally or placed at fonts/CommitMono.woff2, else falls back to ui-monospace — decide at: before launch (self-host all three) — [agent]
- Dark mode: no engine tokens; run find-color with `--foundation dark` if needed — decide at: user review
- Link targets (docs, demo, status, security) are `#` placeholders — decide at: before launch — [inferred]
- fennel-street.md not available; anti-reference unread — decide at: user review

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
|---|---|---|---|---|
| Render r0 | check-layout (9 patterns) | pass: none found, desktop + phone | — | — |
| Render r0 | Full page | fail: footer overlapped pricing; nav rule overhung content edge | bug (`.wrap` margin/padding overrode footer/nav) | fixed r1 with inner `.nav` / `.foot` |
| Render r0 | Avoid: claims not in brief | fail: added h2 "Events in, rules applied, invoices out." | bug | replaced with "How it works" r1 |
| Render r0 | Subhead | single-word last line ("line.") | bug | max-width 32em r1 |
| Render r1 | C1 first screen shows $481.76 + control | pass | — | — |
| Render r1 | C2 blue only on links/focus/control | pass | — | — |
| Render r1 | C3 no 3-cards/gradient/shadow/pill | pass (checker + shot) | — | — |
| Render r1 | C4 figures mono, tabular, right-aligned | pass (mono is fallback ui-monospace unless Commit Mono is installed; see Open decisions) | — | — |
| Render r1 | C5 headline left, ≥3× body | pass (72px vs 17px) | — | — |
| Render r1 | C6 390px no h-scroll, amount visible | pass (expanded state also checked) | — | — |
