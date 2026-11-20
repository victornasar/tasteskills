# tasteskills

Design skills for AI coding agents, so the websites they build look designed, not generated.

Ask an agent to build a site and it reaches for the same choices every time: Inter, a blue-to-purple gradient, a
centred hero, three feature cards. None of it is wrong, but all of it looks like every other AI-built site. These
skills teach the agent to think like a design director instead: read the brief, work out what the brand needs,
make choices it can defend, and check the rendered result.

They're plain Markdown. There are no engines, catalogs to query or scripts to run; the agent does the thinking.

## What we mean by AI slop

AI slop is design that would have come out the same regardless of the brief.

It isn't necessarily bad design. It can be polished, accessible, functional and visually appealing. What makes it
slop is the absence of real design decisions: the type, colour, layout, imagery and composition are there because
they're familiar defaults, not because they suit this business, its audience and its content.

No single choice is slop on its own. Inter, a centred hero or a gradient can each be right when the brief leads
there. A choice becomes slop when it would have appeared whatever the context.

The fix isn't to make everything look unique. A daycare doesn't need to look unlike every other daycare; warmth,
familiarity and trust may be exactly what its families expect. The aim is a page that looks right for its brief,
and looks that way because the brief called for it.

Two tests, used throughout the skills:

- **The swap test.** Put another business's name on the page, ideally one from a different category. If nothing
  looks wrong, the design came from defaults, not the brief.
- **The why test.** For each major choice, name the part of the brief that led to it. "Clean and modern" doesn't
  count.

**The ethos: take the design from the brief, not from the defaults.**

## The skills

| Skill | What it does |
| --- | --- |
| [`taste`](skills/taste/SKILL.md) | The design director. Reads the brief and the brand's positioning, writes a short `DIRECTION.md`, coordinates the skills below, builds, and critiques the render against the direction |
| [`find-font`](skills/find-font/SKILL.md) | Typography: type roles, category conventions, letterforms, weights and variable axes, pairing, a rendered type proof, and a curated list of fonts plus the AI defaults to avoid |
| [`find-color`](skills/find-color/SKILL.md) | Colour: directions built from positioning, honest conventions, OKLCH, calculated contrast, a working token system, and 51 curated directions as starting points |
| [`check-layout`](skills/check-layout/SKILL.md) | Layout: plan the page from the visitor's questions, then look at the render and fix the layout patterns AI-built sites overuse |

Each works on its own. `taste` uses the other three when they're installed.

## Install

Works with Claude Code, Cursor, Codex and any agent that supports the [Agent Skills](https://agentskills.io)
format.

```bash
npx skills add https://github.com/victornasar/tasteskills            # choose from the list
npx skills add https://github.com/victornasar/tasteskills --skill '*' # all four
npx skills add https://github.com/victornasar/tasteskills --skill taste --skill find-font
```

Then ask your agent:

```
/taste independent daycare for local families
/find-font cozy bakery website
/find-color neighbourhood bakery
```

Or ask it to build or review a page "with check-layout".

Agent without skills support? Point it at a skill's `SKILL.md` and give it the brief.

## What the skills are based on

The skills came out of experiments that are no longer in the repo (they're in git history, tagged
`pre-simplify`). What they found:

- **AI defaults are real and measurable.** In 90 sites built by three Claude models from one-line briefs, landing
  pages had rounded boxes everywhere 100% of the time, a pill badge above the headline 93% and a decorative
  gradient 87%. Inter was on 72% of the pages that load a web font, and Fraunces on 50%.
- **Better fonts and colours don't change the page.** With type and colour skills, default fonts disappeared,
  but page structure stayed within normal run-to-run variation. Planning the structure from the brief and
  checking the render is what moved it.
- **Removing slop leaves a new default.** Once the overused patterns were gone, skill-built pages converged on a
  pale, type-only, ruled look whatever the brief said. `taste` now plans directions on six visual axes and checks
  the render for that house style.
- **Judgement beats ranking.** A font recommender that ranked by metadata picked faces a person rejects on sight;
  models that looked at the fonts caught them. That's why the skills ask the agent to look rather than look up.
- **Not yet proven:** that people prefer the sites the skills produce. Blind ratings had only an AI rater when
  this version was written.

## Repository layout

```text
skills/
  taste/          SKILL.md, references/direction-template.md, references/visual-direction.md
  find-font/      SKILL.md, references/fonts.md
  find-color/     SKILL.md, references/directions.md
  check-layout/   SKILL.md
```

To change a skill, edit its Markdown. Keep the advice judgement-based: explain the reasoning and the evidence,
give examples rather than recipes, and don't add lookup tables that map a kind of business to a font or colour.

## License

[MIT](LICENSE). Fonts keep their own licences (OFL or Fontshare's FFL); the repo stores no font files.
