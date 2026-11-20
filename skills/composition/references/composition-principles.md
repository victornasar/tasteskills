# Composition principles

The reasoning behind each compositional decision: what it is, why it works, when it doesn't, and how to see it
on a rendered page. Read the principle you're working on, and always read **How the principles interact** at
the end; none of these works alone.

Each principle follows the same shape: what it means, why it matters, good and poor execution, ways to do it
and when each fits, the mistakes agents make, and how to check it on the render.

Contents:

1. Visual weight and balance
2. Symmetrical and asymmetrical composition
3. Visual hierarchy and focal points
4. Eye movement and visual flow
5. Negative space and spatial relationships
6. Scale, proportion and contrast
7. Alignment, grids and controlled deviations
8. Grouping, proximity and separation
9. Density, rhythm and pacing
10. Overlapping elements and layering
- Reading a direction into composition
- How the principles interact
- Evidence and its limits

---

## 1. Visual weight and balance

**What it means.** Visual weight is how strongly an element pulls the eye. Balance is whether the weight across
a frame (a screen, a section, a card) feels resolved, so that no area pulls so hard that the rest seems to slide
off, unless that pull is the point.

What adds weight:

| Factor | Heavier | Lighter |
| --- | --- | --- |
| Size | Large | Small |
| Value contrast with its surroundings | A dark block on a pale ground, or a pale one on dark | Close to the ground |
| Colour | Saturated, warm, the one accent on the page | Desaturated, cool, one of many |
| Detail and texture | A detailed photo, a dense block of small text | A flat field, a single line |
| Isolation | Alone in space | One of a crowd |
| Content | Faces, hands, prices, numbers, the word the visitor came for | Generic or repeated content |
| Shape | Compact, regular, closed | Thin, open, irregular |
| Position | Far from the centre (Arnheim's lever: weight further out counts for more); higher in the frame | Near the centre or the bottom |
| Direction | Things pointed at: by a gaze, an arrow, a diagonal | Things nothing points to |

These add and offset each other. A small, dark, dense block of text can balance a large pale photograph. A tiny
red price can outweigh a big grey heading.

**Why it matters.** Balance decides whether a page feels stable, formal, relaxed or restless before a word is
read. An unintended imbalance reads as broken or unfinished: the visitor senses something missing without
knowing what.

**Kinds of balance.**

- **Symmetrical:** mirrored weight around an axis. Stable, formal, ceremonial, still. (Section 2.)
- **Asymmetrical:** unequal elements counterweighted, like a heavy child near a seesaw's pivot and a light one
  far out. Directional and alive, but it needs a reason and a grid to stay deliberate.
- **Even, all-over:** weight spread evenly with no single focal point: a product grid, a gallery wall, a
  pattern. Right when the items are the subject and no one item should lead.
- **Deliberate tension:** visible imbalance used on purpose, such as one huge element pushed to an edge. For
  brands whose message is disruption or energy (a protest campaign, a club night). Still controlled: the tension
  is in one place, and the rest steadies it.

**Good and poor.**

- *Good:* a hero with a headline and short paragraph on the left, a real product screenshot on the right, the
  screenshot's detail matching the text block's weight so neither side wins by accident. A memorial page set
  dead centre, still and formal.
- *Poor:* the content pinned in a narrow column on the left of a 1920px screen, the right half empty.
  A decorative gradient blob added on the right to "balance" a text block, so the decoration now outweighs the
  message. A heavy dark band at the top of the page with nothing below to anchor it, so the page feels
  top-heavy without meaning to.

**Ways to do it.**

- Counterweight with different factors rather than duplicating size: big and pale against small and dark; one
  photo against a dense list.
- Set column ratios from the content's weight (`grid-template-columns: 5fr 7fr`), not by habit (`1fr 1fr`).
- Balance each screen and each section, not just the page. On the web the frame is the viewport, and it moves.
- On a phone, the frame is narrow and tall. Balance becomes mostly vertical (heavy over light), and left-right
  balance comes from alignment and scale rather than columns.

**Mistakes agents make.**

- Treating balance as two equal columns.
- Filling an empty side with decoration (blobs, gradients, floating icons) instead of asking what content should
  balance it, or whether the side should exist.
- Composing at 1440px only. A max-width container that's balanced at 1440 can sit lopsided at 1920.
- Using a transparent product cut-out that weighs far less than its box suggests, so a "balanced" two-column hero
  tips toward the text.

**Check on the render.** Mirror the screenshot (see the critique reference) and look again: imbalance you'd
stopped seeing becomes obvious. Cover each half in turn: does the remaining half look like a complete thought or
like a page missing something? Check at the widest size you support.

---

## 2. Symmetrical and asymmetrical composition

**What it means.** A symmetrical composition arranges elements around one central axis. An asymmetrical one
uses several alignment axes (usually a strong left edge plus column lines) and balances unequal elements
against each other.

**Why it matters.** The number of axes sets the register. One central axis says formality, stillness, ceremony,
"look at this one thing". Asymmetry says reading, movement, a sequence of different things. Jan Tschichold's
argument for asymmetric typography (1928) was functional, not stylistic: let the arrangement follow the
content's own logic instead of forcing everything onto a centre line. That's still the useful test: which
arrangement follows the content?

**What each is good at.**

| | Symmetry | Asymmetry |
| --- | --- | --- |
| Holds | One object, one message, one action | Several different things of different weight |
| Feels | Formal, stable, ceremonial, monumental | Directional, informal, active, editorial |
| Text | Fine for one to three lines; poor for paragraphs and lists (both edges ragged, so each line start must be found) | Natural for reading: a constant left edge |
| Needs | Content that is genuinely about one thing | A grid, or it looks accidental |

**When each fits.**

- **Symmetry:** a wedding or memorial page; an event sign-up with one action; an institution that should feel
  permanent; a product photographed head-on and presented as an object. Apple's product launch pages are centred,
  one product per screen, because each screen presents one object as a monument.
- **Asymmetry:** reading and tasks (GOV.UK's left-aligned two-thirds column, because people scan from a fixed
  left edge); a text-plus-artifact hero where the two halves differ; editorial and cultural pages where movement
  is part of the message.
- **Mixed:** a centred hero over a left-aligned body is common and can be right, if the switch happens at a clear
  section change and for a reason (the hero presents one thing; the body is read). It fails when axes alternate
  section by section with no reason (centred, left, centred, right).

**Good and poor.**

- *Good:* a symmetrical event page where the date, title and one button sit on the centre axis and nothing else
  competes. An asymmetric menu page where dish names hang on one line and prices on another.
- *Poor:* centred paragraphs of body text; a centred heading over a left-aligned list (two axes in one group);
  "asymmetry" made of random offsets that sit on no line.

**Ways to do it.**

- One axis per group. Within a card or a block, everything shares one alignment.
- For symmetry, centre the container and the content, and keep the content short. Use `text-wrap: balance` on
  centred headings so lines don't leave one orphan word.
- For asymmetry, decide the grid first (section 7), then place elements on its lines.
- **Alternating image-and-text rows** (the zigzag) are a rhythm, not a composition. They make the eye cross the
  page on every row. They suit a short sequence of genuinely parallel steps; three or more in a row usually
  reads as filler.

**Mistakes agents make.** Centring because it feels safe; centring long text; mixing axes inside one group;
zigzag rows as the default way to present features; calling arbitrary offsets "asymmetric".

**Check on the render.** Count the alignment axes on each screen. For centred text, count lines; more than three
lines of centred body copy is a fault. For asymmetry, name the grid line each element sits on; if you can't, the
asymmetry is accidental.

---

## 3. Visual hierarchy and focal points

**What it means.** Hierarchy is the ranking of attention: what's seen first, second, third, and what waits until
it's wanted. The focal point is what wins first. The entry point is where the eye arrives; on a good page they
coincide, or the entry point leads straight to the focal point.

**Why it matters.** People judge a page very fast. In Lindgaard et al. (2006), visual-appeal ratings formed in
about 50 milliseconds were consistent with ratings given after longer viewing. What wins in that moment decides
whether the visitor finds the page is for them. A page without a clear hierarchy makes the visitor do the
ranking, and many won't.

**How hierarchy is made.** Size, weight, value contrast, colour (especially a reserved accent), position (top,
and the left in left-to-right languages, or the centre of a symmetrical layout), isolation, enclosure, imagery
(faces especially), direction cues and motion (the strongest; use sparingly). Three levels plus body text read at
a glance. Beyond that, the steps blur.

**Single and distributed focus.**

- **One strong focal point** suits a page with one job: book, buy, sign up, read this.
- **Distributed focus** suits pages people arrive at with different tasks: a council homepage ("pay, report,
  apply"), a university's front door, a news front page. The focal point is the set of tasks or stories itself,
  ranked within, not a single hero.

**Good and poor.**

- *Good:* a bakery page where "Open now, until 4pm" and the photo of today's loaves lead, the menu is set small and
  orderly, and the order button is the only accent colour. A developer-tool page where the product's real output
  is the focal point and the headline is second.
- *Poor:* a first screen where a big headline, a saturated illustration, a pill badge, a gradient button, a
  secondary button and a logo strip all compete. A "flat" page where every heading is the same size and every
  section has the same density. A slogan as the focal point when the visitor's first question (hours, price,
  status) is answered nowhere near it.

**Ways to do it.**

- Choose the levers that fit the direction. A calm brand can rank by position and space instead of size; an
  urgent one by contrast and colour; an editorial one by scale.
- Don't stack every lever on one element (big + bold + accent + box + icon). It wastes the emphasis budget and
  leaves nothing to rank the next level with.
- Demote rather than promote. Lower the contrast of secondary text (while keeping 4.5:1 for body text), shrink it,
  remove its box.
- One primary action per view. A secondary action is a text link or a quiet outline, not a second filled button.

**Mistakes agents make.** Defaulting the focal point to the hero headline; letting decoration win; making
everything bold; adding icons above every card heading (each icon takes weight); two primary buttons; a pill
badge above the headline that steals the entry point.

**Check on the render.** Blur the screenshot: what's still visible? Look away, look back for five seconds, and
note what you remember. On a phone, check the first screen separately: a stacked image often pushes the focal
point below the fold.

---

## 4. Eye movement and visual flow

**What it means.** Flow is the path the eye takes from the focal point through everything else. It's driven by
weight (the eye goes from heaviest to next heaviest), reading direction, directional cues (a face's gaze, lines,
arrows, diagonals, the direction a product faces), continuity (the eye runs along shared edges) and, on the web,
scrolling.

**What eye-tracking says, and doesn't.** Nielsen Norman Group's studies found the familiar F-shaped scan on pages
of poorly formatted text, and other patterns when pages were well structured: a "layer-cake" pattern of
jumping from heading to heading, and a "spotted" pattern of hunting for specific things such as numbers, prices
or links. Their studies also found that people on left-to-right sites spent most of their viewing time on the
left half of the page, and that the first screen still got more viewing time than any later one. The Z-pattern
and the Gutenberg diagram are design heuristics for sparse layouts with weak evidence; don't treat them as
laws. Faces draw the eye early, and viewers tend to follow where a pictured face is looking (gaze cueing, well
replicated since Friesen and Kingstone 1998).

**Why it matters.** If the path doesn't run from the focal point through the evidence to the action, the visitor
stalls or leaves. Flow is also how a composition explains itself: the order of looking becomes the order of
understanding.

**Good and poor.**

- *Good:* headline, then the proof, then the action, with no doubling back. A photo of a person looking toward
  the headline. Section headings that carry information, so a heading-to-heading scan tells the story ("Open
  until 4pm today", not "Our story").
- *Poor:* the action placed where the path never goes (a button top right while the reading path ends bottom
  left); a face in a photo looking off the page; a dead end (a large image closing a section with nothing after
  it); a "pinball" first screen with several hot spots and no route between them.

**Ways to do it.**

- Put the action where the path ends, usually after the evidence that justifies it.
- Use shared edges as rails. One strong left edge carries the eye down a section.
- Face images inward, toward the content they belong to. Crop or mirror only if the image allows it honestly.
- Make headings landmarks for the layer-cake scan.
- **Hand off between screens.** A full-height hero that looks complete creates a false floor: nothing suggests
  there's more. Let the next section's heading or image show at the bottom of the first screen, or end the first
  screen on something open.
- On a phone there's one column, so flow comes from order, scale and space. The source order matters more.
- In right-to-left languages, mirror the reasoning, not just the layout.

**Mistakes agents make.** Relying on reading order and then breaking it with zigzags; carousels for important
content (most visitors never see past the first slide); `100vh` heroes that create false floors; CTAs outside the
path; headings that are labels ("Features") instead of information.

**Check on the render.** List the first five places your eye lands, in order, and compare them with the plan.
Check that the path passes the primary action. Look at the bottom edge of the first screen on both desktop and
phone: does anything invite a scroll?

---

## 5. Negative space and spatial relationships

**What it means.** Negative space is everything that isn't an element: margins, gaps, line spacing, the space
around an object. It isn't empty. It defines groups, gives isolated elements weight, sets the pace, and separates
figure from ground. Micro space works inside components (letter spacing, line height, the gap between a label and
its input). Macro space works between them (margins, gaps between groups, space between sections).

**Active and passive space.** Active space is shaped and does a job: it isolates the focal point, opens a
direction, lets an image breathe. Passive space is what's left over, and it shows: an awkward gap in the middle
of a layout where a short column meets a tall one, an emptiness nobody planned.

**Why it matters.** The ratios between spaces communicate structure before any content is read: what's together,
what's apart, what's important. The amount of space also signals register: a lot reads as considered, slow or
expensive; little reads as abundant, urgent or practical. But the signal is relative to the content and the
category. A record shop that looks like a gallery misreads its stock; a jeweller crammed like a supermarket
flyer misreads its price.

**Good and poor.**

- *Good:* a product page with ample space around the hero object and tight, orderly spec lists below. A form
  where each label sits tight to its field and the gap between fields is clearly larger.
- *Poor:* the same padding on every section and the same gap between everything, so space says nothing. A "luxury"
  first screen that's 80% blank with 12px text in a corner. Trapped space: a hole in the middle of a section that
  attracts the eye more than the content around it. Cramped content touching the viewport edge on a phone.

**Ways to do it.**

- A spacing scale with few steps, each with a role: inside a component, between related items, between groups,
  between sections, around the focal point. Name tokens by role (`--space-group`, `--space-section`), not by
  size alone, so their purpose survives edits.
- Headings belong to what follows: give them more space above than below (`margin-block: 2.5em 0.6em`, for
  example).
- Use `gap` in grid and flex layouts so relationships stay consistent, and margins only for exceptions.
- Fluid section spacing with `clamp()`, so a phone doesn't inherit desktop gulfs and a wide screen doesn't
  compress.
- Line length is horizontal space too: keep running text to roughly 45–80 characters (find-font covers this).

**When to spend space.**

- *Generously* around a single thing that must be contemplated (a product, a painting, a statement), for brands
  whose position is calm or rare, and in line spacing for long reading.
- *Sparingly* where visitors scan many things or where abundance is the message: a market stall's produce, a
  newspaper, a timetable, a hardware shop's range.
- Generous space around the focal point and tight space elsewhere is often stronger than moderate space
  everywhere.

**Mistakes agents make.** Equal margins above and below headings; one `gap` value everywhere; identical section
padding; whitespace used as a shortcut to "premium"; a short paragraph centred in a huge empty section; desktop
section spacing scaled down unchanged to a phone, so the page becomes an endless scroll of gaps.

**Check on the render.** Measure the vertical gaps (the critique reference has a snippet). Inside a group should
be smaller than between groups, which should be smaller than between sections. Find headings closer to the
content above than to their own. Squint: do groups pop out as groups? Look for holes surrounded by content on
three sides.

---

## 6. Scale, proportion and contrast

**What it means.** Scale is an element's size relative to the others and to the viewport. Proportion is the set
of ratios between parts: column widths, image aspect ratios, type steps. Contrast is any difference that
separates one thing from another: size, value, colour, weight, density, texture, shape, direction.

**Why it matters.** Scale contrast is the strongest weight lever, so the biggest element usually becomes the
focal point whether you meant it to or not. Consistent proportions repeated across a page (type steps, column
ratios, image shapes) make it feel considered. And nothing is noticed without contrast against something.

**Three scale positions, each right somewhere.**

- **Large contrast** (one element many times body size): campaigns, events, posters, a brand built on one
  statement. The big moment must be the right content, and short enough to stay big on a phone.
- **Moderate contrast:** most marketing and service pages. A clear headline, a few heading steps, body text.
- **Flat scale** (everything near body size): documents, reference, tools, indexes, some restrained luxury and
  catalogue sites where the items are the interest. Hierarchy then comes from position, weight, space and order,
  and must be deliberate, or the page reads as unstyled.

**Good and poor.**

- *Good:* one dominant element and a few clearly different steps below it. A deliberately flat page where a
  strict grid and bold weights do the ranking.
- *Poor:* many near-identical sizes (16, 17, 18, 20, 22, 24px), which reads as indecision. A hero headline at 96px
  regardless of copy length, wrapping to five lines on a phone and pushing the action below the fold. A giant
  heading on every section, so there's no big moment at all. Columns at `1fr 1fr` when one holds a paragraph and
  the other a detailed image. Side-by-side images in unrelated aspect ratios.

**Ways to do it.**

- Choose sizes by role, then check the steps are distinct. A ratio scale (1.2 for dense interfaces, larger for
  expressive pages) is a starting point, not a law.
- `clamp()` for display sizes, with a phone minimum chosen from the real headline's wrap, not a formula.
- Use a small set of image aspect ratios with a reason each (a portrait crop for people, a wide one for places).
- Contrast on one or two dimensions at a time. As with type pairing, contrast in everything competes; contrast
  in nothing blurs.
- Dimensions other than size are underused: one dark band in a pale page, one dense table among open sections,
  one photograph among flat illustrations, one rotated stamp among square elements.

**Mistakes agents make.** The same hero size and scale ratio for every brief; display type not reduced on phones;
rows of giant numbers; emphasising one element with size, weight, colour and a box at once; proportion by habit.

**Check on the render.** Count the distinct font sizes (the critique snippet lists them). Compare the largest text
with body text. Check the hero's wrap on a phone. Confirm the biggest element is the focal point you planned in
step 2 of SKILL.md.

---

## 7. Alignment, grids and controlled deviations

**What it means.** Alignment creates invisible lines that connect elements. A grid is a system of those lines
shared across the page: columns, gutters, margins, sometimes rows and a baseline. A controlled deviation is an
element that leaves the grid on purpose: a full-bleed image, a number hanging into the margin, a featured item
spanning two columns, a stamp set at an angle. A deviation reads as intentional only against a grid strong enough
to deviate from.

**Optical alignment.** Align by what the eye sees, not by bounding boxes. Round letters and icons need to overshoot
a straight edge slightly; a play triangle in a circle sits a little right of centre; quotation marks hang outside
the text edge; an icon beside text aligns to the cap height or x-height, not the line box.

**Why it matters.** Alignment makes order visible, lets the eye find related things, and lets many elements share
a page without noise. Strict alignment reads as precise and trustworthy; loose alignment as relaxed or handmade;
accidental misalignment as careless.

**Kinds of grid.**

| Grid | Suits |
| --- | --- |
| Manuscript (one column) | Reading: articles, documentation, policies, letters |
| Column grid (12, 6, 4, or proportions such as two-thirds and one-third) | Most marketing and service pages |
| Modular (columns and rows) | Catalogues, galleries, products, timetables |
| Hierarchical (custom proportions for one page) | Front pages and homepages with mixed content |
| Baseline | Long text where neighbouring columns should line up |

Müller-Brockmann's *Grid Systems in Graphic Design* (1981) remains the clearest account of why grids work.

**Good and poor.**

- *Good:* few left edges on a screen, all intended; elements in different sections sharing the same lines; one or
  two deviations, each pointing at something important.
- *Poor:* near-miss alignment (a heading at 120px, text at 124px, an image at 112px); a different container width
  in every section (1280, 1200, 1440); "broken grid" styling with no grid underneath; centred and left-aligned
  items in one group; card prices at different heights because titles wrap differently.

**Ways to do it.**

- Declare the page grid once, with named lines, and let children choose a track:

  ```css
  .page {
    display: grid;
    grid-template-columns:
      [full-start] minmax(1rem, 1fr)
      [content-start] minmax(0, 72rem) [content-end]
      minmax(1rem, 1fr) [full-end];
  }
  .page > * { grid-column: content; }
  .page > .bleed { grid-column: full; }
  ```

  Breakouts then land on real lines instead of arbitrary offsets.
- Use `subgrid` so the parts of repeated items (title, description, price) align across a row.
- Make deviations few and purposeful. Name, for each: the line it leaves, what it points at, and what would be
  lost without it.

**When to be strict or loose.** Strict grids with rare deviations suit precise, technical, institutional and
catalogue brands, and anything people compare. More deviation suits editorial, cultural and campaign work. But
the grid is still there; a loose composition with no structure isn't loose, it's lost.

**Mistakes agents make.** Random `translate` or margin offsets to look designed; per-section container widths;
deviations aligned to nothing; an image hanging out of the container while its text doesn't; no subgrid, so
repeated items misalign; icons visibly off their text.

**Check on the render.** Outline every element and screenshot (the critique reference shows how). Run the edge
audit: list the left edges of visible blocks; any two within 1–8px of each other are almost certainly a bug. List
each deviation with its reason.

---

## 8. Grouping, proximity and separation

**What it means.** People perceive some elements as belonging together. The Gestalt principles describe the cues:
**proximity** (near things group), **similarity** (alike things group: shape, colour, size), **common region**
(things inside a shared boundary group, Palmer 1992), **connectedness** (things joined by a line group, Palmer and
Rock 1994), **continuity** (things along a line or curve group) and **common fate** (things that move together
group). Separation is the reverse: the tools that keep groups apart.

**Strength of cues.** Connection and enclosure usually beat proximity, and proximity usually beats similarity of
shape. But a strong colour similarity can beat weak proximity. Treat this as a tendency and look at the result.

**Separation tools, quietest to loudest:** space; a change of alignment; a hairline rule; a change of background
(common region); a border or card; a shadow. The louder the tool, the more visual weight it adds and the less
meaning it keeps when overused.

**Why it matters.** Groups reduce the number of things the visitor has to process. Misgrouping makes them misread:
which price goes with which dish, which label belongs to which field, which button acts on which offer.

**Good and poor.**

- *Good:* a label clearly closer to its field than to the field above. A caption tight under its image. A menu
  where each dish and its price form one line, and a larger gap separates courses.
- *Poor:* equal spacing, so a label floats between two fields. Everything in cards, cards inside cards, until
  enclosure means nothing (check-layout's "rounded boxes everywhere"). Links and headings in the same colour, so
  similarity groups things that do different jobs. A divider, a background change and a border all separating
  the same two things.

**Ways to do it.**

- Start with space alone. Add a rule only when the space needed would be too large. Use a tinted region for the
  one group that must stand apart (today's hours, a warning). Use a card when each item is an object: clickable as
  a whole, with its own state, or genuinely separate.
- Make proximity unambiguous: the gap inside a group should be visibly smaller than the gap between groups.
- Use similarity deliberately: everything clickable looks clickable, and nothing else does.

**When to use stronger separation.** Dense pages need rules and tints because space is scarce. Open pages can
group by space alone, and adding boxes there just adds weight.

**Mistakes agents make.** One `gap` value for everything; cards for every list; a divider and padding between
every item; placing an action closer to the wrong content (a "Buy" button nearer a testimonial than the offer it
buys).

**Check on the render.** Squint: do the groups you planned appear, and no others? For every label, caption, price
and button, ask: is it unambiguously closest to what it belongs to? Measure where unsure.

---

## 9. Density, rhythm and pacing

**What it means.** Density is how much content occupies an area. Rhythm is the pattern of repetition and
variation in sizes, spaces and kinds of section: regular, alternating or progressive. Pacing is how density and
intensity change as the visitor scrolls: where the page slows down (a large image, a single statement) and where
it speeds up (a list, a table, a run of short items).

**Why it matters.** Density signals what kind of page this is before anything is read: newspaper, catalogue and
utility at one end; gallery, invitation and manifesto at the other. Uniform density from top to bottom reads as
monotonous and hides what matters; taste's house-style check calls this "flat after the hero". Changes of pace
mark changes of subject and give the eye somewhere to rest.

**Good and poor.**

- *Good:* density that matches use: dense where visitors compare and scan (a timetable, a menu with prices, a spec
  table), open where one thing should be considered (a product photo, a single claim). A steady rhythm in
  repeated items, broken at a meaningful point (today's special, the recommended plan).
- *Poor:* every section with the same padding, the same eyebrow-heading-paragraph-grid recipe and the same
  density. Alternating zigzag rows as the only rhythm. Pacing too slow for the content: one sentence per screen,
  scroll after scroll. Pacing too fast: a wall of content with no rest. Variation without reason (sizes that change
  for nothing), which is noise, not rhythm.

**Ways to do it.**

- Write a pace profile: list the sections and mark each loud or quiet, dense or open. For a bakery, perhaps
  quiet-dense (hours board), loud-open (today's bread), quiet-dense (menu), quiet-open (order a cake). Then build to
  it.
- Vary space between sections by relationship: related sections closer; a change of subject gets more space or a
  change of ground.
- Give parallel items the same internal structure, and break the pattern only for a reason.
- In text, keep vertical spacing related to the line height so paragraphs, lists and headings fall into a rhythm.

**When to be steady or varied.** A steady pace suits documents, reference and utility, where predictability is the
point. A varied pace suits marketing narratives, cultural pages and portfolios. Dense often suits professionals and
repeat visitors; open often suits first-time, considered decisions. These are tendencies, not rules: a watch
maker's specification page is dense and premium; an emergency notice may be almost empty because it has one
message.

**Mistakes agents make.** Identical section padding; every section built from the same recipe; uniform density
after the hero; slow "scrollytelling" for content that needed a list; card grids where every card is the same size
even though one item matters more.

**Check on the render.** Look at the full-page screenshot zoomed right out. Describe its rhythm as a strip. Does it
look like a barcode of identical blocks? Does the profile match the plan? On a phone, is the page absurdly long
because desktop spacing was scaled down unchanged?

---

## 10. Overlapping elements and layering

**What it means.** Elements that share an area at different depths: text over an image, an image crossing a
section boundary, a card sitting over a coloured band, stacked objects, shadows and translucency, a sticky header
over content. Layering creates depth and figure-ground, ties elements together across a boundary, and gives the top
layer weight.

**Why it matters.** Layering can express something true: physical objects (records in a crate, papers on a desk), a
product in its context (an interface over a photo of where it's used), continuity (an image linking two sections).
Without such a reason, it adds clutter and legibility problems, and it breaks first when the layout changes width.

**Good and poor.**

- *Good:* text over a photograph where the photo has a calm area under the text at every crop and contrast passes
  (WCAG 1.4.3). An overlap that's clearly deliberate: substantial rather than a few pixels, with an obvious top
  layer. On a phone, the overlap scales down or is removed by design.
- *Poor:* text over a busy photo rescued by a heavy dark gradient. Small accidental collisions that look like bugs.
  Overlaps that cover text when it wraps differently. Decorative blobs and translucent cards over gradients, which
  is now an AI cliché. A face in the photo covered by the headline. Overlap that contradicts reading order.

**Ways to do it.**

- Stack with grid, not absolute positioning: put both elements in the same cell (`grid-area: 1 / 1`) and offset
  with the grid's own tracks. They stay in flow and responsive.
- Contain stacking with `isolation: isolate` instead of escalating `z-index` values.
- Keep the important part of an image visible at every crop with `object-position`, and check each crop.
- Test overlaps against text resizing and spacing: 200% zoom (WCAG 1.4.4), increased text spacing (1.4.12) and
  reflow at 320px (1.4.10). Fixed heights and overlaps are where these fail.

**When it fits.** Tactile or physical brands, editorial, fashion and culture, collage-based identities, products
shown in context. Rarely for utility, data, or tasks done under stress.

**Mistakes agents make.** Overlap as a signal of "designed"; pixel offsets that only work at one width; text over
the subject of the photo; overlaps that collide on a phone; glassmorphism without a reason.

**Check on the render.** Check every overlap at 390, 1024, 1440 and 1920. Measure text contrast at the worst point
of the image behind it. Zoom to 200%. Write the overlap's reason in one sentence; if you can't, remove it.

---

## Reading a direction into composition

Each line is a pair of qualities a direction might ask for and what tends to follow. These are tendencies to test,
not a lookup table, and each pole has its own cliché.

| Quality | Tends toward | Its cliché |
| --- | --- | --- |
| Calm | Small steps between sizes, steady rhythm, symmetry or gentle asymmetry, space spent evenly, little layering | Emptiness with nothing to look at |
| Energetic | Strong scale contrast, diagonals or tension, varied pace, tighter space, possibly layering | Everything shouting; motion everywhere |
| Formal | Symmetry or a strict grid, centred focal objects, measured spacing | Stiff institutional sameness |
| Informal | Asymmetry, looser grid, hand-placed elements (still on lines), mixed scales | Random placement |
| Abundant | Density, repetition, a modular grid, many items visible at once | Clutter with no groups |
| Rare or exclusive | Few elements, isolation of the focal object, slow pace | The 80%-empty "luxury" screen |
| Precise | Strict alignment, consistent spacing, tables, few deviations, small scale contrast | Cold spec sheet with no focal point |
| Handmade | Irregularity within a grid, overlapping physical objects, organic edges | Fake mess; scattered stickers |
| Guided (one path) | One focal point per screen, a single column of flow, actions where the path ends | A long, slow funnel |
| Exploratory (many paths) | Distributed focus, an index or grid of entry points, scannable labels | No hierarchy at all |
| Reading | One measure, a strong left edge, generous line spacing, quiet margins | Text wall without landmarks |
| Comparing | Aligned columns, shared baselines, subgrid, tables | Everything in identical cards |

Two directions can ask for opposite things from the same category: a neighbourhood bakery that sells abundance
and a patisserie that sells rarity should not share a composition.

---

## How the principles interact

None of these can be adjusted alone. Some of the chains that matter most:

- **Scale ↔ space ↔ balance.** A large element needs proportionally more space around it to read as one thing.
  Enlarging it takes space from neighbours and shifts weight to its side, so the counterweight must change too.
- **Space ↔ weight ↔ hierarchy.** Isolation adds weight. A small element surrounded by space can be the focal
  point, so whitespace is a hierarchy tool, not just breathing room. Space spent everywhere ranks nothing.
- **Density ↔ contrast.** Emphasis is relative to the baseline. In a dense timetable, one bold line is loud; on an
  open page, it takes a big change to register. Dense pages need smaller, sharper contrasts; open pages need larger
  ones.
- **Grid ↔ deviation ↔ hierarchy.** A deviation attracts attention, so it's a hierarchy tool. Spend it only on
  what deserves rank. Too many deviations become the new grid and nothing stands out.
- **Grouping ↔ flow.** Groups are the units the eye travels between. Misgrouping creates detours: the eye goes to
  the label, then the wrong field, then back.
- **Symmetry ↔ hierarchy.** Symmetry concentrates attention on the axis, so the centre line is the focal path.
  Asymmetry spreads attention and needs a deliberate ranking to replace the axis.
- **Layering ↔ grouping.** Overlapping elements read as strongly connected. Use overlap to join things that belong
  together, never to decorate unrelated ones.
- **Rhythm ↔ contrast.** Regular repetition is what makes the exception visible. A featured item stands out only
  against a steady pattern.
- **Flow ↔ pacing.** The path through one screen and the pace across many are the same thing at two scales. A
  section that ends on its heaviest element stalls the scroll; one that ends open hands off.
- **The phone collapses several.** On a narrow screen, balance becomes vertical, asymmetry becomes alignment and
  scale, grouping depends more on space, scale contrast must shrink, and layering usually reduces.

**A worked example.** A bakery wants "Open now, until 4pm" to be the first thing seen. Four levers would do it,
and each costs something elsewhere:

- *Size:* make it large. It becomes the headline, competes with the bread photo and changes the hero's balance.
- *Colour:* the accent. Then the accent can't also mark the order button, so the action loses rank.
- *Isolation:* give it space at the top. It costs height, and on a phone it pushes the photo down.
- *Position and enclosure:* a slim band above everything. Cheap and clear, but bands are also where notices and
  ads live, so it may be skipped.

A good answer might combine position with modest size and leave colour for the action. The point is that the
decision is about the whole composition, not the one element.

---

## Evidence and its limits

Most composition knowledge is craft: tested by practice, not experiments. Treat it as reasoning to apply and check
on the render, not as law. Where research exists:

- **Gestalt grouping** (Wertheimer 1923; Palmer 1992 on common region; Palmer and Rock 1994 on connectedness) is
  well established. The relative strength of cues depends on context.
- **First impressions** form very fast (Lindgaard et al. 2006). Tuch et al. (2012) found that websites with lower
  visual complexity and higher prototypicality (looking like their category) were judged more beautiful at first
  glance. That's evidence that a conventional composition can be the right one, not that every page should be
  simple and typical.
- **Eye-tracking** (Nielsen Norman Group's studies of scanning patterns, left-side attention and the first
  screen) shows how people tend to look at real pages. It describes typical behaviour on typical pages and
  changes with design.
- **Faces and gaze** draw and redirect attention (gaze cueing, Friesen and Kingstone 1998).
- **Visual weight and balance** come mainly from Arnheim's *Art and Visual Perception* (1954, revised 1974). Some
  of his claims, such as the right side of a frame being heavier, have mixed evidence; don't build on them.
- **The golden ratio and rule of thirds** have little evidence of a reliable aesthetic preference. They're
  starting points at best; never a reason in a composition plan.
