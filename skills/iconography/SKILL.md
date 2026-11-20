---
name: iconography
description: Decide whether a website needs icons at all, and when it does, choose one coherent family and use it with consistent size, stroke, weight, alignment and meaning. Covers when icons help and when words do better, recognisability, choosing and matching icon families, stroke and visual weight, optical sizing and alignment, icon-and-text relationships, icon-only controls, colour, and accessibility. Use when adding, choosing or reviewing icons, icon buttons, feature lists with icons, or navigation icons, or when icons look mismatched or decorative. Not for illustration and photography (imagery) or component anatomy (component-craft).
argument-hint: "[page, component or icon set]"
---

# iconography

An icon is a word in a visual language that only works if people already know it. A few icons are almost
universal (search, close, play, home, menu for many audiences); most are ambiguous without a label. Use icons
where they speed recognition or save space for things people already understand, keep them one consistent family,
and never use them to decorate a list that reads fine as words.

Page, component or icon set:

$ARGUMENTS

If this is empty, review the icons in the current project.

## Where this sits

- `iconography` decides whether an icon is used, which family, and how it sits with text.
- `component-craft` builds the components icons sit in. `imagery` owns illustration and photography.
  `web-accessibility` owns accessible names and contrast rules (summarised here where they affect icons).
- check-layout lists emoji as icons and icon-topped feature cards among the patterns AI-built pages overuse.

## Principles

1. **Icons need a reason.** Good reasons: recognition in a repeated UI (toolbars, navigation people use daily),
   saving space where the meaning is established (close, search, menu), marking status or type consistently
   (warning, success, file types), or scanning long lists where each item has a stable category. A row of three
   feature cards each topped with a generic icon is not a reason; the icon carries nothing the heading doesn't.
2. **Labels beat guessing.** Usability research (Nielsen Norman Group among others) has repeatedly found that
   most icons are ambiguous on their own and that labelled icons perform better. Default to icon plus text; use
   icon-only only for the handful of near-universal symbols, or for space-constrained repeated UI, with an
   accessible name and ideally a tooltip.
3. **One family, one voice.** Mixing families mixes stroke widths, corner styles, perspective and metaphors, and
   it shows immediately. Pick one family that covers the needed set; draw or adapt the few missing ones in the
   same grid and stroke.
4. **Match weight to text.** An icon next to text should feel as heavy as the text beside it: thin-stroke icons
   with bold labels look faint; heavy filled icons with light body text look shouty.
5. **Same meaning, same icon; different meaning, different icon.** One trash icon for delete everywhere; never the
   same icon for two actions.
6. **Style follows the direction.** Outline or filled, rounded or sharp, thin or sturdy, geometric or hand-drawn:
   each says something. A handmade brand with a crisp engineering icon set contradicts itself; so does a precise
   technical brand with bouncy rounded icons.

## How to work

### 1. Decide where icons belong

List each candidate place and answer: does the icon make this faster to recognise, or does it only decorate? If
the label alone works, drop the icon. Common results:

| Place | Usually |
| --- | --- |
| Search, close, menu, play/pause, back, external link, download | Icon (with accessible name; label when space allows) |
| Primary navigation on a content site | Words; icons rarely help |
| App tab bars | Icon plus short label |
| Toolbars in a tool used daily | Icons with tooltips, labels for less common actions |
| Status (success, warning, error) | Icon plus text, consistent across the product |
| Feature lists and benefit cards | Usually no icon; consider numbers, a real image or the product instead |
| Contact details (phone, email, address) | Optional small icons if the list is scanned; text must stand alone |
| Social links | Brand marks (from the brands' own guidelines), labelled for screen readers |

### 2. Choose the family

Shortlist families that cover every icon needed and match the direction. Well-maintained open sets include
Lucide, Phosphor (several weights), Tabler, Heroicons, Material Symbols (variable weight, fill, grade and optical
size) and Iconoir; check the licence and the exact glyphs before committing. Compare:

- **Construction:** stroke or filled; stroke width; corner and terminal shape (round or square caps); grid size
  (usually 24px with 2px padding).
- **Metaphors:** does the set draw "settings", "share", "account" the way your audience expects?
- **Coverage:** all needed icons, without awkward substitutes.
- **Weights:** a set with multiple weights lets you match different text weights.

Brand marks (logos of other companies) come from their brand guidelines, not reinterpreted in your family's style.

Emoji are not an icon family: they render differently on each platform, can't be recoloured, and carry a tone.
Use them only when the brand voice is genuinely playful and they're part of the copy.

### 3. Size and weight

- Size icons relative to the text they sit with: usually 1–1.25× the font size (16px text → 16–20px icon), and
  use a few fixed sizes (for example 16, 20, 24) rather than arbitrary ones.
- Keep stroke width visually consistent across sizes. With SVG strokes, scaling an icon scales its stroke; set
  `vector-effect: non-scaling-stroke` or pick the family's size-specific variants, or adjust `stroke-width` so a
  16px icon and a 24px icon look equally heavy.
- Match the icon's weight to the adjacent text's weight. Use filled variants for selected or active states only if
  the family is designed for it.

### 4. Align optically

- Centre icons on the text's x-height or cap-height optical centre, not the line box. In flex rows,
  `align-items: center` works for single-line labels; for multi-line text, align the icon to the first line.
- Visually asymmetric icons (play triangles, arrows, speech bubbles) need nudging to look centred in a circle or
  square.
- Gap between icon and label: a consistent value, often about 0.4–0.5em.
- Icon-only buttons: square hit areas of at least 24×24 CSS px (44×44 for primary touch targets), with the icon
  centred.

### 5. Colour and contrast

- Use `currentColor` so icons inherit the text colour and its states.
- Icons that convey meaning need 3:1 contrast against their background (WCAG 1.4.11). Purely decorative icons
  don't, but question why they're there.
- Don't rely on icon colour alone for status; the shape and a text label must carry it too.

### 6. Implement

- Inline SVG or an SVG sprite (`<use href="#icon-search">`), not icon fonts (which fail when fonts don't load and
  confuse screen readers).
- Decorative icons next to text: `aria-hidden="true"` and `focusable="false"`.
- Icon-only controls: an accessible name on the button (`aria-label="Close"` or visually hidden text), not on the
  SVG.
- Ship only the icons used.

### 7. Check the render

At real size, at 2×, and on a phone:

1. Cover the labels: could a first-time visitor say what each icon-only control does? If not, add a label.
2. Cover the icons: does anything become harder to understand? If not, the icons are decoration.
3. Do all icons look like one family (stroke, corners, size, perspective)?
4. Do icons look as heavy as their text? Are any visibly larger or fainter than their neighbours?
5. Are icons optically centred with their labels and in their buttons?
6. Is any icon used for two meanings, or two icons for one meaning?
7. Are tap targets large enough on the phone?

Report where icons are used and why, the family and its licence, sizes and weights, and where you chose words
instead.

## Mistakes agents make

- An icon above every feature card heading, from a generic set (lightning bolt for speed, shield for security,
  rocket for launch).
- Emoji as icons.
- Mixing two or three icon sets on one page.
- Icon-only buttons with no accessible name; ambiguous icon-only navigation.
- Icons sized by the line box, sitting low or high against text.
- Thin 1px icons beside bold text, or heavy filled icons beside light text.
- Icons in coloured circles or rounded squares everywhere, adding a container and an extra colour to each.
- Icon fonts; icons that disappear in forced-colours mode because colour was set with backgrounds.
- The same icon for "settings" and "filters", or a heart meaning "save" on one page and "like" on another.
