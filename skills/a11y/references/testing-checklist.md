# Accessibility testing checklist

A working checklist mapped to WCAG 2.2. Levels: A and AA are the target; AAA items are noted where they're
practical good practice. Criterion numbers let you look up the full text and its Understanding document on w3.org.

## Automated checks

Automated tools catch missing names, contrast failures, missing labels, invalid ARIA and some structure problems.
They can't judge whether alt text is meaningful, focus order is logical or an error message is helpful.

```js
// Playwright with axe-core (npm i -D @axe-core/playwright)
import AxeBuilder from '@axe-core/playwright';
const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
console.log(results.violations.map(v => `${v.id}: ${v.nodes.length} × ${v.help}`));
```

```js
// Accessibility tree snapshot (Playwright 1.49+): names, roles and order as assistive tech sees them
console.log(await page.locator('body').ariaSnapshot());
```

Run them on every page template and in each significant state (menu open, dialog open, form with errors).

## Manual checklist

### Structure and semantics

- [ ] Page has a unique, descriptive `<title>` (2.4.2)
- [ ] `<html lang>` set; language changes marked (3.1.1, 3.1.2)
- [ ] Landmarks present and labelled where repeated
- [ ] One `h1`; heading levels reflect structure (1.3.1, 2.4.6)
- [ ] Skip link to main content works (2.4.1)
- [ ] Lists, tables, buttons, links use the right elements (1.3.1, 4.1.2)
- [ ] Reading and focus order match the visual order (1.3.2, 2.4.3)

### Keyboard

- [ ] Everything operable by keyboard (2.1.1)
- [ ] No keyboard trap (2.1.2)
- [ ] Focus visible everywhere (2.4.7); focus indicator has strong contrast and size (2.4.13, AAA, good practice)
- [ ] Focused element not hidden by sticky content (2.4.11)
- [ ] Single-key shortcuts can be turned off or remapped (2.1.4)
- [ ] Custom widgets follow APG keyboard patterns (tabs: arrows; menus: arrows, Escape; dialogs: trap, Escape)

### Names, roles, values

- [ ] Every control has an accessible name (4.1.2)
- [ ] Visible label text is part of the accessible name (2.5.3)
- [ ] Link text makes sense out of context, or with its sentence (2.4.4); no "click here" lists
- [ ] States exposed (`aria-expanded`, `aria-current`, `aria-pressed`, `aria-selected`, `aria-invalid`)
- [ ] Status messages announced without moving focus (4.1.3)

### Visual

- [ ] Text contrast ≥ 4.5:1; large text ≥ 3:1 (1.4.3)
- [ ] UI component boundaries, focus indicators and meaningful graphics ≥ 3:1 (1.4.11)
- [ ] Colour not the only way to convey information (1.4.1)
- [ ] Text resizes to 200% without loss (1.4.4)
- [ ] Reflows at 320 CSS px without horizontal scrolling, except tables, maps and similar (1.4.10)
- [ ] Text spacing override (line height 1.5, paragraph spacing 2×, letter spacing 0.12em, word spacing 0.16em)
      doesn't clip or overlap (1.4.12)
- [ ] Hover and focus content is dismissible, hoverable, persistent (1.4.13)
- [ ] No images of text where real text would do (1.4.5)

Text spacing bookmarklet equivalent:

```css
* { line-height: 1.5 !important; letter-spacing: 0.12em !important; word-spacing: 0.16em !important; }
p { margin-bottom: 2em !important; }
```

### Images and media

- [ ] Meaningful images have alt text describing their purpose (1.1.1)
- [ ] Decorative images have `alt=""` or are CSS backgrounds
- [ ] Complex images (charts, diagrams) have a text equivalent
- [ ] Video has captions (1.2.2); audio-only and video-only have transcripts or descriptions (1.2.1); audio
      description where needed (1.2.5)
- [ ] No auto-playing audio over three seconds without a control (1.4.2)

### Forms

- [ ] Labels or instructions for every input (3.3.2), programmatically associated (1.3.1)
- [ ] Purpose of personal data fields identified with `autocomplete` (1.3.5)
- [ ] Errors identified in text (3.3.1) with suggestions (3.3.3)
- [ ] Legal, financial or data-changing submissions can be reviewed, corrected or reversed (3.3.4)
- [ ] No re-entering information already given in the same process (3.3.7)
- [ ] Authentication doesn't require a cognitive test without an alternative; paste and password managers allowed
      (3.3.8)
- [ ] Changing a setting doesn't change context unexpectedly (3.2.2)

### Motion, time, seizures

- [ ] Moving, blinking or auto-updating content over five seconds can be paused (2.2.2)
- [ ] Time limits can be extended (2.2.1)
- [ ] Nothing flashes more than three times a second (2.3.1)
- [ ] `prefers-reduced-motion` respected for non-essential motion (2.3.3, AAA, good practice)

### Pointer and touch

- [ ] Targets ≥ 24 × 24 CSS px or spaced (2.5.8)
- [ ] Multi-point or path gestures have single-pointer alternatives (2.5.1)
- [ ] Dragging has a single-pointer alternative (2.5.7)
- [ ] Activation on up-event, cancellable (2.5.2)
- [ ] Motion actuation (shake, tilt) has an alternative and can be disabled (2.5.4)

### Consistency and help

- [ ] Navigation consistent across pages (3.2.3); same functions labelled the same way (3.2.4)
- [ ] Help mechanisms (contact, chat, FAQ) in the same place across pages (3.2.6)

## Screen reader quick reference

| Task | VoiceOver (macOS) | NVDA (Windows) |
| --- | --- | --- |
| Start / stop | Cmd + F5 | Ctrl + Alt + N / Insert + Q |
| Read next item | VO (Ctrl + Option) + Right | Down arrow |
| List headings | VO + U, then arrows to Headings | H to jump; Insert + F7 for list |
| Jump by landmark | VO + U, Landmarks | D |
| Jump by form field | VO + U, Form Controls | F |
| Activate | VO + Space | Enter |

Test the main flow end to end, not just the homepage. Listen for: unnamed buttons ("button"), missing state
changes, focus jumping to the top of the page, content announced twice, and decorative noise ("image, image,
image").

## Accessible patterns worth reusing

- **Visually hidden text** (for names that shouldn't show):

  ```css
  .visually-hidden {
    position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
    overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
  }
  ```

- **Disclosure:** `<button aria-expanded="false" aria-controls="panel">`, or `<details>`/`<summary>`.
- **Dialog:** `<dialog>` with `showModal()`; label with `aria-labelledby` pointing at its heading.
- **Error summary:** a `role="alert"` region or focused heading listing errors as links to fields.
- **Live status:** `<p role="status">` updated with text such as "12 results" or "Saved".
