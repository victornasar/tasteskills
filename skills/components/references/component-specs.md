# Component specs

Per-component craft notes. Values are typical starting points; the design system and the direction set the real
ones. Behaviour comes from `interaction` and the ARIA pattern from `a11y`; these notes cover how
each is built and finished.

## Buttons

- **Element:** `<button>` for actions, `<a>` for navigation. Style them alike if the design wants, but don't swap
  them.
- **Emphasis variants:** primary (filled with the accent), secondary (outline or tinted), tertiary (text only,
  still clearly interactive), destructive (a danger tone, used only for destructive actions). One primary per view.
- **Sizes:** two or three, matching input heights.
- **Anatomy:** label, optional leading or trailing icon, optional loading indicator. Icon-only buttons need an
  accessible name and a square hit area.
- **Details:** `white-space: nowrap` for short labels; allow wrapping for long ones rather than overflowing; a
  minimum width so "OK" isn't a tiny square; consistent letter-spacing; no text shadow.
- **Loading:** keep the width; overlay the spinner or replace the icon; keep `aria-busy` or an announcement (see
  `a11y`); prevent repeat activation.

## Text inputs and textareas

- **Anatomy:** visible label above, optional hint between label and field, the field, error message below. Group
  them with consistent spacing (label → field tight; field → next label wider).
- **Field:** a visible boundary (border or a filled background with a bottom border) with 3:1 contrast; font size
  at least 16px on mobile; padding matching button heights.
- **States:** focus (ring or border change, clearly stronger than hover), error (border, icon, message linked by
  `aria-describedby`), disabled, read-only (looks like text, not a disabled input).
- **Affixes:** units, currency or icons inside the field must not overlap the text; pad the text side.
- **Textarea:** resizable vertically; a sensible initial height for the expected answer; character count only when
  there's a limit.

## Selects, comboboxes and dropdown menus

- Prefer native `<select>` for simple single choice; it's accessible and uses the platform picker on phones.
  Style the closed state; leave the open list native.
- A custom combobox (search and select) follows the ARIA combobox pattern: input, listbox, active option, typing
  filters, arrow keys move, Enter selects, Escape closes.
- A dropdown menu of actions is a menu button pattern, not a select.
- **Panel craft:** aligned to the trigger's edge, at least as wide as the trigger, max height with internal scroll,
  elevation shadow, 4–8px offset from the trigger, flips when near the viewport edge. Options have generous height
  (36–44px), a clear highlighted state distinct from the selected state, and checkmarks for selection.

## Checkboxes, radios and switches

- Native inputs styled with `accent-color` where that's enough; custom styling via `appearance: none` must keep
  focus, checked, indeterminate and disabled states.
- The label is part of the hit area (wrap or use `for`).
- Switches only for settings that take effect immediately; label the setting, not the state ("Email
  notifications", not "On").

## Navigation bars

- **Current page** marked visibly (weight, underline, indicator) and with `aria-current="page"`.
- Items aligned to the page grid; consistent spacing; touch targets padded.
- Sticky headers: modest height, a background (not transparent over content) and a subtle edge once scrolled.
  Make sure focused elements aren't hidden under them (WCAG 2.4.11; `scroll-padding-top`).
- Mobile menu panels: full height, focus trapped, a close button in the same place as the open button.

## Sidebars, lists and toolbars

Dense app chrome is where misalignment shows most: rows repeat, so one item off by 2px stands out against
twenty that aren't. Each rule names the line things sit on, so you can decide cases these rules don't list.

- **One icon column.** Every row's icon sits in a slot of the same fixed width (`flex: none; width: 1rem` or the
  icon size), centred in it, whatever the glyph's own width. Icons differ in visual width (a narrow pin beside a
  wide grid), so sizing the slot rather than the glyph is what keeps the column straight. Rows with no icon either
  keep an empty slot or are designed to start on the text line. Decide which per list, not row by row.
- **One text line.** Every label starts at the same x: the icon slot plus one fixed gap. Avatars, checkboxes and
  status dots take the icon slot's width too, or the labels drift. Nested rows indent to the parent's text line
  (one whole step), never by an arbitrary amount, so the hierarchy reads as lines and not as noise.
- **Headers on the icon edge.** Section headers ("Favourites", "Projects") start on the icon column's left edge,
  not the text line. The group then has one outer edge, the header marks the group's start instead of reading as
  one more item, and the eye reads down the icons. Pick that or the text line for the whole sidebar. Mixing the
  two is the bug.
- **Trailing items on one right edge.** Counts, shortcuts, chevrons and badges share one right edge with
  `margin-left: auto`, using tabular figures so counts don't change width as they update.
