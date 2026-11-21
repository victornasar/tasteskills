---
name: inspect
description: Look at the rendered interface, not the code, and find what's visibly wrong. That means places where the build doesn't match the direction or the plan, things of the same kind that don't match each other, states nobody designed, and rendering defects (overflow, clipping, collisions, fallback fonts, broken images, layout shift) at real widths, in real states and with real content. Fixes what it finds, re-renders the same view, and confirms each fix worked without breaking its neighbours. Use before calling a page or feature done, after a round of changes, when something "looks off", or when a site needs a visual QA pass. Not for judging the design decisions themselves (each owning skill's render check does that), accessibility testing (`a11y`) or code review.
argument-hint: "[page, flow or URL to inspect]"
---

# inspect

An agent judges its work from the code it wrote, and the code is not what people see. The stylesheet says the
cards share a padding token; the screenshot shows one card with a stray margin. The font is declared; the page
renders in the fallback because the file never loaded. The fix is in the diff; the button still wraps on a
phone. Look at the render, at the widths and in the states people meet, compare it with what was decided, fix
what's wrong, and look again.

Page, flow or URL:

$ARGUMENTS

If this is empty, inspect the current project's main pages and flows. Read `DIRECTION.md` if it exists: its
constraints, avoid list and composition plan are what the render is checked against.

## Where this sits

- Every other skill makes a decision and checks it on the render: `compose` asks whether the focal point wins,
  `hierarchy` whether the ranking reads, `fonts` whether the faces work. Those checks ask "is this decision
  right?" This skill asks "did that decision render, everywhere?", and it owns the defects no decision covers.
- It checks that decisions rendered; it doesn't make them. Whether a phone layout should stack differently is
  `responsive`'s call, whether a section belongs is `layout`'s, whether a focal point is right is `compose`'s.
  When a finding is a design question rather than a build fault, name the owning skill and raise it. Don't
  redesign during QA.
- `a11y` owns accessibility testing with axe, a keyboard and a screen reader. This skill notes visible symptoms
  (an invisible focus ring, text over a busy photo) and hands them over.
- `taste` uses this skill in its critique when it's installed.

## Principles

1. **The screenshot is the evidence.** "The CSS sets `gap: 2rem`" is a claim; the screenshot shows whether it
   happened. Every finding and every fix is confirmed on a render.
2. **Inspect the states people meet, not the one you built.** The default state at 1440px with ideal content is
   the view most likely to look fine. Defects live at other widths, in hover, focus, open, error, empty and
   loading, and with long names and missing images.
3. **Check against a written intent.** "Looks fine" isn't a check. `DIRECTION.md`, the skills' plans, the design
   system or the site's most finished page is the reference.
4. **Things with the same role look the same.** Two cards of one kind, two primary buttons, every section heading.
   Near-misses (an edge 3px off, two greys, 15px beside 16px text) are the commonest visible defect and the
   hardest to see in code. They're what makes a site feel unconsidered.
5. **A fix isn't done until it's seen.** Re-render the same view at the same width and state. Then check the
   neighbours: a fix to one card can break the grid, and a token change reaches pages you didn't open.
6. **Fix causes, not pixels.** If one card sits wrong because it has its own padding, fix the component or token,
   not that card with a nudge. One-off overrides make the next instance wrong too.

## How to work

### 1. Set the reference

Write down what the render should show: the `DIRECTION.md` constraints and avoid list, the composition plan, the
tokens and variants, and what each page must answer first. If none of that exists, take the most finished page
as the reference for consistency and say so.

### 2. Plan the views

A view is a page or component at one width, in one state, with one set of content. List the ones that matter:

- **Widths:** 390 (phone), 768, 1024 and 1440 as the base; 320 for small phones (it's also what 400% zoom
  looks like); 1920 or wider when content has a maximum width or the hero scales. Then drag the window slowly
  through the whole range once. Layouts often break between breakpoints, not at them.
