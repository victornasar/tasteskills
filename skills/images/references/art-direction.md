# Art direction for web imagery

Deeper guidance for directing, selecting and treating images. Use it after you've named each image's job
(SKILL.md step 1). None of this is a style to apply everywhere; each choice needs a reason in the brief.

## Framing

| Framing | Says | Use for | Watch for |
| --- | --- | --- | --- |
| Extreme close-up (texture, hands, a detail) | Craft, material, care | Makers, food, materials, repairs | Losing what the thing is; needs a wider shot nearby |
| Close (a face, an object filling the frame) | Intimacy, the object itself | People who matter, products | Faces covered by text; uncomfortable crops at the chin and forehead |
| Medium (a person at work, an object in use) | Activity, use, scale | Services, how something is used | Clutter in the background |
| Wide (a room, a place, a group) | Context, scale, atmosphere | Places people will visit | Details too small on a phone |
| Overhead (flat lay) | Order, inventory, a set | Menus, kits, collections | A cliché for food and stationery; use when the arrangement means something |

A set of images usually needs more than one distance: a wide shot to establish, closer ones to prove. A page of
only close-ups loses context; a page of only wide shots loses detail.

**Subject position.** Centred subjects are stable and direct, right for products and portraits that address the
viewer. Off-centre subjects create direction and leave room, for text or for the eye to move toward the content.
Decide from where the image sits on the page, and keep the subject away from edges that responsive crops will cut.

**Eye lines and gaze.** People follow where a pictured person looks. A face looking toward the headline leads the
eye there; a face looking off the page leads it away.

## Light

| Light | Reads as | Fits |
| --- | --- | --- |
| Soft window light | Natural, calm, domestic | Homes, cafés, care, everyday products |
| Hard sun, strong shadows | Energy, heat, outdoors, candour | Sport, travel, summer, bold brands |
| Raking side light | Texture, craft, three dimensions | Materials, tools, food surfaces |
| Even studio light on a seamless background | Precision, comparability | Catalogues where products are compared |
| Low-key (mostly dark) | Drama, evening, intimacy, premium | Restaurants at night, performance, some luxury |
| High-key (mostly light) | Openness, cleanliness, ease | Health, cleaning, baby products — and the generic default for all of them |
| Mixed practical light (lamps, screens, streetlights) | Real places, documentary | Bars, workshops, cities |

Keep the light consistent across a set: similar direction, hardness and colour temperature. One hard-sun photo in
a set of soft window light looks borrowed.

## Colour treatment

- **Natural:** colour as it was. The default for documentary honesty.
- **Graded to the palette:** a consistent shift (warmer, cooler, desaturated, lifted blacks) so photos sit with the
  brand's colours. Grade the whole set the same way.
- **Duotone or monotone:** photos mapped to two brand colours or one. Unifies mismatched sources and suits strong
  graphic identities; loses information (food in duotone stops looking edible; skin tones suffer).
- **Black and white:** timeless, documentary, or a way to unify mixed photos. Can read as archival or as a premium
  cliché.

With CSS you can preview treatments (`filter: grayscale(1) contrast(1.1)`, `mix-blend-mode` over a colour field
for a duotone), but bake final treatments into the files when you can, so the image is the same everywhere it's
used.

## Illustration

Decide the style from the job and the direction, then keep it:

| Variable | Range |
| --- | --- |
| Line | None (shape-based), uniform line, varied hand-drawn line |
| Fill | Flat, textured, gradient, none |
| Palette | The brand palette only, or a wider illustrative palette |
| Figures | No people, abstracted people, characterful people |
| Detail | Iconic and simple, editorial and rich |
| Perspective | Flat, isometric, true perspective |

The generic defaults to look past: flat "corporate Memphis" figures with tiny heads and long limbs; isometric
office scenes; abstract 3D blobs and glossy spheres; gradient meshes. They signal "template" in the same way stock
photos do. A diagram drawn in the page's own line weight and type often does more.

SVG illustration the agent draws itself should be simple and confident: a map of the three shops, a cross-section
of the product, the steps of the process. Don't attempt detailed figurative illustration in SVG by hand; it reads
as clip art.

