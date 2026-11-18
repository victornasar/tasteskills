- **Lead with the artifact:** the first screen is a left-aligned headline beside the invoice line, which opens into 31 daily totals that sum to 1,204,388. The daily figures are illustrative and labelled that way, and the 1,204,388 × $0.0004 = $481.76 arithmetic is checked.
- **Fonts (engine picks, self-hosted):** Overpass for headlines, IBM Plex Sans for body, Iosevka for figures and code. I didn't bundle the files, so `./fonts/*.woff2` needs adding, and system fallbacks apply until then. Steps Mono was ruled out because it lacks `= { } [ ]`.
- **Colour (engine, Graphite and Signal):** one blue (#0E6EE6) is used only for links, focus and the toggle, and buttons are graphite. Grouping is by hairline rules, with no cards, pills, gradients or icons.
- **Cut from the default page:** the stats row, testimonials, logos and a CTA band. The brief supplies none of them, so the page ends at pricing and a repeat of the two actions.
- **Critique:** the layout checker found none of the nine patterns, and one fix round restored the side gutters I had lost on the hero and closing section. `DIRECTION.md` stays `draft` because it was not approved in this non-interactive run. Link targets, the font files and the reading of fennel-street.md are listed as open decisions.

Files are in `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmpw9zio3b8`:
- `DIRECTION.md`
- `index.html`
