# color

A library of 51 curated color directions, and a skill that picks the right ones for your project.

Describe what you're building ("neighbourhood bakery", "dashboard for a fintech") and an AI agent gets back
3–5 clearly different color directions, each one checked for contrast, plus a recommended pick. Pick one and
the agent writes it into your project.

## What a direction is

Award galleries such as Awwwards summarize a site by its main colors. Each direction here is built the same
way, around a **pair**:

- **Ground:** the background and largest surfaces.
- **Figure:** the main color on top of it: headings, type, logo.
- **Accent** (optional): a small amount of a third color for prices, tags or highlights.

Body text, muted text, tints and shades are derived from the pair. Colors are stored in
[OKLCH](https://oklch.com), a format that matches how people see lightness, and output as HEX too.

Every color comes from the library. The agent is told never to invent or adjust one, and every contrast
number comes from the script.

## Install

Works in Claude Code, Cursor, Codex and any agent that supports skills. Needs [Node.js](https://nodejs.org)
18 or later. No clone, no API keys, no network.

```bash
npx skills add https://github.com/victornasar/tasteskills --skill find-color
```

This installs only the skill folder (about 280 KB): instructions plus one script with the whole library inside.

## Use it

Ask your agent:

```
/find-color neighbourhood bakery
```

The agent shows each direction with its colors, contrast numbers, when to choose it and what to watch out for,
then waits for you to pick. For this brief:

| Direction | Ground | Figure |
| --- | --- | --- |
| Espresso and Milk (recommended) | `#2B1F16` | `#ECE3D6` |
| Oxblood and Pistachio | `#62141C` | `#C3DC9B` |
| Bronze Monochrome | `#3B220D` | `#DFBE92` |
| Clay and Linen | `#F5EDE4` | `#8D5951` |

Say which one you want and the agent applies it: CSS custom properties, a Tailwind v4 theme or design tokens,
with each token's job noted:

```css
:root {
  --color-ground: #2B1F16;
  --color-ground: oklch(0.25 0.025 55); /* Page background and the largest surfaces */
  --color-figure: #ECE3D6;
  --color-figure: oklch(0.92 0.02 80); /* Headings, type and logo */
  --color-accent: #D18E46;
  --color-accent: oklch(0.7 0.12 65); /* Prices, tags and highlights */
  /* …plus text, muted text, tints and shades */
}
```

You can add constraints in plain words: "must work in dark mode", "no gold", "photography-heavy", "avoid the
usual colors for this industry". Or tell the agent to choose for you while it builds ("use find-color to pick
and apply a palette"); it takes the recommended pick and tells you what it chose.

### Run the engine directly

The agent runs these for you, but you can too:

```bash
node scripts/find-color.mjs recommend --brief "neighbourhood bakery"
node scripts/find-color.mjs recommend --domains saas,fintech --foundation dark --count 5
node scripts/find-color.mjs apply lib.espresso-and-milk --format css --text
node scripts/find-color.mjs classify --ground "oklch(0.95 0.02 90)" --figure "oklch(0.62 0.06 140)" --area 80/20
```

`scripts/` is inside the installed skill folder. From a clone of this repo, run the same commands with
`node tools/cli.mjs` from the `color/` folder.

## Change the library

Edit pairs in `library/source/*.json`, then run `node tools/build.mjs all`. The build stops on any color out
of gamut, any contrast failure, any near-duplicate and any change to the golden briefs' results.
[`AGENTS.md`](AGENTS.md) has the full rules.

**Status:** 51 directions. Research on Awwwards sites ([`research/report.md`](research/report.md)) tested
the classification and the library; its two-axis model was adopted as a result. Everything stays provisional.

## What exists

| Path | Contents |
| --- | --- |
| [`skills/find-color/`](skills/find-color/) | The installable skill: [`SKILL.md`](skills/find-color/SKILL.md) and the bundled engine `scripts/find-color.mjs` |
| [`library/`](library/) | 51 curated directions. Edit `library/source/`, then run `node tools/build.mjs all` |
| [`tools/cli.mjs`](tools/cli.mjs) | The engine's entry point: `recommend`, `get`, `apply`, `classify`, `domains`, `conventions` |
| [`tools/query.mjs`](tools/query.mjs), [`tools/apply.mjs`](tools/apply.mjs), [`tools/classify.mjs`](tools/classify.mjs) | Selection with a default pick, the tokens output, and the pair classifier |
| [`tools/build.mjs`](tools/build.mjs), [`tools/bundle.mjs`](tools/bundle.mjs), [`tools/check.mjs`](tools/check.mjs) | Build and rule checks, the skill bundle, and the golden briefs (`tools/golden.json`) |
| [`AGENTS.md`](AGENTS.md) | How agents use the repo and change the library |
| [`classifications/`](classifications/) | The provisional classifications, with OKLCH tests and thresholds |
| [`contexts/`](contexts/) | 89 domains in 17 groups, and sourced category conventions |
| [`prompts/`](prompts/) | The classifier prompt and a prompt for testing the classifier |
| [`docs/`](docs/) | Color principles, the classification system, the data model and the recommendation design |
| [`schemas/`](schemas/) | JSON Schemas for all data |
| [`examples/`](examples/) | Two hand-authored recommendations |
| [`research/`](research/) | Pinned Awwwards source data, the Phase 2 analysis, thumbnail review and report |

## Principles

- OKLCH is the source of truth, and HEX is its sRGB output.
- Every color an agent shows comes from the library or the classifier. Nothing is invented.
- Ground and figure are assigned from visual evidence, never from the order a source lists colors.
- Measured tags come from tests, and judgement tags are labelled as judgement.
- Domains never determine colors. A domain only helps choose which curated directions to show.
- Real category conventions, such as blue in finance, are surfaced as sourced context to follow or avoid, never as a rule. Unsourced folklore is not used.
- Taste over frequency: a common pattern is not automatically a good recommendation. For luxury, black or black and white is preferred over gold.
- Reasoning makes no unsupported psychological claims.

## Library coverage

The 51 directions are classified on two axes, foundation and structure: Light 31 and Dark 20; Chromatic 23, Neutral 13, Two-Tone 11, Monochromatic 3 and Multicolor 1. By display label: Neutral 13, Two-Tone 11, Light + Muted 7, Light + Vibrant 7, Dark + Vibrant 6, Dark + Muted 3, Monochromatic Foundation 3, Multicolor 1. There is no Image-Led direction yet; see [`docs/02-classification-system.md`](docs/02-classification-system.md#image-led). Every one of the 89 domains has at least one direction. Most have several, and the thinnest are the newest additions such as Pet brands and Science and research.

## Open questions

1. **When is Image-Led ready?** The engine supports directions with no ground, but the model needs validating on fresh award data before any are written.
2. **Which secondary tags merge?** For example Sophisticated, Elegant and Luxurious, or Natural, Organic, Pastoral and Earthy.
3. **Should directions include status colors?** SaaS and data products need success, warning and error colors.
4. **How should light and dark counterparts link?** Currently the skill re-queries with the opposite foundation.
5. **Should the engine adapt a pair to an existing brand color?** Today `--existing` only ranks directions that already contain a close color.

## Next steps

1. Validate the Image-Led model on photo-led sites outside the Phase 2 sample, then write the first Image-Led directions.
2. Deepen the domains with only one or two directions, without growing the paused Two-Tone and Light + Muted groups.
3. Link light and dark counterparts and add status colors.

## License

[MIT](LICENSE)
