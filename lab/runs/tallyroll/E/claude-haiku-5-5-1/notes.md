The full-page render passes the constraints I can check by eye, so I'm not running a fix round. The headline is the largest text, the invoice line with its arithmetic sits above the fold, there are no gradients, shadows or accent colour, and the phone render doesn't clip. The complete page is below.



- **Direction:** Overcast, a cool grey ground with slate type and no accent. It challenges the blue-as-lead convention and reads as a printed ledger.
- **Signature:** the example invoice line sits above the fold and expands to the 31 daily totals behind it.
- **Type:** Switzer for headlines, IBM Plex Serif for body, Iosevka for code. I switched the code font from the engine's top pick, Departure Mono, because its pixel sizing and retro feel clash with the calm tone.
- **Fonts are not bundled.** The page points at `./fonts/*.woff2`, and the fallback stacks render until those files are added. Switzer is licensed for self-hosting only, not public repos.
- **Placeholders:** the daily-total values are dashes, since the brief has no daily figures, and all links are `#`.

Files are in the project: `DIRECTION.md` and `index.html` at `/private/var/folders/rh/c3zlwpy56yd7gcc101pb318w0000gn/T/tmp08kg31q6/`. The brief's `fennel-street.md` reference is not in this project, so I didn't use it. The direction choice and the other inferred items are open for your review in DIRECTION.md §12.
