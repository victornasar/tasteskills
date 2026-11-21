---
name: a11y
description: Make a website usable by people with disabilities as part of its design quality, meeting WCAG 2.2 AA as the floor. Covers the POUR principles, semantic HTML and landmarks, headings, keyboard access and focus order, visible focus, screen reader names and announcements, colour contrast and use of colour, accessible forms and errors, accessible custom widgets, reduced motion, zoom and reflow, touch targets, images and media, and how to test with real tools. Use when building or reviewing any page or component, before calling work done, or when asked about WCAG, ARIA, screen readers or keyboard support. Not a substitute for testing with disabled users when the stakes are high.
argument-hint: "[page, component or flow]"
---

# a11y

Accessibility is whether the design works for the people who use it: someone navigating by keyboard, listening
with a screen reader, zoomed to 300%, using a phone with tremor, colour-blind, in bright sun, or with a cognitive
disability. A page that fails them isn't a well-designed page with a compliance gap; it's a page that doesn't
work. Build it in from the first element, and test it with the tools disabled people use.

Page, component or flow:

$ARGUMENTS

If this is empty, audit the current project's main pages and flows.

## Where this sits

This skill sets the requirements and test methods. Other skills apply them in their own domain:
`interaction` (behaviour, errors), `components` (focus rings, states), `palette` (contrast
calculation), `motion` (reduced motion), `responsive` (reflow, touch), `images` (alt text),
`content` (plain language, link text), `dataviz` (accessible charts). `inspect` notes visible symptoms on the
render (missing focus rings, text over busy images) and hands them here for testing.

The legal baseline in many places is WCAG 2.1 or 2.2 at level AA (for example the European Accessibility Act,
applying since June 2025, and the US ADA Title II rule). Target **WCAG 2.2 AA**.

## Principles

WCAG's four principles, with what they mean on a website:

1. **Perceivable.** Everything conveyed visually is also available another way: text alternatives for images,
   captions for video, structure in the markup not just the styling, contrast enough to see, meaning not carried by
   colour alone, content that survives zoom and reflow.
2. **Operable.** Everything works with a keyboard (and switch devices and voice control, which act like a
   keyboard), focus is visible and in a logical order, nothing traps focus, there's enough time, nothing flashes,
   targets are big enough, and gestures have simple alternatives.
3. **Understandable.** Language is plain, labels and instructions are clear, behaviour is predictable (no
   surprise context changes), errors are identified and explained, help is findable.
4. **Robust.** Standard HTML used as intended, so assistive technologies can read names, roles, states and values.

And three working rules:

- **Native HTML first.** A `<button>` is focusable, activates with Enter and Space, and announces as a button. A
  `<div>` with a click handler is none of those until you rebuild them. The first rule of ARIA is not to use ARIA
  when a native element does the job.
- **Design it, don't patch it.** Focus styles, error states, contrast, target size and reading order are design
  decisions. Retrofitted accessibility looks retrofitted.
- **Test with the tools.** Automated checkers find perhaps a third of issues. The rest needs a keyboard, a screen
  reader and zoom.

## How to work

### 1. Structure

- Landmarks: one `<header>`, `<nav>` (labelled if more than one), `<main>`, `<footer>`; `<aside>` and `<section>`
  with headings where useful.
- One `<h1>`; headings in order without skipping levels for styling. Style is separate from level.
- Lists as lists, tables as tables with `<th>` and `scope`, buttons as buttons, links as links.
- A skip link to `<main>` as the first focusable element.
- `lang` on `<html>`, and on passages in another language.
- Source order matches visual order and reading order.

### 2. Keyboard and focus

