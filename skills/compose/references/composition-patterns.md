# Composition patterns

Recurring ways to compose a page, a section or a hero, with when each fits, when it fails, what poor execution
looks like, how to build it and what happens on a phone. Use them to widen what you consider after you've mapped
the content's relationships (SKILL.md step 3). They are not a menu, and no pattern belongs to a kind of business.
Most good pages combine two or three, and the best answer may be one that isn't listed.

A pattern describes relationships, not a look. A "reading column" can be austere or warm, serif or sans, pale or
dark. The direction decides the look; the content's relationships decide the pattern.

Contents: page patterns · first-screen patterns · controlled deviations · pacing patterns · phone translation ·
same principles, different outcomes.

---

## Page patterns

### Single axis (centred, symmetrical)

Everything sits on one central axis. The page presents one thing at a time.

- **Fits:** one message and one action (an event sign-up, an RSVP); ceremony (weddings, memorials); objects
  presented as monuments, one per screen; institutions that should feel permanent.
- **Fails:** long text, several actions, comparison, anything with many parts of different weight.
- **Poor execution:** centred paragraphs; centred lists; every section centred because the hero was.
- **Build:** short lines (`max-width` in `ch`), `text-wrap: balance` on headings, one primary action on the
  axis, generous space above and below each centred unit so each reads as a moment.
- **Phone:** works naturally; watch headings that wrap into ragged centred shapes.

### Reading column

One measure of text with a strong left edge, perhaps with a narrow side column for notes or navigation. GOV.UK's
two-thirds column is the standard example.

- **Fits:** articles, policies, documentation, letters, services people read under pressure, anything where
  understanding beats impression.
- **Fails:** pages whose content is mainly visual or comparative; a first screen that must show a product.
- **Poor execution:** a narrow column pinned to one side of a wide screen with nothing else; no landmarks (headings
  too weak for a heading-to-heading scan); images squeezed into the measure when they needed width.
- **Build:** the measure from type (roughly 60–75 characters), headings with information in them, figures allowed
  to break out to a wider track on named grid lines.
- **Phone:** nearly unchanged, which is one of its strengths.

### Text and artifact

A split: a short text block and the product's own artifact (the interface, the menu, the invoice line, the
map) side by side, balanced by weight, not by width.

- **Fits:** products with something real to show; services whose proof is a document or object.
- **Fails:** when the "artifact" is decoration (an abstract illustration, a stock photo); when the text is long.
- **Poor execution:** `1fr 1fr` columns regardless of weight; a floating cut-out that weighs too little; the
  artifact a fake screenshot making claims the brief doesn't make.
- **Build:** column ratio from content (`5fr 7fr`, or text at a fixed measure and the artifact taking the rest);
  align the text's first line or the artifact's top edge to a shared line; the artifact built in HTML from the
  brief's facts when possible.
- **Phone:** decide what comes first. Often the text's first line, then the artifact cropped to its most telling
  part, then the rest of the text.

### Dominant object

One large image or object takes most of the frame; small text supports it.

- **Fits:** when the object is the argument: a building, a garment, a dish, a painting, a place.
- **Fails:** when the image is generic, or the visitor's first need is a fact.
- **Poor execution:** a stock photo as the dominant object; text set on the busiest part of the image; the object
  cropped differently at each width until its subject disappears.
- **Build:** `object-position` chosen per crop; text in the image's quiet area or beside it, not on top by
  default; a caption that adds information.
- **Phone:** the object usually stays first; check the crop shows the subject.

### Index or directory

Many entry points of similar importance, ranked within: tasks, departments, stories, categories.

- **Fits:** visitors arriving with different jobs: council services, a university, a hospital, a news front page,
  a support centre.
- **Fails:** when one job dominates (then lead with it) or when the list is padding.
- **Poor execution:** every entry an identical card with an icon; no ranking, so the top task is as quiet as the
  tenth; entries labelled with internal jargon.
- **Build:** text links in a clear grid or list, the top tasks larger or first, groups by subject with space
  between groups, a search when the list is long.
- **Phone:** a list, top tasks first; avoid two-column grids of tiny cards.

### Modular catalogue

A grid of repeated items of the same kind: products, books, records, works, listings. Rhythm comes from
repetition.

- **Fits:** browsing and comparing many similar things; abundance as the message.
- **Fails:** fewer than about six items (it looks empty); items that aren't comparable.
- **Poor execution:** misaligned internals (prices at different heights); every item boxed and shadowed; no point
  of emphasis when one item genuinely matters.
