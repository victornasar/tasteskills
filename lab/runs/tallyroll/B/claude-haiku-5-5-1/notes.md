I'll build the page from the returned tokens, then reply with it in one code block.



**Fonts:** Switzer (headlines, Fontshare FFL, self-host only), IBM Plex Sans (body, OFL) and Iosevka (code and invoice figures, OFL). Put the `.woff2` files in `./fonts/` and name them to match the `@font-face` rules.

**Colors:** Graphite and Signal, light only. The color engine returned no dark variant for this direction, so I didn't invent one. Signal Blue is limited to links and focus.

**Design decisions:**
- Body uses IBM Plex Sans, not the serif the font engine ranked first, because your brief asked for a UI sans.
- Iosevka over Departure Mono: it's calmer and more precise for figures. Its web package is large.
- The primary button uses Graphite, not the accent, since the color roles assign it that way.
- The engine returned no status colors, so invoice states must use text labels, not color.
- Links point to `#docs` and `#demo`; the sign-up and docs URLs need replacing.
