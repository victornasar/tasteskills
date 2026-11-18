# AGENTS.md

This repo is a catalog of free, self-hostable typefaces chosen to avoid the look of AI-generated sites.
`fonts.json` is the single source of truth: its `vocab` defines every tag, `fonts` holds the catalog, and
`avoid` lists the overused defaults with replacements. The repo stores no font files.

Two branches:

- **Picking a font for a brief** → follow [Picking a font](#picking-a-font).
- **Changing the catalog** → follow [Editing the catalog](#editing-the-catalog).

---

## Picking a font

Follow [`skills/find-font/SKILL.md`](skills/find-font/SKILL.md). The agent reads the brief into roles, feel tags
and constraints; the script `skills/find-font/scripts/find_font.py` filters, ranks and pairs, so the same
reading always gives the same picks. From a clone, run it from this folder:

```bash
python3 skills/find-font/scripts/find_font.py recommend --role headlines --role body --feel warm
```

### How the engine decides

These rules live in code; change them there and in this list together.

1. **Filter.** A font can fill a role when the role is in its `use`, it has every required script, and: for
   `body`, italics and at least two weights; for `ui`, at least three weights. With `--public-repo`, Fontshare
   (FFL) fonts drop out while any OFL font fits.
2. **Rank.** Feel first, because it's what makes picks follow the brief: the brief's primary feel as the font's
   main feel scores most, then anywhere in its feel, then the secondary feel. Use fit refines within that: the
   role as the font's first `use` beats second beats third. Fonts listed as replacements for a `--replaces`
   font rank first.
3. **Break ties by brief.** Equal scores are equally good fits. They're ordered by a hash of the brief's
   reading, so different briefs don't all land on the catalog's first font.
4. **Pair** the first two text roles, from each role's top 8:
   - **Contrast:** different categories (serif with sans), or one family with 5+ weights in both roles.
   - **Share a feel:** at least one feel tag in common, or one is `neutral`.
   - **One voice:** at most one font is `loud`, `experimental` or `playful`.

   The pair that bends the fewest rules wins, then the highest combined score; contrast beats one family on a
   tie. A `code` role sits beside the pair and prefers a font sharing its feel.
5. **Caveats** aren't scored. The agent reads them and switches to an alternative only when one bites.

`tests/test_engine.py` checks these rules, that every eval brief passes, that opposite feels get different top
picks, and that no font is the top pick for more than 30% of feel readings in any role.

### Licenses

- **OFL**: free to use, modify, subset and redistribute. Keep the OFL license file next to the font files.
- **FFL** (Fontshare, `url` on fontshare.com): free commercial use and self-hosting. The files stay
  out of public repos and stay unmodified: use the `.woff2` from the zip's `Fonts/WEB/fonts/` folder as-is.
  Each designer or contractor downloads their own copy.
- Every recommendation is self-hosted. Font CSS points at the project's own files, never at
  `fonts.googleapis.com`, `fonts.gstatic.com` or `api.fontshare.com` (the Munich GDPR ruling; see README).

---

## Editing the catalog

1. Edit `fonts.json` only. The README catalog is generated.
2. Use tags from `vocab` only, 1–3 per `feel` and `use`, primary tag first. Adding a tag to `vocab` is a
   decision for the user; ask first.
3. Take `weights`, `italics`, `variable` and `scripts` from a source (the foundry's files, the Fontshare
   API at `api.fontshare.com/v2/fonts`, or the Fontsource API at `api.fontsource.org/v1/fonts/<id>`), never from
   memory. `scripts` comes from `python3 scripts/glyphs.py <every style's OTF or TTF>`: list exactly what it
   earns. Set `"review": true` on any font whose tags are your judgement and haven't been checked by the user.
4. Write `note` as one or two plain sentences on what it feels like and what it's for. Name the overused
   font it replaces when there is one ("an alternative to Inter").
5. `url` is the font's source page, never a CDN.
6. No font may be the listed replacement for more than 3 avoid entries; the build enforces it.
7. Run `python3 scripts/build.py`. It also rewrites the skill's `catalog.json`. Done when it prints `✓`,
   `python3 scripts/build.py --check` passes and `python3 -m unittest discover -s tests -q` passes.
