# Creative direction: Tallyroll
Status: draft (not approved; non-interactive fast run) · Mode: fast · v1

## 1. Context
- Product: usage-based billing API that turns raw usage events into invoices — [client]
- Audience: engineering leads at software companies with usage-based pricing (integrate it), and the finance leads who sign off and reconcile line items monthly — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to book a demo — [client]

## 2. Values (user-owned, 2–5)
- V1 Traceability: every number can be followed back to its source — "Every cent traces back to an event" — [client]
- V2 Show, don't sell: the buyer sees the mechanism, not adjectives — "They distrust marketing and want to see how it works" — [client]
- V3 Calm precision — "Register: technical, calm, precise" — [client]
- V4 Two readers on one page, engineering and finance, given equal standing — derived from audience + "For finance / For engineering" copy — [inferred]

## 3. Opening vocabulary
"technical, calm, precise. The opposite of fennel-street.md."
Reading: deliberate preference. The register is stated outright, and the brief contrasts it with another brief that was not supplied to this run — [agent]

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
|---|---|---|---|---|
| fennel-street.md (file not provided) | — | — | Whatever it is: the brief calls this page its opposite — [client] | — |

## 5. Directions explored (2–4)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
|---|---|---|---|---|---|
| A. Ledger document: IBM Plex Serif (ibm-plex-serif) headlines + IBM Plex Sans (ibm-plex-sans) body + Commit Mono (commit-mono) figures; Graphite and Signal (lib.graphite-and-signal); the page reads like an annotated invoice, built around the expanding line | agent | The invoice line is the product's proof | V1, V2, V3 | Selected [agent] | n/a, non-interactive |
| B. Engine top pair: Technor (technor) + IBM Plex Serif; Graphite and Signal; spec-sheet grid | engine pair | "technical" feel | V3 partly | Not selected [agent] | Technor's note reads "sci-fi and industrial", which is louder than "calm" |
| C. Plex family + Bottle Green Ledger (lib.bottle-green-ledger); a print-statement look | agent | Finance reconciliation | V1, V4 | Not selected [agent] | The engine's chooseIf targets "an established financial firm". Tallyroll is an API product, and engineers are half the audience |

Other-client test (A): another billing product could use these fonts and colors. It could not use the page's structure, which is a single invoice line that expands into 31 daily totals with the method shown beside it. — [agent]

## 6. Selected direction
A. Ledger document — origin: agent — [agent]
The page is laid out as a working document. A left-aligned serif headline sits beside one real invoice line, and that line opens into the daily totals behind it. Everything after that is reference material for the two readers, set as rules and lists rather than marketing blocks. This serves V1 and V2 directly and keeps V3 through a quiet, single-ink palette.
The one memorable thing: in the first screen you can click the $481.76 line and see the 31 days that add up to it.

## 7. Design system
### Typography — [engine]
- Headlines: IBM Plex Serif (ibm-plex-serif), OFL, weights 100–700, italics. Engine body pick #1; its uses include headlines — [engine]. Chosen for headlines over the engine's top headline pick, Technor, because Technor's note ("sci-fi and industrial") doesn't fit "calm" — [agent]
- Body / UI: IBM Plex Sans (ibm-plex-sans), OFL, weights 100–700 — [engine]
- Figures and code: Commit Mono (commit-mono), OFL, weights 200–700 — [engine]
- Loading: Fontsource files via cdn.jsdelivr.net, because this run could not download the files to self-host them — [agent] (see Open decisions)
### Color — [engine]
- Direction: Graphite and Signal (lib.graphite-and-signal), Light, Neutral — [engine]
- Ground Paper White #F9FAFB / oklch(0.985 0.002 250); Figure Graphite #15181E / oklch(0.21 0.012 260); Accent Signal Blue #0E6EE6 / oklch(0.56 0.2 258) — [engine]
- Text #3C3F46 (10.09:1), muted #6B6F76 (4.82:1), tints #44484F / #797E85 / #B2B8C0 — [engine]
- Roles: primary button is a Graphite fill with a Paper White label (17.01:1). Signal Blue is only for links and focus, never decoration — [engine]
### Layout plan — [agent]
- Default I'd reach for: nav, centered hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor questions, in order: What is it? → Show me a number traced to its source → How do I integrate it? → Does it fit finance and engineering? → What does it cost? → Where do I go next?
- Only this brief has: the invoice line that expands into its 31 daily totals. It leads the page, beside the headline.
- Cut: stats row (no numbers supplied), testimonials (none supplied), feature cards (replaced by a numbered sequence and a two-column spec list), CTA band (the actions come again under pricing).
### Judgment tokens — [agent]
- Spacing: tight inside a group (4–12px), wide between questions (96–144px). The section rhythm changes at the reference half of the page — V3
- Radii: 2px, and only on the invoice and buttons. Everything else is grouped with hairline rules — V3
- Imagery: none. The invoice built in HTML is the only picture — V2
- Motion: none beyond the native disclosure. Nothing animates on scroll — V3
- Numerals: tabular, monospaced, right-aligned in columns — V1

