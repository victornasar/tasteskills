---
name: find-font
description: Choose, pair and critique typography for a website, product or brand like a typographic art director. Reads the brief and positioning into type roles (display, heading, body, UI, editorial, monospace), judges real candidates by their letterforms, weights and variable axes, checks them on a rendered proof, and avoids the fonts AI-built sites overuse. Use when choosing fonts or a pairing, replacing a default like Inter, or reviewing a page's typography.
argument-hint: "[brief, e.g. cozy bakery website]"
---

# find-font

Choose type the way an art director would. Work out which jobs type does on this page, find candidates that
could do them, look at them set in the real copy, and choose with reasons you could defend to the client.

Brief:

$ARGUMENTS

If the brief is empty, infer one from the project (its name, README, copy, the CSS and any fonts it already
loads) and say what you inferred.

## What goes wrong without judgement

- **Defaults.** Without help, models reach for the same faces. In a corpus of 90 AI-built sites, Inter was on
  72% of pages that load a web font and Fraunces on 50%. Every bakery page in the lab's experiment used Fraunces
  for headings, across three models. `references/fonts.md` lists these overused faces.
- **Metadata instead of looking.** A recommender that ranked fonts by tags picked faces a person rejects on
  sight: sci-fi display lettering for a brief that said "technical, calm, precise", a monospace with no braces
  for a code-heavy page, a headline face that "reads technical" for a bakery. Tags describe a font in general.
  Only setting it in the brief's copy shows whether it fits this page.
- **Swapping one default for another.** Replacing every default with the same "tasteful" alternative on every
  brief is a new default.

## 1. Read the brief into a type brief

**Roles.** A role is a job on the page, not a slot for a font. One family can fill several. Decide the roles
before looking at any candidate.

| Role | Where it appears | Typical size | What it must do | What rules a face out |
| --- | --- | --- | --- | --- |
| **Display** | Hero headline, one or two big moments | 48–160px | Carry the brand's voice at a glance; hold up at extreme weights and tight spacing | Little at large size, but often anything under ~24px |
| **Heading** | Section and card titles | 22–48px | Hold up 5–15 times per page at different lengths; wrap well on a phone | Very wide letters that break phone headings into many lines; quirks that grate when repeated |
| **Body** | Paragraphs, descriptions | 16–20px | Long, even reading: generous x-height, open apertures, moderate contrast, a true italic, a regular and a bold | Hairlines, condensed widths, display-tight spacing, no italic |
| **UI / interface** | Navigation, buttons, labels, forms, tables | 12–15px | Clear at small sizes; distinct `1 l I` and `0 O`; tabular figures where numbers line up; at least three weights | High contrast, tight spacing, decorative numerals |
| **Editorial** | Long reads, pull quotes, captions, footnotes | 17–22px plus small sizes | Book-like rhythm; italics and small caps; old-style figures in running text | Interface-tuned faces that turn cold across several screens |
| **Monospace** | Code, IDs, data, terminal output | 13–15px | A full set of code symbols (`{ } [ ] \| ~ = @`), distinct look-alikes, readable small | Missing glyphs; "mono" display faces built for posters |

Most sites need two families: one with a voice (display or heading) and one that disappears (body and UI). Add a
third only for a role neither covers, usually monospace for code or data. A family with optical sizes or a wide
weight range can fill everything on its own, which is often the stronger answer for a minimal brand.

**Category conventions.** Name what the category's sites usually do with type and, more importantly, *why*:

| Force behind a convention | What it tends to produce | Where it often applies |
| --- | --- | --- |
| Numbers get compared | Tabular figures, steady sans or mono for data, restrained display faces | Finance, analytics, developer tools, pricing |
| Reading under stress, or for everyone | Large x-height, plain sans, generous sizes | Health, government, utilities, insurance |
| Authority and heritage | Serifs on historical models, symmetrical setting, small caps | Law, universities, banks, institutions |
| Appetite and handmade craft | Warm or irregular faces, scripts, hand-drawn lettering | Food, hospitality, makers |
| Prestige through restraint | Fine detail at large sizes, wide spacing, few weights | Luxury, fashion, hotels |
| Energy and noise | Heavy, condensed or wide display faces in capitals | Sport, events, music, campaigns |

