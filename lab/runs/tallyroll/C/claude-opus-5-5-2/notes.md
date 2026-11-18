I built the page and saved it to `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp6ywj0lzj/index.html`. I checked it with check-layout at 1440px and 390px: it found none of the nine overused patterns at either width. The first phone render had one real problem: the code blocks pushed the "How it works" text off the screen. I fixed that, and now only the code blocks scroll sideways inside their own boxes. I haven't confirmed that the Commit Mono font file loads from the CDN. If it doesn't, the browser falls back to the system monospace font.



- **The invoice line is the hero.** It's a working line that opens into 31 daily totals, which add up exactly to 1,204,388 calls. The totals, the request and the pricing rule are invented examples and are labelled that way on the page. I didn't add stats, testimonials or a closing call-to-action band.
- **Fonts:** IBM Plex Serif for headlines, IBM Plex Sans for body text and Commit Mono for figures and code, all free (OFL) and loaded from jsDelivr. find-font's top headline pick was Technor, but I dropped it because its sci-fi style doesn't fit "calm" and its license only allows self-hosting.
- **Colors:** Graphite and Signal, find-color's own pick. The page is near-white and graphite, with Signal Blue used only for links and focus.
- **Layout:** How it works is a numbered sequence where each step sits next to its real artifact. Finance and engineering get two side-by-side lists separated by rules, not cards.
- **Corners:** only real objects like the invoice and code blocks have a frame, and its corners are barely rounded.
