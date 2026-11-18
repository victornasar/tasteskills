# Creative direction: Tallyroll
Status: draft (not approved: non-interactive run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (they integrate it), plus the finance leads who sign off with them (they reconcile line items every month) — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]
- Primary action is Read the docs, secondary is Book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability: every number can be followed to its source — "Every cent traces back to an event." — [client]
- V2 Show, don't claim — "They distrust marketing and want to see how it works." — [client]
- V3 Calm precision — "technical, calm, precise" — [client]
- V4 Legible to two readers at once (engineer + finance lead) — from the audience line and the For finance / For engineering split — [inferred]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md."
Reading: deliberate preference, since the register is stated as an instruction and backed by the audience description. fennel-street.md is not in the project, so "the opposite of" can't be read further — [agent]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
|---|---|---|---|---|
| fennel-street.md (anti-reference) | — | — | whatever it is; file not available | — |

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
|---|---|---|---|---|---|
| **A. Ledger in the open**: IBM Plex Serif headlines (ibm-plex-serif) + IBM Plex Sans body (ibm-plex-sans) + Commit Mono for figures (commit-mono); Graphite and Signal (lib.graphite-and-signal); structure: hero is the invoice line itself, expandable into its 31 days | agent | the expandable invoice line in the brief | V1, V2, V3 | selected [agent] | non-interactive |
| B. Instrument panel: Technor headlines (technor) + IBM Plex Serif body (ibm-plex-serif); Graphite and Signal; structure: hero is a code/event stream | agent | the engine's top pair | V2 | not selected: Technor's "sci-fi and industrial" note reads louder than "calm"; putting code first leaves the finance reader out (V4) | — |
| C. Statement paper: IBM Plex Serif + IBM Plex Sans; Mint Ledger (lib.mint-ledger); structure: page reads like a printed statement | agent | finance reconciliation | V3, V4 | not selected: a tinted ground pulls toward fintech branding, and the engine's chooseIf ("wants a recognisable tinted ground") isn't in the brief | — |

Other-client test (A): the hero only works for a product whose invoice lines open up into source events. Another billing tool without line-level traces couldn't use it honestly.

## 6. Selected direction
A. Ledger in the open — origin: agent — [agent]
The page opens on the product's own evidence: one invoice line, set in tabular figures, that the visitor can open to see the 31 daily totals behind it. Typography and alignment do the work, not decoration (V2, V3), and the finance and engineering facts sit side by side as equals (V4).
The one memorable thing: the hero headline's claim is proved one click below it by an invoice line that opens into its 31 days.

