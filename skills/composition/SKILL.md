---
name: composition
description: Decide the visual relationships between the elements of a web page (weight and balance, symmetry, hierarchy and focal points, eye flow, space, scale and contrast, alignment and grids, grouping, density and pacing, layering) so the composition follows the creative direction instead of a default. Plans the composition from how the content relates, builds it, renders it on desktop and phone, and critiques what the eye actually does. Use when composing or reviewing a page, section or hero once its structure is known, when a page feels flat, cluttered, unbalanced or generic, or when taste needs a direction's composition and scale made concrete. Not for deciding which sections a page needs (check-layout) or for type and colour (find-font, find-color).
argument-hint: "[page, section or brief to compose or review]"
---

# composition

Structure decides what is on the page and in what order. Composition decides how those things relate when
someone looks: what they see first, what belongs together, what stays quiet, where the eye goes next, and
whether the whole feels settled, tense, generous or packed. Make those relationships on purpose, for reasons
you can trace to the brief, and check them on the rendered page.

Page, section or brief:

$ARGUMENTS

If this is empty, work on the page in the current project. Read `DIRECTION.md` if it exists; otherwise infer
the direction from the brief, copy and existing styles, and say what you inferred.

## Where this sits

| Skill | Decides | For example |
| --- | --- | --- |
| `taste` | The creative direction: positioning, perception, positions on six visual axes | "Composition: a catalogue grid of objects, because visitors compare" |
| `check-layout` | Structure: which sections exist, in what order, what the page leads with | "Today's hours and bake come first; testimonials are cut" |
| `composition` | The visual relationships inside that structure | "Today's bake is the focal point; hours and address share a baseline and read as one group; the menu is set dense so the photo can breathe" |
| `find-font`, `find-color` | Typefaces, colour and contrast | |

**The boundary test.** If a change alters what the page says, or the order it says it, it's structure: settle it
with check-layout or the plan. If it changes how elements relate visually while saying the same things in the
same order, it's composition. Composition can expose a structural problem (no section contains anything worth
looking at first); raise it instead of decorating around it.

If `DIRECTION.md` exists, its Composition, Scale, Imagery and Surface positions are this skill's brief. Turn
them into concrete relationships; don't override them. If the direction's composition fails on screen, say so
and raise it, rather than quietly composing something else.

## The model

Every element has **visual weight**: how strongly it pulls the eye. Size, value contrast, saturation, detail,
isolation, faces and words people are looking for all add weight. Composition is the deliberate distribution
of that weight.

- **Balance** is how weight is distributed across the frame; **symmetry** is one way to get it.
- **Hierarchy** ranks the weight; the **focal point** is what wins.
- **Flow** is the order the eye spends it in.
- **Space** and **grouping** decide which elements share weight as one unit.
- **Scale and contrast** are the levers that create weight.
- **Alignment and grids** are the structure every deviation is read against.
- **Density and pacing** set the baseline weight from section to section.
- **Layering** adds depth as one more way to rank.

Because they spend one currency, changing one changes the others. Enlarge a headline and you've also shifted
the balance, possibly moved the focal point, redirected the flow and changed what the space around it does.
Emphasis is zero-sum: contrast exists only against something quieter, so a page where everything is emphasised
has no emphasis. `references/composition-principles.md` covers each principle in depth and how they interact.

## Don't build a new template

Two defaults to look past:

- **The generated default.** Everything centred; the same padding on every section; every item in an equal
  card; two equally loud buttons; medium emphasis everywhere so nothing leads; the same density from top to
  bottom.
- **The "designed" default.** What agents produce when told to be bold or editorial: an asymmetric hero with an
  oversized headline, large empty areas, elements knocked off the grid, images overlapping text, tiny captions
  in the margins. Each move can be right. Together, on every brief, they are a house style as recognisable as
  the first.

So none of these is a default here: asymmetry, oversized type, minimalism, broken grids, generous whitespace,
overlap. Nor are their opposites. A conventional, symmetrical, gridded, moderately dense composition can be
exactly right: GOV.UK's left-aligned reading column and a newspaper's packed front page are excellent
compositions for their jobs. An unconventional composition with no reason behind it is noise. The goal is
intention, not novelty.

