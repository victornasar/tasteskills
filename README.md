# tasteskills

Design skills for AI coding agents, so the websites they build look designed, not generated.

Ask an agent to build a site and it reaches for the same choices every time: Inter, a blue-to-purple gradient, a
centred hero, three feature cards, the same copy about "seamless" products. None of it is wrong, but all of it
looks like every other AI-built site. These skills teach the agent to think like a design team instead: read the
brief, work out what the brand needs, make choices it can defend, and check the rendered result, from the
creative direction down to the words, the images, how the interface behaves, and whether it's accessible and
fast.

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

Seventeen skills, grouped by the part of the work they own. Each answers one question; when two could apply, the
owner decides and the other refers to it, so the skills don't repeat each other.

**Direction**

| Skill | Owns | Covers |
| --- | --- | --- |
| [`taste`](skills/taste/SKILL.md) | What should this site feel like, and why? | The design director. Reads the brief and the brand's positioning, writes a short `DIRECTION.md`, hands each area to the skills below, builds, and critiques the render against the direction |

**The page: what it says and how it looks**

| Skill | Owns | Covers |
| --- | --- | --- |
| [`layout`](skills/layout/SKILL.md) | Which sections, in what order? | Plan the page from the visitor's questions, then look at the render and fix the layout patterns AI-built sites overuse |
| [`compose`](skills/compose/SKILL.md) | How do elements relate in space? | Weight and balance, focal points, eye flow, space, scale, grids and deviations, grouping, density and pacing, layering, planned from the content and checked on desktop and phone |
| [`hierarchy`](skills/hierarchy/SKILL.md) | What matters most, and is that what people see first? | Rank information from the visitor's task, pair headlines with their support, spend emphasis deliberately, design for scanning |
| [`content`](skills/content/SKILL.md) | What do the words say? | Messaging hierarchy, specific headlines, brand voice as decisions, calls to action, microcopy, and a check for generic AI marketing language and invented claims |
| [`images`](skills/images/SKILL.md) | What do the images show? | Give every image a job, choose photography, illustration, the product or diagrams, write shot lists, set crops and ratios, keep a set consistent, refuse generic or dishonest stock |
| [`fonts`](skills/fonts/SKILL.md) | Which typefaces? | Type roles, category conventions, letterforms, pairing, a rendered type proof, a curated list of fonts, and the AI defaults to look past (and when one can still be right) |
| [`color`](skills/color/SKILL.md) | Which colours? | Directions built from positioning, honest conventions, OKLCH, calculated contrast, a working token system, and 51 curated directions as starting points |

**The interface: how it adapts and behaves**

| Skill | Owns | Covers |
| --- | --- | --- |
| [`responsive`](skills/responsive/SKILL.md) | What changes between phone and desktop? | Design each context instead of shrinking the desktop: content-led breakpoints, container queries, touch and input, mobile navigation, fluid type, complex layouts on small screens |
| [`interaction`](skills/interaction/SKILL.md) | What happens when someone acts? | Signifiers, feedback timing, every interaction and view state, navigation behaviour, forms and validation, error prevention and recovery |
| [`motion`](skills/motion/SKILL.md) | How do changes move? | Animate only with a job; timing and easing by role, transitions, micro-interactions, scroll and loading motion, reduced motion |
| [`components`](skills/components/SKILL.md) | Does each component look finished? | Buttons, inputs, navigation, cards, menus, dialogs, tabs and tooltips on native elements, every state designed, the fine details finished |
| [`icons`](skills/icons/SKILL.md) | Icons or words, and which icons? | Whether to use icons at all, one family, weight matched to text, optical alignment, accessible icon-only controls |
| [`design-system`](skills/design-system/SKILL.md) | Which values are shared, and what are they called? | Tokens named by role, type and spacing systems, variants by job, theming, and documented exceptions so consistency doesn't flatten the brand |

**Quality: whether it works for everyone**

