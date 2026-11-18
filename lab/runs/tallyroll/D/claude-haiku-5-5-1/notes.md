I built the page from the brief, with the direction recorded in `DIRECTION.md` and the page in `index.html`, both saved in the project. The direction is a draft: this run was non-interactive, so Gates 1–3 were not approved.



**Design decisions**
- The invoice line is the lead object: a live HTML/CSS exhibit beside a left-aligned headline. It opens to 31 day cells with no invented daily values.
- Palette is Graphite and Signal from find-color (engine rank 1). Signal Blue is limited to links, focus and the expand caret.
- Headline face is Supreme, not Mona Sans, because Mona Sans's GitHub association bites for a developer-tool brand. Body is IBM Plex Sans.
- No cards, gradients, emoji or stats. Steps and audiences are ruled lists. The three-step row is kept because the steps are ordered.
- Fonts are referenced from `./fonts/` but not supplied, so the render used the system fallback. Supreme and Plex are unverified until those files are added.

**Other notes**
- Placeholder links: `#docs`, `#demo`, `#status`, `#security`, `#contact`.
- `fennel-street.md` is not in the project, so the "opposite" register came from the brief alone.
- Critique ran one round. The only flags were uniform section padding (fixed) and the three-step row (kept). Round 2 was not needed.
