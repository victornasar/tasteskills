# Creative direction: three worked examples

Same product, same opening line, three different clients. Each example shows the hidden brief the simulated
client holds, the document taste-grilling should end with, and what a grader checks.

**Product (fictional):** Tallyroll, a usage-based billing API. It turns raw usage events into invoices. Engineers
integrate it; finance teams reconcile its line items every month.

**Opening line, all three:** "I want a minimal, premium SaaS website. Something clean and professional."

---

## Persona A: strong preference (preserve)

**Hidden brief.** Loves restrained product design. References are three product-led SaaS homepages with real
UI and quiet type. Asked why, gives specific reasons ("the product screenshot does the selling"). Values:
credible to engineers, calm, fast to understand.

**Grader checks.** The agent shows at least one stretch direction. It accepts the user's choice after one
explanation, without re-offering the stretch. The selected direction's origin is `user`. Constraints are
specific to minimal product design, not a weakened editorial direction.

```markdown
# Creative direction: Tallyroll
Status: agreed · Mode: guided · v1

## 1. Context
- Product: API that turns usage events into invoices
- Audience: engineering leads decide; engineers integrate
- The page must: show the product working within one scroll

## 2. Values
- V1 Credible to engineers — "they smell marketing instantly"
- V2 Calm — "no shouting, no countdown timers"
- V3 Fast to understand — "the screenshot does the selling"

## 3. Opening vocabulary
"Minimal, premium SaaS. Clean and professional."
Reading: deliberate preference — references agree with each other; gave specific reasons; picked it again
after seeing two alternatives.

## 4. References
| Reference | Admire | Borrow | Avoid | Just interesting |
| Product-led SaaS home 1 | real UI as hero | UI-first hero | — | — |
| Product-led SaaS home 2 | quiet type | type restraint | marketing illustrations | — |
| Product-led SaaS home 3 | short page | page length | — | dark mode toggle |

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| Minimal product | user | user's references | V1 V2 V3 | selected | "this is what we are" |
| Editorial | agent | — (vocabulary stretch) | V1 V2 | rejected | "reads like a blog; buyers want the product" |

## 6. Selected direction
Minimal product — origin: user
The product UI carries the page; type and color stay quiet around it.
The one memorable thing: the hero shows an invoice line building from raw events, live.

## 7. Constraints
- C1 The real product UI appears above the fold → check: hero contains UI, not illustration
- C2 One typeface, at most 4 sizes → check: count sizes in the DOM
- C3 One accent color, used only for primary actions → check: accent appears on nothing but buttons and links
- C4 Page is at most 5 sections → check: count sections

## 8. Avoid
- Illustrations of people or abstract shapes
- Gradient backgrounds
- Logo walls above the fold

## 9. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction | showed Editorial as a stretch | Minimal product | buyers want to see the product | yes |
Rejected (final): Editorial — "reads like a blog"

## 10. Open decisions
- Typeface — decide at: round 3, from find-font with feel `technical`
- Dark or light hero — decide at: first render

## 11. Checkpoints
(empty until first render)
```

---

## Persona B: limited vocabulary (discover)

**Hidden brief.** Says "minimal SaaS" because it's the only design language they can name. References are
a long-form magazine, a type foundry and one SaaS homepage. What they value is confidence and considered
ordering, not a magazine look, which they reject outright. Full client sheet and grading:
[persona-b.md](persona-b.md).

**Grader checks.** See persona-b.md: discovery quality (truths T1–T6) and discovery integrity (codes
I1–I6) are scored separately. The selected direction is named by the client's qualities, not by a style label
the agent brought in.

