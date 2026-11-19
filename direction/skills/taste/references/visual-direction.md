# Visual direction: axes, difference rule, house-style check, imagery plan

Phase 2 uses this file to make directions concrete. A direction is not a font pair plus a mood. It is a position
on six axes, each one traced to the brand's Positioning (DIRECTION.md §3) or Values (§2).

## The six axes

Every direction takes one plain, observable position on each axis. Write what a reviewer would see in a
screenshot, not a style name.

| Axis | The question it answers | Example positions (not a menu; invent from the brief) |
| --- | --- | --- |
| **1. Composition** | How is the page organised, and how dense is it? | one reading column · asymmetric two-column grid · full-bleed modules stacked like a poster series · a catalogue grid of objects · a working tool on the page, with the product as the layout |
| **2. Scale** | Where is the one big moment, and how big is it against body text? | one huge statement, everything else small · several big moments, one per section · a flat, even scale where nothing shouts |
| **3. Imagery** | What carries the visuals, and what does it show? | photography (state the subject, framing and light) · illustration · the real product interface · type used as image · a graphic pattern or map · data drawn as a picture |
| **4. Signature device** | What single recurring element could belong to this brand only? | a stamp or seal · a ruled ledger line · a timeline · a cut-out shape · a hand-drawn mark · a live status line · a recurring crop |
| **5. Colour proportion** | How much of the page does each engine colour cover, and in what role? | ground almost everywhere, figure as thin accents · figure as large solid fields alternating with ground · one colour inverted for a whole band. The colour *values* come only from find-color; the proportions are [agent] |
| **6. Surface** | What are edges, corners, depth, texture and motion like? | flat paper, square edges, no shadows · soft and rounded like an object you hold · layered cards with real depth · printed texture or grain · quick, mechanical motion |

Each cell in the direction table reads `<position> — because <P or V reference>`. Examples:
`Imagery: close photos of worn tools on the bench, raking side light — because perception "they fix things by hand"`,
`Surface: square, flat, ruled — because convention "forms read like official documents" is Adopt`. A position with no
reason is unfinished.

## The difference rule

1. Directions explored in Phase 2 differ on **at least three of the six axes**. A different adjective for the
   same thing is not a difference: "warm cream" and "soft linen" grounds are the same position.
2. Each direction's positions trace back to Positioning. At least one direction **challenges** a convention
   that Positioning marks Challenge. If Positioning marks no convention Challenge, say why in the Decisions log.
3. Directions must answer the same brief. A direction that ignores the page's one job, the audience or a value
   doesn't count toward the 2–3.
4. Write each direction's `Distinct on:` line naming the axes where it differs from the others. Fewer than
   three means merge it with a sibling or rework it.

## House-style check

In the lab's 36 skill-built pages (two opposite briefs, three models), the same look came back whatever the
brief said: Taste's own default. These are its markers:

| # | Marker | Observable as |
| --- | --- | --- |
| H1 | Type only | No photography, illustration or graphic beyond a product mock or a labelled placeholder box |
| H2 | Pale ground, one muted figure | Off-white, cream or white ground covers almost everything; one desaturated colour does the rest |
| H3 | Rules and small capitals as structure | Hairline dividers and small, letter-spaced uppercase labels carry the hierarchy |
| H4 | Square and flat everywhere | Corners at 0–4px, no shadows, no texture, no depth |
| H5 | Left headline, then a document | One big left-aligned headline, then sections of small text that read like a printed list or spec sheet |
| H6 | Flat after the hero | Below the first screen, text sizes and density barely change from section to section |

**Rule.** Count the markers for each direction (Phase 2) and again on the screenshot (Phase 5). On the
screenshot, write yes or no for each marker with what you see; a marker you hesitate over counts as yes. The
render's count is the one that decides.

- **4 or more markers = the house style.** It may be selected only when Positioning requires it. Name the
  convention marked Adopt, or the perception quality, that this look serves, and explain why a different
  position on at least two marker axes would serve the brand worse. Record this in the Decisions log as
  `House style kept because <reason>`.
- Otherwise move at least two marked axes to a position the brief supports, and record what changed.
- **At least one explored direction scores 3 or fewer**, so the choice is a real one.
- Restraint itself is fine. The fault is arriving at the same restraint for opposite briefs.

## Imagery plan

Every selected direction has an Imagery plan in Design system (§8). Imagery is a design decision, not a slot
to fill later.

1. **Job:** what the imagery must make a visitor believe. Tie it to one perception quality from §3.
2. **Kind:** photography, illustration, the real product interface, type used as image, pattern or map, data
   drawn as a picture, or none. "None" needs the same justification as the house style.
3. **Shot list (photography and illustration):** 2–5 concrete subjects, each with framing, light or treatment
   and where it sits on the page. "The mechanic's hands truing a wheel, tight crop, raking light, full-bleed after the
   prices" passes. "Workshop photo" fails.
4. **Treatment:** crop, colour treatment (using engine colours only), and how images meet the grid (full-bleed,
   inset, cut out, overlapping type).
5. **What ships now.** Without client assets, the page still carries real visuals the agent can make honestly:
   - the real product interface, built in HTML from the brief's facts;
   - SVG illustration, diagrams, maps or patterns that serve the signature device;
   - typographic compositions that use the brief's own copy as image.

   **Never ship an empty image frame.** Photography the agent can't supply stays in the shot list for the
   client to commission; the page uses only what ships now, and the layout doesn't leave holes for it.
6. **Honesty.** No stock photos posing as the business, no invented customers, products or results in images,
   no fake screenshots that make claims the brief doesn't make.