- **Build:** CSS grid with `repeat(auto-fill, minmax(…, 1fr))`, `subgrid` for the internal parts, one consistent
  image ratio, separation by space and alignment rather than boxes, one spanning item for a real feature.
- **Phone:** one or two columns; denser text per item rather than smaller images.

### Mixed modules (bento)

Modules of different sizes packed into a grid.

- **Fits:** a set of items of genuinely different importance or kind that should be seen together: a portfolio
  front page, a front page mixing news and features.
- **Fails:** when the sizes are arbitrary. A bento box of equal features with random spans is now a recognisable
  AI and template pattern.
- **Poor execution:** sizes chosen to fill the grid rather than to rank; every module a rounded card with a
  gradient; a module per feature with a one-line description each.
- **Build:** decide the ranking first, then the spans; use rules or space between modules rather than cards when
  you can.
- **Phone:** it becomes a list; decide the order from the ranking, not the source order of the desktop grid.

### Ledger or table

Rows and columns of comparable attributes: prices, timetables, specifications, opening hours, plans.

- **Fits:** anything people compare or look up; precise and practical brands; where the data is the product.
- **Fails:** two items (a table is heavier than a sentence); unlike items.
- **Poor execution:** comparison data split into separate cards so the eye has to carry values between them;
  numbers in proportional figures that don't line up.
- **Build:** real `<table>` markup, tabular figures, right-aligned numbers, rules or zebra stripes only as dense as
  the data needs, the key column or row emphasised once.
- **Phone:** keep the comparison: fewer columns, a sticky first column, or rows that become labelled stacks. Don't
  drop columns people need.

### Poster sequence

Full-width modules, each composed like a poster, stacked so the scroll becomes a sequence of distinct moments.

- **Fits:** campaigns, events, festivals, launches, cultural seasons; brands with strong imagery and few words.
- **Fails:** information-heavy pages; visitors who need one fact fast.
- **Poor execution:** every module the same composition at a different colour; one sentence per full screen for
  content that needed a list.
- **Build:** vary composition between modules on purpose (pace profile), keep one grid underneath, and let each
  module's bottom edge hand off to the next.
- **Phone:** modules need recomposing, not shrinking; big type must be re-cut for the narrow frame.

### Annotated (marginalia)

A main column with notes, figures or labels hung in a margin and tied to points in the text.

- **Fits:** technical explanation, scholarly or editorial content, recipes, product pages where details annotate an
  object.
- **Fails:** when notes are decoration (tiny uppercase labels that say nothing), which is part of the "designed"
  default.
- **Poor execution:** notes not aligned to what they annotate; notes that vanish on a phone with their information.
- **Build:** grid with a named margin track; notes placed in the same row as their anchor.
- **Phone:** notes move inline after their paragraph, or behind a disclosure.

### Layered collage

Objects overlapping on a surface, as if placed by hand.

- **Fits:** physical, tactile or scrapbook identities; zines, makers, music, fashion; when the overlap says
  something about the objects (a stack, a pile, a desk).
- **Fails:** utility, data, accessibility-critical tasks; anything read under stress.
- **Poor execution:** overlaps covering text; pixel offsets that collide at other widths; collage as a style
  pasted onto a brand that isn't tactile.
- **Build:** grid stacking (shared cells, offset tracks), `isolation: isolate`, a few layers rather than many,
  text never on the bottom layer.
- **Phone:** fewer layers, larger overlaps or none.

### Workspace

The product is the layout: sidebar plus canvas, a working tool on the page.

- **Fits:** software whose interface is the proof; documentation; anything used rather than read.
- **Fails:** marketing pages pretending to be apps.
- **Build:** real interactive HTML, the same density and grid the product uses.
- **Phone:** the product's own phone layout, not a shrunken desktop.

---

## First-screen patterns

The first screen gets more attention than any other, so its composition matters most. Choose from the focal point
you ranked in SKILL.md step 2.

| Pattern | Focal point | Fits when | Watch for |
| --- | --- | --- | --- |
| Fact first | An answer: status, hours, price, the next date | The visitor's first question is factual | The fact set so small it loses to decoration |
| Artifact first | The product's real output or object | Seeing it is the proof | A fake or decorative "artifact" |
| Statement | One short line of type | The brand's claim is genuinely the point and short enough to stay big on a phone | A slogan nobody needed; five-line wraps |
| Task list | Several actions, ranked | Visitors arrive with different jobs | No ranking; icon cards |
| Object portrait | A single image or product, centred or dominant | The object is the argument | Stock imagery; text on the subject |
| Invitation | Date, place and one action | Events and bookings | Hiding the date in small print |

