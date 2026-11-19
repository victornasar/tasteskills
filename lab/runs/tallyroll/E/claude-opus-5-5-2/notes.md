Here is the finished page. The layout checker found none of the nine overused patterns at 1440px or 390px. All five constraints in DIRECTION.md passed. I used one of the two allowed fix rounds: the price now comes before the buttons in the pricing section, and "0.5%" is set in the headline font.

Two things to check before launch:
- **The web fonts didn't load in my renders.** Overpass and IBM Plex Serif load from Fontsource on jsDelivr. I couldn't confirm those font URLs or the `5.0.0` version, so the screenshots may show fallback fonts. The fonts should be self-hosted for production.
- **The 31 daily totals in the invoice are made up.** The brief doesn't give them, so I wrote example numbers that add up to exactly 1,204,388 and labelled them "illustrative". Swap in a real export if you have one.

DIRECTION.md is still a draft because nobody has approved it. Its Open decisions also list: the real link targets (all `#` for now), the missing `fennel-street.md` (so the "opposite of" reading is unchecked), and Commit Mono (no copy loaded, so code text uses the system's monospace font).



- **Invoice in the first screen:** the "API calls, March" line sits next to the headline with its arithmetic showing, already opened to its 31 daily totals and their sum. It shows how the product works before any claim.
- **Fonts (from find-font):** Overpass for headlines, IBM Plex Serif for body text, Commit Mono for code and figures. The engine's first headline pick, Technor, has a self-host-only licence that can't go out in a shared single file, so I used the free-licence list instead.
- **Colours (from find-color):** "Graphite and Signal", the engine's top pick. The blue is used only on links and buttons; nothing decorative is blue.
- **Finance and engineering:** they sit side by side at equal width, with engineering on an inverted graphite band. The "↳" trace mark repeats from the invoice through both lists.
- **No added claims:** the page uses only the brief's copy, with no stats, logos or testimonials. The invoice is the only raised surface; the rest is flat.

Files are in `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp0haz6ccf`:
- DIRECTION.md
- index.html