```markdown
# Creative direction: Tallyroll
Status: agreed · Mode: guided · v1

## 1. Context
- Product: API that turns usage events into invoices
- Audience: engineering leads and finance leads, together
- The page must: make a careful buyer trust the product with their revenue

## 2. Values
- V1 Credible — "it touches people's revenue"
- V2 Calm — "not salesy"
- V3 Considered — "you can tell someone cared"

## 3. Opening vocabulary
"Minimal, premium SaaS. Clean and professional."
Reading: hypothesis — "minimal" means "nothing careless or there for show", not "little on the page"; the
SaaS reference was inherited ("our competitors look like that"); the magazine and foundry carry what they
actually respond to.

## 4. References
| Reference | Admire | Borrow | Avoid | Just interesting |
| Long-form magazine | "says the important thing big"; dense index page that "never feels messy" | confidence, ordered density | article columns, bylines, "it's not a blog" | — |
| Type foundry | "everything placed on purpose" | deliberate placement | — | variable-font sliders |
| SaaS homepage | "it looks expensive" (inherited) | — | feature card grid | — |

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| Minimal product | user | opening line | V1 V2 | kept as fallback | "fine, but it's everyone" |
| Confident and ordered | reference | magazine's confidence + index page; foundry's placement | V1 V2 V3 | selected | "that's the feeling" |
| Architectural | agent | — (vocabulary stretch) | V2 V3 | rejected | "no photography to lead with" |

## 6. Selected direction
Confident and ordered — origin: reference
Each section states its one important thing plainly and large; detail sits below it, dense but strictly
ordered. Nothing is there for show.
The one memorable thing: the promise stated in one large sentence, with no supporting graphic.

## 7. Constraints
- C1 Each section leads with one statement, the largest text in that section → check: one dominant line per section
- C2 Statements at least 4× body size → check: computed sizes
- C3 At least one dense section (pricing, event table or API reference) on the same grid as the rest → check: column edges line up across sections
- C4 No card grid of features → check: features are rows or a list
- C5 Every element has a job: no decorative graphics → check: each image or graphic shows product or data
- C6 One accent, used for links and actions only → check: accent usage

## 8. Avoid
- Magazine furniture: article columns, bylines, drop caps
- Three-card feature grid
- Decorative icons beside features
- Rounded containers around every block
- Stock photography

## 9. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction | Confident and ordered, from the reference qualities | Confident and ordered | "that's the feeling" | yes |
| Navigation | minimal nav | conventional top nav with Pricing, Docs | buyers look for Pricing first | yes |
Rejected (final): Architectural — no photography to lead with. Magazine look — "it's not a blog" (client's own exclusion)

## 10. Open decisions
- Statement typeface — decide at: round 3, from find-font, role `headlines`; feel from the client's words (confident, considered), not a label
- How product UI is framed — decide at: first render

## 11. Checkpoints
(empty until first render)
```

---

## Persona C: agent-originated opportunity (expand)

**Hidden brief.** Clear values, no references, no visual ideas beyond "minimal". Groundable facts the agent
can find only by asking: finance teams reconcile Tallyroll invoices line by line, and the founder's pitch is
"every cent traces back to an event". Values: credible, transparent, calm.

**Grader checks.** The agent proposes exactly one direction of its own. That direction cites a product fact
learned in the conversation (the reconciliation, or "every cent traces back"). Its other-client test is
answered honestly. It's shown visually. If rejected, it doesn't come back.

```markdown
# Creative direction: Tallyroll
Status: agreed · Mode: guided · v1

## 1. Context
- Product: API that turns usage events into invoices
- Audience: engineering leads decide; finance teams live with the output
- The page must: prove every number on an invoice can be traced

## 2. Values
- V1 Credible — "it's people's revenue"
- V2 Transparent — "every cent traces back to an event"
- V3 Calm — "boring in the good way"

## 3. Opening vocabulary
"Minimal, premium SaaS. Clean and professional."
Reading: hypothesis — no references; "minimal" meant "not cluttered", not a specific look.

## 4. References
(none given)

## 5. Directions explored
| Direction | Origin | Grounded in | Serves | Outcome | Reason |
| Minimal product | user | opening line | V1 V3 | rejected | "doesn't say anything about tracing" |
| The ledger | agent | finance reconciles line by line; "every cent traces back" | V1 V2 V3 | selected | "that's literally our pitch" |
Other-client test (The ledger): partly transferable — any fintech can borrow ledger styling. What makes it
Tallyroll's is the trace: the page shows one invoice line expanding into the events that produced it.
Ledger styling without the trace would fail this test.

## 6. Selected direction
The ledger — origin: agent
The page is set like a financial statement: ruled lines, aligned tabular figures, numbers as the hero.
The one memorable thing: the hero is one invoice line that expands into its raw usage events.

## 7. Constraints
- C1 Numbers are the hero → check: the largest element above the fold is a figure, not a headline
- C2 All figures use tabular numerals, right-aligned in columns → check: font-variant-numeric and alignment
- C3 Structure comes from ruled lines, not boxes → check: no rounded containers; dividers are 1px rules
- C4 The hero trace works without JavaScript showing the final state → check: render with JS off
- C5 Color is near-monochrome; one accent marks the traced path only → check: accent usage

## 8. Avoid
- Charts used as decoration
- Green-and-red finance clichés
- Dashboard mockups at an angle
- Coins, wallets, money icons

## 9. Decisions log
| Decision | Agent recommended | User chose | Reason | Settled |
| Direction | The ledger | The ledger | "that's literally our pitch" | until first render |
Rejected (final): Minimal product — "doesn't say anything about tracing"

## 10. Open decisions
- Body and figure typeface — decide at: round 3, find-font roles `body` + `code` (for figures), feel `technical`
- Whether the trace animates — decide at: first render

## 11. Checkpoints
(empty until first render)
```

---

## What the three together test

- **Same words, different intent.** A and B open identically. An agent that ends both in the same place
  isn't reading the client.
- **Origin spread.** Selected origins are `user`, `reference` and `agent`. An agent whose directions win as
  `agent` for all three personas is persuading, not offering.
- **Constraint spread.** The three constraint lists barely overlap. That's the repo's diversity rule applied
  to directions.