- **States:** for each control, the states `interaction` defines (hover, focus-visible, active, disabled,
  loading, error, success, open, selected); for each view, empty, loading, error, partial and full.
- **Content extremes:** the longest real label, a name with no spaces, one item and fifty, a missing image, and
  copy about 30% longer, as a translation into German often is.
- **Settings:** dark mode if the site has it, reduced motion, 200% text size, a slow connection for loading
  states.

Scale it to the job. After a small change, inspect what the change could have touched and its neighbours, not
the whole site.

### 3. Capture

Use whatever browser tooling there is: a browser tool, Playwright or headless Chrome. Take first-screen and
full-page screenshots at each width. Trigger states for real: hover the element, Tab to it for focus, submit
the form empty for errors, throttle the network for loading. `references/capture.md` has patterns for states,
settings and the measurements that find defects faster than looking. Look at every screenshot at full size;
a downscaled full-page image hides 2px problems and small text.

### 4. Look in passes

Ask one question per pass, across all the screenshots. Looking for everything at once misses things.

1. **Broken.** Horizontal scroll; text clipped, overflowing or overlapping; elements colliding; content under
   sticky bars; broken images or empty frames; placeholder text; the fallback font instead of the chosen face;
   unstyled flashes; layout shifting as content loads.
2. **Intent.** Each `DIRECTION.md` constraint passes or fails, with what you see. Any item from the avoid list on
   screen? Does the first screen answer the visitor's first question at every width?
3. **Consistency.** Put same-role elements side by side: cards, buttons, headings, inputs, icons, image ratios,
   the space between sections. Count the distinct left edges, text sizes, greys, radii and shadows on a screen.
   Each should be a value someone decided.
4. **States.** Every state exists and looks designed. Focus is visible; hover isn't the only cue; disabled is
   distinct but readable; errors sit by their field; the empty state says something useful; loading holds the
   layout.
5. **Content.** Real copy fits: no truncation that loses meaning, no button wrapping onto two lines, no headline
   ending on one stranded word where it matters, figures aligned in columns.
6. **Between widths.** Anything that jumps, overlaps or disappears as the window resizes.

### 5. Triage

For each finding, write: what you see (view, width, state) → what it should be (the reference) → the cause →
who owns it. Then rank:

- **Blocks:** someone can't read, reach or finish something. A clipped call to action, an overlay covering the
  form, horizontal scroll on a phone.
- **Breaks intent:** a constraint fails, an avoided pattern appears, the first screen doesn't answer.
- **Inconsistent:** same-role elements differ; values off the system.
- **Polish:** optical alignment, ragged line endings, small rhythm problems.

Fix in that order. Design questions go to the owning skill or the user, not into a quiet redesign.

### 6. Fix and verify

- Fix the cause at the right level: token, component or layout rule.
- Re-capture the exact view (same width, state and content) and compare before and after side by side.
- Re-capture the neighbours: the same view at other widths, other instances of the component, other pages
  that use the changed token.
- Stop after two rounds. What's left goes in the report.

### 7. Report

List the views inspected (widths, states, settings), the findings by severity with before and after for each
fix, what you handed to other skills or the user, and what you didn't inspect and why. Don't call a view fine
if you didn't capture it.

## Mistakes agents make

- Declaring a fix done from the diff, without rendering it.
- Inspecting one desktop screenshot of the default state.
- Judging a downscaled full-page screenshot, where text and small offsets are invisible.
- Overriding one instance instead of fixing the shared rule.
- "Fixing" a design decision during QA, such as swapping the direction's unusual typeface, instead of raising it.
- Not noticing the fallback font: the page renders in a system face because the font never loaded, and it looks
  fine.
- Imagining hover, focus, error and empty states instead of triggering them.
- Hiding overflow with `overflow: hidden` instead of fixing what overflows.
- Reporting everything at one severity, so the clipped checkout button sits beside a 1px icon nudge.
