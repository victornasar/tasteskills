# Creative direction: Tallyroll
Status: draft (non-interactive fast run; not approved by the user) · Mode: fast · v1

## 1. Context
- Product: Usage-based billing API. Turns raw usage events into invoices. — [client]
- Audience: Engineering leads at software companies with usage-based pricing, and the finance leads who sign off with them. They distrust marketing and want to see how it works. — [client]
- The page must: make a careful buyer trust Tallyroll with their revenue, then send them to the docs or to book a demo. — [client]
- Register: technical, calm, precise. The opposite of fennel-street.md. — [client]
  - Note: fennel-street.md is not present in this project, so the contrast was taken from the brief's wording only. — [inferred]

## 2. Values (user-owned, 2–5)
- V1 Traceability: every number on an invoice opens to the events behind it — "Every cent traces back to an event." — [client]
- V2 Reconcilability: finance can check each line — "reconcile line by line." — [client]
- V3 Plainness: state what it does and how, no marketing claims — "They distrust marketing and want to see how it works." — [client]

## 3. Opening vocabulary
"Every cent traces back to an event."
Reading: deliberate preference — the page proves the headline with a real-looking invoice line, not with adjectives. — [agent]

## 4. References (0–5)
None supplied. The brief's register reference (fennel-street.md) is not available in the project. — [inferred]

## 5. Directions explored (2–4)
| Direction | Origin | Grounded in | Serves | Outcome | User's reason |
| --- | --- | --- | --- | --- | --- |
| A. Ledger Plain (selected) | agent | Invoice line as the page's one artifact; graphite-on-paper color from find-color; Technor + IBM Plex Serif from find-font | V1, V2, V3 | Selected by agent | Non-interactive run; best serves the page job |
| B. Dark terminal | agent | Dev-tool convention | V3 | Not built | Dark ground excluded by the brief's trust-with-finance framing and by find-color's light foundation filter |
| C. Editorial long-read | agent | Brief's "how it works" framing | V3 | Not built | Adds length without answering the buyer's questions |

Engine picks for A: Technor (headlines, id `technor`), IBM Plex Serif (body, id `ibm-plex-serif`), Graphite and Signal (color, id `lib.graphite-and-signal`). Combining these into one direction is [agent].

Other-client test (A): could this belong to another client? Possibly, since the color direction is a common product palette. What makes it Tallyroll is the expandable invoice line and the arithmetic shown in full. — [agent]

## 6. Selected direction
Ledger Plain — origin: agent — [agent]
A white ledger page, graphite type, one blue reserved for links and focus. The page is a document a finance team would read, not a campaign. The first screen shows an invoice line that can be opened.
The one memorable thing: the invoice line expands into its 31 daily totals on the page itself.

