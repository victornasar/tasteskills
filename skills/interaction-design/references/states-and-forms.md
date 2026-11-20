# States, forms and error handling

## View states

Every view that loads or holds data can be in more than one state. Design each that can happen.

| State | Show | Avoid |
| --- | --- | --- |
| First load | A skeleton matching the final layout for content; a spinner only for small, unpredictable areas | A blank page; a full-page spinner for a partial load |
| Empty (first use) | What will appear here, why it's empty, the one action that fills it | "No data" alone; an illustration with no action |
| Empty (no results) | What was searched or filtered, how to widen it, a one-tap "clear filters" | A dead end |
| Partial | What loaded, and what didn't with a retry for that part | Failing the whole view for one part |
| Error | What failed in plain words, whether data is safe, retry, a way to get help | Error codes alone; stack traces; blaming the user |
| Offline | What still works, what's queued, when it will sync | Silently failing actions |
| No permission | Why, and who can grant access | A generic 404 |
| Too much | Pagination, virtualisation or "load more" with a count; search and filters | Rendering 5,000 rows |
| Stale | When it was last updated; a refresh | Presenting old data as live |

## Control states, behaviour notes

- **Hover** must never be the only way to discover something. It's a confirmation for pointer users, not a
  signifier.
- **Focus** must be visible on every interactive element, and distinct from hover. Use `:focus-visible` so mouse
  clicks don't show the keyboard ring where that would confuse, but never remove focus styles.
- **Pressed** feedback matters most on touch, where there's no hover.
- **Disabled** controls are often better as enabled controls that explain what's missing when used. If you do
  disable, make the reason visible nearby, and keep the control discoverable (disabled buttons aren't focusable by
  default, so screen-reader users may not find them; consider `aria-disabled` with a message).
- **Loading on a button:** keep the label (or change it to "Saving…"), keep the width stable, prevent repeat
  submission.
- **Selected vs focused vs current:** three different things. A list can have a focused item, several selected
  items and a current item; each needs its own look.

## Forms in depth

**Structure**

- One column. Group related fields under a heading or `<fieldset>`/`<legend>`.
- Order fields as people think of them (name, then address, then payment), not as the database stores them.
- Mark optional fields "(optional)" rather than marking required ones with asterisks, when most fields are
  required; do the reverse when most are optional. Be consistent.
- Split long forms into steps only when steps group naturally and the user benefits from a sense of progress.
  Show the step count and allow going back without losing data.
- Don't ask twice for the same information in a session (WCAG 3.3.7, Redundant Entry).

**Inputs**

| Need | Use |
| --- | --- |
| A number people don't calculate with (card number, postcode, code) | `type="text" inputmode="numeric"`, not `type="number"` |
| Email | `type="email"`, `autocomplete="email"` |
| Phone | `type="tel"`, `autocomplete="tel"` |
| One-time code | `inputmode="numeric" autocomplete="one-time-code"` |
| Choosing one of 2–5 | Radio buttons, all visible |
| Choosing one of many | A select, or a searchable combobox for long lists |
| Choosing several | Checkboxes |
| A date people know (birthday) | Three text fields (day, month, year) or a text field with a clear format |
| A date people choose (booking) | A date picker, with text entry allowed |
| An on/off setting that applies immediately | A switch; otherwise a checkbox |

- Size inputs to their expected content: a postcode field shouldn't be full width; a short field signals a short
  answer.
- Accept formats generously (spaces in card numbers, any capitalisation of postcodes) and normalise them yourself.
- Passwords: allow paste, offer show/hide, state the rules before input, support password managers
  (`autocomplete="new-password"` / `"current-password"`).

**Validation timing**

| Moment | Use for |
| --- | --- |
| Before input | Format hints, constraints, examples |
| While typing | Only positive, progressive feedback (password strength, characters remaining); never errors on the first pass |
| On blur, after the field was completed | Format errors ("That email is missing an @") |
| On submit | Everything, plus anything that needs the server (username taken, card declined) |
| After an error is shown | Re-validate while typing, so the error clears as soon as it's fixed |

**Error messages** (content-design writes them; this is what they must contain)

- What's wrong and how to fix it, specific to this field: "Enter a postcode, like SW1A 1AA", not "Invalid input".
- Next to the field, and announced to assistive technology (web-accessibility covers how).
- On submit, an error summary at the top that links to each field, with focus moved to it.
- Never clear valid input because another field failed.

**Success**

- Say what happened and what happens next ("Booked for Saturday 3pm. We've emailed a confirmation to …").
- Offer the next likely action.

## Error prevention patterns

- **Constraints:** offer only valid choices (unavailable dates disabled, with the reason).
- **Defaults:** sensible pre-selections that most people keep.
- **Suggestions:** "Did you mean gmail.com?"
- **Previews:** show the result before committing (the invoice before sending).
- **Undo:** the best safety net for reversible actions.
- **Confirmation:** only for irreversible actions; name the consequence.
- **Autosave:** for long or important input; show "Saved" status.
- **Leave warnings:** warn before navigating away from unsaved changes, but only when there are unsaved changes.

## Common conventions worth keeping

- Logo links to the home page.
- Links are visually distinct from body text (underline or a strong cue beyond colour alone).
- Primary action on the right in dialogs on desktop in most Western interfaces, or ordered consistently across the
  product; whichever you choose, be consistent.
- Escape closes dialogs, menus and popovers; clicking outside closes non-modal popovers.
- Search at the top; a magnifying glass is understood.
- Basket or cart top right on shops.
- Pagination or "load more" over infinite scroll when people need to reach the footer or return to a position.
