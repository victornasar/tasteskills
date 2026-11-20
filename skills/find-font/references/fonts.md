# Curated fonts and the avoid list

Use this file to look further than the fonts you'd reach for from memory. It's a curated list of free,
self-hostable typefaces that don't read as AI-generated, plus the fonts AI-built sites overuse. It is not
ranked, and no font here is right for a kind of business. Judge every candidate with the SKILL.md process.

Facts (weights, italics, scripts, licence) were taken from the foundry's files when each font was added.
Check the source page before you depend on a specific weight, axis or glyph.

**Licences.** OFL: free to use, modify and redistribute; keep the licence file next to the fonts. FFL
(Fontshare): free commercial use and self-hosting, but the files stay out of public repos and stay unmodified,
and each designer downloads their own copy. Always self-host: never point CSS at `fonts.googleapis.com`,
`fonts.gstatic.com` or `api.fontshare.com`, which send visitor IPs to a third party (a Munich court ruled this
breaks the GDPR).

## Avoid list

Fonts AI-built sites and templates overuse. In the lab's corpus of 90 AI-built sites, Inter was on 72% of the
pages that load a web font and Fraunces on 50%; with no skill, every bakery page in the experiment used
Fraunces for headings. Using one of these is fine when the client's brand already does; otherwise treat it as
a default to look past. "Instead" names are places to start looking, not swaps.

| Font | Why it reads as a default | Instead, look at |
|---|---|---|
| Inter | The default of nearly every AI-generated UI and SaaS template. | Switzer, Public Sans, Atkinson Hyperlegible Next |
| Geist | Vercel's font; now the default look of AI-generated Next.js apps. | Supreme, Mona Sans / Hubot Sans, Overpass |
| Space Grotesk | The go-to 'techy but friendly' choice in templates. | Technor, Karrik, Overpass |
| Instrument Serif | The default 'tasteful serif' in AI landing pages. | Erode, Gambarino, Linden Hill |
| DM Sans | Ubiquitous geometric default. | Plein, Ranade |
| Plus Jakarta Sans | Ubiquitous in startup templates. | Red Hat Display / Text, Synonym |
| Manrope | Ubiquitous in startup templates. | Switzer, Ranade |
| Outfit | Ubiquitous geometric default. | League Spartan, Alpino |
| Poppins | The most overused geometric sans on the web. | Red Hat Display / Text, League Spartan |
| Montserrat | The most overused display sans on the web. | League Spartan, Panchang |
| Roboto | Android and Material default; reads as 'no decision made'. | Public Sans, IBM Plex Sans |
| Open Sans | Reads as 'no decision made'. | Source Sans 3, Plein |
| JetBrains Mono | The default mono in AI-generated code UIs. | Commit Mono, Intel One Mono, Monaspace |
| Satoshi | Fontshare's most-used font; the default of Framer-style templates. | Switzer, Supreme |
| General Sans | Heavily used in Framer-style templates. | Author, Plein |
| Clash Display | The default 'bold display' of Framer-style templates. | Panchang, League Gothic, Tanker |
| Cabinet Grotesk | Heavily used in Framer-style templates. | Synonym, Sporting Grotesque |
| Fraunces | Claude's default 'warm editorial' serif: in half of the AI-built sites that load a web font. | Erode, Gambetta, Zodiak |
| Playfair Display | The default 'elegant serif' of free templates. | Boska, Melodrama, Zodiak |
| Lato | The default 'friendly humanist sans' of free templates. | Source Sans 3, Ranade, Author |
| Raleway | The default 'stylish thin sans' of free templates. | Alpino, Synonym |
| Nunito | The default 'rounded friendly sans' of free templates. | Atkinson Hyperlegible Next, Red Hat Display / Text |
| Figtree | A ubiquitous geometric UI default. | Overpass, Public Sans |
| Oswald | The default condensed headline font. | League Gothic, Tanker, Mona Sans / Hubot Sans |
| Bebas Neue | The default condensed all-caps poster font. | League Gothic, Ostrich Sans, Tanker |
| Merriweather | The default 'readable screen serif' of free templates. | Source Serif 4, Sentient, Bespoke Serif |
| Rubik | A ubiquitous soft-cornered sans default. | Recursive, Author |
| Cormorant Garamond | Claude's default 'elegant serif': on 22% of AI-built pages that load a web font. | Linden Hill, Gambarino |
| Jost | A frequent geometric default in AI-built pages: on 17% of those that load a web font. | Supreme, Alpino |

