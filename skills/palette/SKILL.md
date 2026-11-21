---
name: palette
description: Develop a colour direction and a working colour system for a website, product or brand. Reads the brief's positioning and setting, proposes clearly different ground + figure directions, checks contrast properly, and writes the palette into the project as CSS variables, a Tailwind theme or design tokens. Use when choosing colours or a palette, replacing a generic default palette, or reviewing a page's colour.
argument-hint: "[brief, e.g. neighbourhood bakery]"
---

# palette

Choose colour as a design decision that follows from the brand, then make it work as a system: roles, contrast,
states, light and dark.

Brief:

$ARGUMENTS

If the brief is empty, infer one from the project (its name, README and any existing brand colours in CSS
variables, the Tailwind theme or tokens) and say what you inferred. An existing brand colour is a fact to build
around, not something to replace.

## What a direction is

Award galleries describe a site by its main colours. Think about a direction the same way, as a **pair** with a
proportion:

- **Ground:** the background and the largest surfaces.
- **Figure:** the main colour on top of it: headings, type, logo.
- **Accent** (optional): a small amount of a third colour reserved for one job, such as actions, prices or
  highlights.
- **Proportion:** roughly how much each covers (for example 85/12/3). The same two colours read completely
  differently at 90/10 and at 50/50.

Body text, muted text, borders, tints and shades are derived from the pair.

## 1. Read the brief

- **Positioning:** sophistication, intended perception, what it should feel like against the alternatives. If
  `taste` wrote a `DIRECTION.md`, use it.
- **Setting:** a dark room or screen, printed on white, photography-led (the photos carry the colour), a working
  interface with data and states.
- **Constraints the user gave:** "no gold", "must work in dark mode", "avoid the usual colours for this
  industry".

Note your assumptions briefly. Don't apply stereotypes: a religious, cultural or national descriptor doesn't imply
a colour.

## 2. Know the conventions, and their evidence

A category convention is context you can follow or depart from, never a rule. State one only with its real
strength:

| Convention | Evidence | Confidence |
| --- | --- | --- |
| Blue leads in finance | Blue in 31% of finance logos, red close behind at 28% (secondary summary). Newer fintech departs more often | Medium. The repeated "60–90% of banks use navy" has no traceable source; don't use it |
| Blue in technology | About 60% of tech logos, from an analysis of 14,000+ logos (secondary summary). Software sub-categories untested | Medium |
| Blue in healthcare | Reported as dominant; many wellness brands now avoid the clinical look | Low. The "85% of healthcare logos" figure is unverified |
| Luxury: black, or black and white | The curator's taste rule: severe and restrained without a metallic cue | Taste, not frequency |
| Luxury: gold on black | Conventional premium signalling, easy to do badly. If used, keep it scarce and flat | Flag it as a cliché risk |

Commonly repeated but unverified, so don't state them: red dominates food and beverage, fitness uses dark grounds
with red or orange, green is the default for sustainability and wellness.

**No colour psychology claims.** "Blue builds trust" and "red makes people hungry" aren't established. The
research is early, often underpowered, depends on context and mostly ignores chroma (Elliot 2015). Colour–emotion
associations are broadly shared across 30 nations but vary by country, and they concern colour *words*, not a
specific shade in a brand (Jonauskaite et al. 2020). Describe what a palette looks like and what it's for, not
what it will make people feel.

## 3. Know what good sites actually do

From every Awwwards Site of the Day, 2009–2026 (6,295 sites; exact colours for 2023 onward), plus a visual review
of 320 thumbnails:

- **Most award pairs are neutral.** 49% of two-colour pairs are neutral (both colours near grey) and 15% are pure
  black and white. Neutral grounds split cleanly into dark (L 0–0.30) and light (L 0.80–1.0), with almost nothing
  in between.
- **When they use colour, it's usually vibrant.** 73% of chromatic colours are vibrant, and many sit at the
  maximum chroma sRGB allows. Muted, dusty "tasteful" palettes are rarer than agents assume.
- **About a third have no flat pair at all.** A photograph or illustration fills the frame and carries the colour.
  "Imagery plus one type colour" is a real direction.
- **The AI default** is the opposite of all this: a white ground, a blue-to-purple gradient and an indigo or
  violet button. In the lab corpus, decorative gradients appeared on 87% of AI-built landing pages.

Award frequency says what juries liked, not what suits a brief. Use it to widen what you consider, not as a quota.

## 4. Build in OKLCH

OKLCH (`oklch(L C H)`) separates lightness (0–1), chroma (colourfulness, 0 upward) and hue (degrees), and its L
tracks perceived lightness far better than HSL. Use it to design, and output HEX alongside for compatibility.

