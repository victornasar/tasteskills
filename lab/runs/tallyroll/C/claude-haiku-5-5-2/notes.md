The phone render matches the plan: the invoice line stacks under the headline, sections stack with no horizontal scroll, and the checker still reports no overused patterns. Here is the complete page, saved at `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmpa3axyeb2/index.html`.



- **Structure:** I dropped the default centered hero, feature cards, stats, testimonials and CTA band. The page leads with the invoice line that expands to its daily totals, beside the headline.
- **Fonts:** Technor for headlines (Fontshare, self-host only) and IBM Plex Sans for body (OFL). I used Plex Sans rather than the catalog's Plex Serif pick because a calm product page reads better in sans. The font files are not in `./fonts/` yet, so the page currently renders in the system stack.
- **Color:** Graphite and Signal. Graphite carries text and the primary button, and Signal Blue is only for links, focus and the expand control.
- **Daily totals:** the brief gives no daily values, so the expanded view shows Mar 1–31 with a note that values are omitted. I did not invent figures.
- **Placeholders:** the links use relative paths such as `/docs` and `/demo`. Point them at the real URLs.
