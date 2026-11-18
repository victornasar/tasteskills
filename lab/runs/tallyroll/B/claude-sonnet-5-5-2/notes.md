I've built the page and I'm now sending the full file. I haven't opened it in a browser.



- **Type:** IBM Plex Sans for text and headlines, and IBM Plex Mono for the invoice, endpoint and numbers. Both are open-licence (OFL) fonts from the find-font catalog. The `@font-face` rules try locally installed copies first, then `./fonts/*.woff2`, so you need to add those files, and nothing loads from a third-party CDN. I skipped the skill's top headline pick, Steps Mono, because it lacks code glyphs and accents.
- **Colour:** The find-color direction is "Graphite and Signal". It uses near-black graphite on a cool off-white, with one blue accent (`#0E6EE6`) for the chevron and logo mark. Body text on the ground measures 10.09:1.
- **Invoice line:** It's the centrepiece: a native `<details>` element that opens into 31 daily rows. They sum exactly to 1,204,388 calls, and 1,204,388 × $0.0004 rounds to $481.76. The daily split is illustrative, generated in JS, and that script is the only JavaScript on the page. If you'd rather not ship made-up daily figures, replace them with real data.
- **Copy:** Everything comes from the brief, with no added claims. I wrote only the section labels and the closing heading "Read how it works, or see it on your data." The docs and demo links are `#` anchors for you to point at the real destinations.