- Every interactive element reachable with Tab, in a logical order; no positive `tabindex`.
- Visible focus on everything, with enough contrast against its surroundings (3:1 is the practical target; WCAG
  2.2's 2.4.13 Focus Appearance at AAA defines a full standard). Never `outline: none` without a replacement.
- Focus not hidden behind sticky headers or footers (2.4.11): use `scroll-padding`.
- Dialogs move focus in, trap it while open, close with Escape and return focus to the trigger. Menus and custom
  widgets follow the ARIA Authoring Practices Guide (APG) keyboard patterns.
- No keyboard traps; no actions only available on hover or by dragging (2.5.7 needs a single-pointer alternative to
  dragging).

### 3. Names, roles, states

- Every control has an accessible name that matches its visible label (2.5.3): a visible "Search" button is named
  "Search".
- Icon-only buttons get a name (`aria-label` or visually hidden text).
- Text animated letter by letter or word by word (split, scrambled or wave reveals) still reads as one phrase.
  Split spans make screen readers spell it out, and scrambles expose garbage while they run. For headings and
  running text, keep the complete text in a visually hidden element and set `aria-hidden="true"` on the split
  spans; `aria-label` on a plain `div`, `span` or heading is prohibited or announced unreliably. Buttons and
  links can take an `aria-label` that matches the visible text. Either way, the accessible text is the final
  text from the first frame and never changes during the animation. With reduced motion, render the final
  text straight away.
- States are exposed: `aria-expanded` on disclosure triggers, `aria-current` for current page or step,
  `aria-pressed` for toggle buttons, `aria-selected` in tabs, `aria-invalid` on fields in error.
- Dynamic updates that the user needs to know about are announced: a polite live region (`role="status"`) for
  "Saved" or "3 results", an assertive one (`role="alert"`) only for urgent errors.

### 4. Perception

- Text contrast 4.5:1 (3:1 for large text, 24px or 18.66px bold); non-text contrast 3:1 for control boundaries,
  focus indicators, icons that carry meaning and chart elements (1.4.3, 1.4.11). Calculate, don't estimate
  (`palette` shows how).
- Colour never the only signal: errors, links in body text, status, chart series and required fields need a
  second cue (text, icon, underline, pattern).
- Images: meaningful `alt`, `alt=""` for decorative ones; complex images (charts, diagrams) get a text
  equivalent nearby.
- Video and audio: captions, transcripts, and no autoplay with sound.
- Reflow at 320 CSS px and 400% zoom without two-dimensional scrolling (1.4.10); text resizable to 200% (1.4.4);
  increased text spacing doesn't break layout (1.4.12).
- Content on hover or focus is dismissible, hoverable and persistent (1.4.13).

### 5. Forms

Visible labels tied with `for`/`id`; grouped fields in `<fieldset>` with `<legend>`; hints and errors linked
with `aria-describedby`; required fields marked in text; `autocomplete` on personal data fields (1.3.5); errors
identified in text and announced, with a linked error summary on submit; no time limits without a way to extend;
no CAPTCHA or memory test without an alternative (3.3.8). `interaction` covers the behaviour.

### 6. Motion and time

Respect `prefers-reduced-motion`; a pause control for anything that moves, blinks or auto-updates for more than
five seconds (2.2.2); nothing flashing more than three times per second (2.3.1). See `motion`.

### 7. Touch and pointer

Targets at least 24 × 24 CSS px or adequately spaced (2.5.8, AA), and 44 × 44 for primary touch targets as good
practice; actions fire on release, not press, so they can be cancelled (2.5.2).

### 8. Test

Use `references/testing-checklist.md` for the full checklist and commands. The minimum before calling a page
done:

1. **Automated:** run axe (axe-core via the browser extension, `@axe-core/playwright`, or Lighthouse's
   accessibility audit). Fix every violation; treat a clean run as the start, not the end.
2. **Keyboard:** unplug the mouse. Tab through the whole page and every flow. Can you see focus at every step,
   reach and operate everything, escape every overlay, and finish the task?
3. **Screen reader:** VoiceOver (macOS/iOS) or NVDA (Windows). Navigate by headings and landmarks, then
   through the main flow. Is every control named, every state announced, every update heard?
4. **Zoom and reflow:** 200% and 400% browser zoom, and a 320px-wide viewport. Nothing clipped, overlapped or
   lost.
5. **Contrast and colour:** check contrast of every text and UI pair; view the page in grayscale and with a
   colour-blindness simulation (Chrome devtools rendering emulation).
6. **Reduced motion and forced colours:** emulate both. Everything still works and stays visible.
7. **Accessibility tree:** inspect it in devtools (or Playwright's `ariaSnapshot`) for names, roles and order.

Report what was tested, with which tools, what failed and was fixed, and what remains (with the WCAG criterion).

## Mistakes agents make

- `<div>` and `<span>` buttons; links with `href="#"` that act as buttons.
- `outline: none` for a cleaner look, with no replacement focus style.
- ARIA added on top of native semantics (`role="button"` on a `<button>`), or ARIA roles without the keyboard
  behaviour they promise.
- Headings chosen for size, skipping levels or used for non-headings.
- Placeholder-only labels; errors shown only in red; errors not announced.
- Low-contrast grey text for "subtle" secondary content; light placeholder text carrying instructions.
- Icon-only buttons without names; alt text like "image" or the filename; descriptive alt on decoration.
- Modals that don't trap or return focus; menus that can't be closed with Escape.
- Animations that ignore reduced motion; carousels that auto-advance without pause.
- Treating a perfect Lighthouse score as proof of accessibility.
