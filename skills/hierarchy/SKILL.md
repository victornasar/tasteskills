---
name: hierarchy
description: Decide what matters most on a page or screen and make that ranking visible, so visitors notice, understand and act in the right order. Covers ranking information from the visitor's task, the headline and its supporting content, emphasis and prominence, reading and scanning patterns, scannability and checking that the hierarchy survives on the render. Use when a page feels flat or noisy, when everything looks equally important, when key information is missed, or when building any dense screen (pricing, product, dashboard, article, form). Not for spatial balance and placement (`compose`) or writing the words (`content`).
argument-hint: "[page, screen or section]"
---

# hierarchy

Hierarchy is a ranking of information, made visible. First decide what matters to this visitor, in what order;
then spend emphasis so that order is what they see. Most hierarchy failures are ranking failures: nobody decided,
so everything got medium emphasis, or the brand's message got the emphasis the visitor's question needed.

Page, screen or section:

$ARGUMENTS

If this is empty, review the current project's main page. Read `DIRECTION.md` if it exists.

## Where this sits

- `content` decides what is said and writes it. `hierarchy` decides how prominent each piece is.
- `compose` decides where things sit and how weight balances (its principles reference explains visual
  weight, focal points and eye flow in depth). This skill decides *what* deserves weight and checks that the
  ranking reads.
- `fonts` sets the type scale; `palette` reserves the accent. This skill decides which content gets them.
- `conversion` finds which facts and actions the visitor needs at each point; this skill makes them prominent.

## Principles

1. **Rank from the visitor's task, not the org chart.** The most important thing is what the visitor needs to
   decide or do next: the price, the opening hours, whether the outage affects them, which plan fits. The
   company's favourite message is often third.
2. **Emphasis is relative and finite.** Something is prominent only against quieter things. Every bold word,
   colour, badge and box spends the budget. To raise one thing, lower others.
3. **Few levels, clearly separated.** Most screens need three visible levels plus body text. Five levels that
   differ by 2px each read as one muddled level.
4. **Every element has a role.** Headline, supporting line, body, label, metadata, action. Each role looks the
   same everywhere it appears, so visitors learn the system once.
5. **People scan before they read.** They read a small fraction of the words on a page (Nielsen Norman Group's
   studies put it well under a third on average). Hierarchy decides which fraction.
6. **The hierarchy must survive without colour, at a glance and on a phone.**

## How to work

### 1. Rank the content

List every piece of content in the view and give it one of:

- **Primary:** the one thing that answers the visitor's first question or is the one action. One per view.
- **Secondary:** what they need next to trust or decide (the evidence, the key detail).
- **Tertiary:** useful when wanted (descriptions, metadata, secondary actions).
- **Background:** must be available, should not compete (legal, navigation chrome, footnotes).
- **Cut:** answers no question. Remove it rather than styling it quietly.

If two things claim primary, decide. If nothing deserves primary, the content is the problem, not the styling.
Write the ranking down; it's the spec for everything after.

### 2. Pair headlines with their support

A headline and what supports it are one unit:

- **Headline:** the claim or the answer, as specific as the brief allows (`content` writes it).
- **Supporting line:** the evidence or the specifics that make the headline believable. It should be clearly
  subordinate (smaller, lighter or quieter) and close to the headline.
- **Proof or detail:** the artifact, the numbers, the example.
- **Action:** what to do now, after the reason to do it.

Common failures: a vague headline with the real information in the supporting line (swap them, or rewrite); a
supporting line as large as the headline; an eyebrow label above the headline that competes with it; the action
before any reason to take it.

### 3. Choose the emphasis tools

Use the fewest tools that make the ranking unmistakable. In rough order of cost:

| Tool | Good for | Cost |
| --- | --- | --- |
| Position (first, top, start of the line) | The primary item | Free, but only one thing can be first |
| Size | Headlines, the key number | Takes space; big text wraps on phones |
| Weight | Labels, key words, names in a list | Too much bold becomes texture |
| Value contrast (darker or lighter text) | Demoting metadata and secondary text | Must keep 4.5:1 for body text |
| Colour (the reserved accent) | Actions, the one highlight | Loses meaning when used twice for two jobs |
| Space and isolation | Making something stand alone | Composition's domain; costs height |
| Enclosure (a box, a band) | One group that must stand apart | Heavy; loses meaning when everything is boxed |
| Iconography, badges | Status, categories | Adds noise; a badge on everything is no badge |
| Motion | Change of state | Strongest and most distracting; see `motion` |

Demote before you promote. Most flat pages are fixed by making secondary and tertiary content quieter, not by
making the primary louder.

### 4. Build for scanning

- Headings carry information, so a visitor reading only headings gets the story ("Open until 4pm today", not
  "About us").
- Front-load: the distinguishing words come first in headings, list items, links and buttons.
- Keep one emphasis style per role. If bold means "key term" in one paragraph and "warning" in another, it means
  nothing.
- Make the things people hunt for (prices, dates, numbers, names) visually consistent so they can be found by
  shape: same position, tabular figures, same weight.
- Break long text with real structure (headings, lists, tables), not decorative breaks.
- Collapse or move background content rather than shrinking it until it's unreadable.

Reading patterns and how hierarchy changes them are in `references/reading-and-scanning.md`, with hierarchy
patterns for common screens (pricing, product, article, form, dashboard, search results).

### 5. Check the render

On desktop and phone screenshots:

1. **Squint or blur.** List what survives, in order. It should match your ranking.
2. **Grayscale.** Does the ranking hold without colour?
3. **Five-second test.** Look for five seconds, look away, write what you remember. Is the primary item there?
4. **Headings-only read.** Read only the headings and bold text. Does it tell the story and answer the first
   question?
5. **Count levels.** How many distinct text styles are visible? Is each step clearly different from its
   neighbours?
6. **Count emphasis.** How many things are bold, coloured, boxed or badged in one view? More than a handful means
   the emphasis has stopped working.
7. **Phone.** Is the primary item on the first screen? Did stacking change the ranking?

Report the ranking, the tools used for each level, and what you demoted or cut.

## Mistakes agents make

- No ranking: every section, card and heading gets the same medium emphasis.
- The brand slogan gets the biggest type while the visitor's question (price, hours, status) is in small print.
- An eyebrow label, a badge, the headline and a gradient button all competing in the first screen.
- Two primary buttons side by side.
- Bold and colour sprinkled through body text until nothing stands out.
- Six or more near-identical text sizes.
- Grey-on-grey secondary text that fails contrast, used as the way to demote.
- Headings as labels ("Features", "Benefits") that say nothing when scanned.
- Icons and badges on every item, so the one that matters can't stand out.