---

## Controlled deviations

A deviation leaves the grid on purpose to rank something. Each needs a grid to leave, a reason, and a plan for
the phone. A page rarely needs more than two kinds.

| Deviation | What it signals | Needs | Fails when |
| --- | --- | --- | --- |
| Full-bleed breakout | "This is bigger than the column": a place, an image, a pause | A clear content column it breaks out of | Every section breaks out, so the column disappears |
| Hanging into the margin | Something to find at the edge: numbers, dates, initials, punctuation | A strong text edge | The hung items carry no information |
| One spanning item | "This one matters more": the feature in a catalogue | A regular grid of peers | The span is chosen to fill a gap, not to rank |
| Crossing a section edge | Two sections belong together | A real link between them | It's used on every boundary |
| Rotation or stamp | A physical mark: approval, a date, handmade | An otherwise square page; a reason the object would be stamped | It's on several elements, or covers text |
| Scale break | One word, number or object at a scale nothing else approaches | A calm scale elsewhere | Every section has one |
| Offset image | Movement, an editorial step | Column lines it offsets to | The offset is arbitrary pixels |

---

## Pacing patterns

How intensity and density change across the page. Write the profile before building.

- **Steady:** the same density throughout. Documents, references, utilities. Predictability is the point; hierarchy
  comes from headings.
- **Front-loaded:** the answer first and strongest, then progressively quieter detail. Services and tools
  where visitors leave once they have what they came for.
- **Crescendo:** quiet opening, building toward a big moment, often the action. Launches, campaigns,
  storytelling.
- **Alternating:** loud and quiet sections in turn, so each loud one registers. Narrative marketing pages,
  portfolios. Becomes mechanical if the alternation is strict and every loud section looks the same.
- **Chapters:** distinct sections, each with its own internal composition, separated by clear changes of ground or
  space. Long pages covering several subjects.

---

## Phone translation

A phone composition is designed, not derived. For each section decide:

- **Focal point.** Is it the same as desktop? Often a fact or the product's most telling crop instead of the
  desktop's hero image.
- **Order.** What does a single column read first? If grid placement changed the visual order on desktop, check the
  source order is right for the phone.
- **Scale.** How much contrast survives? Display type usually drops more than body text; keep at least one clear
  step.
- **Space.** Section spacing drops more than component spacing, or the page becomes a scroll of gaps.
- **Groups.** Side-by-side groups become stacked; make sure each stays together and separated from its neighbour.
- **Deviations and layers.** Which stay, which go? A full-bleed image usually stays; marginalia move inline;
  overlaps shrink or vanish.
- **Tables.** Keep the comparison.

---

## Same principles, different outcomes

Three short sketches, to show how the same principles lead to different compositions when the brief changes. They
illustrate reasoning, not answers to copy.

**A regional hospice** (families of dying patients, often reading on a phone, often older, often distressed;
perception: calm, human, competent).

- Focal point: "Talk to a nurse now" with the phone number, because that's the question under stress.
- Reading column with a strong left edge; moderate scale; generous line spacing; no overlaps; a steady pace with
  space between subjects. One photograph of real staff, beside the text, never under it.
- Conventional on purpose: prototypicality and predictability help people in distress. The composition's quality
  is in its spacing, grouping and calm, not novelty.

**An independent record shop** (collectors who browse; perception: abundant, knowledgeable, a bit loud).

- Focal point: this week's arrivals as a dense catalogue, with the record of the week spanning two cells.
- Modular grid, tight gaps, small type for details, sleeves at one size so the colours do the work; a little
  overlap is allowed where sleeves stack in a "just in" crate, because records are physical objects that stack.
- Dense and alternating pace: a dense grid, a loud staff pick, a dense list of events.

**An architecture practice** (clients commissioning buildings; perception: rigorous, spatial, considered).

- Focal point: one completed building, photographed, dominant.
- Strict modular grid with few deviations, because rigour is what's being sold; large images; small, precise text
  in a ledger of project facts (location, year, area).
- The risk here is the "designed" default: vast whitespace and tiny captions. The space must be active, framing
  images the way the buildings frame space, and the facts must be legible and complete.
