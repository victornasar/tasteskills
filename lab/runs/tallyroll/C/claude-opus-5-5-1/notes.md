I've built the page and saved it to `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmps16wmk26/index.html`. The layout checker found none of the nine overused patterns at desktop or phone width. Looking at the phone screenshot, the invoice amount had dropped below the "Show" link, so I moved it back to the right of the line and re-checked. I didn't take a screenshot with the daily totals open, and I didn't check that the font links load (see the last line below).



- **Structure:** the order follows a careful buyer's questions: the claim, then the invoice line as proof, then how it works, what each team gets, and the price. I cut the stats, testimonials and closing banner. The only boxed object is the invoice; everything else is grouped with lines and spacing.
- **Invoice:** the line opens into 31 daily totals that add up exactly to 1,204,388 calls and $481.7552 (rounds to $481.76). The daily numbers are made up, and a note on the page says so.
- **Color:** I used find-color's "Bottle Green Ledger" (ink #194430 on cream #F6F2E7, 9.8:1 contrast) instead of its default pick, "Graphite and Signal", because the ledger look suits the finance sign-off. Graphite with a blue accent is the main alternative.
- **Fonts:** IBM Plex Serif for headings, IBM Plex Sans for text and IBM Plex Mono for numbers and code, all from find-font. I skipped its top headline pick, Technor, because it reads as sci-fi rather than calm. Technor also can't be linked from a CDN, which matters for a single file.
- **Font loading:** the fonts load from Fontsource on jsDelivr, not Google Fonts. I couldn't check that version 5.1.0 exists, so if those links fail the page falls back to system fonts.
