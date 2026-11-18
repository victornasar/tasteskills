# Creative direction: format

taste-grilling writes this document, implementation follows it, and screenshot review tests it. It's the only
creative state that survives between sessions, so anything not written here hasn't been decided.

One page. If a section grows past its limit, the direction isn't settled yet: move items to **Open decisions**.

## Principles it encodes

1. **User values are authoritative.** The agent can question how a value is read, but can't replace it.
2. **Aesthetic vocabulary can be expanded.** The user's words for a look are a guess, not a spec.
3. **Agent ideas must be grounded.** An agent-originated direction names the product fact it comes from and
   passes the other-client test. Being new isn't a reason.
4. **Rejection is final.** A rejected direction is logged with its reason and never re-offered in other words.
5. **The render decides.** A direction succeeds when the screenshot passes its constraints, not when it sounds
   good.

## Who may change what

| Section | Owner | Changes when |
| --- | --- | --- |
| Values | User | The user says so. The agent never edits them on its own reading |
| Opening vocabulary, References | User's words, agent's reading | The user corrects the reading |
| Directions, Selected | Shared | A grilling round ends with the user choosing |
| Constraints, Avoid | Shared | A checkpoint finds a *lesson* and the user approves the change |
| Overrides, Rejected | Log only | Append only, never edit |
| Open decisions | Shared | Resolved by the user, or by the checkpoint named next to it |

---

## Template

```markdown
# Creative direction: <product>
Status: draft | agreed <date> · Mode: guided | fast · v<n>

## 1. Context
- Product: <one line, what it does>
- Audience: <who decides, who uses>
- The page must: <the one job: what a visitor should do or believe on leaving>

## 2. Values (user-owned, 2–5)
- V1 <value> — "<the user's words it came from>"

## 3. Opening vocabulary
"<the user's first description, verbatim>"
Reading: hypothesis | deliberate preference — <evidence for the reading>

## 4. References (0–5)
| Reference | Admire | Borrow | Avoid | Just interesting |
Items in "Just interesting" are never built in.

## 5. Directions explored (2–4)
| Direction | Origin (user / reference / agent) | Grounded in | Serves | Outcome | User's reason |
Agent-originated rows also answer: Other-client test: <could this belong to another client? why not?>

## 6. Selected direction
<name> — origin: <user / reference / agent>
<2–3 sentences: what it is and which values it serves>
The one memorable thing: <one sentence>

## 7. Constraints (4–8, each pass/fail on a screenshot)
- C1 <constraint> → check: <what a reviewer looks for in the render>

## 8. Avoid (≤6, each observable)
- <thing a reviewer could point at in a screenshot>

## 9. Decisions log (append only)
| Decision | Agent recommended | User chose | Reason | Settled |
Settled = yes: implementation follows it and never reopens it unasked. Settled = until <checkpoint>: revisit then.
Rejected (final): <direction or idea> — <reason>

## 10. Open decisions
- <decision> — decide at: <checkpoint or round>

## 11. Checkpoints
| Checkpoint | Constraint | Pass / fail | Bug or lesson | Action |
Bug: the code missed the direction → fix the code. Lesson: the direction looked wrong rendered → reopen with
the user; don't edit constraints silently.
```

## Writing rules

- **Constraints must be checkable.** "Elegant" fails. "Headlines are at least 4× body size; nothing else on
  the page competes in size" passes. If two reviewers could disagree on pass/fail, rewrite it.
- **Avoid items name things, not moods.** "Gradient mesh backgrounds" passes; "anything generic" fails.
- **Open decisions stay open.** The agent doesn't fill them in by implementing a choice. It implements a
  placeholder, or asks at the named checkpoint.
- **Fast mode** fills Context, Values, one Selected direction with its alternatives named in Directions, 4
  constraints and Avoid. Everything else goes to Open decisions with a checkpoint.
- **The diversity rule covers agent ideas too.** Across unrelated products, agent-originated directions should
  differ. Repeating the same "distinctive" move (serif headlines, asymmetry, grain) is the agent's own default.