These are forces, not answers; two bakeries can need opposite type. Keep the *reason* when the audience relies
on it (a finance lead compares columns, so tabular figures stay). Challenge the *habit* when it only makes the
alternatives look alike (every competitor in the same neutral grotesque).

**Brand position.** Read it from the brief's positioning, not the industry. Each line describes qualities to
look for, not a genre:

| Axis | Toward the first pole | Toward the second |
| --- | --- | --- |
| Premium ↔ affordable | Restraint, space, detail visible at large sizes, few weights, controlled contrast | Sturdy, open, bigger x-height, heavier weights, plain and direct |
| Traditional ↔ contemporary | Historical models, old-style figures, calligraphic stress | Recent constructions, lining figures, rational or unusual shapes |
| Technical ↔ approachable | Constructed, monoline, squarish curves, tabular figures | Humanist, open apertures, varied stroke, softer terminals |
| Serious ↔ playful | Steady rhythm, conventional proportions | Irregularity, bounce, unexpected shapes |
| Minimal ↔ expressive | One family, small scale contrast, few weights | A distinctive display face, big scale contrast, type used as image |

Every word in the brief limits the choice, the display face included: "technical, calm, precise" rules out
sci-fi lettering as firmly as it rules out a script. And each pole has its cliché. The thin, high-contrast,
tracked-capitals "luxury" look and the geometric sans of "modern startup" are defaults too.

## 2. Gather candidates

- Start with what's given: fonts the brand already uses, or ones the user names.
- Look beyond your first instincts. `references/fonts.md` is a curated list of free, self-hostable faces that
  don't read as AI-generated, unranked and grouped by category. Your own knowledge is welcome too.
- Treat the avoid list in `references/fonts.md` as defaults to look past, unless the brand already uses one.
- Shortlist two to four candidates per role.
- Take facts from the font's source page or files, never from memory: weights, italics, variable axes, scripts,
  licence, and features such as tabular figures and small caps. If you can't check a fact, say it's unverified
  and don't plan around it.

## 3. Judge the letterforms

Classification is a starting point, not a verdict: two geometric sans faces can feel opposite. Describe what you
actually see.

| Trait | What to look at | What it does |
| --- | --- | --- |
| Classification | Serif (old-style, transitional, didone), slab, sans (grotesque, neo-grotesque, geometric, humanist), mono, display, script | Era and register: history, neutrality, construction, handwriting |
| Contrast | Thick-to-thin stroke difference | High reads refined and fragile when small; low reads sturdy and plain |
| x-height | Lowercase height against capitals | Large reads open and legible small; small reads elegant and literary but needs bigger sizes |
| Width and proportions | Condensed to wide; even widths or classical variation | Condensed is urgent and saves space; wide is calm or loud; classical proportions read traditional |
| Apertures | How open `c e a s` are | Open is friendly and legible; closed is compact, formal or cold |
| Terminals | Stroke endings: flat, angled, rounded, ball, flared | Rounded is soft; sharp is precise; flared is crafted |
| Construction | Circles and straight lines, or a pen's strokes | Constructed reads engineered; written reads human |
| Figures | Lining or old-style; tabular or proportional | Old-style suits running text; tabular is needed for aligned numbers |
| Signature glyphs | `a g R Q & ?` and the numerals | Where a face's personality, and its quirks, show most |
| Italic | A true italic or a slanted roman | A true italic gives emphasis a second voice |

**Weights and variable axes.**

- Body needs a regular and a bold (around 600–700). UI needs at least regular, medium and semibold. Headings
  sit far enough from body weight to read as a step. Display faces can use the extremes.
- Never let the browser fake a missing bold or italic: set `font-synthesis: none` and plan around the styles
  that exist.
- With an optical-size axis, use `font-optical-sizing: auto` so display and text sizes get their own drawing. A
  width axis helps narrow phone headlines; a grade axis changes weight without reflow (dark grounds, hover).
- Each weight and style is a file. Ship only what the page uses, self-hosted, with `font-display: swap`.

**Pairing.**