## Generated images

Image generators are useful for illustration, texture, concept sketches, mood, and things that don't exist yet.
They are never a substitute for documenting the real business.

**Honesty first.**

- Never present a generated image as the real business, place, product, staff, customer or result.
- Prefer styles that are clearly illustrative over photorealism when documenting is impossible.
- Tell the user which images are generated, and check the tool's terms for commercial use.

**From shot list to prompt.** Write the shot-list line first (SKILL.md step 3); the prompt is that line plus the
medium and what to leave out. Keep the parts in a fixed order so a set can share them:

1. Subject and action: what is in the frame, doing what.
2. Framing and viewpoint: distance, angle, lens feel ("close, at bench height, slightly from above").
3. Light: direction, hardness, time of day (from the Light table above).
4. Setting: the specific place, with the ordinary detail that makes it real.
5. Treatment: the colour grade or palette from the direction.
6. Medium: photograph, gouache, linocut, line drawing, collage.
7. Exclusions: text, logos, people, whatever the job doesn't need.

"Flour-dusted hands folding dough on a scarred wooden bench, close, bench height, soft window light from the left,
overcast morning, muted warm grade, 35mm photograph, no faces, no text" gives the generator decisions to follow.
"Beautiful artisan bakery, cinematic" leaves every decision to its defaults.

**The generator's own defaults.** Generators have a house style as recognisable as Inter and a purple gradient:
glossy, over-smoothed surfaces and skin, a centred subject, shallow focus on everything, teal-and-orange grading,
haze and light rays, saturated colour, "epic" scale. Name ordinary, specific conditions instead: flat noon light,
overcast, clutter on the bench, a wide aperture only where depth means something. If the result could illustrate
any brand in the category, it has the same problem as stock.

**Keeping a set consistent.**

- One prompt skeleton for the set; change the subject line and keep the rest word for word.
- Use a style or reference image where the tool supports it, so the set shares a look across sessions.
- Generate at the slot's aspect ratio, not square then cropped.
- Generate more than you need and choose; grade the chosen images together.

**Check every image at full size before using it.** Hands and fingers; garbled text and fake logos; product details
that don't match the real product; impossible architecture, shadows or reflections; the same face repeated; and
details that would mislead, such as a dish the bakery doesn't sell. Reject rather than retouch when the error is
in the subject.

## Stock imagery

When the client has no photography and stock is the only route:

- Use stock for things that aren't claims: a place's weather, a material, a city, an ingredient. Not for "our
  team", "our customers" or "our office".
- Avoid the clichés: handshakes, people pointing at screens, laughing at salads, headsets in call centres,
  lightbulbs, puzzle pieces, chess pieces, targets with arrows, glowing brains, generic skylines.
- Avoid the over-used images every site in the category uses; search past the first page of results.
- Grade stock to the set's treatment so it doesn't stand out.
- Prefer one honest diagram or the product itself over three stock photos.

## Consistency checklist for a set

- Same or deliberately related aspect ratios.
- Same distance for parallel items (all team portraits head and shoulders, at the same eye line).
- Same light direction and temperature.
- Same colour treatment.
- Same background logic (all in context, or all on seamless).
- Product shots share a baseline and a scale, so a small object doesn't look as big as a large one unless that's
  intended.

## Responsive cropping

- Write the crop for each ratio the slot takes. For a hero that is 21:9 on desktop and 4:5 on a phone, these are
  two different pictures of the same scene; use `<picture>` with `media` sources and supply both crops.
- With one file and `object-fit: cover`, set `object-position` to the subject (`object-position: 30% 40%`), and
  check every width in between, not just the ends.
- For catalogue items, crop the files to a consistent ratio rather than relying on CSS to hide inconsistent
  framing.

## Alt text

Write what the image contributes to the page, in the page's context. The same photo of a loaf might be
"Sourdough with a dark, blistered crust, sliced to show an open crumb" on the menu, and `alt=""` as a background
texture. Don't start with "Image of". Don't repeat the caption. Text inside an image must be in the alt or on the
page.