Also worth knowing: in technical briefs, models converge on IBM Plex Sans for body text (8 of 9 pages without
skills, 6 of 9 with them). It's a good font and in the list below, but treat it as a default too.

## Sans-serif

- **Alpino** — Magazine humanist sans: small x-height, long ascenders, oldstyle figures, softly rounded corners. 100–900 (6 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Alisa Nowak (Fontshare). <https://www.fontshare.com/fonts/alpino>
  Caveat: No italics. Small x-height reads small at UI sizes.
- **Atkinson Hyperlegible Next** — Made for low-vision readers: every confusable letter (I l 1, O 0) is distinct. A humane alternative to Inter for UI. 200–800 (7 weights), variable, italics. Scripts: latin, latin-ext. OFL, by Braille Institute. <https://www.brailleinstitute.org/freefont>
- **Author** — Slightly wide humanist sans made for publications. Roomy, readable, a sans that likes books. 200–700 (6 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Satya Rajpurohit (Fontshare). <https://www.fontshare.com/fonts/author>
- **IBM Plex Sans** — Corporate-engineered grotesque with small quirks that keep it from being bland. Pairs with Plex Serif and Plex Mono. 100–700 (7 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese. OFL, by IBM. <https://github.com/IBM/plex>
  Caveat: Separate Plex families also cover Arabic, Devanagari, Hebrew, Thai, Japanese, Korean and Chinese.
- **Karrik** — Deliberately clumsy early-sans revival with uneven widths and missing optical corrections. Feels like faded road signs and ghost-town lettering. 400, italics. Scripts: latin, latin-ext. OFL, by Jean-Baptiste Morizot, Lucas Le Bihan (Velvetyne). <https://gitlab.com/phantomfoundry/karrik_fonts>
  Caveat: Single weight plus italic; best at display sizes.
- **League Spartan** — Bold geometric in the Futura tradition; the heaviest weights are the reason to use it. 100–900 (9 weights), variable, no italics. Scripts: latin, latin-ext, vietnamese. OFL, by The League of Moveable Type / Tyler Finck. <https://github.com/theleagueof/league-spartan>
  Caveat: No italics.
- **Mona Sans / Hubot Sans** — GitHub's variable grotesque with a width axis, so one family covers condensed headlines and normal UI. Hubot Sans is its squarer, more mechanical sibling. 200–900 (8 weights), variable, italics. Scripts: latin, latin-ext, vietnamese. OFL, by GitHub. <https://github.com/github/mona-sans>
  Caveat: Strongly associated with GitHub; avoid for developer-tool brands that shouldn't look like GitHub.
- **Overpass** — Based on US highway signage (Highway Gothic): open, legible, a little civic. Has a matching mono. 100–900 (9 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by Red Hat / Delve Fonts. <https://github.com/RedHatOfficial/Overpass>
- **Plein** — Monolinear humanist sans with open, pleasant forms. An alternative to DM Sans. 300–900 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Inga Plönnigs (Fontshare). <https://www.fontshare.com/fonts/plein>
- **Public Sans** — The U.S. government's plain, dependable grotesque. An alternative to Inter or Roboto with less baggage. 100–900 (9 weights), variable, italics. Scripts: latin, latin-ext, vietnamese. OFL, by U.S. Web Design System. <https://github.com/uswds/public-sans>
- **Ranade** — Neo-grotesque with high-contrast diagonals, a little kick that sets it apart from Helvetica clones. 100–700 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Easha Ranade (Fontshare). <https://www.fontshare.com/fonts/ranade>
- **Red Hat Display / Text** — Friendly geometric-humanist pair: Display for big sizes, Text for small. An alternative to Poppins or Montserrat. 300–900 (7 weights), variable, italics. Scripts: latin, latin-ext. OFL, by Red Hat / MCKL. <https://github.com/RedHatOfficial/RedHatFont>
  Caveat: Red Hat Text stops at 700; 800 and 900 are Display only.
- **Source Sans 3** — Adobe's calm humanist workhorse with wide language support. An alternative to Open Sans. 200–900 (8 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese. OFL, by Adobe. <https://github.com/adobe-fonts/source-sans>
- **Sporting Grotesque** — Wide, slightly old-fashioned grotesque with sporty swagger and calligraphic quirks (droopy r, wedge cuts, closed apertures). Feels like a vintage club badge. 400–700, no italics. Scripts: latin, greek. OFL, by Lucas Le Bihan (Velvetyne). <https://gitlab.com/velvetyne/Sporting-Grotesque>
  Caveat: Two weights only, no italics. Not for long reading. Missing Õ Š Ž.
- **Supreme** — Straight-sided, monolinear engineer's grotesque. An alternative to Space Grotesk without the trend. 100–800 (7 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jérémie Hornus (Fontshare). <https://www.fontshare.com/fonts/supreme>
  Caveat: Italics are obliques (slanted uprights).
- **Switzer** — Classic neo-grotesque with 9 weights and true italics. The quieter, less-seen alternative to Inter and Satoshi. 100–900 (9 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jérémie Hornus (Fontshare). <https://www.fontshare.com/fonts/switzer>
- **Synonym** — Humanist sans with visible stroke contrast; personality without losing legibility. Made for branding and editorial. 200–700 (6 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Hugo Dumont (Fontshare). <https://www.fontshare.com/fonts/synonym>
  Caveat: No italics, so weak for long body text with emphasis.
- **Technor** — Constructed sans with flat sides and rounded tops. Sci-fi and industrial without being a cliché. 200–900 (7 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jean-Baptiste Morizot (Fontshare). <https://www.fontshare.com/fonts/technor>

## Serif

- **Avara** — A curveless serif: every curve drawn as straight segments. Classic silhouette, faceted up close. 700–900, italics. Scripts: latin. OFL, by Raphaël Bastide et al. (Velvetyne). <https://gitlab.com/velvetyne/Avara>
  Caveat: Bold and Black only; italic only for Bold. Missing ß Ø Ł Š Ž.
- **Bagnard** — Based on graffiti carved by a Napoleonic-era prisoner: rough, heavy, unusual serif with real character. 400, no italics. Scripts: latin. OFL, by Sébastien Sanfilippo. <https://github.com/sebsan/Bagnard>
  Caveat: Single style. Display only. Small character set: missing ß Ø Ł Š Ž and # % * + = [ ] { }.
- **Bespoke Serif** — Wedge-serif text face with big open counters, designed for reading. 300–800 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jérémie Hornus (Fontshare). <https://www.fontshare.com/fonts/bespoke-serif>
- **Boska** — High-contrast Didone with a pointed-pen flourish. Fashion-magazine elegance. An alternative to Playfair Display. 200–900 (6 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Barbara Bigosinska (Fontshare). <https://www.fontshare.com/fonts/boska>
  Caveat: Hairlines break up at small sizes; headlines only.
- **Cormorant** — Delicate Garamond-style display serif with long, sharp details. Luxurious at large sizes. 300–700 (5 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by Christian Thalmann. <https://github.com/CatharsisFonts/Cormorant>
  Caveat: Too thin for body text on screens; pair it with a sturdier body face. A sibling of Cormorant Garamond, which AI-built sites overuse, so the two read alike: don't offer it as a replacement for an overused serif.
- **Erode** — Contrasty serif with long ascenders and open counters. Made for pull quotes and eye-catching headlines. 300–700 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Nikhil Ranganathan (Fontshare). <https://www.fontshare.com/fonts/erode>
- **Gambarino** — Condensed post-modern Garalde for headlines. Pair it with a quieter text serif or sans. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Théo Guillard (Fontshare). <https://www.fontshare.com/fonts/gambarino>
  Caveat: Single weight, display only.
- **Gambetta** — Text serif with diagonal stress and contrast that grows with weight. Newspaper-grade reading. 300–700 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Paul Troppmair (Fontshare). <https://www.fontshare.com/fonts/gambetta>
- **Happy Times at the IKOB** — A cheeky contemporary riff on Times New Roman with odd, joyful details, made for a museum identity. Times, but it smiles. 400–700, italics. Scripts: latin. OFL, by Lucas Le Bihan (Velvetyne). <https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB>
  Caveat: Regular, Bold and Italic only; no bold italic. Western European accents only: missing Ł Š Ž.
- **Hoover** — Monolinear slab with no curves at all. Pure American collegiate and varsity-jacket lettering. 100–700 (5 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Gaetan Baehr (Fontshare). <https://www.fontshare.com/fonts/hoover>
- **IBM Plex Serif** — A serif with an engineer's precision; pairs naturally with Plex Sans and Plex Mono. 100–700 (7 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by IBM. <https://github.com/IBM/plex>
- **Junicode** — Scholar's old-style serif with massive medieval and linguistic coverage. Old-world without being a costume, but clearly academic in flavour. 300–700 (5 weights), variable, italics. Scripts: latin, latin-ext, greek, vietnamese. OFL, by Peter S. Baker. <https://github.com/psb1558/Junicode-font>
  Caveat: Variable axes: weight, width and Enlarge. Wide default line spacing. Very large character set; subset it for the web.
- **Libertinus** — Classic old-style book face with huge language coverage and a math companion. For essays, papers, long reads. 400–700 (3 weights), italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese, hebrew. OFL, by Khaled Hosny, Caleb Maclennan. <https://github.com/alerque/libertinus>
- **Linden Hill** — A revival of Goudy's Deepdene: graceful, slightly calligraphic old-style serif. 400, italics. Scripts: latin, latin-ext. OFL, by Barry Schwartz (The League of Moveable Type). <https://github.com/theleagueof/linden-hill>
  Caveat: Regular and italic only; no bold.
- **Recia** — Low-contrast, slightly condensed contemporary serif with true cursive italics. A serif that works on screens. 300–700 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Carlos de Toro (Fontshare). <https://www.fontshare.com/fonts/recia>
- **Sentient** — Slightly wide, robust serif for immersive long reading. Holds up at small sizes. 200–700 (5 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Noopur Choksi (Fontshare). <https://www.fontshare.com/fonts/sentient>
- **Sorts Mill Goudy** — A revival of Goudy Oldstyle: warm, bookish, early-20th-century American printing. 400, italics. Scripts: latin, latin-ext. OFL, by Barry Schwartz (The League of Moveable Type). <https://github.com/theleagueof/sorts-mill-goudy>
  Caveat: Regular and italic only; no bold.
- **Source Serif 4** — Sturdy transitional serif with an optical-size axis, so it looks right from captions to headlines. 200–900 (8 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese. OFL, by Adobe. <https://github.com/adobe-fonts/source-serif>
- **Trench Slab** — Slab serif with big, prominent ink traps that become a visible style at large sizes. 300–700 (5 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Shiva Nallaperumal (Fontshare). <https://www.fontshare.com/fonts/trench-slab>
  Caveat: Made for larger-than-reading sizes.
- **Zodiak** — Sturdy Century-style serif. Middle weights set text; the extreme thin and black weights make great display pairs. 100–900 (6 weights), variable, italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jérémie Hornus (Fontshare). <https://www.fontshare.com/fonts/zodiak>

## Display

- **Aktura** — Modern blackletter with ornate Lombardic capitals. Newspaper nameplate, diploma or metal band. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Gaetan Baehr (Fontshare). <https://www.fontshare.com/fonts/aktura>
  Caveat: Single weight. Don't set all caps, the capitals are ornate.
- **Basteleur** — Medieval-meets-Cooper-Black serif designed with the Tarot de Marseille in mind. Soft Bold and sharper Moonlight. Strong personality for covers and posters. 300–700, no italics. Scripts: latin, latin-ext, greek. OFL, by Keussel (Velvetyne). <https://gitlab.com/velvetyne/basteleur>
  Caveat: Two weights only. Display-oriented; not for long reading.
- **Knewave** — Bold brush script with skate and surf energy. 400, no italics. Scripts: latin. OFL, by Tyler Finck (The League of Moveable Type). <https://github.com/theleagueof/knewave>
  Caveat: Single weight.
- **Kola** — Rounded techno stencil sans, a bit like LED signage. Large x-height keeps it readable. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Jean-Baptiste Morizot (Fontshare). <https://www.fontshare.com/fonts/kola>
  Caveat: Single weight.
- **Le Murmure** — Tall, narrow display face with alternate letters. Made for a Paris agency; fashion-poster attitude. 400, no italics. Scripts: latin, latin-ext, cyrillic, greek. OFL, by Jérémy Landes (Velvetyne). <https://gitlab.com/velvetyne/murmure>
  Caveat: Single weight.
- **League Gothic** — Tall condensed gothic (an Alternate Gothic revival) with a width axis. Classic newspaper and poster shout. An alternative to Bebas Neue and Oswald. 400, variable, no italics. Scripts: latin, latin-ext, vietnamese. OFL, by The League of Moveable Type. <https://github.com/theleagueof/league-gothic>
  Caveat: One weight; the variable axis is width, not weight.
- **Melodrama** — Sans with extreme contrast that grows with weight. Glamorous and theatrical. 300–700 (5 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Shaily Patel (Fontshare). <https://www.fontshare.com/fonts/melodrama>
  Caveat: Thin strokes vanish at small sizes.
- **Ostrich Sans** — Ultra-condensed caps with rounded, inline and dashed variants. Fun, tall and skinny. 300–900 (4 weights), no italics. Scripts: latin. OFL, by Tyler Finck (The League of Moveable Type). <https://github.com/theleagueof/ostrich-sans>
  Caveat: Mostly caps-only. Display only.
- **Ouroboros** — Art-nouveau-ish display face with alchemical and astronomical symbols. Made for the weird and the occult. 400, no italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by Ariel Martín Pérez (Velvetyne). <https://gitlab.com/velvetyne/ouroboros>
  Caveat: Highly decorative. Single weight. Best at large sizes; not for body text.
- **Panchang** — Ultra-wide, almost panoramic sans. Industrial and very confident. 200–800 (7 weights), variable, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Barbara Bigosinska (Fontshare). <https://www.fontshare.com/fonts/panchang>
  Caveat: Takes a lot of horizontal space; short words only.
- **Segment** — LCD-style letters built from segments. Digital clocks, transit boards, calculators. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Frode Helland (Fontshare). <https://www.fontshare.com/fonts/segment>
  Caveat: Single weight.
- **Tanker** — Condensed caps-only sans: the lowercase keys type classic caps and the uppercase keys type dynamic, experimental ones. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Ruosi Huang (Fontshare). <https://www.fontshare.com/fonts/tanker>
  Caveat: Uppercase only. Single weight.
- **Terminal Grotesque** — Rough pixel grotesque, cyberpunk zine energy. 400, no italics. Scripts: latin. OFL, by Jérémy Landes (Studio Triple / Velvetyne). <https://github.com/StudioTriple/Terminal-Grotesque>
  Caveat: Single weight, plus an 'Open' variant. Missing Ł Š Ž Œ.
- **Zina** — Stately inline Didone with ball terminals. Early-1800s grandeur. 400, no italics. Scripts: latin, latin-ext. FFL (Fontshare), by Théo Guillard (Fontshare). <https://www.fontshare.com/fonts/zina>
  Caveat: Single weight. Large sizes only, the inline disappears small.

## Monospace

- **Commit Mono** — Neutral, anonymous coding font with smart kerning. Configurable on the site before download. An alternative to JetBrains Mono. 200–700 (6 weights), italics. Scripts: latin, latin-ext, greek. OFL, by Eigil Nikolajsen. <https://commitmono.com>
- **Departure Mono** — Monospaced pixel font with a lo-fi techy vibe. Strong for code, terminals, retro interfaces and sci-fi moments. 400, no italics. Scripts: latin, latin-ext, cyrillic, greek. OFL, by Helena Zhang. <https://departuremono.com>
  Caveat: Pixel font: size in increments of 11px for crisp rendering. Single weight.
- **iA Writer Mono / Duo / Quattro** — Plex Mono reworked for writing. Duo and Quattro are duospace and quattrospace, so prose reads more naturally than in a true mono. 400–700, variable, italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by iA. <https://github.com/iaolo/iA-Fonts>
- **IBM Plex Mono** — Mono with a slightly humanist italic. Works for code and for tech-flavoured UI labels. 100–700 (7 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, vietnamese. OFL, by IBM. <https://github.com/IBM/plex>
- **Intel One Mono** — Coding font designed with and for low-vision developers. Clear, open and calm. 300–700 (4 weights), variable, italics. Scripts: latin, latin-ext, vietnamese. OFL, by Intel / Frere-Jones Type. <https://github.com/intel/intel-one-mono>
- **Iosevka** — Narrow, highly configurable coding font. Fits lots of columns; build your own variant. 100–900 (9 weights), italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese. OFL, by Belleve Invis. <https://github.com/be5invis/Iosevka>
  Caveat: Huge download; pick a prebuilt web package or a custom build.
- **Monaspace** — Five metric-compatible monos (Neon, Argon, Xenon, Radon, Krypton) you can mix in one editor, e.g. a handwriting-style mono for comments. 200–800 (7 weights), variable, italics. Scripts: latin, latin-ext. OFL, by GitHub Next. <https://github.com/githubnext/monaspace>
- **Recursive** — One variable font that slides from sans to mono and from linear to casual brush. Great for friendly dev brands. 300–900 (7 weights), variable, italics. Scripts: latin, latin-ext, vietnamese. OFL, by Arrow Type. <https://github.com/arrowtype/recursive>
  Caveat: Italics come from the slant and cursive axes, not separate files.
- **Sligoil** — Funky monospace with large inktraps. Made for a game interface; carries whiskey-sign and Space Cadet keyboard DNA. Includes upright italic forms. 400–700 (3 weights), variable, no italics. Scripts: latin, latin-ext, vietnamese. OFL, by Ariel Martín Pérez (Velvetyne). <https://gitlab.com/velvetyne/sligoil>
  Caveat: Styles are named Micro, Micro Medium and Micro Bold.
- **Steps Mono** — Clean collaborative monospace made for the magazine étapes:. More restrained than most Velvetyne monos. 100–400, no italics. Scripts: latin. OFL, by Jean-Baptiste Morizot, Raphaël Bastide (Velvetyne). <https://github.com/raphaelbastide/steps-mono>
  Caveat: Not usable for code: the files have no = @ [ ] { | } ~ (Thin also lacks &). Few accents: no ä ö ü ß ñ. Two weights only.
- **Victor Mono** — Narrow mono with a cursive italic. Comments and keywords look handwritten. 100–700 (7 weights), variable, italics. Scripts: latin, latin-ext, cyrillic, greek, vietnamese. OFL, by Rune Bjørnerås. <https://rubjo.github.io/victor-mono>