## 8. Constraints (each pass/fail on a screenshot)
- C1 The invoice line text "API calls, March: 1,204,388 calls × $0.0004 = $481.76" is visible in the first 1440×900 viewport and expands to 31 dated rows → check: desktop first-screen shot plus an expanded shot — [agent]
- C2 Signal Blue appears only on links and focus rings. The primary button is Graphite → check: no blue fills or blue decoration — [agent]
- C3 Only the invoice is drawn as a bordered or filled box (buttons excepted). Other groups use rules and spacing → check: count the boxed elements — [agent]
- C4 Every figure, amount and code token is set in the mono with tabular numerals, and the page has no claims or numbers beyond the brief except the labelled example daily totals → check: read the copy — [agent]
- C5 At 390px wide there is no horizontal scroll, and the invoice line stays readable without clipping → check: phone shot — [agent]
- C6 The headline is left-aligned on a strong edge, not centered → check: first screen — [agent]

## 9. Avoid
- Pill badge above the headline — [agent]
- Emoji or icon glyphs beside features — [agent]
- Gradient backgrounds or glows — [agent]
- Row of big statistic numbers — [agent]
- Row of three equal cards — [agent]
- Testimonials or logos (none supplied) — [client]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
|---|---|---|---|---|
| Direction | A. Ledger document | — (non-interactive) | Leads with the product's proof and serves V1/V2 | until Gate 3 review |
| Headline font | IBM Plex Serif over Technor | — | Technor reads sci-fi, not calm | until Gate 3 review |
| Color | Engine pick Graphite and Signal | — | Its chooseIf ("data and actions must stand out from a quiet UI") fits an invoice-led page | until Gate 3 review |

## 11. Open decisions
- Gate 1/2/3 approvals were not given; Values V4 and the direction are unconfirmed — decide at: first client review — [inferred]
- Self-host the fonts (find-font rule) instead of loading them from jsdelivr — decide at: before production — [agent]
- Dark theme: the color engine returned light tokens only, so no dark values were invented — decide at: re-run find-color with --foundation dark if needed
- The daily totals are illustrative example data that sum to 1,204,388. Replace them with real example data from the product — decide at: content review — [inferred]
- Link targets for Docs, Pricing, Status, Security, Contact and Book a demo are placeholders (#) — decide at: content review
- fennel-street.md was not supplied, so the "opposite" contrast is unchecked — decide at: first client review

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
|---|---|---|---|---|
| Render 1 (1440 / 390) | C1 | pass, though the line was collapsed and the trace hidden | bug | Opened the disclosure by default; rows tightened |
| Render 1 | C2, C3, C4, C5, C6 | pass | — | — |
| Render 1 | check-layout: uniform spacing (3 of 4 sections) | flagged | bug | Pricing given a wider gap and heavier top padding |
| Render 1 | Subhead widow ("line.") | — | bug | Measure widened to 34ch |
| Render 2 | C1–C6; check-layout | all pass; 0 of 9 patterns | — | Headline column made sticky beside the long invoice (desktop only). Stopped at the two-round cap |
