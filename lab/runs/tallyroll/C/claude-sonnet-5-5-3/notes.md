I've saved the page to `index.html`, and the layout checker found none of the nine overused patterns at desktop or phone width. The page below is the same file, with the 31 daily rows filled in.



- **Fonts:** Mona Sans for headlines and body, and Iosevka for code and figures. Both are open-licence, self-hosted fonts from the font tool's catalog. The woff2 files aren't bundled, so until you add them to `./fonts/` the page uses the system sans and mono. Mona Sans is strongly tied to GitHub, which is a mild risk for a developer-tool brand.
- **Colour:** Graphite and Signal, the colour tool's default pick. Blue is used only for links and the secondary action. I rejected the green-and-cream option because it signals an old private bank.
- **Structure:** the hero is left-aligned, with the expandable invoice line as the main content beside the headline. The page order follows a careful buyer's questions: what it does, how it works, who it's for, what it costs. I cut testimonials, stats and feature cards.
- **Invented numbers:** the 31 daily call counts are made up, and the page says so. They sum to exactly 1,204,388. The brief gave only the total, and the line shows daily totals but never a dollar column, so no rounding mismatch can appear.
- **Check results:** none of the nine patterns showed up at desktop or phone width. I fixed one bug the screenshot showed, a hero left edge that didn't line up with the sections below it.