## 7. Design system
### Typography — [engine]
- Headlines: Technor (`technor`), FFL, Fontshare. Self-hosted from `./fonts/Technor.woff2`. Weights 200–900 variable. Self-host only; keep font files out of public repos. — [engine]
- Body: IBM Plex Serif (`ibm-plex-serif`), OFL, GitHub. Self-hosted from `./fonts/IBMPlexSerif.woff2`. Weights 100–700 variable. — [engine]
- Fallback stacks: `system-ui` for headlines, `Georgia` for body. — [engine]
- Monospace for the endpoint and figures: system stack `ui-monospace, SFMono-Regular, Menlo, monospace`. No catalog font was requested for a code role. — [agent]
- Notes: a code font (for example from find-font's `code` role) is an obvious next role for a developer-facing page. Not requested in this run. — [agent]

### Color — [engine]
- Direction: Graphite and Signal (`lib.graphite-and-signal`), Light foundation, Neutral structure.
- Ground: Paper White `#F9FAFB` · oklch(0.985 0.002 250)
- Figure: Graphite `#15181E` · oklch(0.21 0.012 260)
- Accent: Signal Blue `#0E6EE6` · oklch(0.56 0.2 258), for links and focus only.
- Text: `#3C3F46` (10.09:1 on ground). Text-muted: `#6B6F76` (4.82:1 on ground). Figure on ground: 17.01:1. Accent on ground: 4.57:1.
- Area: 86/11/3 (ground / figure / accent). — [engine]

### Layout plan — [agent]
- The default section list: nav, centred hero with two buttons, three feature cards, stats row, testimonials, CTA band, footer.
- Visitor's questions, in order: (1) What does it do to my usage? (2) How does a line become a number I can check? (3) What does finance get? What does engineering get? (4) What does it cost, and how do I start?
- The one thing only this brief has: the invoice line that expands into its daily totals. It leads the page as content, not decoration.
- Cut: testimonials and stats rows (no supplied content). Three-card row replaced by two audience columns and a numbered sequence.
- Order: left-aligned headline and subhead with actions → live invoice line → how it works (3 steps) → for finance / for engineering → pricing → closing actions → footer.

### Judgment tokens — [agent]
- Spacing: 4px base. Section rhythm varies by content: tight in lists, wider between the hero and the ledger, wider before pricing. Not a fixed scale.
- Radius: 2px on the invoice line and code only. No rounded cards.
- Borders: 1px rules in tint-3 carry structure. No shadows.
- Imagery: none. The invoice line is the picture, built in HTML and CSS.
- Motion: one expand/collapse on the invoice line, 150ms. Disabled under `prefers-reduced-motion`.

## 8. Constraints (4–8, each pass/fail on a screenshot)
- C1 Headline is left-aligned and shares its left edge with the subhead and the action pair; the hero is not centred. → check: left edges align on desktop and phone. — [agent]
- C2 The example invoice line (description, calculation, amount) is visible without scrolling on a 1280×800 desktop and a 390px phone, with no horizontal scroll. → check: first screen shows the line in full. — [agent]
- C3 The accent colour appears only on links and focus rings. → check: no blue fills, text, rules or decoration outside links and focus. — [agent]
- C4 On desktop the H1 is at least 4× body size, and no other text is larger than 2× body size. → check: measured computed font sizes. — [agent]
- C5 No gradients, shadows, emoji, pill badges, or rounded cards. → check: none visible in the screenshot. — [agent]
- C6 The three how-it-works steps appear in order with the brief's copy, and step 1 shows `POST /v1/events`. → check: text matches the brief. — [client]
- C7 Primary action "Read the docs" and secondary action "Book a demo" appear in the hero, with the primary visually stronger. → check: both visible on first screen; primary uses the figure fill. — [client]
- C8 The invoice line arithmetic reads exactly: 1,204,388 calls × $0.0004 = $481.76. → check: text matches; 1,204,388 × 0.0004 = 481.7552, rounds to $481.76. — [client]

## 9. Avoid (≤6, each observable)
- Gradient or mesh backgrounds, anywhere on the page. — [agent]
- A pill badge or "New" label above the headline. — [agent]
- A row of three identical rounded feature cards. — [agent]
- A row of large stat numbers ("10k+ users" style). No stats were supplied. — [agent]
- A purple or indigo button. — [agent]
- Emoji used as icons or bullets. — [agent]

## 10. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
| --- | --- | --- | --- | --- |
| Color direction Graphite and Signal | Graphite and Signal (engine pick) | not confirmed (non-interactive) | Engine's top pick for enterprise-software + finance, light foundation, quiet | until user review |
| Font pair Technor + IBM Plex Serif | engine top pair | not confirmed (non-interactive) | Engine's top pair for technical + neutral | until user review |
| Direction A Ledger Plain | A | not confirmed (non-interactive) | Best serves the page job; B and C rejected above | until user review |

Rejected (final): Dark terminal direction — excluded by the light foundation and trust framing. Editorial long-read — adds length without answering buyer questions.

## 11. Open decisions
- Docs URL and Book-a-demo URL are placeholders (`#docs`, `#demo`). — decide at: user review — [inferred]
- Font files: Technor and IBM Plex Serif must be downloaded into `./fonts/` (see Typography). Until then the fallback stacks render. — decide at: build hand-off — [inferred]
- Whether to add a code font for the endpoint and figures. — decide at: user review — [agent]
- Status, Security, Contact, Pricing targets in the footer are placeholders. — decide at: user review — [inferred]
- Approval of this direction (Gate 2 and Gate 3 were not run interactively). — decide at: user review — [inferred]

## 12. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
| --- | --- | --- | --- | --- |
