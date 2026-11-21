---
name: images
description: Direct the images on a website like an art director. Decides what each image must prove, chooses between photography, illustration, the real product, diagrams and type, writes shot lists, sets crops, aspect ratios, light and treatment, keeps a set consistent, places images so they work at every width, and rejects generic stock and dishonest images. Use when choosing, briefing, generating, cropping or placing photos, illustrations or graphic assets, or reviewing a page whose images feel generic, inconsistent or decorative. Not for page structure (`layout`), spatial balance (`compose`), icons (`icons`) or image file performance (`performance`).
argument-hint: "[brief, page or set of images]"
---

# images

An image on a website is evidence or it's filler. Decide what each one has to make a visitor believe, choose the
kind of image that can honestly do that, direct it (subject, framing, light, crop, treatment), and check that the
set reads as one brand at every width.

Brief, page or images:

$ARGUMENTS

If this is empty, review the images on the current project's pages. If `DIRECTION.md` exists, its imagery plan
(job, kind, shot list, treatment, what ships now) is the brief: execute it, don't replace it. If something in it
can't work on screen, say so.

## Where this sits

- `taste` decides the imagery plan as part of the direction (the imagery plan in its
  `references/visual-direction.md`).
- `images` turns that plan into actual images: selection, art direction, crops, ratios, consistency, placement.
- `compose` decides how images weigh against everything else on the page; `responsive` owns how the
  layout adapts; `performance` owns formats, sizes and loading; `icons` owns icons.

## Principles

1. **Every image has a job.** Prove the product exists and looks like this; show the place, the people, the
   result; explain how something works; set a mood the copy can't. If you can't name the job in one sentence
   tied to the brief, the image is decoration, and decoration is the first thing visitors' eyes learn to skip.
2. **Specific beats pretty.** A slightly imperfect photo of the actual bakery's actual counter does more than a
   flawless stock loaf. Visitors are very good at recognising stock: generic people, generic light, generic
   smiles. Recognition costs trust.
3. **The kind of image follows the job.** Photography proves things exist. Illustration explains, imagines or
   shows what can't be photographed. The real product interface proves software. Diagrams explain mechanisms.
   Type can be the image when words are the product. Choosing "none" is a decision too (see taste's imagery
   plan).
4. **A set is one voice.** Consistent light, colour treatment, distance and crop logic make many images read as
   one brand. Inconsistency reads as assembled from different sources, because it was.
5. **Crops are composition.** What's in the frame, where the subject sits, and how much room it has decide what
   the image says. A crop that works at 16:9 can cut off the subject at 4:5.
6. **Honesty.** No stock people posing as staff or customers. No AI-generated images presented as the real
   business, product, place or people. No fake screenshots making claims the brief doesn't make. Illustration
   and clearly illustrative generated imagery are fine when they don't pretend to document.

## How to work

### 1. Name the jobs

For each place an image would go, write: the job, the perception quality it supports, and what a visitor should
be able to tell from it. Delete slots whose job is "fill the space" or "break up the text": fix those with
composition, not pictures.

Ask first whether the page needs images at all. A tool whose interface is the product, a statement page or a
reference document can be better with none; then type, colour and composition carry it. If `DIRECTION.md`
chose "none", respect it.

### 2. Choose the kind

| Kind | Does well | Weak at | Good when |
| --- | --- | --- | --- |
| Documentary photography | Proving real things, people, places | Explaining abstractions | The business has a physical reality worth showing |
| Product photography | Showing the object exactly | Context, scale | The object is the decision |
| Product interface (built in HTML or real screenshots) | Proving software works | Emotion | Software, tools, data products |
| Editorial or illustrative illustration | Ideas, processes, tone, things not yet built | Proof | Services, abstract products, warmth without faces |
| Diagram, map, chart | Mechanisms, location, comparisons | Mood | How it works, where it is, how much |
| Type as image | Voice, statements | Proof of anything physical | The words are the product, or nothing else is honest |
| Texture, pattern, material | Surface, craft, atmosphere | Information | Supporting a signature device, never as the main image |

