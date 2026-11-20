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
| [`find-font`](skills/find-font/SKILL.md) | Typography: type roles, category conventions, letterforms, weights and variable axes, pairing, a rendered type proof, and a curated list of fonts, plus the AI defaults to look past and when one can still be right |
| [`find-color`](skills/find-color/SKILL.md) | Colour: directions built from positioning, honest conventions, OKLCH, calculated contrast, a working token system, and 51 curated directions as starting points |
| [`check-layout`](skills/check-layout/SKILL.md) | Layout: plan the page from the visitor's questions, then look at the render and fix the layout patterns AI-built sites overuse |
| [`composition`](skills/composition/SKILL.md) | Composition: the visual relationships inside the page's structure (weight and balance, hierarchy and focal points, eye flow, space, scale, grids and deviations, grouping, density and pacing, layering), planned from the content and checked on the desktop and phone render |
| [`visual-hierarchy`](skills/visual-hierarchy/SKILL.md) | Hierarchy: rank information from the visitor's task, pair headlines with their support, spend emphasis deliberately, design for scanning, and check the ranking survives blur, grayscale and a phone |
| [`imagery`](skills/imagery/SKILL.md) | Imagery: give every image a job, choose photography, illustration, the product or diagrams, write shot lists, set crops and ratios, keep a set consistent, and refuse generic or dishonest stock |
| [`content-design`](skills/content-design/SKILL.md) | Words: messaging hierarchy, specific headlines, brand voice as decisions, calls to action, microcopy, and a check for generic AI marketing language and invented claims |
| [`responsive-design`](skills/responsive-design/SKILL.md) | Adaptation: design each context instead of shrinking the desktop; content-led breakpoints, container queries, touch and input, mobile navigation, fluid type, and tables and complex layouts on small screens |
| [`interaction-design`](skills/interaction-design/SKILL.md) | Behaviour: signifiers, feedback timing, every interaction and view state, navigation behaviour, forms and validation, error prevention and recovery |
| [`motion-design`](skills/motion-design/SKILL.md) | Motion: animate only with a job, timing and easing by role, transitions, micro-interactions, scroll and loading motion, choreography and reduced motion |
| [`component-craft`](skills/component-craft/SKILL.md) | Components: buttons, inputs, navigation, cards, menus, dialogs, tabs and tooltips built on native elements, with every state designed and the fine details (heights, radii, borders, focus rings, hit areas) finished |
| [`iconography`](skills/iconography/SKILL.md) | Icons: whether to use them at all, one consistent family, size, stroke and weight matched to text, optical alignment, and accessible icon-only controls |
| [`design-systems`](skills/design-systems/SKILL.md) | Systems: tokens in tiers named by role, semantic colour, type and spacing systems, variants by job, theming, and documented exceptions so consistency doesn't flatten the brand |
| [`web-accessibility`](skills/web-accessibility/SKILL.md) | Accessibility: WCAG 2.2 AA as part of design quality, semantic HTML, keyboard and focus, screen reader names and announcements, contrast, forms, motion, and testing with axe, a keyboard and a screen reader |
| [`data-visualization`](skills/data-visualization/SKILL.md) | Data: start from the question, choose a sentence, number, table or chart, encode for accuracy, label directly, design dashboards with context, use colour for data and avoid misleading scales |
| [`web-performance`](skills/web-performance/SKILL.md) | Performance: Core Web Vitals, perceived speed, images, fonts and scripts delivered efficiently, layout stability, smooth animation, and measuring in the lab and the field |

Each works on its own. `taste` uses the others when they're installed.

### Who owns what

The skills divide the work so they don't repeat each other. When two could apply, the owner decides and the other
refers to it.

| Question | Owner |
| --- | --- |
| What should this site feel like, and why? | `taste` |
| Which sections, in what order? | `check-layout` |
| How do elements relate in space; what balances? | `composition` |
| What matters most, and is that what people see first? | `visual-hierarchy` |
| What do the words say? | `content-design` |
| What do the images show, and how are they directed? | `imagery` |
| Which typefaces and colours? | `find-font`, `find-color` |
| What changes between phone and desktop? | `responsive-design` |
| What happens when someone acts; which states exist? | `interaction-design` |
| How do changes move? | `motion-design` |
| Does each component look finished in every state? | `component-craft` |
| Icons or words; which icons? | `iconography` |
| Which values are shared, and what are they called? | `design-systems` |
| Does it work for disabled people? | `web-accessibility` |
| How should these numbers be shown? | `data-visualization` |
| Does it load fast and stay stable? | `web-performance` |

`check-layout` and `composition` divide the page between them: check-layout decides which sections exist and in
what order; composition decides how the elements inside that structure relate visually: what's seen first, what
belongs together, how weight is balanced and how the page paces itself. Neither prescribes a look. Asymmetry,
oversized type, minimalism, broken grids, generous whitespace and overlap are all choices that need a reason
from the brief, and a conventional composition is often the right one.

## Install

Works with Claude Code, Cursor, Codex and any agent that supports the [Agent Skills](https://agentskills.io)
format.

```bash
npx skills add https://github.com/victornasar/tasteskills            # choose from the list
npx skills add https://github.com/victornasar/tasteskills --skill '*' # all seventeen
npx skills add https://github.com/victornasar/tasteskills --skill taste --skill find-font
npx skills add https://github.com/victornasar/tasteskills --skill web-accessibility --skill interaction-design
```

Then ask your agent:

```
/taste independent daycare for local families
/find-font cozy bakery website
/find-color neighbourhood bakery
/composition the homepage hero feels flat and cluttered
/content-design rewrite the pricing page copy
/web-accessibility audit the checkout flow
```

Or ask it to build or review a page "with check-layout", "with composition" or any other skill by name.

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
  composition/    SKILL.md, references/composition-principles.md,
                  references/composition-patterns.md, references/composition-critique.md
  visual-hierarchy/    SKILL.md, references/reading-and-scanning.md
  imagery/             SKILL.md, references/art-direction.md
  content-design/      SKILL.md, references/voice-and-microcopy.md
  responsive-design/   SKILL.md, references/adaptation-patterns.md
  interaction-design/  SKILL.md, references/states-and-forms.md
  motion-design/       SKILL.md, references/timing-and-easing.md
  component-craft/     SKILL.md, references/component-specs.md
  iconography/         SKILL.md
  design-systems/      SKILL.md, references/token-architecture.md
  web-accessibility/   SKILL.md, references/testing-checklist.md
  data-visualization/  SKILL.md, references/chart-guide.md
  web-performance/     SKILL.md, references/measuring.md
```

To change a skill, edit its Markdown. Keep the advice judgement-based: explain the reasoning and the evidence,
give examples rather than recipes, and don't add lookup tables that map a kind of business to a font or colour.
Don't treat a convention as slop just because it's common: the skills use one when the brief calls for it and
break it when the brief calls for something else.

## License

[MIT](LICENSE). Fonts keep their own licences (OFL or Fontshare's FFL); the repo stores no font files.
