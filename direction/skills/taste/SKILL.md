---
name: taste
description: Design-director skill that interviews a brief, writes DIRECTION.md, and coordinates find-font, find-color and check-layout into one art-directed build. Use when starting a website or brand surface from a business brief, when the user invokes /taste, or when they want creative direction before implementation — not for isolated font, color or layout checks.
argument-hint: "[fast|guided] <brief, e.g. independent daycare for local families>"
---

# taste

Thin conductor. It runs a conversation, writes decisions into `DIRECTION.md` in the user's project, calls the
sibling TasteSkills at the right moments, and checks the built page against that file. It holds no font catalog,
color library or layout checker of its own.

Brief and mode:

$ARGUMENTS

If the argument starts with `fast` or `guided`, that is the mode; the rest is the brief. Otherwise choose a mode
(below). If the brief is empty, infer one from the current project and say what you inferred, tagged `[inferred]`.

## Modes

| Mode | When | Status |
| --- | --- | --- |
| **fast** | The user pastes a written brief, says "fast", or a lab / non-interactive run supplies the brief | Primary. Measured first. |
| **guided** | The brief is thin and the session is interactive | **Experimental.** Discovery not yet scored. Follow `references/interviewing.md`. |

A brief that only *sounds* complete is not complete. If audience, page objective or business values are missing,
fast mode records the gaps as `[inferred]` or Open decisions — it does not quietly fill them as `[client]`.

## Locating sibling skills

Skills cannot call each other directly. Find each sibling and follow its `SKILL.md` exactly, including its
"never invent what the script didn't return" rules.

1. Look next to this skill folder for `find-font`, `find-color`, `check-layout` (same skills parent, or
   `.claude/skills/`, `.cursor/skills/`, etc.).
2. If missing, search the workspace for `find_font.py`, `find-color.mjs` or `check_layout.mjs`.
3. If still missing, tell the user the install command and continue without that step. **Never guess fonts,
   colors or checker results to fill the gap.**

```bash
npx skills add https://github.com/victornasar/tasteskills --skill find-font
npx skills add https://github.com/victornasar/tasteskills --skill find-color
npx skills add https://github.com/victornasar/tasteskills --skill check-layout
```

Record engine output (ids, names, values, ratios) in `DIRECTION.md` with the `[engine]` tag. Combining engine
picks into a creative direction is `[agent]`.

## References in this skill

| File | Use |
| --- | --- |
| `references/direction-template.md` | The only creative-direction format. Write `DIRECTION.md` from it. |
| `references/interviewing.md` | Guided-mode questions. Open questions only; no style-label choices. |
| `references/visual-direction.md` | The six visual axes, the difference rule, the house-style check and the imagery plan. |

## Provenance

Every material line in `DIRECTION.md` carries one tag: `client`, `inferred`, `engine`, `agent`, `approved`.
Definitions live in the template. Do not upgrade `inferred` to `client` or `approved` without an explicit user
act.

## Skip rules

| Situation | Behaviour |
| --- | --- |
| Complete written brief | Fast mode; skip interview; Gate 1 is a short confirm of Context/Values (or proceed labelled in non-interactive runs) |
| Existing brand palette | Skip `find-color` recommend, or run it with `--existing`; still record values as `[client]` / `[engine]` |
| "Just fix the type" | Run `find-font` alone; do not start the full workflow |
| Existing `DIRECTION.md` | Read it; resume at the unfinished phase; do not restart discovery |
| Sibling skill missing | Report the limitation; leave that Design-system row open |

## Workflow (five phases)

### Phase 1 — Discover

Business and creative discovery together.

- **Guided:** one open question at a time per `references/interviewing.md`. Stop when audience, one job of the
  page, 2–5 values, positioning, avoid-list seeds and reference readings are known.
- **Fast:** extract the same from the written brief. Tag gaps `[inferred]` or list them under Open decisions.

**Positioning** (DIRECTION.md §3) is how the brand stands against its alternatives. Build it in this order:

1. **Category** in the buyer's words, not the founder's.
2. **Alternatives:** what the audience would choose instead. Name companies only when the brief or user names
   them (`[client]`); otherwise describe them by kind ("a freelancer from a marketplace", "doing it themselves") and
   tag `[inferred]`. Never present a guessed competitor as a client fact.
3. **Conventions:** 3–5 things the category's sites commonly do, each observable in a screenshot. Marking each
   Adopt, Challenge or Avoid is `[agent]`, with the reason tied to a value, the audience or a perception quality.
   Adopt what the audience relies on to act (the facts they came to check); challenge what makes the alternatives
   interchangeable.
