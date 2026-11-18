The page is saved at `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp4nur_3t2/index.html`. The layout checker found none of the nine overused patterns at desktop width. I looked at the desktop screenshot of the first screen. I did not run the phone-width or full-page checks, and I did not click the invoice line open to check the table.



- **Structure:** The hero is left-aligned and leads with the invoice line. It opens into 31 daily totals, which are illustrative and labelled that way, set to sum to 1,204,388. The sections after it follow the buyer's questions: how it works, finance and engineering, pricing, then a closing call to action.
- **Cut from the usual page:** No cards, stats row, gradients, badges or icons. Rules and spacing group the content, and the CTA band is the only dark block.
- **Type:** Overpass for headlines, IBM Plex Sans for body, Commit Mono for code and numbers. All three are OFL and self-hosted from `./fonts/`. I haven't added the woff2 files, so the render used system fallbacks (the checker's font report named Overpass and IBM Plex Sans; I didn't confirm which actually rendered). Drop the files in to get the intended type.
- **Color:** I took the engine's pick, Mint Ledger: ground #CBF7E6, navy figure #0E294A, 12.5:1 contrast. The alternative is Graphite and Signal, which is plainer and has 17:1 contrast. The one non-token color is a lighter paper tone mixed from the ground and white for the invoice.
- **Placeholders:** All links are `#`. The brief gave no docs, demo or footer URLs.
