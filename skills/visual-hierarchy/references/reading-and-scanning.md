# Reading, scanning and hierarchy patterns

## How people actually read web pages

Eye-tracking research (Nielsen Norman Group's studies are the most cited) describes patterns, not laws. Which
pattern appears depends on the page's hierarchy and the visitor's task.

| Pattern | What happens | Caused by | What to do |
| --- | --- | --- | --- |
| F-pattern | Reading the first lines, then less of each line further down, along the left edge | Undifferentiated text with weak headings | Treat it as a symptom. Add meaningful headings, front-load lines, use lists |
| Layer-cake | Eyes jump from heading to heading, reading body only where a heading earns it | Clear, informative headings | Design for it: headings must carry the story |
| Spotted | Skipping around looking for something specific: a number, a price, a link, a name | A task ("how much?", "when?") | Make the hunted things consistent in shape, position and figures |
| Marking | Eyes stay still while scrolling (common on phones) | Mobile scrolling | Put the key information where it passes the eye; keep it visually distinct |
| Bypassing | Skipping the repeated first words of list items | Items that all start the same ("Our…", "Get…") | Front-load the distinguishing words |
| Commitment | Reading everything | High motivation (a contract, a diagnosis) | Don't rely on it; even committed readers benefit from structure |

Other findings worth knowing:

- In left-to-right languages, people spend most viewing time on the left half of the page, so left-aligned
  headings and the starts of lines are prime positions.
- The first screen gets more attention than any later one, but people do scroll when the page signals there's
  more and the first screen earns it.
- Things that look like adverts (boxed, brightly coloured, in a sidebar, with stock imagery) get ignored: banner
  blindness. A crucial notice styled like a promo will be missed.
- Visitors decide very quickly whether a page is relevant; the primary item has to be recognisable at a glance,
  not after reading.

The Z-pattern and Gutenberg diagram are heuristics for sparse layouts, not established findings. Use them only as
a reminder that sparse pages are read top-left to bottom-right.

## Hierarchy patterns for common screens

These show typical rankings. The brief can change any of them; write your own ranking first.

**Pricing.**
Primary: the plan most visitors should pick, and its price. Secondary: the differences between plans, in the same
order and position for each. Tertiary: the full feature list, ideally a comparison table. Mistakes: three
identical cards with one "Popular" badge; prices in different positions; feature lists that repeat what every
plan has.

**Product page.**
Primary: the product (image or interface) and its name and price. Secondary: the action, availability or delivery,
and the two or three facts that decide a purchase (size, material, compatibility). Tertiary: full description,
specifications, reviews. Mistakes: marketing paragraphs above the price; the add-to-basket button the same weight
as "Add to wishlist".

**Article or long read.**
Primary: the headline and the standfirst (the one-sentence summary). Secondary: subheadings that summarise their
sections. Tertiary: body text, captions, pull quotes. Background: author, date, share links. Mistakes: pull quotes
as loud as the headline; metadata and share buttons before the first sentence.

**Form.**
Primary: the current question or the next field. Secondary: labels and help that prevent errors. Tertiary:
optional fields, explanations. The submit action is primary at the end, not before. See interaction-design for
behaviour.

**Dashboard.**
Primary: the one or two numbers or alerts that need action now. Secondary: trends that explain them. Tertiary:
everything else, on demand. Mistakes: a row of equally large KPI tiles, none of which says whether anything is
wrong. See data-visualization.

**Search results or listings.**
Primary: the attribute people choose by (the title, the price, the date, the distance), consistent in every
result. Secondary: the attributes that rule a result out. Tertiary: descriptions. Mistakes: each result laid out
differently; the selection attribute buried in a description.

**Homepage with many audiences.**
Primary: the set of top tasks, ranked within. Secondary: the current, time-sensitive thing (a notice, an event).
Mistakes: a hero slogan that serves none of the audiences, pushing the tasks below the fold.

## Type roles in a hierarchy

Define the roles once and reuse them. A typical set:

| Role | Job | Distinguished by |
| --- | --- | --- |
| Display or page title | The primary statement | Size, and often the display face |
| Section heading | A landmark for scanning | Size and weight, space above |
| Subheading | Structure within a section | Weight more than size |
| Body | Reading | The baseline everything is measured against |
| Supporting or lead | Context for a heading | Size between body and heading, or body in a quieter colour |
| Label | Naming a field, a value, a category | Weight or case, small |
| Metadata | Dates, authors, counts | Lower contrast (still accessible) or smaller size |
| Action | Buttons and important links | The accent, or a shape |

find-font picks the faces and sizes; this list decides which content takes which role.
