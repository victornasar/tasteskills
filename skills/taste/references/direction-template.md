# DIRECTION.md template

`/taste` writes this into the user's project. Implementation follows it and the critique tests the render
against it. Keep it to about a page; a section that keeps growing means the decision isn't settled, so move it
to Open decisions.

Mark where facts came from: `[client]` the user said it, `[inferred]` your reading, not confirmed, `[agent]`
your decision, `[approved]` the user signed off. Never upgrade an inference to a client fact without the user
saying so.

```markdown
# Creative direction: <product>
Status: draft | agreed <date>

## 1. Context
- Product: <one line> — [tag]
- Audience: <who decides, who uses> — [tag]
- The page must: <what a visitor should do or believe on leaving> — [tag]
- Values: <2–5, in the client's words where possible> — [tag]

## 2. Positioning
- Category: <in the buyer's words> — [tag]
- Alternatives: <what the audience would choose instead> — [tag]
- Conventions:
  | Convention (visible in a screenshot) | Adopt / Challenge / Avoid | Why |
- Intended perception: P1 <quality> → check: <what in the render shows it>; P2 …; P3 …
- Sophistication: everyday | considered | premium | luxury — <the signal it rests on>
- Differentiate on: <the one thing the alternatives don't say>

## 3. Directions explored
| Axis | <Direction A> | <Direction B> | <Direction C> |
| --- | --- | --- | --- |
| Composition | <position> because <reason> | | |
| Scale | | | |
| Imagery | | | |
| Signature device | | | |
| Colour proportion | | | |
| Surface | | | |
| Type approach | | | |
| Colour approach | | | |
| House-style markers | <count: which> | | |

## 4. Selected direction
<name> — [approved | agent]
<2–3 sentences: what it is and which values and perception qualities it serves>
The one memorable thing: <one sentence>
House style: <marker count>; if 4 or more, "House style kept because <reason>"

## 5. Design system
### Typography
- <Role>: <family> — weights, sizes (desktop / phone), axes or features — because <reason> — seen: proof | specimen | no
- Pairing: contrasts on <dimension>, shares <quality>
- Rejected: <candidate> — <reason>
### Colour
- Ground / figure / accent: <values> — area roughly <split>
- Text pairs checked: <pair> <ratio>:1 for <use>
### Layout
- Visitor's questions in order, what the page leads with, what was cut
### Imagery
- Job · Kind · Shot list · Treatment · Ships now (see visual-direction.md)
### Other decisions
- Spacing, radii, motion: few, each tied to a value or product fact

## 6. Constraints (4–8, each pass/fail on a screenshot)
- C1 <constraint> → check: <what a reviewer looks for>

## 7. Avoid (up to 6, each observable)
- <thing a reviewer could point at>

## 8. Decisions and open questions
- Decided: <decision> — <reason> — [tag]
- Rejected: <direction or idea> — <reason> (final)
- Open: <decision> — decide when: <checkpoint>

## 9. Critique
| Round | Constraint or marker | Pass / fail | What changed |
```

## Writing rules

- **Constraints must be checkable.** "Elegant" fails. "Headlines are at least 4× body size and nothing else
  competes in size" passes. If two reviewers could disagree on pass or fail, rewrite it.
- **Avoid items name things, not moods.** "Gradient mesh backgrounds" passes; "anything generic" fails.
- **Open decisions stay open.** Build a neutral placeholder or ask at the named point; don't settle them by
  implementing a choice.
- **Positioning is a reading, not research.** Conventions and alternatives come from the brief and what the
  category commonly does. Never present a guessed competitor as a fact the client gave.