**Composition swap test.** Write the composition plan, then cross out the business name. If the plan would fit a
brief from a different category just as well, it came from habit.

## How to work

Scale the process to the job. A single section needs a few lines of plan; a full page needs the whole thing.

### 1. Read the direction

Write down what the composition has to serve, and translate each point into a compositional consequence:

- **Where and how the page is used.** On a phone in the street (one answer, found fast; little layering),
  at a desk comparing options (density, alignment, tables), browsing for pleasure (pacing, large images, room
  for a slower path), under stress (one clear focal point, calm, predictable).
- **Intended perception.** Each quality has compositional consequences, and each pole has its own cliché.
  "Calm" might mean small steps between sizes and a steady rhythm; "abundant" means density, not emptiness;
  "precise" means a strict grid with few deviations. The table in `references/composition-principles.md`
  (Reading a direction into composition) goes further.
- **Sophistication.** Premium doesn't mean empty, and everyday doesn't mean cramped.
- **The default.** The composition you'd reach for without thinking. Naming it lets you depart from it, or
  keep it, on purpose.

### 2. Find the focal point and the order of attention

For the first screen and each section, rank what must be seen: **first** (one thing), **second**, **third**,
and **available but quiet**. The focal point is content (the product, the answer, the fact, the action), not
decoration. If two things tie for first, decide. If nothing deserves to be first, that's a content or structure
problem, not a styling one. Do the same for the phone's first screen (about 390 × 700): it often needs a
different answer.

### 3. Map the relationships

Before choosing any visual treatment, write how the elements relate:

- **Groups:** what belongs together (item and price, image and caption, label and field).
- **Parallels:** what is equal in kind *and* importance. Check that it really is: three plans are rarely equal.
- **Subordinates:** what supports something else.
- **Contrasts:** what must read as different (the primary and secondary action; today and the rest of the week).
- **Sequences:** what must be read in order.

Most composition faults are a wrong relationship made visible: equal cards for unequal items, a label equally
far from two things, a secondary action dressed as a primary one, a heading closer to the section above than to
its own content.

### 4. Choose the approach

Fill in the composition plan below. Every line takes a position and a reason from steps 1–3. Consider at least
one genuinely different approach for the most important section, and say why you didn't take it.
`references/composition-patterns.md` describes page and section patterns with when each fits and fails; use it
to widen what you consider, not as a menu.

```markdown
## Composition plan
- Direction says: <qualities, context, sophistication> → <what that means for composition>
- Default I'd reach for: <…>; keeping / departing because <…>
- Focal order, first screen (desktop / phone): 1 <…> 2 <…> 3 <…>; quiet: <…>
- Key relationships: <groups, parallels that really are equal, subordinates, contrasts>
- Balance: <symmetrical | asymmetrical | even all-over | deliberate tension> because <…>
- Grid: <columns or measure, margins, what aligns to what>; deviations: <each one, the line it leaves, why>
- Scale: <the big moment and its size against body text; how many steps> because <…>
- Space: <inside a group / between groups / between sections; where space is spent and why>
- Density and pacing: <each section as loud or quiet, dense or open> because <…>
- Layering: <none | what overlaps what, why, and what happens on a phone>
- Phone: <what changes in the composition, not just "it stacks">
- Considered and rejected: <approach> because <…>
```

When working inside `taste`, put this plan in the Layout or Other decisions part of `DIRECTION.md`.

### 5. Build

- **Space from relationships.** Use a few spacing steps, each with a role: inside a group, between related
  groups, between sections, around the focal point. Something must be clearly closer to what it belongs with:
  make it a visible step (often 1.5–2× or more), not 24px against 32px. Give headings more space above than
  below.
- **One grid, declared once.** A single container system (CSS grid with named lines, or one column count and
  one content width) so alignments are shared, not coincidental. Place deviations on the grid's own lines (span
  to full bleed, hang into the margin) instead of nudging with arbitrary offsets.
