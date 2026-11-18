---
name: find-font
description: Pick typefaces from the curated tasteskills typography catalog, free and self-hostable fonts that don't read as AI-generated. Use when choosing a font, a font pairing or typography for a project, or replacing an overused default like Inter, Geist or Poppins.
argument-hint: <brief, e.g. "cozy bakery website">
---

# find-font

The engine is `scripts/find_font.py`, in the same folder as this file. It holds the whole catalog
(`catalog.json`) and needs only Python 3.8 or later, with no install and no network.

```bash
python3 <this-skill-folder>/scripts/find_font.py <command> ...
```

**Never recommend a font the script didn't return, and never invent its weights, scripts or license.**

Brief:

$ARGUMENTS

If the brief is empty, infer one from the current project (its name, README, existing CSS and any fonts it
already loads) and say what you inferred.

## 1. Read the brief

This is the part that needs judgement. Work out:

- **Roles**: which `use` tags the brief needs. A website usually needs `headlines` plus `body` (or `ui` for an
  app). A logo needs `logos`, a poster `posters`, a code editor `code`. Pick exactly the roles the brief needs;
  mention an obvious next role (a code font for a dev site) in one line under **Notes** instead.
- **Feel**: one or two `feel` tags, primary first, from the brief's words (table below). Run `vocab` to see
  every tag. Feel is always inferred; a wrong guess shows up in the alternatives.
- **Constraints**: languages (table below), whether the font files will live in a **public repo**, and any
  overused font the project uses now (run `avoid` to see the list).

Ask one short question only when the roles can't be inferred.

| Brief says | Feel |
|---|---|
| cozy, friendly, approachable, human, community | `warm` |
| clean, minimal, calm, professional, trustworthy | `neutral` |
| dev tool, data, engineering, precise, infrastructure | `technical` |
| books, essays, scholarly, long reads | `literary` |
| magazine, journalism, opinionated, culture | `editorial` |
| luxury, fashion, refined, beauty, wedding | `elegant` |
| bold, punchy, sports, events, protest, brutalist | `loud` |
| fun, kids, quirky, cheeky, games | `playful` |
| art, gallery, avant-garde, zine, music, weird | `experimental` |
| nostalgic, vintage, 8-bit, varsity, medieval, 70s | `retro` |

| Language | `--script` |
|---|---|
| English only | (none needed; every font has `latin`) |
| German, French, Spanish, Polish, Czech and other Western or Central European | `latin-ext` |
| Russian and other Cyrillic, Greek, Vietnamese, Hebrew | `cyrillic`, `greek`, `vietnamese`, `hebrew` |
| Turkish, Romanian, Baltic | `latin-ext`, and say coverage is unverified |

## 2. Run the engine

```bash
python3 scripts/find_font.py recommend --role headlines --role body --feel warm [--feel literary] \
  [--script latin-ext] [--public-repo] [--replaces Inter] [--category mono] [--exclude id,id]
```

| Flag | When |
|---|---|
| `--role` | Once per role, in order of importance |
| `--feel` | Primary feel, then optionally a secondary one |
| `--script` | Once per language tag the text needs |
| `--public-repo` | The font files will be committed to a public repo (drops Fontshare fonts) |
| `--replaces <name>` | The project uses an avoid-list font now; its listed replacements rank first |
| `--category` | The brief demands one: `sans`, `serif`, `display`, `mono` |
| `--exclude` | The user wants other options: the ids already shown |

The result is JSON:

| Field | Contents |
|---|---|
| `roles[].picks` | Up to three fonts per role, ranked, each with `why`, license, url, weights, scripts, `caveats` and `note` |
| `pair` | The ids of the top headline/body pair and any pairing rule it `bends` |
| `css` | `font_family` with the fallback stack, and an `@font-face` template, for each role's top pick |
| `notes` | Things to tell the user: no feel match, Fontshare dropped, a bent rule |
| `picks` | The JSON block to end the answer with |

Start from the top picks. Switch to an alternative only when a top pick's `caveats` clearly bite this brief
(for example "no italics" for a long-read blog), and say why.

## 3. Answer

Use this shape, nothing longer:

```
**Top pick:** <Font> for <role> (+ <Font> for <role>)
<One sentence: why it fits the brief, in the brief's words.>

| | Font | Why | License | Get it |
|---|---|---|---|---|
| 1 | ... | ... | OFL / FFL + limit | <url> |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

**CSS**
<the css.font_face and css.font_family from the result; tell the user to match the file name to their download>

**Replaces:** <the avoid-list font this stands in for, if any>
**Notes:** <the result's notes, caveats that bite, Fontshare limits>
```

- For FFL fonts the License cell says: *"Fontshare: self-host only, keep files out of public repos."*
- Add the download line for each top pick:
  - **fontshare.com:** "Download family" → zip → `Fonts/WEB/fonts/*.woff2`, used as-is.
  - **github.com:** the latest release's assets; look for a `webfonts` or `woff2` folder, plus `OFL.txt`.
  - **gitlab.com:** the repo's `fonts/` folder.
  - **Other sites:** the site's download button.
- Fonts are always self-hosted. Never point CSS at `fonts.googleapis.com`, `fonts.gstatic.com` or
  `api.fontshare.com` (they send visitor IPs to a third party, which a Munich court ruled breaks the GDPR).
- When a `notes` entry says no font fits, say so plainly. You may then name at most one outside font, marked
  **outside the catalog, license unverified**.

End with the result's `picks` as a fenced `json` block, unchanged:

```json
{"picks": [{"role": "headlines", "ids": ["synonym", "alpino", "red-hat"]}, {"role": "body", "ids": ["sentient", "author", "plein"]}]}
```

## Other commands

- `vocab`: every feel and use tag with what it means.
- `get <id>`: one font's full record.
- `avoid [<name>]`: the overused fonts and what to use instead.
