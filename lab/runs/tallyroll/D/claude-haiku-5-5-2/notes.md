Built and checked. Both files are saved in the project: `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmpsnmk9t60/DIRECTION.md` and `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmpsnmk9t60/index.html`.



**Design decisions**
- **Invoice line leads.** The brief's arithmetic is built in HTML as an expandable `<details>` row above the fold, so the page proves "every cent traces back" instead of asserting it.
- **Type and color from the engines.** Technor (headlines) and IBM Plex Serif (body) from find-font; Graphite and Signal from find-color, with blue reserved for links and focus.
- **Structure over decoration.** Ruled sequences and two audience columns replace cards, gradients, badges and stat rows; no shadows, emoji or imagery.
- **Fonts are not bundled.** The font files aren't in the project, so the page renders the system fallbacks until `./fonts/Technor.woff2` and `./fonts/IBMPlexSerif.woff2` are added. Technor is Fontshare self-host only, so keep it out of public repos.
- **Placeholders.** Docs, demo, status, security and contact links are `#` anchors. The 31 day rows are labelled but carry no figures, because the brief gave none. Copy is limited to the brief; I did not add claims.

Critique used both rounds: round one fixed invoice-line indent and uniform section spacing; round two removed a duplicate "Pricing" label. Final check: no overused patterns on desktop or phone. Gate 2 and Gate 3 were not run interactively, so `DIRECTION.md` stays `Status: draft`, and the approval and URLs are listed under Open decisions.