- **Hue angles aren't the paint wheel.** sRGB red sits at about 29°, yellow 110°, green 142°, blue 264°. An OKLCH
  "opposite" isn't an RYB complement.
- **Chroma isn't comparable across hues.** The maximum sRGB can show depends on lightness and hue: an emerald at
  L 0.47 maxes out near C 0.10, while a blue at the same lightness can reach about 0.27. Judge saturation by both C
  and how close the colour sits to its limit.
- **Neutrals:** C up to about 0.04 behaves as neutral; around 0.02 is at the edge of visible. A typical cream is
  about C 0.027. A tinted neutral ties greys to the brand; pure black and white are a deliberate choice, not a
  mistake.
- **Tints and shades:** hold the hue, step L, and keep chroma proportional to what each lightness allows.
  Holding C constant pushes light and dark steps out of gamut. Give each step a job (background, border, fill,
  text) rather than generating ten steps nobody uses.
- **Stay in gamut.** Check that every colour you ship is displayable in sRGB. Clamping RGB shifts the hue;
  reduce chroma instead.
- **Harmony labels describe, they don't prove.** Monochromatic, analogous and complementary are vocabulary.
  Research on pair harmony shows that lightness and chroma relationships matter as much as hue (Ou and Luo
  2006). A palette is good because it looks right for the brief, not because it fits a scheme.

`references/directions.md` holds 51 curated directions with their values. Use them as starting points, as
evidence of what a specific direction looks like, or to break your own habits. Building your own is just as
valid.

## 5. Check contrast properly

WCAG 2.2 is the standard:

| Use | Minimum |
| --- | --- |
| Body text | 4.5:1 |
| Large text (24px, or 18.66px bold) | 3:1 |
| Interface components, focus rings, meaningful graphics | 3:1 |
| Logos, inactive controls | Exempt |

- **Calculate, never estimate.** Relative luminance is `0.2126R + 0.7152G + 0.0722B` on linearised sRGB channels
  (threshold 0.04045); the ratio is `(L1 + 0.05) / (L2 + 0.05)`. Run a few lines of code to compute it. Don't
  round up: 4.499:1 fails 4.5:1.
- A ratio proves only that a specific pair passes, so record pairs with their intended use ("figure on ground,
  body text, 11.2:1").
- Never carry meaning by hue alone. About 5–8% of men have a colour vision deficiency, mostly red-green, so
  status needs a label, an icon or a shape as well.
- APCA isn't a standard: it was dropped from the WCAG 3 drafts.

## 6. Propose directions

Offer 3–5 directions that are **clearly different**: different structure (neutral, one chromatic colour, two
hues, monochrome, image-led), different foundation (light or dark ground), different proportion. "Warm cream"
and "soft linen" are the same direction. Follow a category convention in at most one of them, and say so.

For each direction give:

- the ground, figure and accent, in OKLCH and HEX, with the rough proportion;
- why it fits, in the brief's words, with any interpretation marked as interpretation;
- **choose if** (the situation where it's the right answer) and **watch out** (where it fails: photography it
  depends on, print, an accent that reads as an error);
- the key contrast numbers you calculated;
- the open questions that would change the recommendation.

Then recommend one and say what would make you pick another. If the user asked you to choose, or you're
mid-build, pick, apply it and tell them in a line or two what you chose, why, and the main alternative.

## 7. Apply it as a system

Write the palette into the project's existing theme: CSS custom properties, a Tailwind v4 `@theme` block or
design tokens. Name tokens by role, not by hue:

```css
:root {
  --color-ground: oklch(0.25 0.025 55);  /* #2B1F16  page background, large surfaces */
  --color-figure: oklch(0.92 0.02 80);   /* #ECE3D6  headings, type, logo */
  --color-accent: oklch(0.7 0.12 65);    /* #D18E46  prices and actions only */
  --color-text: …;  --color-text-muted: …;  --color-border: …;
}
```

- Derive text and muted-text colours from the pair, and check them on every surface they appear on.
- Interfaces need states: hover, focus, disabled, and success, warning and error colours that don't clash with
  the accent (a red accent and a red error are a problem; define them apart).
- For dark mode, design a counterpart rather than inverting: grounds rarely go to pure black, and saturated
  colours need less chroma on dark grounds.

## 8. Look at it rendered

Numbers are necessary but not sufficient. A colour looks different beside its neighbours (simultaneous
contrast), saturated colours look brighter than their luminance suggests, and an accent that worked in a swatch
can take over a full page. Look at the built page on desktop and phone. Check that the proportion matches the
direction, that the accent stays reserved for its one job, that photography and colour aren't fighting, and that
the page doesn't look like the AI default (white, gradient, purple button) unless the brief chose that on purpose.
