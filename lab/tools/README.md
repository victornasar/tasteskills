# lab tools

Render AI-built pages in a real browser and measure them.

```bash
cd lab/tools && npm install        # once; uses your installed Google Chrome
npm test                           # calibration: layout/tests/fixtures: slop.html trips every check, clean.html none
```

| File | What it does |
|---|---|
| `detect.mjs` | Opens pages at 1440×900 and checks the nine layout patterns from `layout/skills/check-layout/scripts/patterns.mjs` on the rendered page (computed styles, not source). Saves screenshots with `--shots`, full-page ones with `--full` |
| `../../layout/tests/fixtures/` | One page with every pattern, one with none (shared with the layout skill) |
| `resolve-fonts.mjs` | Finds a hosted stylesheet for each catalog font → `font-sources.json` |
| `fetch-fonts.mjs` | Downloads the OFL catalog fonts no host serves, into `.font-cache/` (not committed) |

## The nine patterns

| Pattern | Caught when |
|---|---|
| Centered hero | The main heading in the first screen is centered |
| Row of three cards | Three boxed siblings of similar width sit side by side, each with real text |
| Decorative gradient | A large background or text uses a gradient with real colour in it (dark scrims over photos don't count) |
| Emoji icons | Three or more elements whose whole text is one or two emoji |
| Rounded everything | At least 60% of boxed elements have a corner radius of 8px or more |
| Same spacing everywhere | At least 75% of top-level sections share one padding |
| Purple button | The first filled button's OKLCH hue is 270–320° (indigo, violet, purple; blue is about 260°) |
| Pill badge | A small fully-rounded label sits just above the headline ("✨ New: …") |
| Stats row | Three or more siblings each led by a big number ("10k+", "99.9%") |

None of these is wrong in itself. They're slop when nearly every page reaches for them whatever the brief says.

## Why fonts are supplied at render time

Pages built with `find-font` self-host their fonts, but the lab has no font files, so screenshots would show
fallback fonts and misrepresent the design. `detect.mjs` removes `@font-face` rules that point at missing files
and swaps in a hosted or locally fetched copy of the same catalog font. This is for local screenshots only;
real sites still self-host. Each record's `fonts.loaded` says whether the heading and body fonts rendered.