| Skill | Owns | Covers |
| --- | --- | --- |
| [`a11y`](skills/a11y/SKILL.md) | Does it work for disabled people? | WCAG 2.2 AA as part of design quality: semantic HTML, keyboard and focus, screen readers, contrast, forms, motion, and testing with axe, a keyboard and a screen reader |
| [`dataviz`](skills/dataviz/SKILL.md) | How should these numbers be shown? | Start from the question; a sentence, number, table or chart; accurate encodings, direct labels, dashboards with context, honest scales |
| [`performance`](skills/performance/SKILL.md) | Does it load fast and stay stable? | Core Web Vitals, perceived speed, images, fonts and scripts delivered efficiently, layout stability, measuring in the lab and the field |

Each works on its own. `taste` uses the others when they're installed. None of them prescribes a look:
asymmetry, oversized type, minimalism, generous whitespace, rounded cards or a centred hero are all choices that
need a reason from the brief, and the conventional answer is often the right one.

## Install

Works with Claude Code, Cursor, Codex and any agent that supports the [Agent Skills](https://agentskills.io)
format.

```bash
npx skills add https://github.com/victornasar/tasteskills            # choose from the list
npx skills add https://github.com/victornasar/tasteskills --skill '*' # all seventeen
npx skills add https://github.com/victornasar/tasteskills --skill taste --skill fonts --skill color \
  --skill layout --skill compose                                     # the core set for a new site
npx skills add https://github.com/victornasar/tasteskills --skill a11y --skill interaction
```

Then ask your agent:

```
/taste independent daycare for local families
/fonts cozy bakery website
/color neighbourhood bakery
/compose the homepage hero feels flat and cluttered
/content rewrite the pricing page copy
/a11y audit the checkout flow
```

Or ask it to build or review a page "with layout", "with compose" or any other skill by name.

Agent without skills support? Point it at a skill's `SKILL.md` and give it the brief.

The names are short, so one may match a skill you already have. Some agents ship their own `dataviz`, for
example. When two installed skills share a name, the agent sees only one of them: installed in a project, this
repo's `dataviz` replaces the built-in one there. Keep the one you want, or install these per project.

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

Those experiments covered `taste`, `fonts`, `color` and `layout`. `compose` and the newer
skills haven't been through the lab yet. They draw on established research and practice (Gestalt grouping,
eye-tracking studies, Cleveland and McGill on chart perception, WCAG 2.2, Core Web Vitals, among others), cited
where they're used, and on the same lessons: name the default before you depart from it, give every choice a reason
from the brief, and look at the render.

## Repository layout

```text
skills/
  taste/           SKILL.md, references/direction-template.md, references/visual-direction.md

  layout/          SKILL.md
  compose/         SKILL.md, references/composition-principles.md,
                   references/composition-patterns.md, references/composition-critique.md
  hierarchy/       SKILL.md, references/reading-and-scanning.md
  content/         SKILL.md, references/voice-and-microcopy.md
  images/          SKILL.md, references/art-direction.md
  fonts/           SKILL.md, references/fonts.md
  color/           SKILL.md, references/directions.md

  responsive/      SKILL.md, references/adaptation-patterns.md
  interaction/     SKILL.md, references/states-and-forms.md
  motion/          SKILL.md, references/timing-and-easing.md
  components/      SKILL.md, references/component-specs.md
  icons/           SKILL.md
  design-system/   SKILL.md, references/token-architecture.md

  a11y/            SKILL.md, references/testing-checklist.md
  dataviz/         SKILL.md, references/chart-guide.md
  performance/     SKILL.md, references/measuring.md
```

To change a skill, edit its Markdown. Keep the advice judgement-based: explain the reasoning and the evidence,
give examples rather than recipes, and don't add lookup tables that map a kind of business to a font or colour.
Don't treat a convention as slop just because it's common: the skills use one when the brief calls for it and
break it when the brief calls for something else.

Keep the boundaries. Each `SKILL.md` has a "Where this sits" section naming what it owns and what it leaves to its
neighbours. If new advice belongs to another skill, put it there and refer to it, rather than repeating it. A new
skill needs its own question in the tables above; if it doesn't have one, it's probably a section of an existing
skill. Keep `SKILL.md` short enough to use while coding, and put depth in `references/`.

## License

[MIT](LICENSE). Fonts keep their own licences (OFL or Fontshare's FFL); the repo stores no font files.
