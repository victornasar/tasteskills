---
name: responsive
description: Adapt a website across phones, tablets, laptops and wide screens by redesigning for each context instead of shrinking the desktop. Covers choosing mobile-first or desktop-first, breakpoints set by content, container queries, adapting content and order, device-specific art direction, touch targets and input modes, mobile navigation, fluid typography, responsive images and complex layouts (tables, multi-column grids, dashboards, wide media) on small screens. Use when building or reviewing any layout that must work at more than one size, or when a page "works on desktop but feels wrong on a phone". Not for the composition of each size (`compose`) or image file weight (`performance`).
argument-hint: "[page, component or layout]"
---

# responsive

A responsive page is one design solved several times, for different screens, inputs and situations. The phone
isn't a small desktop: it's held in one hand, touched instead of pointed at, used in daylight and on the move,
and seen one narrow column at a time. Decide what each context needs, then build the changes between them.

Page, component or layout:

$ARGUMENTS

If this is empty, review the current project's pages at several widths.

## Where this sits

- `compose` decides the composition at each size (its "Phone translation" section). This skill decides when
  and how the layout changes between sizes, and builds the mechanics.
- `images` decides what each crop shows; this skill delivers the right crop at the right size; `performance`
  keeps the files light.
- `interaction` owns behaviour; this skill adapts it for touch, keyboard and mouse. `a11y` owns
  the WCAG requirements for reflow, zoom and target size.

## Principles

1. **Design from the content's needs, not device names.** Breakpoints go where the content breaks: where a line
   gets too long, a row too cramped, a table unreadable. Device widths change every year; content limits don't.
2. **Adapt, don't shrink.** Each context may need different order, density, crops, navigation and even content
   emphasis. Scaling everything down keeps the desktop's decisions where they no longer fit.
3. **Input is not screen size.** A large touchscreen, a small laptop with a mouse, a tablet with a keyboard.
   Test capabilities (`hover`, `pointer`) rather than assuming from width.
4. **The phone is often the primary context.** For many audiences (local businesses, services, events, anything
   shared on social), most visits are on phones. Design that first when the audience says so.
5. **Everything must reflow.** Content works at 320 CSS pixels wide and at 400% zoom without horizontal scrolling
   (WCAG 1.4.10), except things that genuinely need two dimensions, like large tables and maps.

## Mobile-first or desktop-first

| Approach | Means | Choose when |
| --- | --- | --- |
| Mobile-first | Base styles are the narrow layout; `min-width` queries add complexity | Most visits are on phones; content is linear; you want the simplest version to be the default |
| Desktop-first | Base styles are the wide layout; `max-width` queries simplify | The product is used mainly at a desk (dense tools, dashboards, admin); the narrow version is a reduced companion |
| Intrinsic | Layouts that adapt without breakpoints (`auto-fill`, `minmax`, `flex-wrap`, `clamp`), plus a few queries | Components reused in many contexts; catalogues, card grids, galleries |

Whichever you choose, *design* both ends. "Mobile-first" CSS with an un-designed phone layout is still a shrunk
desktop.

## How to work

### 1. List the contexts

