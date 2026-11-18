I've picked the fonts and colors and am writing the page now.



- **Fonts:** IBM Plex Serif for headings and body, IBM Plex Mono for code and figures, loaded from Fontsource on jsDelivr. Both are OFL licensed. The font skill's first choice for headlines was Steps Mono, but I dropped it: it has only two weights, it's missing symbols like `=`, `@` and `{ }`, and there's no CDN copy. Self-host the Plex files before you ship.
- **Colors:** "Graphite and Signal" from the color skill. The text is graphite on near-white (17.01:1 contrast). The blue is used only for links, focus and hints, never as decoration.
- **Invoice as the hero:** the invoice line is real HTML. Clicking it opens the 31 daily totals with a running sum that adds up to exactly 1,204,388 calls. The page labels the daily figures as illustrative and notes that the price is applied to the monthly total and rounded once.
- **Ledger layout:** dark rules, small mono column labels and right-aligned figures in fixed-width digits. With such a plain palette, the type and layout give the page its character.
- **Copy:** only the brief's claims. The curl request and the pricing-rule rows illustrate claims already in the brief (`POST /v1/events`, idempotent ingestion, the four rule types); they add none.
