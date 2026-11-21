# Chart guide

## Perceptual accuracy

Cleveland and McGill (1984) ranked how accurately people judge quantities by encoding. From most to least
accurate:

1. Position along a common scale (aligned bars, dots on one axis)
2. Position along non-aligned scales (small multiples)
3. Length, direction, angle
4. Area
5. Volume, curvature
6. Shading and colour saturation

Use the top of the list for the comparison that matters. Use lower encodings (colour, size) for secondary
information or rough pattern.

## Forms and their pitfalls

**Bar chart.** The workhorse for comparing categories. Start at zero. Sort by value. Horizontal bars for long
labels and many categories (they also survive phones). Keep bar gaps narrower than bars. Label values at the bar
ends when exact values matter, and drop the axis.

**Grouped and stacked bars.** Grouped bars compare within groups; more than three or four series per group becomes
unreadable. Stacked bars show totals well but only the bottom segment is easy to compare; use a 100% stacked bar
for composition, and consider small multiples instead.

**Line chart.** For continuous change over time. Up to about four or five series before it tangles; highlight one
and grey the rest, or use small multiples. Don't connect points across missing data without showing the gap. A
zoomed y-axis is acceptable for lines when the axis is labelled and the change is the point.

**Area chart.** Emphasises volume; stacked areas make all but the bottom layer hard to read. Use sparingly.

**Pie and donut.** Only for part-to-whole with two or three parts where approximate proportion suffices. Never for
comparing across several pies. A single stacked bar usually does better.

**Scatter plot.** For relationships. Label notable points directly; add a trend line only if it's meaningful; use
transparency for overplotting.

**Histogram, dot plot, box plot.** For distributions. Averages hide distributions; show them when spread matters
(response times, prices, ages).

**Slope chart and dumbbell plot.** For change between two points across categories: clearer than grouped bars.

**Small multiples.** The same chart repeated for each category with shared axes. Usually better than one chart with
ten series.

**Heatmap.** For patterns across two dimensions (hour × weekday). Use a sequential ramp; label the scale.

**Map (choropleth).** Area distorts importance (big empty regions dominate). Normalise values (per capita), use a
sequential ramp, and consider a sorted bar chart instead when geography isn't the point.

**Gauges, radial bars, 3D charts, word clouds.** Almost always worse than a number with context or a bar.

## Single numbers

A big number needs:

- **Context:** compared to what (previous period, target, benchmark).
- **Direction and meaning:** up is good or bad? Say it ("12% fewer complaints than last month").
- **Period and unit.**
- **Precision that matches the decision:** "£4.2M", not "£4,213,887.42", unless the exact figure is needed.

A sparkline beside the number shows trend without a full chart.

## Tables

- Numbers right-aligned with tabular figures (`font-variant-numeric: tabular-nums`), same decimal places in a
  column.
- Text left-aligned. Headers aligned with their column's content.
- Units in the header ("Revenue (£k)"), not repeated in every cell.
- Sort by the column people care about; let them re-sort when they need to.
- Light horizontal rules or subtle zebra stripes for long rows; no vertical rules unless columns are dense.
- Highlight the row, column or cell the reader should notice; keep everything else neutral.
- Sticky header and first column for large tables; on phones, see `responsive`'s table patterns.
- Real `<table>` with `<th scope>`; a `<caption>` that states what the table shows.

## Dashboards

1. Write the decisions the dashboard supports ("Do we need more staff this week?").
2. For each decision, the one number or chart that answers it.
3. Arrange by priority: what needs action first, then what explains it, then reference detail.
4. Keep shared time ranges, scales and colours across charts.
5. Use words for status alongside colour.
6. Limit the first screen to what fits without scrolling on the main device, and put detail one click deeper.

Density depends on the user: an operations team watching all day can handle dense displays they've learned; an
executive glancing weekly needs three numbers with context.

## Colour for data

| Data | Palette | Notes |
| --- | --- | --- |
| Categories (no order) | Distinct hues of similar lightness and chroma | Up to about 6–8; beyond that, group or label directly. The Okabe–Ito palette is a well-tested colour-blind-safe set |
| Ordered quantity | Sequential: one hue (or a perceptual multi-hue ramp) from light to dark | Lightness carries the order; viridis-style ramps are perceptually uniform |
| Quantity around a midpoint | Diverging: two hues meeting at a neutral | The midpoint must mean something (zero, average, target) |
| Highlight | Grey for everything, one accent for the focus | Often the clearest choice for websites |

- Derive data colours from the brand palette where possible, but don't force the brand's single accent to do
  categorical work.
- Build ramps in OKLCH so steps are perceptually even (`color` explains OKLCH).
- Check marks against the background at 3:1, and adjacent categories against each other.
- Status colours (good, warning, bad) must not collide with category colours.
- In dark themes, re-tune: saturated colours glow on dark grounds.

## Misleading patterns to avoid

- Truncated y-axis on bar charts.
- Dual y-axes that make two unrelated series look correlated.
- Area or volume scaled by height (a doubled icon has four times the area).
- Cherry-picked time ranges that hide context.
- Cumulative charts presented as if they were growth.
- Averages hiding bimodal or skewed distributions.
- Inconsistent intervals on the x-axis without showing it.
- Percentages without the base ("up 200%" from 1 to 3).
- Uncertainty hidden: show ranges or confidence intervals when the data has them.

## Implementation notes

- SVG for most web charts (sharp, styleable, accessible). Canvas for thousands of points, with an accessible table
  alternative.
- Libraries (D3, Observable Plot, Vega-Lite, Chart.js, Recharts) are fine; override their default colours,
  gridlines and legends rather than shipping them unchanged.
- Responsive: redraw at container width (`ResizeObserver`), reduce tick counts and labels on narrow widths, switch
  to horizontal bars or a table when needed.
- Animate only transitions that help track change between states (`motion`), and respect reduced motion.