Write down who uses the page on what, and doing what: "on a phone outside the shop, checking if it's open", "at a
desk comparing plans", "on a tablet in the kitchen following a recipe". Each context gets a first-screen priority
(`hierarchy`'s ranking may change between them).

### 2. Plan what changes

For each section, decide per context:

- **Order and emphasis.** What comes first on the phone? Is it the same as desktop? The source order should suit
  the narrowest layout and reading order; rearranging visually with grid is fine within a section, but large
  reorders that break reading order fail keyboard and screen-reader users.
- **Content.** Same content everywhere by default. Shorten or collapse secondary content on small screens (a
  disclosure, a "show all"), but never hide what someone needs to complete a task.
- **Layout.** Columns to rows, sidebars to disclosures or bottom sections, grids to fewer columns or horizontal
  scrollers (with care), tables to the patterns in `references/adaptation-patterns.md`.
- **Navigation.** See below.
- **Images.** Which crop at which ratio (`images` decides), delivered with `<picture>` or `srcset`.
- **Type and space.** Fluid sizes with limits; section spacing reduces more than component spacing.

### 3. Choose breakpoints

- Start narrow and widen the viewport slowly. Add a breakpoint where the layout stops working, and name it for
  what changes (`--bp-two-columns`), not for a device.
- Prefer **container queries** (`@container`) for components that appear in different-width slots: a card in a
  sidebar and in a main column should adapt to its container, not the viewport.
- Use `clamp()` to remove breakpoints for type and spacing.
- Check the in-between widths (about 600–900px is where most layouts break) and wide screens (1920 and up).

### 4. Design for touch and input

- Touch targets: aim for at least 44 × 44 CSS px for primary controls (Apple's guidance; Material uses 48dp).
  WCAG 2.2's AA minimum is 24 × 24 with spacing. Extend the hit area with padding or a pseudo-element without
  making the visual bigger when needed.
- Space adjacent targets so a thumb doesn't hit two.
- Put frequent actions within thumb reach on phones (lower half, or a sticky bottom bar for the one main action).
- Don't depend on hover. Anything revealed on hover must have a touch and keyboard equivalent. Gate hover-only
  effects with `@media (hover: hover) and (pointer: fine)`.
- Inputs: the right `type` and `inputmode` (numeric keypad for codes, email keyboard for email), `autocomplete`
  for known fields, font size at least 16px so iOS doesn't zoom on focus.

### 5. Mobile navigation

Choose from the number and importance of destinations:

| Pattern | Fits | Watch for |
| --- | --- | --- |
| All links visible (wrapped or a short row) | Three to five destinations | Wrapping into a messy second line |
| Bottom tab bar | Apps and app-like sites with 3–5 frequent destinations | Unusual on content sites; needs safe-area padding |
| Menu button opening a full or partial panel | Many destinations | Hides navigation; label it "Menu", not just three lines, when the audience may not know the icon |
| Priority+ (visible links plus "More") | Several destinations of unequal importance | Needs a sensible priority order |
| No nav, one action | Single-purpose pages | Users still need a way home |

Keep the most important action visible outside the menu (Book, Call, Order). Mobile menus must trap focus while
open, close with Escape, and return focus to the button (see `interaction` and `a11y`).

### 6. Build

- Use the viewport meta tag, `dvh`/`svh` instead of `100vh` for full-height layouts on mobile browsers, and
  `env(safe-area-inset-*)` for notches and home indicators.
- Never set fixed heights on text containers; text wraps differently at every width and at 200% zoom.
- Use intrinsic grids (`repeat(auto-fill, minmax(16rem, 1fr))`) where items are parallel.
- Prevent overflow: long words, URLs and emails need `overflow-wrap: anywhere` in narrow containers; images and
  embeds need `max-width: 100%`.
- Test with real content lengths, including the longest name and a translated string.

### 7. Check the render

Capture at 320, 390, 768, 1024, 1440 and 1920 wide, plus a slow drag through the widths in between if your tool
allows. Then:

1. **Horizontal scroll.** Any at any width? (`document.documentElement.scrollWidth > innerWidth`)
2. **The phone's first screen.** Does it answer the phone visitor's first question? Is the main action visible or
   one tap away?
3. **Breakpoint seams.** Look just above and below each breakpoint for cramped columns, orphaned items and lonely
   single cards in a row.
4. **Touch.** Measure target sizes and spacing on the phone render. Is anything hover-only?
5. **Navigation.** Open and close the menu with touch and with the keyboard.
6. **Type.** Headlines wrap into a few balanced lines on a phone; body is at least 16px; line lengths stay
   readable on wide screens.
7. **Images.** Each crop shows its subject at each width.
8. **Zoom and reflow.** At 200% zoom and at 320px, nothing is clipped, overlapped or lost.
9. **Wide screens.** At 1920+, is the content stranded, stretched or too far apart?

Report the contexts, what changes between them and why, the breakpoints and what each one changes.

## Mistakes agents make

- Designing at 1440 and letting CSS stack the columns: the phone gets the desktop's order, a giant hero image
  before any answer, and desktop spacing.
- Breakpoints copied from a framework (640/768/1024/1280) with no relation to the content.
- `100vh` heroes that hide content behind mobile browser bars.
- A hamburger menu for three links; the primary action hidden inside it.
- Hover-only menus, tooltips and reveals.
- Tables squeezed to illegibility or with columns silently dropped.
- Fixed heights that clip text at another width or zoom.
- Tiny tap targets packed together; inputs under 16px that zoom the page on iOS.
- Testing only at 390 and 1440, never in between.
