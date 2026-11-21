---
name: interaction
description: Design how a website behaves when people use it, so every control looks like what it does, every action gets feedback, mistakes are prevented or easy to recover from, and behaviour matches what people expect. Covers affordances and signifiers, discoverability, feedback and system status, the full set of interaction states, navigation behaviour, forms and input behaviour, validation and errors, destructive actions, and conventions. Use when building or reviewing anything interactive (forms, navigation, menus, filters, checkout, sign-up, settings, search) or when users are confused, make errors, or can't find things. Not for component visual polish (`components`), animation (`motion`) or ARIA and keyboard specifics (`a11y`).
argument-hint: "[flow, page or component]"
---

# interaction

People judge an interface by whether they can tell what to do, whether it did what they meant, and whether they
can recover when it didn't. Design those three things deliberately for every interactive element, and check them
by actually using the page.

Flow, page or component:

$ARGUMENTS

If this is empty, review the interactive parts of the current project.

## Where this sits

- `interaction` decides behaviour: what's clickable, what states exist, what feedback appears, when
  validation runs, what happens on error.
- `components` makes those states look finished. `motion` decides how changes move.
  `a11y` makes the behaviour work with keyboards, screen readers and other assistive tech.
  `content` writes the labels, errors and confirmations.

## Principles

1. **Signifiers make affordances visible.** An affordance is what an element lets you do; a signifier is how you
   can tell. Links look like links, buttons like buttons, inputs like inputs, draggable things like they can be
   grabbed. When a signifier is removed for minimalism (flat text that's secretly a button, an input with no
   border), people miss the action.
2. **Every action gets feedback, fast.** Acknowledge input within about 100ms (a pressed state, a spinner, the
   item appearing). Show progress for anything longer than about a second. Confirm the outcome. Silence makes
   people click again.
3. **Visibility of system status.** People should know where they are (current page, step 2 of 4), what's
   selected, what's loading, what's saved and what failed.
4. **Prevent errors before reporting them.** Constrain inputs, suggest, show formats, disable impossible options
   with an explanation, confirm or (better) make undoable anything destructive.
5. **Recovery is part of the design.** Errors say what happened and how to fix it, next to where it happened, and
   keep what the user entered.
6. **Follow conventions unless the brief gives a reason.** Logo goes home, underlined text is a link, the basket is
   top right, Escape closes things. Jakob's law: people spend most of their time on other sites, so they expect
   yours to work like those. Novel interaction needs a payoff that justifies the learning.
7. **Keep people in control.** No surprises: no navigation on focus, no auto-advancing carousels, no content that
   jumps under the pointer, no modal that appears unprompted mid-task.

## How to work

### 1. Map the interactions

For the page or flow, list every interactive element and the user's goal for each. For flows, write the steps,
the decision at each, and the exits (back, cancel, save for later). Cut steps that collect nothing needed.

### 2. Define states for each element

Write out the states before styling. Most interactive elements need:

| State | Meaning |
| --- | --- |
| Default | Available, at rest |
| Hover (pointer only) | "This responds to you" |
| Focus (keyboard) | Where keyboard input goes; must be clearly visible |
| Active / pressed | The press registered |
| Selected / checked / current | A persistent choice or location |
| Disabled | Not available now; say why if it isn't obvious |
| Loading / pending | Working on it |
| Success | Done |
| Error | Something's wrong, and what |
| Empty | Nothing here yet, and what to do about it |
| Read-only | Visible but not editable |

Views also have states: loading, empty, partial, error, offline, no permission, and too much (the 500-item list).
Design every one that can happen. `references/states-and-forms.md` has the detail.

### 3. Design feedback

| Wait | Feedback |
| --- | --- |
| Under ~100ms | Immediate state change; nothing else needed |
| ~100ms–1s | Pressed or pending state on the control; avoid flashing spinners |
| 1–10s | A spinner or skeleton in place of the result; disable double submission |
| Over 10s | Progress with an estimate or steps, and a way to leave and come back |

Prefer optimistic updates (show the result, reconcile later) for low-risk, reversible actions like a like or a
reorder; roll back visibly on failure. Use pessimistic updates (wait for confirmation) for payments, deletions and
anything with consequences.

Put feedback where the user is looking: next to the button, on the field, in the list. A toast in the far corner
is for background events, not the result of the action they just took.

### 4. Design navigation behaviour

- Show where people are: the current item marked in the nav, breadcrumbs on deep sites, step indicators in flows.
- Links navigate, buttons act. Don't make a button that navigates or a link that submits.
- Back must work: filters, tabs and steps that change the view should update the URL when a user would expect
  Back to undo them.
- Menus open on click or tap (hover-open menus with a delay are acceptable on desktop only if they also work by
  click and keyboard); close on Escape and outside click; don't close when the pointer slips diagonally toward a
  submenu.
- Preserve scroll position and form state when returning.

### 5. Design forms

The essentials (detail in the reference):

- Ask only what's needed, in the order people think about it. One column.
- Visible labels above fields; never placeholder-only labels.
- Use the right input: `type`, `inputmode`, `autocomplete`, native date and select where they serve.
- Show format and constraints before input ("At least 12 characters"), not only after failure.
- Validate on submit, and inline after a field loses focus once the user has finished it. Don't show errors while
  someone is still typing a field for the first time. Clear an error as soon as it's fixed.
- On submit errors: keep all input, show a summary at the top linking to each field, and mark each field.
- Disable the submit button only with a visible reason; otherwise let people submit and tell them what's missing.
- Confirm success clearly and say what happens next.

### 6. Make destructive actions safe

Prefer undo (delete, then "Undone? Undo" for a few seconds, with the action actually reversible) over
confirmation dialogs. Use a confirmation when it can't be undone, and make the dialog name the consequence ("Delete
3 invoices? This can't be undone.") with a specific button label ("Delete invoices"), not "OK". For severe actions,
require typing the name.

### 7. Use it

Don't review interaction from screenshots alone. Load the page in a browser tool and:

1. Click, tap and tab through every control. Does each look interactive before you touch it, and respond when you
   do?
2. Trigger every state: submit an empty form, enter invalid data, slow the network (devtools throttling) to see
   loading states, go offline, empty the list, overfill it.
3. Try to make a mistake, then recover. Is the input kept? Is the error next to its cause, in plain words?
4. Double-click submit buttons. Press Back mid-flow. Reload a filtered view.
5. Use it with the keyboard only, and on a phone-sized viewport with touch emulation.
6. Find the one thing a new visitor would most likely miss, and fix its signifier.

Report the states designed, the feedback for each action, how errors are prevented and recovered, and any
convention you broke and why.

## Mistakes agents make

- Only the default and hover states exist; no focus, loading, error, empty or disabled design.
- Clickable cards, text and icons with no signifier; or non-clickable elements styled like buttons.
- Placeholder text as labels; errors only in a toast; errors that clear the form.
- Validation that shouts while the user types the first character.
- Submit buttons disabled with no explanation, or not disabled during submission, so orders go through twice.
- `<div onclick>` instead of buttons and links, losing keyboard access and expected behaviour.
- Spinners for everything, including actions that finish in 50ms (flashing) and ones that take 30s (no progress).
- Confirmation dialogs with "Are you sure?" and "OK / Cancel".
- Tabs, filters and steps that don't survive Back or reload.
- Carousels that auto-advance, modals that open on page load, sticky banners that cover content.
