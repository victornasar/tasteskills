# Composition critique

How to evaluate a composition on the rendered page: what to capture, what to look at, how to measure what the eye
can't settle, how to write findings, and how to fix them without introducing a new default. There's no score.
The output is a short list of observations, each tied to a relationship and a fix.

## 1. Capture

Render the page and capture:

| View | Size | Why |
| --- | --- | --- |
| Desktop, first screen | 1440 × 900 | What most desktop visitors judge the page by |
| Desktop, full page | 1440 wide | Pacing, rhythm, alignment across sections |
| Phone, first screen | 390 × 844 | The phone's own focal point |
| Phone, full page | 390 wide | Length, phone pacing, stacked groups |
| Wide | 1920 × 1080 | Lopsided max-width containers, stretched layouts (when the content has a max width) |
| Tablet | 1024 × 768 | Grids that change between sizes (when they do) |

Then make three diagnostic versions of the desktop and phone first screens. Inject one of these rules before
screenshotting (through the browser tool's evaluate, a Playwright `addStyleTag`, or a temporary `<style>`):

```css
html { filter: blur(6px); }        /* blur: what wins, and which groups form */
html { filter: grayscale(1); }     /* value: weight without colour */
html { transform: scaleX(-1); }    /* mirror: balance seen fresh */
```

A fourth, for alignment:

```css
* { outline: 1px solid rgb(255 0 0 / 0.35); }
```

Look at every image yourself. A description of what the page probably looks like is not a critique.

## 2. Look, in order

Go from the whole to the detail. Write a sentence for each check, on desktop and on phone.

1. **First glance (blur).** What wins? Is it the focal point from the plan? Which shapes group together? Does any
   area look heavy or empty?
2. **Value (grayscale).** Without colour, does the hierarchy hold? If the focal point depended on hue alone, it's
   weaker than it looks, and invisible to some colour-blind visitors.
3. **Eye path.** List the first five places your eye lands, in order. Does the path reach the primary action? Does
   anything decorative interrupt it? Does the bottom of the first screen invite a scroll?
4. **Balance (mirror and wide).** Does the mirrored screenshot feel lopsided? Cover each half: is either half a
   complete thought? At 1920, is the content stranded?
5. **Hierarchy.** How many levels can you see? Are there competitors for first place? Is there exactly one primary
   action per view?
6. **Space and grouping.** Is every label, caption, price and button unambiguously closest to what it belongs to?
   Is the gap inside groups clearly smaller than between them? Any trapped holes?
7. **Alignment (outlines).** How many left edges on a screen? Are any a few pixels apart? Does each deviation leave a
   real line, for a reason you can name?
8. **Scale and contrast.** How many sizes? Are the steps clearly different? Is the biggest thing the focal point?
   Does the headline wrap well on a phone?
9. **Density and pacing (full page, zoomed out).** Describe the rhythm as a strip of loud/quiet and dense/open. Does
   it match the plan? Does it look like a barcode of identical blocks?
10. **Layering.** Does anything overlap text or the subject of a photo? Check each overlap at every captured width
    and at 200% zoom. Measure text contrast at the worst point of any image behind it.
11. **Phone as its own composition.** Is there a focal point on the first screen? Did groups survive stacking? Is the
    page sensibly long?
12. **Direction.** Name the intended perception qualities and say what in the render shows each. Run the composition
    swap test: would this composition suit a different business from another category just as well? Look for both
    defaults:
    - *Generated:* everything centred; identical section padding; equal cards for unequal items; two equal primary
      buttons; no single focal point; flat density after the hero.
    - *Designed:* an oversized headline with no content reason; image and text overlapping; most of the first screen
      empty; elements knocked off the grid or rotated; tiny uppercase captions in the margins; every section a
      different layout "to keep it interesting".

    Any marker present needs a reason from the brief. If several appear and the plan can't justify each, the page
    has landed on a default. If `taste` wrote a `DIRECTION.md`, its house-style markers H5 and H6 are compositional;
    count them here too.

## 3. Measure what you can't settle by eye

Run this in the page (a browser tool's evaluate, Playwright's `page.evaluate`, or DevTools). It lists the left
edges of visible blocks, edges that nearly but don't quite align, the distinct font sizes, and headings that sit
as close or closer to the content above them as to their own content.

```js
(() => {
  const visible = (e) => {
    const r = e.getBoundingClientRect(), s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none';
  };
  const blocks = [...document.querySelectorAll(
    'h1,h2,h3,h4,h5,h6,p,li,blockquote,figure,img,table,form,label,input,button,a.button,[class*="btn"]'
  )].filter(visible);

  const edges = {};
  for (const e of blocks) {
    const x = Math.round(e.getBoundingClientRect().left);
    (edges[x] ||= []).push(e.tagName.toLowerCase());
  }
  const xs = Object.keys(edges).map(Number).sort((a, b) => a - b);
  const nearMisses = [];
  for (let i = 1; i < xs.length; i++) {
    const d = xs[i] - xs[i - 1];
    if (d > 0 && d <= 8) nearMisses.push(`${xs[i - 1]}px / ${xs[i]}px`);
  }

  const fontSizes = [...new Set(blocks.map((e) => getComputedStyle(e).fontSize))]
    .sort((a, b) => parseFloat(a) - parseFloat(b));

  const headingSpacing = [...document.querySelectorAll('h2,h3,h4')].filter(visible).map((h) => {
    const r = h.getBoundingClientRect();
    const prev = h.previousElementSibling, next = h.nextElementSibling;
    const above = prev && visible(prev) ? Math.round(r.top - prev.getBoundingClientRect().bottom) : null;
    const below = next && visible(next) ? Math.round(next.getBoundingClientRect().top - r.bottom) : null;
    return { heading: h.textContent.trim().slice(0, 40), above, below };
  }).filter((h) => h.above !== null && h.below !== null && h.above <= h.below);

  return {
    leftEdges: xs.map((x) => `${x}px × ${edges[x].length}`),
    nearMisses,
    fontSizes,
    headingsCloserToContentAbove: headingSpacing,
  };
})();
```

Read the output with judgement:

- **Left edges.** Expect a handful per screen width. Indented list items and centred elements add edges
  legitimately; edges 1–8px apart almost never are.
- **Font sizes.** Several sizes within a pixel or two of each other suggest indecision. More than about eight
  distinct sizes on a marketing page is worth questioning.
- **Headings.** The check only sees headings with element siblings on both sides. Check headings that open a
  section or card by eye.
- Run it at desktop and phone widths; the problems differ.

## 4. Write findings

For each weakness, one line:

`<what you see> → <the relationship it breaks> → <the change>`

For example:

- "At 390px the order button sits below the photo and the full menu, two screens down → the primary action is off
  the path for the main phone task → move the button to follow the opening line, keep the photo, collapse the menu
  to today's items."
- "The price is 24px from its dish and 28px from the next dish → proximity is ambiguous, so prices read as
  belonging to either → 4px inside the item, 20px between items."
- "Headline, illustration and badge all survive the blur → three competitors for first place → remove the badge,
  reduce the illustration's saturation, keep the headline."

Rank by consequence:

1. **Breaks the job:** the focal point is wrong, the first question isn't answered where the eye lands, the primary
   action is off the path, text is covered or unreadable.
2. **Weakens it:** ambiguous groups, competing focal points, unintended imbalance, flat pacing.
3. **Polish:** near-miss alignment, uneven optical alignment, slightly too many sizes.

Also write a **keep** list: what works and must survive the fixes. Fixes often break the thing that was right.

## 5. Fix without adding a default

| Symptom | Likely cause | Try first | Don't |
| --- | --- | --- | --- |
| Cluttered | Too many equal weights; weak grouping | Demote and group; remove what serves no visitor question | Add whitespace everywhere |
| Empty or unfinished | Passive space; a weak focal point | Strengthen the focal point, or tighten the space so content forms a whole | Add blobs, gradients or floating icons |
| Static or boring | Flat hierarchy; uniform pacing | Rank more sharply; vary density between sections to fit their content | Make every section a different layout |
| Chaotic | Too many axes or deviations | Return to the grid; keep one or two deviations that rank something | Box everything to impose order |
| Everything equally important | Hierarchy by one lever, or none | Pick the one thing; demote the rest by size, contrast or space | Make the one thing bigger and bolder and coloured and boxed |
| The action is ignored | Off the eye path; competing with a second button | Put it where the path ends; make the second action quiet | Make it bigger and brighter |
| Lopsided on a wide screen | Fixed max-width content left-aligned in a wide frame | Centre the container, or let a full-bleed element anchor the width | Stretch text lines past a comfortable measure |
| The phone is an endless scroll | Desktop spacing and images scaled down unchanged | Reduce section spacing, crop images to their subject, merge groups | Hide content people need |
| Looks designed but says nothing | The "designed" default | Ask what each deviation, overlap and empty area does for this brief; remove those without an answer | Swap in a different trendy device |

Change one relationship at a time, render again, and look. Stop after two rounds; report what's left and what needs
a human decision.

## 6. Report

Keep it short:

- **Focal points:** what leads on desktop and phone, and why.
- **Approach:** balance, grid, scale, space, pacing and any layering, each with its reason from the brief.
- **Considered and rejected:** the alternative and why.
- **Found and fixed:** the findings from the render, with what changed.
- **Kept:** conventions or defaults you kept on purpose, and why.
- **Open:** anything that needs the client or a human eye (real photography, copy length, a direction that doesn't
  survive the render).

## Two worked critiques

**A SaaS hero with competing focal points.** The first screen has a 72px centred headline, a pill badge above it,
a saturated 3D illustration below, and two filled buttons.

- Blur: the illustration and the buttons survive; the headline barely does. Grayscale: the illustration still
  dominates. Eye path: badge, illustration, buttons, headline, nothing else.
- Relationships broken: the decoration is the focal point; two actions are presented as equal; the product never
  appears.
- Fixes: replace the illustration with the product's real output (built in HTML), make it the focal point at
  roughly 60% of the width, move the headline to a left-aligned text block beside it at a smaller size, keep one
  filled button and turn the other into a text link, drop the badge. Re-render: blur shows the product, then the
  headline, then one button.
- Kept: a centred layout was considered for a launch page with one action and rejected because the product needs
  to be seen beside the claim, not under it.

**A neighbourhood bakery with uniform spacing.** Every section has 96px padding, every gap is 32px, and the
menu sits in nine equal cards.

- Full-page strip: identical blocks, top to bottom. Phone: eleven screens long. Grouping: each price is equidistant
  from two dishes.
- Relationships broken: no pacing; dishes and prices misgrouped; the menu, which visitors scan, is set as open as
  the hero, which they glance at.
- Fixes: menu as a dense list (dish and price on one line, 6px between lines, 28px between categories); hours and
  address grouped in one band near the top; section spacing varied by subject change; the bread photo given the
  page's one open, quiet moment. Phone drops to five screens.
- Kept: the conventional order (hours, today's bread, menu, cakes), because it's the order of the visitors'
  questions.
