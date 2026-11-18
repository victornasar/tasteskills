# tasteskills

Tools that help AI coding agents make websites that look designed, not generated.

Ask an AI agent to build a site and it reaches for the same choices every time: Inter for the font, a purple
or blue gradient, a centered hero, three feature cards. None of it is wrong. All of it looks like every other
AI-built site. People call this look **AI slop**.

This repo gives agents better defaults to reach for, and the evidence for why they're better:

- **Curated choices.** A short list of fonts and color pairs, each picked by a person, tagged so an agent can
  match them to a brief.
- **Avoid lists.** The fonts and patterns agents overuse, measured from real AI output.
- **Skills.** Commands an agent runs (`/find-font`, `/find-color`) that turn a brief like "cozy bakery
  website" into specific picks, with reasons.
- **Evals.** Checks that the picks avoid the defaults and that different briefs get different answers.

## Quick start

Three skills are ready to use today. All work in Claude Code, Cursor, Codex and any agent that supports skills.
Each one ships with its data and a small script, so the picks are the same every time for the same brief.

### Pick colors: `/find-color`

Needs [Node.js](https://nodejs.org) 18 or later. No clone, no API keys.

```bash
npx skills add https://github.com/victornasar/tasteskills --skill find-color
```

Then ask your agent:

```
/find-color neighbourhood bakery
```

You get 3–5 clearly different color directions (for this brief: Espresso and Milk, Oxblood and Pistachio,
Bronze Monochrome, Clay and Linen), each with contrast numbers and a note on when to choose it. Pick one and
the agent writes it into your project as CSS variables, a Tailwind theme or design tokens. More in
[`color/README.md`](color/README.md).

### Pick fonts: `/find-font`

Needs Python 3.8 or later. No clone, no API keys.

```bash
npx skills add https://github.com/victornasar/tasteskills --skill find-font
```

Then ask your agent:

```
/find-font cozy bakery website
```

You get a top pick per role (for this brief, Synonym for headlines and Sentient for body text), two
alternatives each, the license, where to download it and the CSS to self-host it. More in
[`typography/README.md`](typography/README.md).

### Check the layout: `/check-layout`

Needs Node 22 or later and Chrome (or Chromium, Edge, Brave). No clone, no API keys.

```bash
npx skills add https://github.com/victornasar/tasteskills --skill check-layout
```

Ask your agent to build or review a page "with check-layout". Before building, it plans the page from the brief
instead of the usual template. After building, it renders the page, checks for the patterns AI-built sites
overuse (pill badges, emoji icons, rounded boxes everywhere and six more) and fixes the ones the brief doesn't
justify. More in [`layout/README.md`](layout/README.md).

Agent without skills support? Point it at the skill's `SKILL.md` (in [`color/skills/`](color/skills/),
[`typography/skills/`](typography/skills/) or [`layout/skills/`](layout/skills/)) and give it the brief.

## What's in the repo

| Folder | What it is | Status |
| --- | --- | --- |
| [`color/`](color/) | 51 curated color directions, a script that picks and applies them, and research on 6,295 award-winning sites | Ready to use |
| [`typography/`](typography/) | 63 curated free fonts, an avoid list of 27 overused ones, and the `/find-font` skill | Ready to use |
| [`layout/`](layout/) | The `check-layout` skill: plans page structure from the brief and checks the rendered page for nine overused layout patterns | Ready to use |
| [`lab/`](lab/) | Experiments on whole-page design: a measured corpus of AI defaults, a with/without-skills experiment, blind ratings | First results in |

Each folder works on its own, with its own data, scripts and checks. Start with the folder's `README.md`;
agents start with its `AGENTS.md`.

## What's proven and what isn't

- **Proven:** the skills pick from the curated lists, avoid the overused defaults, and give different answers
  to different briefs. Both areas have automated checks for this, including tests that fail if one font or
  color starts winning most briefs.
- **Measured:** in 90 AI-built sites, landing pages show rounded boxes everywhere 100% of the time, a pill badge
  above the headline 93% and a decorative gradient 87%. With the skills, default fonts vanish (without them,
  every bakery page in the experiment used Fraunces) and layout patterns drop by about a quarter. See
  [`lab/findings.md`](lab/findings.md).
- **Not yet proven:** that people prefer the sites built with the skills. Blind ratings are open. The skills
  also don't change page structure, so layout is the next area to work on.

## Words used here

| Word | Meaning |
| --- | --- |
| Slop | The default look of AI-built sites: the same fonts, colors and layouts every time |
| Brief | A short description of the project: "cozy bakery website", "dashboard for a fintech" |
| Skill | Instructions (and sometimes a script) an AI agent loads to do one job well |
| Ground, figure | In color: the background color and the main color on top of it (type, logo) |
| OKLCH | A way of writing colors that matches how people see lightness; this repo stores colors in it |
| Eval | An automated test of an agent's or skill's output |

## Contributing

Work in one folder at a time and follow its `AGENTS.md`. Before committing, run that folder's checks:

```bash
# Typography: validates the catalog and regenerates its README
cd typography && python3 scripts/build.py --check && python3 -m unittest discover -s tests -q

# Color: rebuilds the library and runs the golden briefs; nothing should change
cd color && node tools/build.mjs all && git diff --exit-code
```

To run the typography check automatically on every commit: `git config core.hooksPath .githooks`.

One rule covers the whole repo: a new skill or rule needs evidence behind it, from an area's evals or from a
finding in `lab/`.

## License

[MIT](LICENSE). Fonts keep their own licenses (OFL or Fontshare's FFL); the repo stores no font files.