- **Source order is reading order.** Rearrange visually with grid placement, but keep the DOM in the order a
  screen reader and keyboard should follow (WCAG 1.3.2, 2.4.3).
- **Overlap by stacking grid cells**, not absolute positioning with magic numbers. Never cover text you need, and
  decide what each overlap does on a phone.
- **Fluid scale with limits.** `clamp()` for type and section spacing, then check both ends.
- **Compose the phone.** Decide its focal point, which groups merge, how much scale contrast survives, which
  deviations go. The desktop layout stacked in source order is not a phone composition.

### 6. Render

Screenshot the first screen and the full page on desktop (about 1440 × 900) and phone (about 390 × 844). Add
about 1024 and 1920 wide when the grid changes between sizes or the content has a maximum width. Use whatever
you have: the dev server in a browser tool, Playwright, or headless Chrome. Look at the screenshots yourself.
Reasoning from the CSS is not looking.

### 7. Inspect

Run the checks in `references/composition-critique.md`. The essentials, on desktop and phone:

1. **Blur or shrink the screenshot.** Does the intended focal point win? Do groups read as groups?
2. **Trace the eye.** List the first five things your eye lands on, in order. Compare with step 2.
3. **Balance.** Does a side or corner feel heavy or empty without a reason? Mirror the screenshot to see it fresh.
4. **Space.** Is everything clearly closer to what it belongs with? Any heading nearer the content above it?
5. **Edges.** Count the distinct left edges on a screen. Each should be intended; edges a few pixels apart are
   bugs.
6. **Scale.** How many distinct sizes are there, and are the steps clearly different? Does the big moment land on
   the focal point?
7. **Pacing.** Describe each section as loud or quiet, dense or open. Does that match the plan, or is every
   section the same?
8. **Layering.** Anything overlapping text, cropping a face, or colliding at another width?
9. **Direction.** Does the composition carry the intended perception qualities? Run the composition swap test,
   and look for both defaults above.

### 8. Correct

For each weakness, write: what you see → the relationship it breaks → the change. Prefer the smallest change that
fixes the relationship; it's usually spacing, demotion or removal, not another element. Never fix emptiness
with decoration or clutter with more whitespace alone. Render again. Stop after two rounds and report what's
left.

### 9. Explain

In a few lines: the focal points and why; the balance and grid and why; where space and scale were spent; any
deviation or layering and what it does; what you considered and rejected; what the render check found and what
you changed; anything that needs a human decision. Tie each reason to the brief, never to a style:
"asymmetric because the menu photo is the product and needs the larger share", not "asymmetric for visual
interest".

## Judgement over formula

- Every deviation needs a structure to deviate from. A broken grid without a strong grid is just disorder.
- Space is a relationship, not a quantity. "More whitespace" isn't a fix; "the price now sits closer to its item
  than to the next one" is.
- Hierarchy is a ranking. You can't raise everything; to promote one thing, lower others.
- Balance isn't symmetry, and asymmetry isn't interest.
- Density is earned by use: dense where people compare, scan and come back; open where one thing must be
  considered.
- Conventions exist because they work for someone. Keep a conventional composition when the audience relies on
  it; leave it when it only makes the page interchangeable.
- Composition happens in pixels. Look at the render, on desktop and on a phone.

## Mistakes agents make

Each is covered with its fix in the references.

- Centring by default, including paragraphs and lists, and mixing centred and left-aligned elements in one group.
- Identical padding on every section and one `gap` value everywhere, so spacing says nothing.
- Equal cards for unequal items; boxes inside boxes until enclosure stops meaning anything.
- Competing focal points in the first screen: headline, illustration, badge and two loud buttons.
- Hierarchy by size alone, or many near-identical sizes.
- Filling an "empty" side with a decorative shape instead of asking what should balance it.
- "Asymmetry" made of arbitrary offsets that sit on no grid line; containers of a different width in each section.
- Overlaps that look deliberate at 1440 and collide at 390 or 1920.
- A full-height hero that looks complete, so nobody scrolls.
- Treating the phone as the desktop, stacked.
- Judging the composition from the code instead of the screenshot.
