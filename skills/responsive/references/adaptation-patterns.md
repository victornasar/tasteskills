# Adaptation patterns

How complex content changes between wide and narrow screens. Each pattern names what it preserves and what it
costs. Choose by what the visitor needs to keep doing on the small screen.

## Tables

| Pattern | Preserves | Costs | Use when |
| --- | --- | --- | --- |
| Horizontal scroll inside the table container, sticky first column | Every value and the ability to compare across rows | Hidden columns need a visible hint (a shadow at the edge, a "scroll" cue) | Comparison across many columns is the point |
| Stacked rows (each row becomes a labelled card: label, value) | Every value of one row | Comparing rows means scrolling | People look up one row at a time (orders, appointments) |
| Fewer columns with a detail view | The key columns | Extra tap for the rest | A few columns decide; the rest are detail |
| Pivot (one item at a time, switchable) | Column-by-column comparison | Only one column visible | Comparing two or three products |
| Summary plus full table on demand | Quick answer | Indirect access to detail | Most visitors need one figure |

Don't drop columns silently. Keep real `<table>` markup; for stacked rows, keep the header association (repeat the
label visually, keep the table semantics or use a description list).

## Multi-column grids

- **Fewer columns:** 4 → 2 → 1 with `auto-fill` / `minmax`. The default for parallel items.
- **Horizontal scroller:** a row that scrolls sideways, used sparingly for a small set of browseable items
  (related products). Show part of the next item so scrolling is discoverable; use `scroll-snap-type`; never put
  essential content in one.
- **Collapse into a list:** cards with images become compact rows with thumbnails. Often better than one huge card
  per screen.
- **Promote one, list the rest:** the featured item stays large; others become a list.

## Sidebars and secondary columns

- **Move below:** the sidebar content follows the main content. Fine for related links.
- **Move above, condensed:** filters or a table of contents become a single control ("Filters (3)", "On this
  page") at the top.
- **Disclosure or drawer:** filters in a sheet opened by a button that shows the active count.
- **Inline:** marginal notes move inline after the paragraph they annotate.

## Navigation and secondary navigation

- Tabs with many items → a horizontally scrolling tab row (with a visible cut-off) or a select-like menu.
- Mega-menus → a drill-down panel (one level at a time, with a back control).
- Breadcrumbs → just the parent ("← Bathroom taps").
- Footer link farms → grouped disclosures.

## Forms

- Two-column forms → one column (two-column forms are usually worse on desktop too, except for genuinely paired
  fields like city and postcode).
- Inline field groups (day / month / year) stay inline if they fit; otherwise stack with labels.
- Sticky submit for long forms on phones, if it doesn't cover inputs when the keyboard opens.

## Media and wide content

- **Hero images:** a different crop per ratio (`<picture>` with `media`), not one image cropped by CSS to nothing.
- **Video:** poster frames that make sense at the phone crop; captions; no autoplay with sound.
- **Charts:** fewer data labels, a simpler form (bars instead of a dense line chart), or a summary sentence plus
  the chart; horizontal bar charts usually survive narrow screens better than vertical ones.
- **Maps:** a static map image with a link to open in the map app often beats an embedded interactive map on a
  phone, which traps scrolling.
- **Code blocks:** horizontal scroll within the block, never wrapping that changes meaning.

## Dashboards and tools

Decide the phone's job. Often it's monitoring (the few numbers that need action and alerts) rather than doing
everything. Show those first, collapse the rest, and say what's available on a larger screen instead of cramming
it in.

## Type and space across sizes

- Fluid type: `font-size: clamp(2rem, 1.2rem + 3vw, 4rem)`. Choose the minimum from the real headline's wrap on
  a 320–390px screen, and the maximum from the wide layout. Include a `rem` term so text still scales with user
  zoom.
- Body text usually stays 16–18px across sizes; the display steps shrink most.
- Line length: cap with `max-width` in `ch` so wide screens don't produce 150-character lines.
- Section spacing: reduce more on phones than component spacing, so groups stay legible and the page isn't an
  endless scroll of gaps.

## Breakpoint naming

```css
/* Named for what changes, set where the content needed it */
@media (min-width: 42em) { /* two-column menu */ }
@media (min-width: 64em) { /* sidebar appears beside the article */ }

/* Components adapt to their slot */
.card-list { container-type: inline-size; }
@container (min-width: 36em) { .card { grid-template-columns: 8rem 1fr; } }
```

`em` in media queries respects the user's font size setting.
