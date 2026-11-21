---
name: design-system
description: Turn a creative direction into a small, consistent, reusable system of tokens, type, colour roles, spacing, components and variants, so a site stays coherent as it grows without flattening its character into a generic UI kit. Covers token tiers and naming, semantic colour, typography and spacing systems, radii, elevation and motion tokens, component variants, patterns, documentation, and when to break the system. Use when setting up styles for a new project, extracting a system from an existing site, adding a theme or dark mode, or when a site has drifted into inconsistent values. Not for choosing the colours or fonts themselves (`color`, `fonts`) or building individual components (`components`).
argument-hint: "[project or area to systematise]"
---

# design-system

A design system is the direction written down as rules a codebase can follow: a few named decisions that every
page reuses. Its job is consistency where consistency helps people (actions look like actions, spacing means
the same thing everywhere) and freedom where the brand needs a moment of its own. Too little system and the
site drifts; too much and every page looks like the framework it was built with.

Project or area:

$ARGUMENTS

If this is empty, audit the current project's styles: tokens, repeated values and component variants.

## Where this sits

- `taste` sets the direction; `color` and `fonts` choose the colours and faces (`color` already
  defines colour tokens by role). This skill organises those choices, plus spacing, radii, elevation and motion,
  into one system with names and rules.
- `components` builds components from the tokens; `motion` defines motion values; `compose`
  decides how spacing expresses relationships, and this skill names those spacing steps.

## Principles

1. **Name decisions, not values.** `--color-action` and `--space-group` survive a rebrand and tell the next
   developer what a value is for. `--blue-500` and `--space-24` don't.
2. **Tiers keep it changeable.** Primitive values (the palette, the raw scale) feed semantic tokens (roles: text,
   surface, action, border, danger), which feed component tokens only where a component genuinely needs its own
   knob. Components use semantic tokens, never primitives.
3. **Small beats complete.** A system people can hold in their heads (a handful of text styles, six to eight
   spacing steps, two or three radii, three elevations) is used. A 400-token system is worked around.
4. **Systematise what repeats; leave room for what's special.** Buttons, inputs, type roles and spacing should be
   strictly consistent. A hero composition, a signature device or an editorial moment can be a one-off, recorded
   as an intentional exception.
5. **The system encodes the direction.** A design system built from a framework's defaults produces the
   framework's look. The values come from `DIRECTION.md`; the system just names and enforces them.
6. **Consistency is perceived, not measured.** Two greys three lightness points apart, three button heights, five
   border radii: these are what make a site feel unconsidered. Fewer, more distinct values read as intentional.

## How to work

### 1. Inventory

For an existing project, list every distinct value in use: colours, font sizes and weights, line heights, spacing
values, radii, shadows, borders, durations, breakpoints. Group near-duplicates. For a new project, list the
decisions the direction has already made.

### 2. Define the tokens

Use `references/token-architecture.md` for tiers, naming and examples. The core sets:

| Set | Typical size | Notes |
| --- | --- | --- |
| Colour roles | ground, surface, text, text-muted, border, action, action-text, focus, plus success, warning, danger, info | From `color`; each text pair checked for contrast on each surface it appears on |
| Type roles | display, heading levels in use, body, small, label, code | From `fonts` and `hierarchy`; each role is size + line height + weight + tracking, fluid where needed |
| Spacing | 6–8 steps named by role or a t-shirt scale | Composition decides which step expresses which relationship |
| Radii | 2–3 plus "full" | From the direction's Surface position; nested radii stay concentric |
| Elevation | 2–3 levels | Only for things that float |
| Borders | 1–2 widths | |
| Motion | 3–4 durations, 3 easings | From `motion` |
| Layout | content widths, gutters, breakpoints or container sizes | From `compose` and `responsive` |

### 3. Define components and variants

- Variants are the system's vocabulary: `button` has `primary | secondary | tertiary | destructive` and `sm | md |
  lg`. Each variant needs a reason to exist (a different job, not a different look).
- Prefer composition of small parts over many variants: an icon in a button is a slot, not a separate component.
- Document states for each component (`interaction`'s state list) and which tokens each state uses.
- When a new need arrives, first ask whether an existing variant does the job. Add a variant only when two or
  more places need it.

### 4. Keep expression

Write down where the brand's character lives so the system doesn't flatten it:

- **Signature elements** (the direction's signature device, a display style, a particular image treatment) are
  part of the system, documented with when to use them, not stripped out as "inconsistent".
- **Sanctioned exceptions:** a campaign page, an editorial feature, the hero. Record them, with the reason, so
  they're decisions and not drift.
- **Range:** a system can include a quiet mode and a loud mode (a dense product UI and an expressive marketing
  layer) sharing the same roots.

### 5. Implement

- CSS custom properties as the source in the browser, organised by tier. If the project uses Tailwind, define
  the theme from the tokens (Tailwind v4 `@theme`) rather than using its default palette and scale; remove unused
  defaults so off-system values are harder to reach for.
- If tokens must be shared with other platforms, keep a JSON source (the W3C Design Tokens Community Group format
  is the emerging standard) and generate CSS from it.
- Theming and dark mode: swap semantic tokens per theme (`[data-theme="dark"]` and
  `prefers-color-scheme`), never component styles. Check every text pair in every theme.
- Lint where it's cheap: a stylelint rule or a search for raw hex values and pixel values outside the token file.

### 6. Check the render

1. Build or render a **specimen page**: every colour role with its text pairs, every type role in real copy, the
   spacing scale, radii, elevations, and every component in every variant and state, in each theme.
2. Look for values that are too close to tell apart (two greys, two sizes, two radii) and merge them.
3. Render two or three real pages. Search the CSS for values not from tokens, and check whether each is a
   documented exception or drift.
4. Swap test for the system: if you replaced the tokens with a framework's defaults, would the site look much
   different? If not, the system hasn't encoded the direction.
5. Change one semantic token (the action colour, the base radius) and check that it propagates everywhere it
   should and nowhere it shouldn't.

Report the token sets, the variants and why each exists, the documented exceptions, and what you merged.

## Mistakes agents make

- Shipping a framework's default palette and scale as the "design system".
- Tokens named after values (`--gray-200`, `--space-16`) used directly in components.
- Fifty colour shades generated from each hue, most never used.
- A spacing scale that doesn't map to relationships, so the page uses every step at random.
- Variants for every visual difference (`button-blue`, `button-big-rounded`) instead of by job.
- Dark mode by inverting colours rather than designing a second set of semantic values.
- Treating the hero, signature device or editorial layouts as "inconsistencies" to normalise away.
- Hard-coded values in components that bypass the tokens, so a theme change misses them.