4. **Intended perception:** three qualities a stranger should report after five seconds, each with a screenshot
   check. Derive them from Values and the page's job; tag `[inferred]` unless the user said them.
5. **Sophistication** (everyday, considered, premium, luxury) from price, audience and setting signals in the
   brief, with the signal named. No signal: `[inferred]` and an Open decision.
6. **Differentiate on:** the one thing this page will communicate that the alternatives don't.

**Gate 1.** Show Context, Values and Positioning with tags. Wait for confirmation in interactive sessions. In non-interactive
fast runs, proceed with tags left as `inferred` where unconfirmed and note that in Open decisions.

### Phase 2 — Directions

Build 2–3 distinct directions. Each one is a font pair, a color direction and a position on each of the six
visual axes in `references/visual-direction.md` (composition, scale, imagery, signature device, colour
proportion, surface), with trade-offs.

1. Follow the `find-font` skill; run its `recommend` (and `vocab` / `avoid` only as that skill requires).
2. Follow the `find-color` skill; run its `recommend` (interactive or autonomous as that skill defines).
3. Combine results into directions. Label the combination `[agent]`. Do not invent engine rows. Pass
   Positioning into the engines where they take it: find-color's `--convention follow|avoid` follows the
   colour conventions marked Adopt or Avoid; find-font's feel tags come from the perception qualities as well as
   the brief's words.
4. Fill the axis table: every position reads `<position> — because <Positioning or Value>`.
5. **Difference rule:** directions differ on at least three axes, and at least one challenges a convention
   Positioning marks Challenge. Fewer than three: merge or rework.
6. **House-style check:** count markers H1–H6 for each direction. At least one direction scores 3 or fewer. A
   direction with 4 or more may be chosen only with `House style kept because <reason>` grounded in Positioning.
7. Explain trade-offs in plain qualities tied to the brief. Do not default every industry to the same look.

**Gate 2.** The user picks one direction, or rejects. Rejections are final: log them and never re-offer in other
words. Silence is not a pick. In non-interactive fast runs, choose the direction that best serves the stated
page job, tag the selection `[agent]`, and record why under Decisions log.

### Phase 3 — Spec

Write `DIRECTION.md` from `references/direction-template.md` for the selected direction.

1. Fill Design system: typography and color from engines; layout plan from check-layout step 1 (plan only)
   plus the selected axis positions; the Imagery plan (`references/visual-direction.md`); judgment tokens
   (spacing, radii, motion) few, explained, brief-tied, tagged `[agent]`.
2. Write 4–8 pass/fail Constraints (at least one checks a perception quality) and an Avoid list (≤6,
   observable).
3. List Open decisions with the checkpoint where each gets decided.

**Gate 3.** User approves the spec in interactive sessions. Non-interactive fast runs keep `Status: draft` and
build against it, noting the missing approval in Open decisions.

### Phase 4 — Build

Implement in the project's existing stack. Re-read `DIRECTION.md` before each major section. Build the
Imagery plan's "ships now" visuals. Never ship an empty image frame or placeholder box. Settled decisions
are not reopened unasked. Open decisions stay open (placeholder or ask at the named checkpoint). Preserve the
user's creative intent; do not "improve" values away.

### Phase 5 — Critique

1. Render on desktop and phone.
2. Follow `check-layout` steps 2–4 on the rendered page.
3. Score each Constraint in `DIRECTION.md` pass or fail on the screenshots. Count house-style markers on the
   screenshot, yes or no for each with what you see; hesitation counts as yes. 4 or more without a recorded
   `House style kept because` is a bug: move two marked axes, as the direction table planned.
4. Fix at most **two** rounds total (same cap as check-layout). Then stop and report what you kept and why.
5. Checkpoints: bug → fix the code; lesson → reopen with the user; never edit constraints silently.

## Non-negotiables

- Never invent engine outputs. Missing sibling → report, don't substitute.
- Keep provenance honest for the whole project.
- Approval gates are real in interactive sessions.
- `DIRECTION.md` is the source of truth for build and critique — not chat memory.
- Two-round critique cap.
- Fast mode is not generic mode: use the brief and labelled inferences; do not fall back to one familiar formula.
- Positioning, business context, audience and personality drive sophistication and composition. Every visual decision has a
  reason. Novelty for its own sake is out. The same visual formula for every industry is out.

## Output the user should see

At each gate: the relevant `DIRECTION.md` sections, tags visible, and a clear ask (confirm / pick / approve).
After critique: which constraints passed, which failed, what changed in at most two rounds, and any lessons that
need a human decision.