## 7. Design system
### Typography — [engine]
- Headlines: IBM Plex Serif (ibm-plex-serif), OFL, weights 100–700, italics. Engine note: "A serif with an engineer's precision; pairs naturally with Plex Sans and Plex Mono." — [engine]
- Body / UI: IBM Plex Sans (ibm-plex-sans), OFL, weights 100–700. — [engine]
- Figures and code: Commit Mono (commit-mono), OFL, weights 200–700. — [engine]
- Role assignment (Plex Serif moved from body to headlines, Plex Sans used for body) — [agent]: Plex Serif lists `headlines` as a use. A sans body reads better at UI sizes in the line-item tables.
- Loading: @fontsource packages from cdn.jsdelivr.net (not Google Fonts) — [agent]. Production should self-host (see Open decisions).
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light / Neutral, area 86/11/3 — [engine]
- Ground Paper White #F9FAFB · Figure Graphite #15181E (17.01:1) · Accent Signal Blue #0E6EE6 — [engine]
- Text #3C3F46 (10.09:1) · Muted #6B6F76 (4.82:1) · Tints #44484F / #797E85 / #B2B8C0 — [engine]
- Code panel (figure as ground): text #BFC3CB (10.05:1), muted #82858D (4.81:1), from `classify` — [engine]
- Signal Blue only for links, focus and the primary action. Never decorative — [engine]
### Layout plan — [agent]
- Default: nav, centered hero with two buttons, three feature cards, stats row, testimonials, finance/eng card pair, three-tier pricing table, CTA band, footer.
- Visitor questions, in order: what is it → show me a number tracing back → how do events get in and become lines → does it fit our finance stack / our engineering stack → what does it cost → where are the docs.
- The thing only this brief has: the invoice line `1,204,388 calls × $0.0004 = $481.76` that expands into 31 daily totals. It leads, as working HTML.
- Cut: stats row, testimonials (none supplied), CTA band, three-tier pricing (pricing is one sentence), feature cards.
### Judgment tokens — [agent]
- Alignment: numbers right-aligned in tabular mono, on the same right edge the invoice uses (V1).
- Separation: hairline rules (#B2B8C0) group things. Only the invoice and the code panel are boxed, because they're objects (V3).
- Radius: 2px on the boxed objects, 0 elsewhere.
- Spacing: tight inside the invoice and lists, wide between sections. The pricing section is tighter because it's one statement.
- Imagery: none. The invoice and the daily-totals bars are the pictures.
- Motion: none beyond the native expand. Respects reduced motion.

## 8. Constraints (each pass/fail on a screenshot)
- C1 The invoice line with its total `$481.76` is visible on the first desktop screen (1440×900) and expands to 31 rows → check: first-screen shot shows the line, full shot shows 31 daily rows — [agent]
- C2 Signal Blue appears only on the primary button, links and focus → check: no blue on headings, rules, bars or backgrounds — [agent]
- C3 All figures are in Commit Mono, tabular and right-aligned in columns → check: invoice digits line up vertically — [agent]
- C4 No claims, numbers or testimonials beyond the brief. Example data is labelled as example → check: read the full shot against the brief copy — [agent]
- C5 Phone (390px): no horizontal scroll, and the invoice line stays readable without cutting digits → check: phone shot — [agent]
- C6 No row of three equal cards and no centered hero → check: check-layout report — [agent]

## 9. Avoid
- Gradients, glows or mesh backgrounds — [agent]
- Pill badges and emoji icons — [agent]
- Stat rows ("10k+ customers") — [agent]
- Testimonials or logos not supplied by the client — [client]
- Blue used as decoration — [engine]

## 10. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction | A. Ledger in the open | — (non-interactive) | Best serves the job: proves the headline in the first screen for both readers | until user review |
| Color | Graphite and Signal (engine pick) | — | Engine pick; its chooseIf ("data and actions must stand out from a quiet UI") matches | until user review |
| Headline font | Plex Serif over engine-top Technor | — | Technor's retro/sci-fi feel conflicts with "calm" | until user review |

## 11. Open decisions
- Approval of this whole spec (Gates 1–3 skipped, non-interactive) — decide at: first user review — [inferred]
- The 31 daily totals are illustrative numbers summing to 1,204,388, labelled "example data". Should they be replaced with real sample data? — decide at: user review — [agent]
- Example pricing rule syntax and event payload: not supplied, so they're left as a labelled placeholder rather than invented API shape — decide at: docs team supplies the real snippet — [agent]
- Self-host fonts instead of jsdelivr (find-font rule) — decide at: production build — [agent]
- Link targets for Docs, Book a demo, Status, Security, Contact — decide at: launch — [inferred]
- What fennel-street.md contains, if it should shape the Avoid list — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
|---|---|---|---|---|
| Round 1 desktop/phone | C1 invoice line + $481.76 in first screen, 31 rows on expand | pass | — | — |
| Round 1 | C2 blue only on actions/links/focus | pass | — | — |
| Round 1 | C3 figures mono, right-aligned | fail: "calls" wrapped under the quantity | bug | widened quantity column, nowrap |
| Round 1 | C3 (reading) | Commit Mono inside the serif pricing sentence looked like a code token | lesson | figures in running prose use Plex tabular figures; C3 is applied to columns only. **Needs user confirmation** |
| Round 1 | C4 no added claims; example data labelled | pass ("Example data", "Example invoice", pricing-rule placeholder) | — | — |
| Round 1 | C5 phone | pass with issues: sum row wrapped mid-equation, 31 rows in one long column | bug | stacked sum; two-column day list |
| Round 1 | C6 / check-layout | phone: uniform section padding flagged | bug | varied padding by content density |
| Round 2 | all | pass; check-layout reports 0 of 9 patterns at 1440 and 390 | — | stopped |
