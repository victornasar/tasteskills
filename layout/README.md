# layout

A skill that helps AI agents stop building the same page every time.

AI-built sites reuse a handful of layout moves whatever the brief: rounded boxes around everything, a pill badge
above a centered headline, emoji icons, a gradient, a row of three cards. In 90 sites built by three models, landing
pages had rounded boxes everywhere 100% of the time and a pill badge 93%. Better fonts and colors didn't change
the page structure at all. See [`lab/findings.md`](../lab/findings.md).

`check-layout` works in two steps:

1. **Before building**, the agent writes down the default page it would reach for, the visitor's questions in
   order, and the one thing only this brief has. It builds from that plan instead of the default.
2. **After building**, it renders the page in Chrome, checks for nine overused patterns, looks at the
   screenshot, and changes each pattern the brief doesn't justify.

## Install

Works in Claude Code, Cursor, Codex and any agent that supports skills. Needs Node 22 or later and Chrome,
Chromium, Edge or Brave. No other install.

```bash
npx skills add https://github.com/victornasar/tasteskills --skill check-layout
```

Then ask your agent to build or review a page "with check-layout", or run `/check-layout <page or brief>`.

## Run the checker yourself

```bash
node skills/check-layout/scripts/check_layout.mjs page.html --screenshot shot.png
node skills/check-layout/scripts/check_layout.mjs http://localhost:3000/ --width 390 --height 844
```

Example output:

```
4 of 9 overused patterns found:
  - Pill badge above the headline (pillBadge): "✨ New: AI-powered insights"
  - Emoji used as icons (emojiIcons): 3 emoji used as icons
  - Rounded boxes everywhere (roundedEverything): 5 of 5 boxes rounded 8px or more
  - Decorative gradient (background or text) (gradient): 1 large gradient background(s), 1 gradient text
```

## Files

| Path | What it is |
|---|---|
| `skills/check-layout/SKILL.md` | The skill: plan, check, decide, re-check |
| `skills/check-layout/scripts/check_layout.mjs` | Renders a page in Chrome and reports the patterns. Talks to Chrome directly; no npm packages |
| `skills/check-layout/scripts/patterns.mjs` | The nine checks, shared with the lab's detector |
| `tests/` | Calibration pages (one with every pattern, one with none) and the tests: `node --test tests/*.test.mjs` |
