---
name: check-layout
description: Plan a web page's structure from its brief, then render it and check for the layout patterns AI-built sites overuse (centered hero, rows of three cards, decorative gradients, emoji icons, rounded boxes everywhere, pill badges, rows of big numbers, identical section spacing, purple buttons), and fix what the brief doesn't justify. Use when building or reviewing a landing page, marketing site, portfolio or any web page, before calling it done.
argument-hint: <brief, page file or URL>
---

# check-layout

The checker is `scripts/check_layout.mjs`, in the same folder as this file. It renders the page in Chrome and
measures its computed styles, so it works on any stack: a plain HTML file or a running dev server. It needs
Node 22 or later and Chrome, Chromium, Edge or Brave. No install.

```bash
node <this-skill-folder>/scripts/check_layout.mjs <page.html | http://localhost:3000/> --screenshot shot.png
```

Brief or page:

$ARGUMENTS

## Why this exists

In 90 sites built by AI models from generic briefs, the same layout moves came back again and again (rates on
landing pages):

| Pattern | Landing pages | All sites |
|---|---|---|
| Rounded boxes everywhere | 100% | 61% |
| Pill badge above the headline ("✨ New: …") | 93% | 40% |
| Emoji used as icons | 93% | 37% |
| Decorative gradient | 87% | 31% |
| Row of three cards | 53% | 39% |
| Centered hero headline | 33% | 32% |
| Row of big numbers ("10k+ users") | 27% (80% on portfolios) | 21% |
| Same padding on every section | 7% (53% on portfolios) | 18% |
| Indigo, violet or purple main button | 20% | 11% |

And when the same models were given better fonts and colors, **the page structure didn't change**: the same
status bar, split hero, pair of buttons and section order came back. None of these moves is wrong. They're slop
because they arrive whatever the brief says.

## 1. Plan the structure before building

Write this down, briefly, before any code:

1. **The default.** The section list you'd reach for without thinking (for example: nav, centered hero with two
   buttons, three feature cards, stats, testimonials, CTA band, footer). Naming it is what lets you depart from
   it.
2. **The visitor's questions, in order.** What does this visitor need to know first, second, third? A bakery
   visitor on a phone asks "is it open, where is it, what's baked"; an engineering buyer asks "what does it do,
   how does it work, can I trust it". The page's order follows these, not the default.
3. **The one thing only this brief has.** The product's own artifact or fact: the invoice line that expands, the
   hours board, the menu with prices, the floor plan. Lead with it, as content, not decoration.
4. **What to cut.** Every section in the default that answers none of the visitor's questions goes. A short page
   that answers them beats a long one that pads them.

Then build from that plan.

## 2. Check the rendered page

```bash
node scripts/check_layout.mjs <page> --screenshot shot.png            # first screen, desktop
node scripts/check_layout.mjs <page> --screenshot shot-full.png --full  # whole page
node scripts/check_layout.mjs <page> --width 390 --height 844 --screenshot shot-phone.png
```

Look at the screenshots yourself (open the PNG) and compare them with your plan from step 1. The report lists
which of the nine patterns the page shows, with evidence. `--json` gives the full measurements.

## 3. Decide on each finding

For each pattern found, either change it or keep it and give a one-line reason tied to the brief. "It looks
modern" isn't a reason.

| Pattern | Fine when | Otherwise, consider |
|---|---|---|
| Centered hero | The page has one short message and one action, like a sign-up for an event | Set the headline on a strong left edge; lead with the product's artifact beside or under it; let the first screen show real content, not just a slogan |
| Row of three cards | There are exactly three parallel items of equal weight | A list with real descriptions; one featured item and the rest smaller; a table when items share attributes; a sequence when order matters |
| Decorative gradient | It carries meaning (a heat map, a time of day) | A flat ground from the color direction; let type and content carry the page |
| Emoji as icons | The brand's voice is genuinely playful and the emoji are part of the copy | No icon at all (most feature lists read better without); a real icon set used consistently; numbers or labels when order matters |
| Rounded boxes everywhere | Rounding is a deliberate part of the identity, and only some elements are boxed | Box only what is a separate object; use rules, spacing and alignment to group; vary radius by role |
| Pill badge above headline | There is real news a returning visitor needs | Put the news where it belongs (a dated line, a changelog link) or drop it |
| Row of big numbers | The numbers are the point and are real (a dashboard, a report) | State the one figure that matters in a sentence; show evidence instead (a real example, a quote with a name) |
| Same padding everywhere | The page is genuinely uniform, like a document | Let spacing follow the content: tight inside a group, generous between ideas, a change of density where the page changes subject |
| Purple button | The brand color is purple | Use the accent from the color direction (see `find-color`), reserved for actions |

Don't swap one default for another: if every page you build ends up left-aligned with a serif headline, that's a
new template. The plan in step 1 should differ when the brief differs.

## 4. Re-check once, then report

Run the checker again after your changes. Then tell the user, in a few lines: what the plan led with and why,
which patterns you removed, and which you kept with their reasons. Don't loop more than twice; the checker is a
second pair of eyes, not a score to drive to zero.
