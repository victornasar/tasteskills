- **Fonts:** Steps Mono for headlines, IBM Plex Serif for body and Commit Mono for the invoice and endpoint (from find-font). They aren't embedded: the CSS uses `local()` plus fallbacks, so they need self-hosting as woff2 in `./fonts/`. My renders used the fallbacks. Colours are Bottle Green Ledger from find-color.
- **Layout:** the first screen is the headline and a live invoice line that opens into 31 daily totals. Below it is a ruled ledger with a label margin instead of cards, and I left out testimonials, logos and stats.
- **Illustrative data:** the 31 daily figures are generated to sum to the stated 1,204,388 calls, and the page labels them illustrative.
- **Open items:** DIRECTION.md is still `draft` because the run was non-interactive. Docs and demo links are `#`. The headings "Three steps, each one readable.", "See the trail for yourself." and "Who it's for" are my wording, not brief copy.
- **Critique:** check-layout found none of the nine patterns on desktop or phone. One fix round: the phone footer links were hidden by an over-broad rule, and the section label margins were misaligned with the header. I did not re-render the phone view after the footer fix.

Files are in `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp274n3lne`: `DIRECTION.md` and `index.html`. The build also left `page.html` and `gen.py` there.
