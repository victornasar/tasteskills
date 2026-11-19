# Creative direction: format

`/taste` writes this document into the user's project as `DIRECTION.md`. Implementation follows it, and
screenshot review tests it. It is the only creative state that survives between sessions, so anything not
written here has not been decided.

One page. If a section grows past its limit, the direction is not settled yet: move items to **Open decisions**.

## Principles

1. **User values are authoritative.** The agent can question how a value is read, but cannot replace it.
2. **Aesthetic vocabulary can be expanded.** The user's words for a look are a guess, not a spec.
3. **Agent ideas must be grounded.** An agent-originated direction names the product fact it comes from and
   passes the other-client test. Being new is not a reason.
4. **Rejection is final.** A rejected direction is logged with its reason and never re-offered in other words.
5. **The render decides.** A direction succeeds when the screenshot passes its constraints, not when it sounds
   good.
6. **Provenance is explicit.** Every material claim carries a tag. Inferences never silently become client
   requirements.

## Provenance tags

Every line that states a fact or a choice ends with one of:

| Tag | Meaning |
| --- | --- |
| `client` | The user said it |
| `inferred` | The agent's reading; not yet confirmed |
| `engine` | A sibling skill's script returned it |
| `agent` | The agent's recommendation (judgment, not script output) |
| `approved` | The user signed off |

Write the tag in square brackets at the end of the line, for example: `Audience: parents choosing care — [client]`.

## Who may change what

| Section | Owner | Changes when |
| --- | --- | --- |
| Values | User | The user says so. The agent never edits them on its own reading |
| Positioning | Client facts: user. Conventions and Adopt/Challenge/Avoid: agent's reading | The user corrects a fact or a reading; the agent never upgrades an inference to a fact |
| Opening vocabulary, References | User's words, agent's reading | The user corrects the reading |
| Directions, Selected | Shared | A grilling round ends with the user choosing |
| Design system (engine rows) | Engine + approval | Only by re-running the engine, then user approval |
| Design system (judgment rows) | Agent + approval | User approves; diversity rule applies |
| Constraints, Avoid | Shared | A checkpoint finds a *lesson* and the user approves the change |
| Overrides, Rejected | Log only | Append only, never edit |
| Open decisions | Shared | Resolved by the user, or by the checkpoint named next to it |

---

## Template

