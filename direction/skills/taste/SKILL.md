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
  page, 2–5 values, avoid-list seeds and reference readings are known.
- **Fast:** extract the same from the written brief. Tag gaps `[inferred]` or list them under Open decisions.

**Gate 1.** Show Context and Values with tags. Wait for confirmation in interactive sessions. In non-interactive
fast runs, proceed with tags left as `inferred` where unconfirmed and note that in Open decisions.

### Phase 2 — Directions

Build 2–3 distinct directions. Each one is a font pair, a color direction and a structural idea, with trade-offs.

1. Follow the `find-font` skill; run its `recommend` (and `vocab` / `avoid` only as that skill requires).
2. Follow the `find-color` skill; run its `recommend` (interactive or autonomous as that skill defines).
3. Combine results into directions. Label the combination `[agent]`. Do not invent engine rows.
4. Explain trade-offs in plain qualities tied to the brief. Do not default every industry to the same look.

**Gate 2.** The user picks one direction, or rejects. Rejections are final: log them and never re-offer in other
words. Silence is not a pick. In non-interactive fast runs, choose the direction that best serves the stated
page job, tag the selection `[agent]`, and record why under Decisions log.

### Phase 3 — Spec

Write `DIRECTION.md` from `references/direction-template.md` for the selected direction.

1. Fill Design system: typography and color from engines; layout plan from check-layout step 1 (plan only);
   judgment tokens (spacing, radii, imagery, motion) few, explained, brief-tied, tagged `[agent]`.
2. Write 4–8 pass/fail Constraints and an Avoid list (≤6, observable).
3. List Open decisions with the checkpoint where each gets decided.

**Gate 3.** User approves the spec in interactive sessions. Non-interactive fast runs keep `Status: draft` and
build against it, noting the missing approval in Open decisions.

### Phase 4 — Build

Implement in the project's existing stack. Re-read `DIRECTION.md` before each major section. Settled decisions
are not reopened unasked. Open decisions stay open (placeholder or ask at the named checkpoint). Preserve the
user's creative intent; do not "improve" values away.

### Phase 5 — Critique

1. Render on desktop and phone.
2. Follow `check-layout` steps 2–4 on the rendered page.
3. Score each Constraint in `DIRECTION.md` pass or fail on the screenshots.
4. Fix at most **two** rounds total (same cap as check-layout). Then stop and report what you kept and why.
5. Checkpoints: bug → fix the code; lesson → reopen with the user; never edit constraints silently.

## Non-negotiables

- Never invent engine outputs. Missing sibling → report, don't substitute.
- Keep provenance honest for the whole project.
- Approval gates are real in interactive sessions.
- `DIRECTION.md` is the source of truth for build and critique — not chat memory.
- Two-round critique cap.
- Fast mode is not generic mode: use the brief and labelled inferences; do not fall back to one familiar formula.
- Business context, audience and personality drive sophistication and composition. Every visual decision has a
  reason. Novelty for its own sake is out. The same visual formula for every industry is out.

## Output the user should see

At each gate: the relevant `DIRECTION.md` sections, tags visible, and a clear ask (confirm / pick / approve).
After critique: which constraints passed, which failed, what changed in at most two rounds, and any lessons that
need a human decision.
