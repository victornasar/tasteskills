# Token architecture

## Tiers

| Tier | Contains | Used by | Example |
| --- | --- | --- | --- |
| Primitive | Raw values: the palette, the size scale, durations | Semantic tokens only | `--ink-900: oklch(0.22 0.02 260)` |
| Semantic | Roles: what a value is for | Components and page styles | `--color-text: var(--ink-900)` |
| Component | A component's own knobs, only when needed | That component | `--button-padding-x: var(--space-3)` |

Components reference semantic tokens. Page styles reference semantic tokens. Only the theme file references
primitives. That way a theme or rebrand changes one layer.

Skip the component tier until you need it. Most small sites need primitives and semantics only.

## Naming

Pattern: `--{category}-{role}-{variant?}-{state?}`.

- `--color-text`, `--color-text-muted`, `--color-surface`, `--color-surface-raised`, `--color-border`,
  `--color-action`, `--color-action-hover`, `--color-on-action`, `--color-focus`, `--color-danger`,
  `--color-danger-surface`
- `--font-display`, `--font-body`, `--font-mono`
- `--text-body-size`, `--text-body-leading`, or a role shorthand used through utility classes
- `--space-1` … `--space-8` (a scale) plus role aliases where composition benefits:
  `--space-inset` (inside components), `--space-related`, `--space-group`, `--space-section`
- `--radius-control`, `--radius-container`, `--radius-full`
- `--shadow-raised`, `--shadow-overlay`
- `--duration-quick`, `--ease-out`

Avoid names that describe appearance (`--color-blue`, `--shadow-big`). Avoid names that describe a single use
(`--homepage-hero-blue`) unless it's a documented exception.

## Colour

`palette` builds the palette and the role names. A semantic colour set usually needs:

- **Ground and surfaces:** the page, raised surfaces (cards, menus), sunken surfaces (wells, code), overlay
  backdrop.
- **Text:** default, muted, subtle (for placeholders, only if it still meets contrast where it carries meaning),
  on-action (text on the action colour), inverse.
- **Borders:** default, strong (inputs and controls, 3:1 against their background), subtle (dividers).
- **Action:** default, hover, active, disabled; plus `--color-focus` for focus rings.
- **Feedback:** success, warning, danger, info, each with a text colour and a surface tint. Keep danger distinct
  from the brand accent if the accent is red.

Check every text/background pair you actually use, in every theme. Record the pairs and ratios next to the
tokens.

## Typography

Define roles, not just sizes. Each role is a bundle:

```css
:root {
  --text-display: 600 clamp(2.5rem, 1.6rem + 3.6vw, 4.5rem)/1.05 var(--font-display);
  --text-h2: 600 clamp(1.5rem, 1.2rem + 1.2vw, 2.125rem)/1.15 var(--font-display);
  --text-body: 400 1.0625rem/1.55 var(--font-body);
  --text-small: 400 0.9375rem/1.45 var(--font-body);
  --text-label: 600 0.875rem/1.3 var(--font-body);
}
h2 { font: var(--text-h2); }
```

Keep tracking adjustments with the role (display sizes often need slightly negative tracking; small caps or
uppercase labels need positive). Keep the number of roles small; `hierarchy` explains why three visible
levels plus body is usually enough.

## Spacing

A scale gives consistency; roles give meaning. A common approach:

```css
:root {
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem;
  --space-5: 1.5rem;  --space-6: 2.5rem; --space-7: 4rem;    --space-8: 6rem;

  --space-related: var(--space-2);   /* label to field, heading to its text */
  --space-group: var(--space-5);     /* between items in a group */
  --space-section: clamp(var(--space-6), 6vw, var(--space-8));
}
```

Steps should be distinct enough to read as different (`compose`'s proximity rule). A linear 4px scale with
twenty steps invites near-identical choices.

## Elevation and surface

- Two or three elevation levels, each a shadow and (in dark themes) a lighter surface, since shadows don't read on
  dark grounds.
- Radii from the direction's Surface position. If the direction is square and flat, the radius tokens may be
  `0` and `2px`, and that's a system too.

## Variants

| Good reason for a variant | Bad reason |
| --- | --- |
| A different job (primary vs destructive action) | A different page wanted a different colour |
| A different density context (compact table rows) | Someone preferred more rounding |
| A different size for a different input mode (touch vs pointer) | One-off tweaks |

When two variants differ by a single value, consider a token override on a wrapper instead of a new variant.

## Documentation that gets used

A single page in the project (or a section of the README) with: the specimen, each token set with its role, the
component list with variants and states, the documented exceptions, and the rule for adding something new
("check existing variants; add only when two places need it"). Keep it next to the code; documentation elsewhere
goes stale.

## Exceptions register

```markdown
| Exception | Where | Why | Owner |
| Hero headline at 9rem, outside the type scale | Home | The direction's one scale break | design |
| Hand-drawn underline on links in the story section | /about | Signature device | design |
```

An exception without a reason is drift. An exception with a reason is part of the system.