- **Highlights don't move content.** Hover and selected backgrounds are inset by the container's padding and
  extend the same distance past the icon on the left as past the trailing item on the right. Switching state
  changes the colour, never the position or weight of the label.
- **Toolbars on one centre line.** Every control in a toolbar shares one vertical centre: heights come from the
  control size set, icon buttons are square at that height, `align-items: center` on the bar, and text, avatars
  and separators are sized to that height rather than to their content. A toolbar's job is to scan as one row,
  and one control 2px low breaks that more than any colour choice.
- **Fix the container, not one item.** Horizontal padding lives on the list or bar, and rows have none of their own.
  When one row is off, find out why (its own margin, a wider icon, a missing slot) and fix the shared rule. A
  `margin-left: -2px` on one row fixes that row and leaves the cause in place for the next one.

Check with the guide-line overlay in `inspect`'s `references/capture.md`: draw lines at the icon edge, the text
line and the toolbar's centre, then look for anything that isn't on one.

## Cards

- Use a card when the item is an object: a product, an article, a booking. Not as a default container for any
  content.
- **Clickable cards:** one link, usually on the title, stretched to cover the card with a pseudo-element; secondary
  actions inside sit above it with `position: relative` and their own focus. Don't wrap a whole card in `<a>`
  containing other interactive elements.
- **Anatomy alignment:** in a row of cards, use `subgrid` (or fixed regions) so titles, prices and actions line up
  despite different content lengths.
- **Media:** a consistent aspect ratio with `aspect-ratio` and `object-fit`; a designed fallback for missing images.
- **Surface:** border, background tint, shadow or none, from the direction. A card with a border and a shadow and
  a tinted background is three separators doing one job.

## Modals and dialogs

- Use `<dialog>` with `showModal()`: it handles the top layer, inertness of the page behind and Escape.
- Use a modal only when the task must interrupt; otherwise a page, a drawer or inline expansion.
- **Anatomy:** title, content, actions. Actions at the bottom, primary action labelled with the verb.
- **Size:** a max width tied to the content (forms ~32–40rem, confirmations ~28rem); on phones, full width or a
  bottom sheet; max height with the content scrolling and the actions fixed.
- **Backdrop:** dim enough to separate, not so dark it hides context.
- **Focus:** to the first meaningful element (or the dialog), back to the trigger on close.
- Prevent background scroll while open; avoid layout shift when the scrollbar disappears
  (`scrollbar-gutter: stable`).

## Tabs

- For switching between views of the same thing, all at the same level. Not for steps in a sequence.
- **Anatomy:** a tab list with the selected tab clearly marked (an indicator bar, weight, a connected background),
  panels below.
- Keyboard: arrow keys move between tabs, Tab moves into the panel (ARIA tabs pattern).
- Overflow: scroll the tab list horizontally with a visible cut-off, or switch to a select on narrow screens.
- Keep tab labels short, and keep the selected indicator's movement quick if animated.

## Tooltips and popovers

- **Tooltip:** a short, non-essential description of a control, on hover and focus, dismissible with Escape, and
  hoverable itself (WCAG 1.4.13). Never the only place important information lives, since touch users can't hover.
- **Toggletip / popover:** for richer or essential help, opened by click. Use the `popover` attribute or a
  disclosure pattern.
- **Craft:** a small arrow or none (be consistent), 4–8px offset, max width ~20–28rem, readable size (not tiny),
  high contrast, a short delay before showing on hover (about 300–500ms) and none on focus, no delay when moving
  between adjacent tooltips.

## Badges, tags and chips

- Badges show status or counts; tags categorise; chips are interactive filters or selections. Don't style all
  three identically.
- Status needs text, not just colour. Keep the set of tones small (neutral, info, success, warning, danger).

## Tables (as components)

- Header styling distinct from rows; numbers right-aligned with tabular figures; sticky header for long tables;
  row hover only if rows are interactive; zebra stripes or rules only as dense as needed; sorting controls in the
  header buttons with an indicator of the current sort.

## Toasts and inline messages

- Inline messages for results of the user's action, at the place of the action. Toasts for background events.
- Toasts: stack consistently, don't cover primary actions, stay long enough to read (or until dismissed when they
  contain an action), announced politely to screen readers.

## Fine details checklist

- Concentric radii on nested elements.
- One border width per family; hairlines at 1px, not 0.5px (which renders inconsistently).
- Shadows tinted to the ground, layered, and only for elevation.
- Optical centring of labels and icons.
- `min-height`, not `height`, on anything containing text.
- No width change between states.
- Focus rings unclipped and visible in forced-colours mode.
- Designed fallbacks for empty, missing and overflowing content.
- `cursor: pointer` on interactive non-link elements is a convention on the web; follow the project's existing
  choice consistently.
