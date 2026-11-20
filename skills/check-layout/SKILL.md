---
name: check-layout
description: Plan a web page's structure from its brief, then look at the rendered page and fix the layout patterns AI-built sites overuse (centred hero, rows of three cards, decorative gradients, emoji icons, rounded boxes everywhere, pill badges, rows of big numbers, identical section spacing, purple buttons). Use when building or reviewing a landing page, marketing site, portfolio or any web page, before calling it done.
argument-hint: "[brief, or the page to review]"
---

# check-layout

Plan the page from what its visitors need, build it, then look at what you actually made.

Brief or page:

$ARGUMENTS

## Why this exists

In 90 sites built by AI models from generic briefs, the same layout moves came back again and again:

| Pattern | Landing pages | All sites |
|---|---|---|
| Rounded boxes everywhere | 100% | 61% |
| Pill badge above the headline ("✨ New: …") | 93% | 40% |
| Emoji used as icons | 93% | 37% |
| Decorative gradient | 87% | 31% |
| Row of three cards | 53% | 39% |
| Centred hero headline | 33% | 32% |
| Row of big numbers ("10k+ users") | 27% (80% on portfolios) | 21% |
| Same padding on every section | 7% (53% on portfolios) | 18% |
| Indigo, violet or purple main button | 20% | 11% |

The average page showed about three of these. When the same models were given better fonts and colours, **the
page structure didn't change**: the same status bar, split hero, pair of buttons and section order came back.
None of these moves is wrong. They're slop because they arrive whatever the brief says.

Planning first works. In the lab, a plan-then-check pass cut these patterns from 1.33 per page to almost none,
and page structure started to follow the brief.

## 1. Plan the structure before building

Write this down briefly, before any code:

1. **The default.** The section list you'd reach for without thinking (for example: nav, centred hero with two
   buttons, three feature cards, stats, testimonials, CTA band, footer). Naming it is what lets you depart from it.
2. **The visitor's questions, in order.** What does this visitor need to know first, second, third? A bakery
   visitor on a phone asks "is it open, where is it, what's baked, can I order a cake?" An engineering buyer asks
   "what does it do, how does it work, can I trust it?" The page's order follows these questions, not the default.
3. **The one thing only this brief has.** The product's own artifact or fact: the invoice line that expands, the
   hours board, the menu with prices, the floor plan. Lead with it as content, not decoration.
4. **What to cut.** Every section in the default that answers none of the visitor's questions goes. A short page
   that answers them beats a long one that pads them.

Then build from that plan.

## 2. Look at the rendered page

Render the page and look at it yourself: the first screen and the whole page on desktop (about 1440px wide), and
on a phone (about 390px). Use whatever you have: the project's dev server in a browser tool, Playwright, or a
headless Chrome screenshot such as:

```bash
"<path to Chrome>" --headless --screenshot="$PWD/shot.png" --window-size=1440,900 "file://$PWD/page.html"
```

Compare the screenshots with your plan. Go through the nine patterns above and note which ones the page shows.
Also look for the failures blind reviewers punished most:

- **A broken desktop layout**, such as the whole page in a narrow column pinned to one side with the rest of the
  screen empty.
- **The visitor's first question isn't answered on the first screen**: the hours below the fold for a bakery, or
  no proof of the product's claim in the first screen for a software product.
- **Placeholders that take over**: giant empty image boxes, or visible "to be added" or "Placeholder:" text.
- **A headline so big it wraps to five or six lines** and pushes the main action down.
- **Missing basics the brief asked for**, such as a way to order, an address with a map link, or pricing.

## 3. Decide on each finding

For each pattern found, either change it or keep it with a one-line reason tied to the brief. "It looks modern"
isn't a reason.

| Pattern | Fine when | Otherwise, consider |
|---|---|---|
| Centred hero | The page has one short message and one action, like an event sign-up | A strong left edge; lead with the product's artifact beside or under the headline; let the first screen show real content, not just a slogan |
| Row of three cards | There are exactly three parallel items of equal weight | A list with real descriptions; one featured item and the rest smaller; a table when items share attributes; a sequence when order matters |
| Decorative gradient | It carries meaning (a heat map, a time of day) | A flat ground from the colour direction; let type and content carry the page |
| Emoji as icons | The brand's voice is genuinely playful and the emoji are part of the copy | No icon at all (most feature lists read better without); a real icon set used consistently; numbers or labels when order matters |
| Rounded boxes everywhere | Rounding is a deliberate part of the identity, and only some elements are boxed | Box only what is a separate object; group with rules, spacing and alignment; vary radius by role |
| Pill badge above headline | There's real news a returning visitor needs | Put the news where it belongs (a dated line, a changelog link) or drop it |
| Row of big numbers | The numbers are the point and are real (a dashboard, a report) | State the one figure that matters in a sentence; show evidence instead (a real example, a quote with a name) |
| Same padding everywhere | The page is genuinely uniform, like a document | Let spacing follow the content: tight inside a group, generous between ideas, a change of density where the subject changes |
| Purple button | The brand colour is purple | The accent from the colour direction, reserved for actions |

**Don't swap one default for another.** If every page you build ends up left-aligned with a serif headline,
hairline rules and small capitals, that's a new template: it's what the lab's skill-built pages converged on once
the overused patterns were removed. The plan in step 1 should differ when the brief differs.

## 4. Fix, look once more, report

Fix what the brief doesn't justify, render again, and look once more. Then tell the user in a few lines what the
plan led with and why, which patterns you removed, and which you kept and why. Don't loop more than twice. This is
a second pair of eyes, not a score to drive to zero.
