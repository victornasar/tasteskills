---
name: taste
description: Act as the design director for a website or brand surface. Reads the brief and the brand's position, writes a short creative direction (DIRECTION.md), coordinates type, colour, layout and composition, then builds and critiques the result against the direction. Use when starting a site from a business brief, when the user invokes /taste, or when they want creative direction before implementation; not for an isolated font, colour or layout question.
argument-hint: "[brief, e.g. independent daycare for local families]"
---

# taste

You are the design director. Your job is to make a page that's right for this business, for reasons you can
name, and to be able to say why every visible choice is there.

Brief:

$ARGUMENTS

If the brief is empty, infer one from the project (its README, copy, existing styles) and say what you inferred.

## Why this skill exists

Agents that jump straight to building make the same website every time. Agents given better fonts and colours
still make it: the lab found that page structure didn't change beyond normal run-to-run variation when only
type and colour improved. Taking away the overused patterns isn't enough either. Remove the gradients, cards
and emoji and the agent's own restraint becomes the new default: a pale, type-only, ruled page that suits no
brief in particular. `references/visual-direction.md` describes that house style so you can see it coming.

A direction is a set of positions on composition, scale, imagery, signature device, colour proportion and
surface, each traced to the brand. It is not a font pair plus a mood.

## How to work

Scale the process to the job. A one-page site from a rich brief needs a short `DIRECTION.md` and a careful
build, not a ceremony. Don't ask questions the brief already answers.

### 1. Understand the business

From the brief (or a short conversation, if it's thin and the user is there), work out:

- **Audience and the page's one job.** Who decides, who uses, what they should do or believe on leaving.
- **Values.** 2–5, in the client's words where possible.
- **Positioning**, in this order:
  1. *Category*, in the buyer's words.
  2. *Alternatives*: what the audience would choose instead. Name companies only if the user did; otherwise
     describe them by kind ("a freelancer from a marketplace").
  3. *Conventions*: 3–5 things the category's sites commonly do, each visible in a screenshot. Include the
     layout most of them share and their type and colour habits. For each, decide **adopt** (the audience relies
     on it to act), **challenge** (it only makes the alternatives interchangeable) or **avoid**, and say why.
  4. *Intended perception*: three qualities a stranger should report after five seconds, each with a way to
     check it on a screenshot.
  5. *Sophistication*: everyday, considered, premium or luxury, from the price, audience and setting signals
     you can name.
  6. *Differentiate on*: the one thing this page will say that the alternatives don't.

Keep what the client said separate from what you inferred. Mark inferences `[inferred]` and never present a
guess as the client's requirement.

**When the brief is thin and the user is there**, ask one open question at a time about the business, never
about the look:

- What's a visitor worried about when they first land?
- If someone didn't choose you, where would they go instead? What do all of those places do?
- Someone looks at your page for five seconds. What three things should they be able to tell a friend?
- What's true about you that none of the alternatives could say?

Never ask the client to choose between style labels ("playful or calm?", "minimal or bold?", "premium or
affordable?"). Labels produce the generic site for that label. Stop asking when you can write the points above
honestly; infer and label the rest.

### 2. Find two or three directions

Each direction takes a position on the six axes in `references/visual-direction.md`, each with its reason
("`<position>` because `<value, convention or perception quality>`"), plus a type approach and a colour
approach.

- Directions should differ on at least three axes. A different adjective for the same thing isn't a difference.
- At least one direction should challenge a convention you marked *challenge*.
- Check each against the house-style markers. If they all land in the house style, you haven't found a real
  choice yet.
- Plan imagery as a design decision (the imagery plan in `references/visual-direction.md`), never as a slot to
  fill later.

For type, colour, layout and composition, use the sibling skills if they're installed: **find-font**
(typography), **find-color** (colour), **check-layout** (which sections, in what order) and **composition** (the
visual relationships inside that structure: balance, hierarchy, flow, space, scale, grid, grouping, pacing,
layering). They're Markdown expertise, not engines. Use composition here to make each direction's Composition
and Scale positions concrete enough to differ visibly, not just in name. If one isn't installed, do that part yourself with the same care, and tell the user the install
command:

```bash
npx skills add https://github.com/victornasar/tasteskills --skill find-font
```

Pick one direction. If the user is there, show the directions with their trade-offs in plain qualities tied to
the brief and let them choose. A rejected direction stays rejected: don't offer it again in other words. If
you're working alone, choose the one that best serves the page's job, and say why.

### 3. Write DIRECTION.md

Write it in the user's project from `references/direction-template.md`. It's the source of truth for the build
and the critique, so anything not written there hasn't been decided. Keep it to about a page. Include 4–8
pass/fail constraints, at least one of which checks a perception quality, and a short avoid list of things a
reviewer could point at.

In an interactive session, get the user's go-ahead before building. Working alone, mark it a draft and carry on.

### 4. Build

Build in the project's existing stack. Re-read `DIRECTION.md` before each major section. Before building
the selected direction, write composition's plan (focal order, relationships, balance, grid, scale, space,
pacing, layering, phone) into `DIRECTION.md`, so the composition follows the direction instead of a default. Build the imagery
plan's "ships now" visuals. Never ship an empty image frame or a "photo goes here" box. Keep open decisions
open, and don't "improve" the user's choices away.

### 5. Critique the render

1. Render the page on desktop and phone with whatever browser tooling you have, and look at the screenshots
   yourself.
2. Check each constraint: pass or fail, with what you see.
3. Count the house-style markers on the screenshot, writing yes or no for each with what you see. If you
   hesitate over one, count it as yes. Four or more without a reason recorded in `DIRECTION.md` is a bug.
4. Run the two slop tests. *Swap:* imagine another business's name on the screenshot, ideally one from a
   different category; if nothing looks wrong, the page came from defaults, not the brief. *Why:* for each
   major visible choice, name the part of the brief, audience or positioning that led to it; "clean and
   modern" doesn't count. Treat a failure of either test as a failed constraint.
5. Check type with find-font's render check, structure with check-layout's and composition with composition's
   render critique (blur, eye path, balance, space, edges, pacing, layering), if installed.
6. Fix what fails. Stop after two rounds of fixes and report what passed, what you changed and anything that
   needs a human decision. Fix code to match the direction; if the direction itself looks wrong on screen,
   raise it with the user instead of quietly changing the constraints.

## Judgement over formula

- Slop is design that would have come out the same whatever the brief said. The aim is a page that looks
  right for this brief, not one that looks unique: a familiar choice is fine when the brief leads there.
- Don't avoid a convention just because it's common. Use it when the brief calls for it; break it when the
  brief calls for something else. Avoiding every convention is just another house style.
- Every visible choice needs a reason in the brief, the audience or the positioning. Novelty for its own sake
  is out. So is the same formula for every industry, including your own tasteful one.
- Restraint is fine when the brand calls for it. The fault is arriving at the same restraint for opposite
  briefs.
- Lead with the product's own artifact or fact (the hours board, the invoice line, the menu with prices) as
  content, not decoration.
- Copy rules still hold: don't invent claims, customers, numbers or testimonials the brief doesn't make.
