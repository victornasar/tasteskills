---
name: dataviz
description: Present data on websites and dashboards so the reader sees the right comparison quickly and isn't misled. Covers starting from the question, choosing between a sentence, a number, a table and a chart, chart selection, visual encoding and perceptual accuracy, tables, dashboard hierarchy, labels, legends and annotation, comparisons, data density, colour for data, accessibility and honest scales. Use when adding a chart, graph, table of figures, KPI row, dashboard or any data display, or reviewing one that's hard to read or might mislead. Not for decorative illustration (`images`) or general page hierarchy (`hierarchy`).
argument-hint: "[data, chart, table or dashboard]"
---

# dataviz

A chart is an argument about data: "these grew", "this one is the outlier", "most of it goes here". Choose the
form that makes that comparison easiest to see accurately, label it so nobody has to decode a legend, and never
let the design exaggerate or hide what the numbers say. Often the best visualization is a sentence, a single
number with context, or a well-set table.

Data, chart, table or dashboard:

$ARGUMENTS

If this is empty, review the data displays in the current project.

## Where this sits

- `hierarchy` ranks a dashboard's contents; this skill designs each data display and the data-specific
  hierarchy within it.
- `color` builds the brand palette; this skill derives data colours from it with rules of its own.
  `a11y` sets the contrast and text-alternative requirements. `responsive` covers adapting
  charts and tables to small screens.
- taste's copy rule applies: never invent data. Use the brief's real figures, or clearly labelled sample data the
  user has agreed to.

## Principles

1. **Start from the question.** What should the reader be able to answer? "Are we on track this month?" needs a
   number against a target; "which region is growing fastest?" needs a sorted comparison; "what's the pattern
   over the year?" needs a time series. The question picks the form, not the data's shape or the chart library's
   gallery.
2. **Encode what matters most with what people judge best.** People compare positions on a common scale most
   accurately, then lengths, then angles and slopes, then areas, then colour saturation and volume (Cleveland and
   McGill, 1984). Put the key comparison on position or length; don't make readers compare pie slices or bubble
   areas when precision matters.
3. **Honest scales.** Bars start at zero, because length is the encoding. Line charts may zoom to the data's range
   when the change is the point, but label the axis clearly. Don't use dual axes to imply correlation, truncated
   axes to exaggerate, or 3D to distort.
4. **Label directly.** Put labels on the data (series names at the line ends, values on bars) rather than in a
   legend the reader has to match by colour.
5. **Remove what doesn't carry data,** but not what helps reading. Heavy gridlines, borders, backgrounds, 3D,
   shadows and gradients go; a light reference line, a target and an annotation stay. Tufte's data-ink idea is a
   direction, not a target: some non-data ink (labels, a title that states the finding) is essential.
6. **Colour encodes, so use it on purpose.** Categorical hues for categories, a sequential ramp for ordered
   quantities, a diverging ramp around a meaningful midpoint, and one highlight colour against grey for "look at
   this one". Never colour alone.

## How to work

### 1. Write the question and the finding

One line each: what the reader needs to answer, and (if known) what the data shows. The finding often becomes the
chart's title ("Signups doubled after the March price change") instead of a label ("Signups 2026").

### 2. Choose the form

Start with the lightest form that answers the question:

| Need | Form |
| --- | --- |
| One number that matters | The number, large, with context: compared to what (last month, target, average) and the direction |
| A few numbers | A sentence or a small table |
| Looking up exact values | A table |
| Comparing categories | A bar chart (horizontal when labels are long), sorted by value unless the order means something |
| Change over time | A line chart (many points) or bars (few periods) |
| Part of a whole | A stacked bar or a single 100% bar; a pie only for two or three parts where rough proportions suffice |
| Distribution | A histogram, dot plot or box plot |
| Relationship between two measures | A scatter plot |
| Ranking and change between two points | A slope chart or dumbbell plot |
| Many small series | Small multiples with shared axes |
| Geographic pattern | A map only when location matters; otherwise a sorted bar chart by region reads better |

`references/chart-guide.md` covers each form's pitfalls, tables, dashboards and colour for data in more depth.

### 3. Design the chart

- **Title** states the finding or the question; a subtitle states units, period and source.
- **Axes:** label units; use few, round tick values; format numbers for humans (1.2M, 12%, £3,400); start bars at
  zero.
- **Labels:** direct labels on lines and bars; label only the values that matter if all would clutter.
- **Highlight:** grey for context, one colour for the series or bar that the finding is about.
- **Annotation:** mark events that explain changes ("price change", "outage").
- **Gridlines:** light and few, or none when values are labelled.
- **Sort** categorical bars by value; keep a fixed order only when the order means something (time, a scale).
- **Aspect ratio:** line charts wide enough that slopes aren't exaggerated or flattened; banking to about 45° for
  the slopes that matter is a useful guide.

### 4. Design tables

Tables are often the right answer. Right-align numbers, use tabular figures, align decimal places, left-align
text, keep units in headers not every cell, use light rules or zebra stripes only as needed, make the header
sticky for long tables, and highlight the one row or column the reader should notice. Add sparklines or inline
bars only when the trend matters.

### 5. Design dashboards

- Rank first (`hierarchy`): the one or two things that need action go top left and largest.
- Every number has context: a comparison, a target, or a trend. A KPI tile with "4,213" and nothing else answers
  nothing.
- Group by the decision they support, not by data source.
- Use the same scales, colours and time ranges across related charts so they can be compared.
- Show status in words and shape as well as colour ("Below target" with an icon, not just a red number).
- Fewer charts that answer questions beat a wall of tiles.

### 6. Build accessibly

- Charts as SVG (or canvas with an accessible alternative) with `role="img"` and an `aria-label` stating the
  finding, plus a data table available nearby (visible, or behind a "Show data" disclosure).
- Contrast: chart marks 3:1 against the background (WCAG 1.4.11); text labels 4.5:1.
- Distinguishable without colour: direct labels, patterns or shapes for series, different line styles.
- Test palettes with a colour-vision-deficiency simulation; avoid red–green pairs as the only distinction.
- Interactive tooltips must also work on focus and touch, and the values must be reachable without them.

### 7. Check the render

At desktop and phone widths:

1. Look for five seconds. Can you say the finding? Does it match the title?
2. Read a value: is it possible without squinting at a legend or hovering?
3. Is the comparison that matters encoded by position or length?
4. Do the scales start where they should? Any truncation, dual axis or 3D that distorts?
5. Grayscale and colour-blindness simulation: can you still tell series apart?
6. Phone: are labels legible, or does the chart need a simpler form or a table?
7. Is every number on the page real and from the brief?

Report the question, the form and why, the encodings, the colour roles and the accessible alternative.

## Mistakes agents make

- A row of big KPI numbers with no comparison or meaning (`layout` lists this among overused patterns).
- Pie and donut charts for many categories or close values; 3D anything.
- Bar charts not starting at zero; dual axes; inconsistent scales between related charts.
- Rainbow palettes for categories with no meaning; a sequential ramp for categories; red and green as the only
  distinction.
- Legends far from the data; tooltips as the only way to read values.
- Decorative gradients, glows and shadows on chart elements.
- Charts for data that's two numbers ("40% vs 60%") or that should be a table.
- Alphabetical sorting of bars that should be ranked.
- Invented sample data presented as real.
- Tiny, unreadable axis labels on phones.