- Contrast on one clear dimension (classification, weight or width) and share something (x-height, proportions,
  era or construction). Faces that differ only slightly look like a mistake; faces that differ in everything
  compete.
- One voice: only one expressive face per page.
- Before adding a family, ask whether a weight, width or size of an existing one already does the job.
- Where faces share a line (inline code in body text, a label beside a number), match their x-heights with
  `size-adjust` or the size itself.

## 4. See it before deciding

Names and descriptions are hypotheses. Look at the shortlist before choosing.

1. Build a **type proof**: an HTML page set in the brief's own copy, one column per candidate or pair. Include
   the hero headline at its real size, a section heading, two body paragraphs with an italic phrase and a link,
   navigation, a button, a form label, a small table of numbers, and a line of code if the page has code. Use the
   characters the copy needs (`€ × → & %`, accents, the brief's price or data format).
2. Load the real font files and show on the proof whether each face loaded (`document.fonts.check()`). A
   fallback system font tells you nothing.
3. Screenshot it at desktop and phone widths with whatever browser tooling you have, and look.
4. Compare: how the real headline wraps, whether the body forms an even texture, missing glyphs, numerals,
   whether the italic is true, whether weight steps are visible, how the type sits on the page's colours. Drop
   candidates and note what you saw.
5. If you can't see a font (no network, a download that needs a person, no browser), look at the foundry's
   specimen page if you can. Otherwise say the choice is unseen, decide from the facts you can verify, and check
   it first on the built page. Never describe how a font looks as if you'd seen it when you haven't.

## 5. Answer

Keep it short:

- **Per role:** the font, the weights and sizes, and one or two sentences on why it fits, in the brief's words.
- **Pairing:** what contrasts and what's shared.
- **Rejected:** the candidates that nearly made it, each with a plain reason ("no true italic, and the body needs
  emphasis"; "wraps the headline into five lines on a phone").
- **Licence and source** for each font, and how to self-host it: `@font-face` pointing at the project's own
  files, the `font-family` stack with fallbacks, and where to download the files.
- Whether you saw it on a proof, on a specimen, or not at all.

When writing into a project, write the `@font-face` rules and family variables into its existing styles.

## 6. Check the built page

Answer yes or no for each, with what you see on desktop and phone screenshots:

1. Every planned face loaded; no role renders in a fallback.
2. The hero headline wraps into a few balanced lines on a phone, with no single word alone on a line of big
   type and no headline so big it pushes the main action off the first screen.
3. Body text is at least 16px on a phone, with lines of roughly 45–80 characters and line-height suited to the
   x-height.
4. No faked bold or italic.
5. The hierarchy reads in a few clear steps, not many near-identical ones.
6. Numbers people compare use tabular figures and line up.
7. The display face never appears at small sizes.
8. In a five-second look, the type supports what the brand should feel like. Say which quality and how.

## Examples

These show the reasoning, not answers to copy.

**A premium artisan bakery** (considered, made by hand; "made this morning", "worth the walk").

- **Display:** an expressive serif with visible craft, such as flared or bracketed terminals and some
  irregularity, at its best at hero size. It carries "made by hand" at a glance.
- **Body:** the same family if it has a text cut or optical sizes. Otherwise a calm, readable serif or a humanist
  sans with a true italic.
- **UI:** the hours and opening status use a clear sans or the body face's figures, because people check them on
  a phone in the street.
- **Rejected:** a geometric sans that reads like a delivery app.
- **Same category, opposite position:** a cheap and cheerful bakery chain wants sturdy, rounded, heavier faces
  with a big x-height. Premium restraint would read as pricey and slow there.

**A developer SaaS with a usage-based billing API** (technical, calm, precise; the buyer distrusts marketing).

- **UI and body:** a neutral sans with tabular figures and clear look-alikes. It disappears so the numbers can be
  checked.
- **Display:** marketing headlines can take a more distinctive face if it stays calm, such as a restrained serif
  or a characterful grotesque. Sci-fi or "hacker" lettering contradicts "calm".
- **Monospace:** for request samples and IDs. It needs braces, pipes and tildes, and should match the sans's
  x-height inline.
- **Rejected:** a wide geometric display face that read as startup-flashy.
