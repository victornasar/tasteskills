I saved `index.html` and `DIRECTION.md` in the project. I rendered the page at desktop (1440px) and phone (390px) widths, and the layout checker found none of its nine overused patterns at either size. I did two fix rounds. I made two small fixes after the last render and didn't render again: I removed a sentence that mentioned a dashboard (not in the brief) and made the invoice hint text change when the line opens or closes.



- **Invoice line first:** the first screen shows the example invoice line already open, with its 31 daily totals. The daily figures are made up and labelled "Example data"; they add up exactly to 1,204,388 calls and $481.7552, which rounds to $481.76. The request and pricing-rule samples are also invented and labelled "Example".
- **Colors:** the color picker's Graphite and Signal set: graphite on near-white, with the blue kept for links and focus. The one dark band holds the finance and engineering columns at equal weight. The primary button is graphite, as the picker specified.
- **Fonts:** IBM Plex Serif, Plex Sans and Plex Mono, loaded from jsDelivr. I didn't use Technor, the picker's headline pick, because its retro sci-fi look works against "calm". Self-hosting the fonts before launch is listed in Open decisions.
- **Cut:** no stat row, logo wall, testimonials or tier cards, and pricing is two plain sentences, so nothing goes beyond the brief's copy.
- **Still open:** nothing was approved because this run was non-interactive. Docs, demo and footer links point to `#`. `fennel-street.md` wasn't in the project. All of these are in `DIRECTION.md` under Open decisions.