```markdown
# Creative direction: <product>
Status: draft | agreed <date> · Mode: guided | fast · v<n>

## 1. Context
- Product: <one line, what it does> — [<tag>]
- Audience: <who decides, who uses> — [<tag>]
- The page must: <the one job: what a visitor should do or believe on leaving> — [<tag>]

## 2. Values (user-owned, 2–5)
- V1 <value> — "<the user's words it came from>" — [client | inferred]

## 3. Positioning
- Category: <what a buyer would file this under, in their words> — [<tag>]
- Alternatives: <2–3 real alternatives the audience would otherwise choose, named when the brief or user names
  them, otherwise described by kind> — [<tag>]
- Conventions (3–5, each observable in competitors' screenshots):
  | Convention | Adopt / Challenge / Avoid | Why (value, audience or perception) |
- Intended perception: three qualities a stranger reports after five seconds on the page, each checkable on a
  screenshot — [<tag>]
  - P1 <quality> → check: <what in the render shows it>
- Sophistication: everyday | considered | premium | luxury — <the price or audience signal it rests on> — [<tag>]
- Differentiate on: <the one thing this page communicates that the alternatives don't> — [<tag>]

## 4. Opening vocabulary
"<the user's first description, verbatim>"
Reading: hypothesis | deliberate preference — <evidence for the reading> — [agent]

## 5. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
Items in "Just interesting" are never built in.

## 6. Directions explored (2–4)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
Each direction names its font pair and color direction as engine results (ids or names copied from the
scripts), plus its positions on the six visual axes (`references/visual-direction.md`). Combining engines and
axes into a direction is [agent].

| Axis | <Direction A> | <Direction B> | <Direction C> |
| --- | --- | --- | --- |
| Composition | <position> — because <P/V/convention> | | |
| Scale | | | |
| Imagery | | | |
| Signature device | | | |
| Colour proportion | | | |
| Surface | | | |
| House-style markers (H1–H6) | <count: which> | | |
| Distinct on | <axes where it differs from the others; at least 3> | | |

Agent-originated rows also answer: Other-client test: <could this belong to another client? why not?>

## 7. Selected direction
<name> — origin: <user / reference / agent> — [approved | agent]
<2–3 sentences: what it is, which values and perception qualities it serves>
The one memorable thing: <one sentence>
House style: <marker count>; if 4 or more, `House style kept because <reason>` — [agent]

## 8. Design system
### Typography — [engine]
- Headlines: <family from find-font> (<id>) …
- Body: <family from find-font> (<id>) …
### Color — [engine]
- Direction: <name from find-color> (<id>) …
- Ground / figure / accent: <values copied from the script>
### Layout plan — [agent]
- <the four planning points from check-layout step 1, briefly>
- The six axis positions of the selected direction, one line each
### Imagery plan — [agent]
- Job: <what imagery must make a visitor believe> — serves P<n>
- Kind: <photography / illustration / product interface / type as image / pattern or map / data / none + why>
- Shot list: <2–5 subjects with framing, light or treatment, and placement>
- Treatment: <crop, colour treatment from engine colours, how images meet the grid>
- Ships now: <the real visuals the page carries without client assets; no empty frames>
### Judgment tokens — [agent]
- Spacing, radii, imagery, motion: few decisions, each tied to a value or product fact.
  Do not ship a fixed scale that would look the same on every brief.

## 9. Constraints (4–8, each pass/fail on a screenshot)
- C1 <constraint> → check: <what a reviewer looks for in the render> — [approved | agent]

## 10. Avoid (≤6, each observable)
- <thing a reviewer could point at in a screenshot> — [approved | agent | client]

## 11. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
Settled = yes: implementation follows it and never reopens it unasked. Settled = until <checkpoint>: revisit then.
Rejected (final): <direction or idea> — <reason>

## 12. Open decisions
- <decision> — decide at: <checkpoint or round> — [<tag for current best guess, if any>]

## 13. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
Bug: the code missed the direction → fix the code. Lesson: the direction looked wrong rendered → reopen with
the user; don't edit constraints silently.
```

## Writing rules

- **Constraints must be checkable.** "Elegant" fails. "Headlines are at least 4× body size; nothing else on
  the page competes in size" passes. If two reviewers could disagree on pass/fail, rewrite it.
- **Avoid items name things, not moods.** "Gradient mesh backgrounds" passes; "anything generic" fails.
- **Open decisions stay open.** The agent does not fill them in by implementing a choice. It implements a
  placeholder, or asks at the named checkpoint.
- **Fast mode** fills Context, Values, Positioning, one Selected direction with its alternatives and their
  axis positions in Directions, the Design system with its Imagery plan, 4 constraints and Avoid. At least one
  constraint checks a perception quality from Positioning. Gaps that a complete brief would have answered stay `inferred` or
  move to Open decisions with a checkpoint. Everything else goes to Open decisions.
- **A brief that only sounds complete** still leaves gaps. If audience, page objective or business values are
  missing, record them as `inferred` or Open decisions — do not quietly treat guesses as `client`.
- **Positioning is a reading, not research.** Conventions and alternatives come from what the brief says and
  what the category commonly does; tag them `inferred` or `agent`. Never present a guessed competitor as a fact
  the client gave.
- **Directions differ on at least three axes** and trace each position to Positioning or Values. Count
  house-style markers for each; see `references/visual-direction.md`.
- **The diversity rule covers agent ideas too.** Across unrelated products, agent-originated directions should
  differ. Repeating the same "distinctive" move on every project is the agent's own default.
- **Never invent engine output.** Font families, color values and contrast ratios appear only when a sibling
  script returned them, tagged `[engine]`. If a sibling skill is missing, say so and leave that row open.
