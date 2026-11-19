- **Lead with the tagline:** it is the hero, with a 7:00 / 9:00 / 14:00 strip under it. A live open/closed line sits at the top, computed from the stated hours in London time, so a phone visitor sees it on the first screen.
- **Order follows the visitor's questions:** open, then where (a street-sign address), then priced menu, then cakes, then the sisters. No cards, stats or reviews, and every price is from your copy.
- **Fonts:** Synonym for headings and Sentient for body, from the find-font engine, both Fontshare FFL. Self-host only. This is **not embedded**: the page expects `./fonts/Synonym.woff2` and `./fonts/Sentient.woff2` and falls back to Georgia/system-ui. The render I checked used those fallbacks.
- **Colour and imagery:** Club Cream (ground #F5E7C3, figure #5B1D26) from find-color. Imagery is three inline SVG line drawings (a pastel de nata, a loaf, the one oven) and no photo placeholders.
- **Checks:** check-layout found none of its nine patterns on desktop or phone. In one fix round I removed a "collect from" step and "or close" from the 14:00 label, since neither was in your copy. Open decisions are in `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp5z0jfyvo/DIRECTION.md`:
  - The Instagram link is a placeholder, and no message channel was given for cake orders.
  - `tallyroll.md` wasn't readable, so "the opposite of" is my reading.
  - Status is still draft.

Files are `index.html` and `DIRECTION.md` in `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp5z0jfyvo/`.
