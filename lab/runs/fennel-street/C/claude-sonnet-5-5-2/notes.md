The page is saved at `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmpilvdwpeg/index.html`. I checked it at 1440px and at 390px phone width, and the layout checker found none of the nine overused patterns. The fonts aren't bundled yet (see below).



- **Order follows the phone visitor's questions:** open now?, what's baked, hours and address, then cake orders. A script reads London time and writes "Open now", "Opens today at 7:00" or "Closed right now" into the first screen, and highlights today's row in the hours table.
- **Menu as a price list:** dotted leaders, no cards, no invented copy. The cake order section is a dark band with a tappable phone number.
- **Fonts:** Red Hat Display for headings and Source Sans 3 for body, both OFL and self-hosted. I did not bundle the font files. Add `RedHatDisplay.woff2` and `SourceSans3.woff2` to `./fonts/`, or the page shows system fonts. The checker did report the two families as the heading and body fonts, but I didn't confirm they actually loaded.
- **Colour:** Clay and Linen, from find-color: linen ground, rose-clay headings at 4.92:1, dark brown text at 10:1. It reads as warm, matt and flat, so there are no gradients.
- **Photo and links:** the photo is a dashed, labelled placeholder. The Instagram link is a bare `#`, because the brief gave no address.
