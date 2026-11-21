---
name: components
description: Build interface components that look and feel finished. Covers buttons, inputs and forms, navigation, cards, dropdowns and menus, modals and dialogs, tabs, tooltips and popovers, every state and variant, and the fine details (borders, radii, shadows, padding, alignment, text fit, icon placement, hit areas) that separate a polished component from a generated one. Use when building or reviewing individual components, a component library, or any UI that looks "almost right". Not for which states and behaviour exist (`interaction`), the token system behind components (`design-system`) or ARIA patterns (`a11y`).
argument-hint: "[component or set of components]"
---

# components

Craft is the difference between a component that works and one that feels made with care: the label sits
optically centred, the focus ring doesn't clip, the radius of the inner element fits the outer one, the button
doesn't change width when it starts loading. These details are individually small and collectively what people
mean by "polished". Build them deliberately, in the brand's own language, and inspect them at real size.

Component or components:

$ARGUMENTS

If this is empty, review the components in the current project.

## Where this sits

- `interaction` decides behaviour and which states exist. `components` makes each state look right.
- `design-system` defines the tokens and variants; this skill uses them and reports when they don't cover a
  case. `a11y` owns semantics and keyboard patterns; build on the native element or the correct
  pattern, then craft its look.
- `taste` and the direction set the surface language (edges, corners, depth, texture). Components express it;
  they don't pick their own.

## Principles

1. **Native first.** Start from `<button>`, `<a>`, `<input>`, `<select>`, `<dialog>`, `<details>`, the popover
   attribute. They bring behaviour and accessibility for free. Style them; don't rebuild them from `<div>`s.
2. **Every state is designed.** Default, hover, focus-visible, active, disabled, loading, selected, error. A
   component with only a default state isn't finished.
3. **Consistent anatomy.** Components of the same family share heights, paddings, radii, borders and type
   sizes, so a button sits on the same line as an input and a select next to it.
4. **Optical, not mathematical.** Align and size by what the eye sees: text in a button with no descenders looks
   high; icons need nudging; round shapes need to be slightly larger to look the same size as square ones.
5. **Surface follows direction.** Radii, borders, shadows and texture are the brand's surface position, not a
   framework's default. Flat and square, soft and rounded, layered with depth: each is right for some brief.
   Rounded boxes everywhere is `layout`'s overused pattern; it's slop because it arrives regardless of brief.
6. **Details survive content.** Long labels, missing images, translated strings, two-line titles, large numbers.
   Build for the real range, not the demo string.

## How to work

### 1. Spec the component before styling

For each component, write: its job, its variants (size, emphasis, tone), its states, its content range (shortest
and longest label, with and without icon, one line and wrapped) and where it appears. Check the design system's
tokens cover it.

### 2. Build the anatomy

Use `references/component-specs.md` for per-component detail. The cross-cutting rules:

- **Sizing.** Define a small set of control heights (for example 32, 40, 48px) and use the same set for buttons,
  inputs and selects so they align in a row. Height comes from padding plus line height, not a fixed `height`
  that clips wrapped or zoomed text; use `min-height`.
- **Padding.** Horizontal padding larger than vertical (often about 1.5–2.5×). Padding on the icon side of a button
  with an icon is slightly smaller so the content looks centred.
- **Radii.** Choose from the direction. Nested elements use `inner radius = outer radius − gap` so curves stay
  concentric. A pill shape on a button and a 4px corner on the card it sits in is a mismatch unless deliberate.
- **Borders.** One width for the family (1px is typical; 1.5–2px reads sturdier). Borders on interactive controls
  must meet 3:1 contrast against the background (WCAG 1.4.11) unless the control has another visible boundary.
- **Shadows.** Shadows imply elevation. Use them for things that genuinely float (menus, dialogs, sticky bars),
  layered as a soft ambient shadow plus a tighter key shadow, tinted toward the ground colour rather than pure
  black. A shadow on every card flattens the depth system into texture.
- **Type.** Controls use the UI role from `fonts`, with tabular figures where numbers change. Labels in buttons
  are verbs or short phrases in sentence case unless the brand's voice says otherwise.
- **Icons in controls.** Sized to the text (usually 1–1.25× the font size), aligned to the text's optical centre,
  a consistent gap. See `icons`.
- **Hit area.** At least 24×24 CSS px (WCAG 2.2 AA), and 44×44 for primary touch targets. Enlarge with padding or
  a pseudo-element when the visual must stay small.

### 3. Design the states

| State | Craft notes |
| --- | --- |
| Hover | A clear but small change (background shift, underline, border darken). Gate with `@media (hover: hover)` |
| Focus-visible | A ring with at least 3:1 contrast against both the component and the background, offset so it doesn't touch the edge (`outline: 2px solid; outline-offset: 2px`). Use `outline`, which isn't clipped by `overflow: hidden` on the element itself and survives forced-colours mode, rather than `box-shadow` alone |
| Active | Slightly darker or inset; near-instant |
| Disabled | Reduced contrast but still legible, `cursor: not-allowed` on pointer devices, no hover effect |
| Loading | Keep the width (reserve the label space or set `min-width`), show a spinner or progress in place, keep the label for context |
| Selected / current | Distinct from hover and focus; not colour alone (a weight change, an indicator bar, a check) |
| Error | Border plus icon plus message; colour alone is not enough |

### 4. Check fine details

- Text optically centred in buttons and badges (check fonts with tall ascenders or no descenders).
- Focus rings not clipped by parent `overflow: hidden`.
- No layout shift when hover, focus, bold-on-select or loading states apply (bold text changes width: reserve it
  or use a different signal).
- Icon and text baselines line up across a row of components.
- Truncation is deliberate: `text-overflow: ellipsis` with the full text available (a tooltip or `title` is not
  enough on touch); multi-line clamps where titles vary.
- Placeholder images and missing data have designed fallbacks (initials avatar, neutral thumbnail), never broken
  image icons.
- Dark mode and forced-colours (Windows High Contrast) don't lose borders or focus rings: test with
  `forced-colors: active` emulation.

### 5. Inspect at real size

Render the component in every state and variant, side by side, at 1× and 2× device pixel ratio, in light and
dark if both exist. A state sheet (one page showing every variant × state) is the fastest way to see
inconsistency. Then:

1. Zoom to 200–400% on a screenshot and check alignment, centring, concentric radii and border joins.
2. Place components in a row (button, input, select, icon button) and check heights and baselines match.
3. Feed worst-case content: a 40-character button label, a three-line card title, an empty card, a 7-digit number.
4. Tab through to see every focus ring, including inside cards, menus and dialogs.
5. Check at 200% browser zoom and with increased text spacing that nothing clips.
6. Compare against the direction's Surface position: do the radii, borders and shadows say what the direction
   says?

Report each component's variants and states, the surface decisions and their reason, and any token gaps you hit.

## Mistakes agents make

- Only the default and hover states styled; focus rings removed with `outline: none`.
- `rounded-xl shadow-lg` on every card, button and input regardless of the brand.
- Mismatched control heights (a 40px button beside a 44px input).
- Non-concentric nested radii; pill buttons in square cards by accident.
- Buttons that change width when loading or when the label goes bold.
- Gradients, glows and glassmorphism as the default way to look "premium".
- Clickable cards with a nested button and link, both receiving focus and doing different things.
- Custom dropdowns and checkboxes rebuilt from divs without keyboard support.
- Text clipped by fixed heights; truncation with no way to see the full text.
- Icons mis-sized against text, sitting on the line box instead of the optical centre.