Mixing kinds is fine with a rule: for example, photography for the place, line diagrams for the process. Mixing
without a rule reads as a template.

### 3. Direct the images

Write a shot list (or illustration brief) per image. Each line states subject, framing, light, treatment and
where it sits. "Baker's hands shaping a loaf, tight crop at bench height, window light from the left, warm but
not orange, full-bleed after the menu" passes. "Bakery photo" fails. `references/art-direction.md` covers
framing, light, colour treatment, illustration styles and the stock clichés to refuse. If you generate images,
write the shot-list line first and translate it; the reference's Generated images section covers prompts, the
generator's own defaults, keeping a set consistent and what to check before using one.

When you have no real photography, ship what you can make honestly (the product built in HTML, diagrams, maps,
typographic compositions, SVG illustration that serves the signature device) and leave the shot list for the
client to commission. Never ship an empty frame or a "photo goes here" box, and never fill a slot with an
unrelated stock image as a stand-in.

### 4. Set ratios and crops

- Use a small set of aspect ratios, each with a reason: portrait (4:5, 3:4) for people and objects, landscape
  (3:2, 16:9) for places and groups, square for catalogue items, very wide (21:9 and beyond) only for
  atmosphere with nothing important at the edges.
- Pick each image's crop from its subject, not from the slot. If a slot changes ratio across widths, decide the
  crop at each ratio: `<picture>` with different sources when the composition must change (art direction), or
  `object-fit: cover` with a deliberate `object-position` when the same frame can stretch.
- Keep the subject's focal point clear of text, UI and the edges where crops will bite.
- In a set (a team, a product grid), keep the same ratio, the same distance and the same position of the subject
  (eye line, horizon, product baseline) so the row reads as one.

### 5. Place

- Images go next to what they prove: the dish beside its description, the interface beside the claim.
- Text over images only when the image has a calm area under the text at every crop, and contrast passes at the
  worst point. A heavy gradient scrim to rescue text is a sign the image or the placement is wrong.
- Faces pull the eye and send it where they look; face them towards the content they belong to.
- Captions add information (who, where, what) or they don't exist.
- Alt text describes what the image shows that matters for the page's purpose; decorative images get `alt=""`.

### 6. Check the render

On desktop (about 1440), phone (about 390) and any width where a ratio changes, look at every image:

1. Does each image do its named job? Cover it: is anything lost?
2. Swap test: could the image appear on a competitor's site, or one from another category? If yes, it's generic.
3. Is the subject intact at every crop: no cut-off heads, no product sliced by the frame, no focal point behind
   text?
4. Does the set read as one: light, colour, distance, eye lines and baselines?
5. Is any text on an image readable at its worst point?
6. Is anything pretending: stock people as staff, a generated image as the real place, a fake screenshot?
7. Are the images the right weight on the page (`compose`'s blur test), or does decoration win?

Report the job, kind and source of each image, what you couldn't supply and what the client should commission.

## Mistakes agents make

- Treating images as slots to fill: a hero image because heroes have images.
- Stock clichés: handshakes, a diverse team laughing at a laptop, a person pointing at a screen, a lightbulb for
  ideas, abstract 3D blobs and gradient meshes.
- Unsplash-style "nice" photos unrelated to the business, or the same photo every agent picks for the category.
- Generated images of the business's "team", "office" or "product" presented as real.
- Accepting a generator's default look: glossy, centred, shallow focus everywhere, teal-and-orange.
- One ratio for everything, or every image a different ratio by accident.
- `object-fit: cover` with the default centre crop, cutting off heads and products on phones.
- Text on the busiest part of a photo, rescued with a black gradient.
- Mixing flat illustrations, 3D renders and photos with no rule.
- Missing or useless alt text ("image", the filename), or descriptive alt on pure decoration.
