# Methodology

**Protocol:** `industry-type/2` · **Selection date:** 2026-11-18 · **Status: Frozen 2026-11-19** (list approved
2026-11-19; `proposed-sites.json` SHA-256 `60f81c18341fde24474cadece27744630e8483788da315233b4ec6eb3b1cdfc1`). The list, the industry scopes in §1 and the rated
subset in §9 are fixed. Changes after freezing are logged under [Protocol changes](#protocol-changes) with a date
and reason, and none may narrow a category or replace a site because a result looks inconvenient.

> This file is generated: edit `methodology.head.md` and run `python3 lab/industry-type/write_methodology.py`,
> which appends §5 and the source-composition table from `proposed-sites.json`.

## 1. Industry definitions

A company belongs to the first industry below (in this order) whose pool contains its domain.

| Id | Definition |
|---|---|
| `dev-tools` | Software whose users are developers or engineering, product and design teams |
| `fintech` | Financial services delivered as technology products: payments, banking, brokerage, lending, insurance, crypto. Traditional financial institutions don't qualify on their own (criterion F) |
| `health` | The healthcare ecosystem, not only providers: providers, payers (health insurers), healthcare technology, health information and accreditation bodies (scope M). Fitness and outdoor apps are consumer apps |
| `luxury-fashion` | High-end fashion houses and luxury goods brands |
| `food-hospitality` | Operators serving guests food, drink or short-stay lodging: restaurants and chains, hotels and chains, inns, hospitality groups (criterion H) |
| `editorial-media` | Publications with their own website, in five strata (§2) |
| `architecture-design` | Practices whose main output is client-commissioned architecture, engineering or design services (criterion A) |
| `consumer-apps` | Consumer software and software-delivered consumer services (delivery platforms included) not in an industry above; games and physical-goods commerce excluded (criterion C) |

### Inclusion criteria for the boundary cases

Each criterion is applied to every candidate the selector reaches, not only to the case that raised it. A struck
site is replaced by the next site under the same rule (§3).

**A. Architecture & design: client-commissioned services, not an artist's own work or a product.** The industry
studies how practices that sell architecture or design to clients present themselves. A studio centred on one
artist's own works (Studio Olafur Eliasson, Studio Roosegaarde) sells art, not commissioned design; a design
company whose main output is its own software (iA, whose site leads with iA Writer) sells a product. Both are out.
Engineering and engineering-led design practices doing commissioned work count (Arup, HDR, Simpson Gumpertz &
Heger). Multidisciplinary practices stay in when commissioned work is their main output: Snøhetta (architecture,
landscape, interiors), ART+COM (commissioned media installations), Duarte and PPT-Design (presentation design for
clients). Earlier strikes on the same grounds: type foundries (P22, Hoefler & Co.), design software (Design.com,
Visme, BioRender), a marketplace (DesignCrowd), media platforms (DAAily).

**H. Food & hospitality: guests, not tenants.** The industry covers operators that serve guests food, drink or
short-stay lodging. Co-living (Stanza Living) is long-term residential rental, which is real estate. The same line
excludes theme parks (Six Flags), lodging marketplaces that don't operate the stay (Airbnb), delivery platforms
and recipe apps (App Store Food & Drink chart dropped as a source), and suppliers to hotels (IXIA). Hotels, inns
with restaurants (Post Ranch Inn), restaurant groups and brewpub-hotel groups (McMenamins) stay in.

**F. Fintech: an independent fintech classification, or digital-native founding.** Traditional banks, brokerages,
insurers and credit bureaus are their own category, and a brief saying "fintech" means technology-led finance. A
candidate counts as fintech when a fintech-specific source lists it (YC's Fintech subindustry or Wikidata's
industry = fintech). A company found only in the App Store Finance chart must have been founded in 2000 or later;
founding years are recorded with a source in `founded.json`, only when the Wikidata entry's official website or
the Wikipedia infobox's website matches the domain. So Charles Schwab (1971), Fidelity (1946), Citibank, Ally,
GEICO, Progressive, Equifax, Experian and LPL are out, while Robinhood (2013), Credit Karma (2007), Acorns (2012)
and Cash App (2013) are in. Kaspi.kz stays: it began as a bank in 1991, but Wikidata classifies it as fintech, and
that independent classification is the test, not the founding year.

**M. Health: the healthcare ecosystem.** The industry is how organizations in healthcare present themselves, so
it is broader than care delivery: providers (hospitals, clinics, dental groups, labs), payers (health insurers),
healthcare technology (Doctolib, Qventus), health information publishers (Drugs.com) and accreditation and
standards bodies (the Joint Commission) all count, and so do pharmacy chains (CVS). Fitness and outdoor apps
are consumer apps.

**C. Consumer apps: software and software-delivered services, not commerce.** Retailers and marketplaces whose
main product is physical goods are commerce, a different industry. Amazon is out, and the App Store Shopping genre
is no longer drawn into consumer apps. Services delivered through software stay in: streaming (Spotify, Peacock),
messaging (WhatsApp, Discord), travel booking (Suiteness), and delivery platforms (DoorDash): the platform sells
a software-delivered service, not goods of its own. (Delivery platforms left food & hospitality as a source in
protocol 2, not as members of consumer apps.) Earlier strike on the same line: a coffee chain (7 Brew).

## 2. Discovery sources and their bias

Each industry unions several sources, so no single directory defines its population. Pool sizes, eligibility
counts and how many chosen sites came from each source are in the [composition table](#source-composition).

| Source | What it is | Used for | Bias [A] |
|---|---|---|---|
| **YC directory** (`yc-oss.github.io` mirror) | Every Y Combinator company with subindustries; Active or Public only | dev tools, fintech, health, consumer apps | Young, venture-backed, US-heavy startups |
| **Wikidata** (SPARQL, classes listed in `pick_sites.py`) | Organizations with an official website and no dissolution date. Developers of programming tools must be a business, company, enterprise or software company | all but consumer apps | Established, notable, Europe-heavy; well-documented companies over small ones |
| **Apple App Store charts** (US, top free + top paid, 100 each per genre; developer site from the iTunes lookup API) | What US consumers actually download | dev tools (Developer Tools), fintech (Finance), health (Medical), consumer apps (overall charts minus Developer Tools, Finance, Medical, News, Magazines & Newspapers, Games and Shopping) | Consumer-facing, app-first, US market, one week's charts |
| **Altagamma members** (Italian luxury association) | Member brands linked from its members page | luxury & fashion | Italian, includes non-fashion luxury (wine, furniture, yachts) |
| **Michelin Guide** (`ngshiheng/michelin-my-maps` dataset, guide restaurants with a website) | Restaurants selected by Michelin inspectors | food & hospitality | Fine dining; independent single restaurants over chains |
| **Wikipedia lists** (*List of architecture firms*, *List of magazines by circulation*, *List of newspapers by circulation*; each link resolved to Wikidata and kept only if its class fits) | Editor-curated lists, separate from Wikidata's class statements | architecture & design, editorial magazines | English-Wikipedia notability; large and historic firms |
| **Tranco `V38GN`** | Frozen research top-1M domain ranking | eligibility and leader rank everywhere | Traffic favors big consumer brands; a site outside the top 1M can't be chosen |

Industries without an App Store source (luxury, food & hospitality, architecture) rely on directories only; the finding states this.

### Editorial strata

Editorial is split into five strata so local newspapers can't dominate. Each stratum has its own pool, its own
leader (best Tranco rank) and two seeded samples: 5 leaders + 10 sampled overall.

| Stratum | Pool |
|---|---|
| National | Wikidata: *national newspaper* (Q11389521); Wikipedia *List of newspapers by circulation* |
| Digital-native | Wikidata: *online newspaper* (Q1153191), *news website* (Q17232649) |
| Magazines | Wikidata: *magazine* (Q41298) with a listed publisher or owner; Wikipedia *List of magazines by circulation* |
| Business | Wikidata: *business periodical* (Q2586014), *business newspaper* (Q106651372) |
| Independent | Wikidata: *magazine* or *online magazine* (Q847906) with **no** listed publisher or owner |

"Independent" is a rule, not a judgement: no publisher (P123) or owner (P127) on Wikidata. Missing data can put
an owned title here; the finding states this.

## 3. Strata: leaders and sampled sites

Leaders and sampled sites are **separate strata** and are reported separately in every finding.

- **Leaders:** the eligible sites with the best Tranco rank that pass the pre-check (5 per industry; 1 per
  editorial stratum). Traffic rank, not reputation.
- **Sampled:** 10 per industry (2 per editorial stratum), drawn source-balanced: each source's eligible sites are
  ordered by `sha256("20261118-<industry>-<stratum>-<source>-<domain>")`, then sources take turns in the order
  listed in `pick_sites.py`, each turn adding its next site that passes the pre-check and isn't already chosen.
  A big source can't crowd out a small one. Because each domain's position is fixed, striking or adding one
  candidate never reorders the others: a replacement is exactly the next site in that order.

**Seed: `20261118`.** `python3 lab/industry-type/pick_sites.py --offline` on the archived sources reproduces
the list, except where a site's liveness changed.

## 4. Eligibility and exclusions

Applied at selection only, before freezing. Every exclusion is recorded with its reason in `proposed-sites.json`.

| Rule | Why |
|---|---|
| Domain not in Tranco `V38GN` | Keeps the pool to sites with measurable traffic; counted, not listed (tens of thousands) |
| Listed site is a page or subdomain, not its own domain's homepage | A company page on GitHub, Facebook, Etsy or a university site would inherit that platform's rank |
| Domain listed by more than one organization within one kind of source | A shared domain is a platform, not one brand's site. The same company found in two kinds of source counts once |
| Struck for this industry in `strikes.json` | The organization's main business is outside §1's definition. Replacement is the next site by the same rule, never hand-picked |
| Domain already in an earlier industry or stratum | One domain, one place |
| Homepage unreachable three times, 30 s apart (`curl`, hard 20 s limit) | Can't be measured. One failure isn't enough: a single timeout once dropped kaspi.kz. Reachable means a 200, or a 401/403 from bot protection; those are flagged `precheck_blocked` and verified in Chrome at measurement, where a block is recorded as a failure, not replaced |
| Homepage redirects to another registrable domain | Not the company's own brand site |
| Parking or for-sale page | Not a brand site |

**No site is excluded for its language or writing system.** The pre-check records each homepage's `lang` and
the writing systems in its text (any script with at least 5% of letters). This is read from the server's HTML, so
it misses text a page renders with JavaScript (cankaoxiaoxi.com and incrussia.ru show as Latin here); it is a
selection-time hint only, and the measurement records the scripts of the rendered glyphs. The measurement then separates a
deliberate typeface from script fallback (§7).

**After freezing,** a site that fails to load, blocks automated browsers or shows only a consent wall is recorded
as a failure with its reason. It is never replaced, and an easier-to-measure site is never substituted. This
matters most for the 22 sites flagged `precheck_blocked`: each is opened in real Chrome, and if Chrome is blocked
too, the failure is recorded and the site stays in the frozen list and in every denominator.

## 5. Final URLs

The list is [below](#5-proposed-sites) and in `proposed-sites.json`. **Approved and frozen 2026-11-19.**
The audit trail: `proposed-sites.v1.json` (protocol 1's proposal, kept unchanged), `strikes.json` (every category
strike with reason and who asked), and [§5's change log](#changes-from-the-first-proposal) listing every
protocol-1 site and what happened to it.

## 6. Raw source archive

The cached sources (74 MB) stay out of git, and the working cache was deleted once the archive was built. Each was audited for its license or terms (`archive.py`, recorded per
file with SHA-256, terms and retrieval details in `archive-manifest.json`) and goes to one of three places:

| Where | What |
|---|---|
| **Deposit archive** (`industry-type-deposit-2026-11-19.tar.gz`, kept with the private copy, not distributed) | Wikidata query results (CC0); Wikipedia-list files (Wikidata data, CC0, list membership attributed to English Wikipedia, CC BY-SA 4.0); selection outputs (`proposed-sites.json`, `proposed-sites.v1.json`, `strikes.json`, `founded.json`, `prechecks.json`, `rated-subset.json`, `pick_sites.py`, `draw_ratings.py`, `methodology.md`); factual extracts of every withheld source |
| **Private copy, not distributed** (outside the repository, read-only, with `SHA256SUMS`) | The Tranco list `V38GN` (published for research download; also re-downloadable by id), `PROVENANCE.md` with each withheld source's URL, retrieval time, query parameters and checksum, and the deposit archive |
| **Checksum, provenance and extract only** | YC directory mirror (no license, so no grant to retain a copy); App Store API responses (Apple's terms, developers' descriptions); Altagamma page (copyright); Michelin dataset (MIT repo, but the rows are Michelin's text) |

The extracts hold only facts (identifiers, names, URLs, status, categories, genre ids) and every field the selector
reads. `archive.py` checks, before writing anything, that each extract gives the selector exactly the entries the
raw file gives, so the deposit plus the Tranco list rebuild every candidate pool and this list. The archive was
first meant for a restricted Zenodo deposit; that was dropped (see Protocol changes), so its own `MANIFEST.json`
and its copy of this file still name Zenodo.

## 7. Measurement protocol (applies after freezing)

Rendered in Google Chrome via Playwright (`../tools/detect.mjs`, extended), at 1440×900, main document only:
iframes, shadow roots of known third-party widgets (chat, cookie consent, embeds) and elements hidden from view
are skipped.

| Role | Rule |
|---|---|
| Headline | The largest text in the first screen, excluding decorative oversized text, logos and navigation |
| Body | The font with the most characters across `p` and `li` in the main content, excluding footer, navigation and hidden text |
| UI | The dominant font across `nav`, `button`, `label` and form controls, excluding the main content where possible |
| Code | `pre`, `code`, `kbd` |

Each role records: declared/computed `font-family`; whether a web font for it loaded (`document.fonts`); the fonts
that actually rendered its glyphs, with glyph counts (CDP `CSS.getPlatformFontsForNode`); whether that is a system
fallback; and the **writing system of the glyphs** in that role. The **rendered** font is the unit counted.

Fallback is classified, not assumed: **deliberate** (the rendered font is one the page declares), **script
fallback** (the declared font lacks the script and the browser substituted a system font), **load failure**
(the declared web font didn't load), or **system by choice** (the page declares only system or generic stacks). A
missing role is recorded as *absent*. [I] The exact tests for "decorative", "logo" and "main content" are fixed in
code and calibrated on fixture pages before the real run.

Each family is classified **custom** (owned by the company), **commercial** (licensed retail), **OFL / open**, or
**system**, from a hand-kept lookup with a source per entry. Findings stay per role and per stratum.

Each real site keeps a dated font record and screenshots (full page and first screen). Pages themselves are not
saved.

## 8. AI corpus

The same 8 industries, with no skills and no personal settings (same setup as `../corpus/generate.py`). Models:
`claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`; 3 runs each: 72 pages. One template for every
industry; only the industry name changes, and it is the §1 name verbatim, with no adjective about look or type:

> Build the homepage for a company in the {industry} industry. Reply with the complete page as a single HTML
> file in one code block, nothing else.

| Id | {industry} |
|---|---|
| `dev-tools` | developer tools |
| `fintech` | fintech |
| `health` | healthcare |
| `luxury-fashion` | luxury fashion |
| `food-hospitality` | food and hospitality |
| `editorial-media` | editorial media |
| `architecture-design` | architecture and design |
| `consumer-apps` | consumer apps |

Every run saves its exact prompt, model id, CLI version, date and the raw reply in a `meta.json` beside the page,
as `../run.py` does. Each page records how its type was set: **explicitly chosen** (it loads or self-hosts a
named web font), **inherited** (only generic or system stacks), or **external** (fonts arrive from a third-party
embed). Pages that choose nothing are counted in their own row.

## 9. Human-rated subset

Drawn when the list is frozen, before any measurement, with `random.Random("20261118-ratings")`: 4 of the 8
industries, then 5 real sites (keeping the leader/sampled split proportional) and 5 AI pages within each. The
draw is written into this file at freezing.

Procedure (`draw_ratings.py`, output `rated-subset.json`): one generator, used in this order. (1) Sample 4
industries from the §1 ids in §1 order. (2) For each drawn industry in §1 order: sample 2 leaders from its leaders
sorted by domain, then 3 sampled sites from its sampled sites sorted by domain (5 × 5/15 ≈ 1.7 leaders, rounded to
2), then 5 AI pages from its 9 (model, run) slots in §8's model order, runs 1–3. The AI slots are drawn before the
pages exist, so the draw can't see them. A drawn site that fails measurement stays drawn and is rated as a
failure screenshot or reported missing; it is not redrawn.

**Drawn '20261118-ratings'** (industries in draw order: dev-tools, health, food-hospitality, fintech):

| Industry | Leaders | Sampled | AI pages (model/run) |
|---|---|---|---|
| `dev-tools` | fontawesome.com, sendbird.com | railway.com, firegiant.com, decentro.tech | claude-haiku-5-5/run1, claude-haiku-5-5/run3, claude-sonnet-5-5/run2, claude-sonnet-5-5/run1, claude-opus-5-5/run1 |
| `fintech` | coinbase.com, paypal.com | grantcash.com, hepster.com, truelinkfinancial.com | claude-opus-5-5/run3, claude-sonnet-5-5/run3, claude-haiku-5-5/run3, claude-opus-5-5/run2, claude-sonnet-5-5/run2 |
| `health` | cvs.com, doctolib.fr | nyp.org, aspendental.com, jointcommission.org | claude-haiku-5-5/run2, claude-sonnet-5-5/run3, claude-sonnet-5-5/run1, claude-haiku-5-5/run3, claude-opus-5-5/run2 |
| `food-hospitality` | chipotle.com, jerseymikes.com | apahotel.com, mcmenamins.com, swiss-belhotel.com | claude-opus-5-5/run1, claude-opus-5-5/run2, claude-sonnet-5-5/run3, claude-sonnet-5-5/run1, claude-opus-5-5/run3 |

## 10. Reproducibility record

Stored with the findings: protocol version, seed, Tranco id, source archive location and checksums, model ids,
exact prompts, Chrome and Playwright versions, measurement dates.

## Protocol changes

After freezing (2026-11-19, nothing measured):

- **No Zenodo deposit.** The deposit archive stays with the private copy (§6) instead of going to Zenodo with
  restricted access. Its contents and checksum are unchanged; only where it is held changed. No site changed.

At freezing (2026-11-19, nothing measured):

- **Scope statements, on approval:** Health is the healthcare ecosystem (scope M: providers, payers, health
  technology, health information, accreditation), so Drugs.com and the Joint Commission are members, not borderline.
  Architecture & design states engineering practices explicitly (Arup, HDR, Simpson Gumpertz & Heger). Consumer
  apps states delivery platforms explicitly (DoorDash). No site changed.
- List frozen; rated subset drawn (§9). Archive split into deposit, private copy and checksum-only (§6), with a
  check that the deposited extracts reproduce the selection.

Before freezing (selection only, nothing measured):

- **2026-11-18 (protocol 1):** the first proposal ranked platform domains as leaders (github.com for a fintech's
  GitHub page, facebook.com for a restaurant, google.com for a magazine). Added "listed site is its own domain's
  homepage" and "domain listed by one organization only", re-ran the same seed on the same sources.
- **2026-11-18 (protocol 2), on review of protocol 1's list:**
  - Category strikes for Y Combinator, Angle Health, Six Flags, Pull&Bear, Design.com, Visme and BioRender
    (requested), and Fatboy and P22 Type Foundry (reviewed on request, then struck). See `strikes.json`.
  - Added independent sources (App Store charts, Altagamma, Michelin, Wikipedia lists) and source-balanced
    sampling; leaders and sampled sites kept as separate strata.
  - Removed the non-Latin-script exclusion; writing systems are recorded and fallback is measured.
  - Editorial split into five strata. The *national newspaper* class alone held one entry, so the national
    stratum also takes Wikipedia's newspaper circulation list. (A Wikidata query for newspapers covering a whole
    country was tried and dropped: it timed out on Wikidata's servers every time.)
  - AI prompts reduced to one template that changes only the industry name.
  - Classification questions on review (2026-11-18): inclusion criteria A, H, F and C written into §1 and applied
    to every candidate. Strikes: Studio Olafur Eliasson, Studio Roosegaarde, iA, Stanza Living. Schwab and
    Fidelity leave fintech under criterion F; Amazon leaves consumer apps under criterion C (Shopping genre).
  - Pre-check now retries a failing homepage 3 times, 30 s apart (one timeout had dropped kaspi.kz), uses curl
    with a hard 20 s limit (Python's per-read timeout let slow servers hang the run), counts bot-protection
    401/403 as reachable but flagged, and saves every result with its time in `prechecks.json`. Sites the old check
    had wrongly failed came back and, by the same rules, displaced some later picks (RevenueCat now outranks
    Cursor as a dev-tools leader). Counting bot-protection 403s as reachable also brought back high-traffic sites
    the earlier checks had silently excluded (PayPal, Coinbase, Mayo Clinic, Louis Vuitton, Hermès, Foster and
    Partners): the previous lists were biased against well-protected sites.
  - Strikes from applying the criteria to the replacements: GoDaddy (fintech mislabel), Freepik's magnific.com
    and The Local Project (criterion A).
  - Sampling order changed from a seeded shuffle to a seeded per-domain hash, after a strike in one industry
    reshuffled another industry's whole draw. Shared-domain rule now counts organizations within one kind of
    source, after it dropped companies (Replit) for appearing in both YC and the App Store.
  - "Health" now includes health insurers, so a strike from fintech isn't a mismatch in health.
  - Source-level fixes after checking a draft run against §1: the App Store Health & Fitness chart (hiking and
    fitness apps) and Food & Drink chart (delivery platforms, recipe apps) were dropped as sources for health and
    food; those apps can still reach consumer apps. Wikidata's developers of programming tools now have to be
    companies (the draft drew a university and an individual's site). Fintech's definition now says plainly that
    incumbents whose apps chart in Finance count.

## Source composition

Raw = entries the source returned. Eligible = after the Tranco, homepage, shared-domain, strike and earlier-industry rules. Chosen = sampled sites drawn from that source (leaders are drawn by rank from the union and listed as `rank`).

**dev-tools** (eligible union 215)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| yc:Engineering, Product and Design|Infrastructure | 675 | 202 | 5 |
| appstore:dev | 150 | 18 | 4 |
| wikidata:programming-tool-developer | 993 | 1 | 1 |
| leaders (by rank) | | | 5 |

**fintech** (eligible union 332)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| yc:Fintech | 491 | 106 | 4 |
| wikidata:fintech | 705 | 187 | 3 |
| appstore:finance | 149 | 61 | 3 |
| leaders (by rank) | | | 5 |

**health** (eligible union 379)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| yc:Healthcare | 547 | 63 | 4 |
| wikidata:health | 873 | 273 | 3 |
| appstore:health | 150 | 46 | 3 |
| leaders (by rank) | | | 5 |

**luxury-fashion** (eligible union 75)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:fashion-house | 144 | 60 | 4 |
| wikidata:luxury-good | 22 | 5 | 3 |
| altagamma | 124 | 13 | 3 |
| leaders (by rank) | | | 5 |

**food-hospitality** (eligible union 758)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:restaurant-chain | 1,565 | 439 | 3 |
| wikidata:hotel-chain | 530 | 165 | 3 |
| wikidata:hospitality | 1,060 | 107 | 2 |
| michelin | 16,948 | 80 | 2 |
| leaders (by rank) | | | 5 |

**editorial-media / national** (eligible union 6)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:national-newspaper | 1 | 1 | 1 |
| wplist:newspapers-by-circulation | 12 | 5 | 1 |
| leaders (by rank) | | | 1 |

**editorial-media / digital-native** (eligible union 1,813)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:online-newspaper | 2,102 | 1,061 | 1 |
| wikidata:news-website | 1,687 | 841 | 1 |
| leaders (by rank) | | | 1 |

**editorial-media / magazines** (eligible union 753)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:magazine-with-publisher | 4,858 | 701 | 1 |
| wplist:magazines-by-circulation | 174 | 104 | 1 |
| leaders (by rank) | | | 1 |

**editorial-media / business** (eligible union 33)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:business-periodical | 16 | 8 | 1 |
| wikidata:business-newspaper | 52 | 25 | 1 |
| leaders (by rank) | | | 1 |

**editorial-media / independent** (eligible union 1,683)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:magazine-independent | 9,584 | 1,605 | 1 |
| wikidata:online-magazine | 1,122 | 294 | 1 |
| leaders (by rank) | | | 1 |

**architecture-design** (eligible union 92)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| wikidata:architectural-firm | 1,381 | 64 | 2 |
| wikidata:design-agency | 327 | 10 | 2 |
| wikidata:architecture | 330 | 35 | 2 |
| wikidata:graphic-design | 78 | 4 | 2 |
| wplist:architecture-firms | 129 | 43 | 2 |
| leaders (by rank) | | | 5 |

**consumer-apps** (eligible union 206)

| Source | Raw | Eligible | Sampled from it |
|---|---|---|---|
| yc:Consumer | 415 | 165 | 5 |
| appstore:all | 97 | 42 | 5 |
| leaders (by rank) | | | 5 |

## 5. Proposed sites

**120 sites.**

Generated from `proposed-sites.json` (protocol `industry-type/2`, seed `20261118`, Tranco `V38GN`, 2026-11-18). Leaders and sampled sites are separate strata. *Scripts* = writing systems in the homepage text (≥5% of letters); *lang* = the page's declared language.

### `dev-tools`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | gitlab.com | GitLab | 400 | en-US | Latin | yc gitlab |
| leader | docker.com | Docker | 527 | en-US | Latin | yc docker |
| leader | fontawesome.com | Font Awesome | 709 | en | Latin | yc font-awesome |
| leader | revenuecat.com | RevenueCat | 983 | en | Latin | yc revenuecat |
| leader | sendbird.com | Sendbird | 1,846 | en-US | Latin | yc sendbird |
| sample | pazi.ai | Pazi | 525,824 | en | Latin | yc pazi |
| sample | herdr.dev | herdr | 13,823 | en | Latin | yc herdr; appstore dev 6828898364 |
| sample | firegiant.com | (no English label) | 640,822 | en | Latin | wikidata programming-tool-developer Q141067418 |
| sample | freestyle.sh | Freestyle | 711,044 | en | Latin | yc freestyle |
| sample | expo.dev | Expo | 5,895 | en | Latin | yc expo; appstore dev 982107779 |
| sample | readme.com | ReadMe | 104,088 | en | Latin | yc readme |
| sample | railway.com | Railway Corporation | 17,037 | en | Latin | appstore dev 6755712493 |
| sample | decentro.tech | Decentro | 179,293 | en | Latin | yc decentro |
| sample | nssurge.com | Surge Networks Inc. | 336,076 | en | Latin | appstore dev 1442620678 |
| sample | rootly.com | Rootly | 130,571 | en | Latin | yc rootly; appstore dev 6478240412 |

### `fintech`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | paypal.com | PayPal | 176 | – | unknown | wikidata fintech Q483959 |
| leader | stripe.com | Stripe | 214 | en-US | Latin | yc stripe |
| leader | coinbase.com | Coinbase | 1,233 | – | unknown | yc coinbase; wikidata fintech Q16972754; appstore finance 886427730 |
| leader | kaspi.kz | Kaspi.kz Joint Stock Company | 1,945 | – | Cyrillic, Latin | wikidata fintech Q106219885 |
| leader | affirm.com | Affirm | 2,529 | en | Latin | wikidata fintech Q65085822 |
| sample | alinea-invest.com | Alinea | 546,769 | en | Latin | yc alinea; appstore finance 1554623825 |
| sample | infront.co | Infront | 672,424 | en | Latin | wikidata fintech Q141927939 |
| sample | grantcash.com | Grant Cash Advance | 276,804 | en | Latin | wikidata fintech Q142095369; appstore finance 6472350114 |
| sample | truelinkfinancial.com | True Link | 219,531 | en-US | Latin | yc true-link |
| sample | massive.com | Polygon.io | 44,362 | – | Latin | wikidata fintech Q105523379 |
| sample | creditkarma.com | Credit Karma, Inc. | 4,253 | en | Latin | appstore finance 519817714 |
| sample | getbalance.com | Balance | 362,408 | en-US | Latin | yc balance; wikidata fintech Q139907991 |
| sample | hepster.com | hepster | 487,178 | de-DE | Latin | wikidata fintech Q140247761 |
| sample | acorns.com | Acorns Grow Incorporated | 4,981 | en-us | Latin | appstore finance 883324671 |
| sample | buxfer.com | Buxfer | 936,306 | en-US | Latin | yc buxfer |

### `health`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | mayoclinic.org | Mayo Clinic | 937 | – | unknown | wikidata health Q1130172 |
| leader | uhc.com | UNITED HEALTHCARE SERVICES, INC. | 2,328 | – | unknown | appstore health 1348316600 |
| leader | cvs.com | CVS Pharmacy | 3,859 | – | unknown | appstore health 395545555 |
| leader | drugs.com | drugs.com | 5,201 | – | unknown | wikidata health Q5308945 |
| leader | doctolib.fr | Doctolib | 5,295 | – | unknown | wikidata health Q22248343 |
| sample | get-carrot.com | Carrot Fertility | 308,683 | en-US | Latin | yc carrot-fertility |
| sample | atriumhealth.org | Atrium Health | 37,704 | en | Latin | wikidata health Q5044932 |
| sample | labcorp.com | LabCorp | 12,465 | en | Latin | wikidata health Q6466630; appstore health 1361264072 |
| sample | inito.com | Inito | 126,493 | en | Latin | yc inito |
| sample | nyp.org | NewYork-Presbyterian Healthcare System | 32,701 | en | Latin | wikidata health Q7005155 |
| sample | aspendental.com | Aspen Dental Management Inc. | 69,584 | en | Latin | appstore health 6814987987 |
| sample | qventus.com | Qventus | 500,341 | en-US | Latin | yc qventus |
| sample | jointcommission.org | Joint Commission | 24,798 | – | unknown | wikidata health Q1703687 |
| sample | bswhealth.com | Baylor Scott & White Holdings | 43,410 | en | Latin | appstore health 1000856979 |
| sample | asha.health | Asha Health | 429,543 | en | Latin | yc asha-health |

### `luxury-fashion`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | louisvuitton.com | Louis Vuitton | 5,293 | – | unknown | wikidata fashion-house Q191485 |
| leader | hermes.com | Hermès | 10,917 | – | unknown | wikidata fashion-house Q843887 |
| leader | patou.com | Patou | 16,842 | en | Latin | wikidata fashion-house Q3173864 |
| leader | hugoboss.com | Hugo Boss | 17,947 | en | Latin | wikidata fashion-house Q491627 |
| leader | burberry.com | Burberry | 20,009 | en-GB | Latin | wikidata fashion-house Q390107 |
| sample | fursac.com | Fursac | 985,200 | fr | Latin | wikidata fashion-house Q22248311 |
| sample | jaeger-lecoultre.com | Jaeger-LeCoultre | 55,254 | en-US | Latin | wikidata luxury-good Q378698 |
| sample | ginori1735.com | (no English label) | 303,156 | – | unknown | altagamma https://www.ginori1735.com/ |
| sample | etro.com | Etro | 122,506 | en | Latin | wikidata fashion-house Q1371677 |
| sample | piaget.com | Piaget | 104,331 | en-US | Latin | wikidata luxury-good Q658961 |
| sample | dolcegabbana.com | Dolce & Gabbana | 27,765 | en | Latin | wikidata fashion-house Q214480; altagamma https://www.dolcegabbana.com/ |
| sample | holzweileroslo.com | Holzweiler | 962,645 | en | Latin | wikidata fashion-house Q57901713 |
| sample | montblanc.com | Montblanc International GmbH | 28,715 | en | Latin | wikidata luxury-good Q142691 |
| sample | alessi.com | (no English label) | 117,045 | en | Latin | altagamma https://alessi.com/ |
| sample | chloe.com | Chloé | 62,831 | en | Latin | wikidata fashion-house Q1075391 |

### `food-hospitality`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | chipotle.com | Chipotle Mexican Grill | 12,264 | en | Latin | wikidata restaurant-chain Q465751 |
| leader | dairyqueen.com | Dairy Queen | 17,590 | – | unknown | wikidata restaurant-chain Q1141226 |
| leader | jerseymikes.com | Jersey Mike's Subs | 18,205 | – | unknown | wikidata restaurant-chain Q6184897 |
| leader | omnihotels.com | Omni Hotels & Resorts | 21,328 | – | unknown | wikidata hospitality Q7090329 |
| leader | princehotels.co.jp | Prince Hotels | 25,948 | – | Kana, Han, Latin | wikidata hotel-chain Q7244088 |
| sample | bartaco.com | Bartaco | 490,519 | en | Latin | wikidata restaurant-chain Q112871922 |
| sample | hennnahotel.com | Henn na Hotel | 326,078 | ja | Kana, Han, Latin | wikidata hotel-chain Q22120267 |
| sample | swiss-belhotel.com | Swiss-Belhotel International | 230,211 | en | Latin | wikidata hospitality Q7658833 |
| sample | rivercafe.com | The River Café | 908,193 | en | Latin | michelin the-river-cafe |
| sample | buffalowildwings.com | Buffalo Wild Wings | 29,649 | en | Latin | wikidata restaurant-chain Q509255 |
| sample | apahotel.com | APA Hotel | 44,678 | – | unknown | wikidata hotel-chain Q17191643 |
| sample | mcmenamins.com | McMenamins | 105,202 | en | Latin | wikidata hospitality Q6802345 |
| sample | postranchinn.com | Sierra Mar | 470,470 | en-US | Latin | michelin sierra-mar |
| sample | dishoom.com | Dishoom | 156,902 | en | Latin | wikidata restaurant-chain Q48699762 |
| sample | sercotelhoteles.com | Sercotel | 181,265 | es | Latin | wikidata hotel-chain Q126182603 |

### `editorial-media`

**national**

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | jagran.com | Dainik Jagran | 1,349 | hi | Devanagari, Latin | wplist newspapers-by-circulation Q1318465 |
| sample | ncregister.com | National Catholic Register | 28,153 | en | Latin | wikidata national-newspaper Q2745511 |
| sample | cankaoxiaoxi.com | Reference News | 87,361 | – | Latin | wplist newspapers-by-circulation Q7307107 |

**digital-native**

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | t-online.de | T-Online | 99 | de | Latin | wikidata online-newspaper Q590940 |
| sample | madridiario.es | Madridiario | 95,482 | es | Latin | wikidata online-newspaper Q61948838 |
| sample | meaww.com | MEAWW | 50,557 | en | Latin | wikidata news-website Q109637723 |

**magazines**

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | time.com | Time | 583 | en | Latin | wikidata magazine-with-publisher Q43297; wplist magazines-by-circulation Q43297 |
| sample | houseandgarden.co.uk | House & Garden | 27,533 | en-GB | Latin | wikidata magazine-with-publisher Q3501362; wplist magazines-by-circulation Q3501362 |
| sample | newyorker.com | The New Yorker | 1,839 | en-US | Latin | wikidata magazine-with-publisher Q217305; wplist magazines-by-circulation Q217305 |

**business**

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | livemint.com | Mint | 4,299 | en | Latin | wikidata business-periodical Q2271133 |
| sample | incrussia.ru | Inc. Russia | 88,235 | ru-RU | Latin | wikidata business-periodical Q124175930 |
| sample | crainsdetroit.com | Crain's Detroit Business | 45,440 | – | unknown | wikidata business-newspaper Q27891854 |

**independent**

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | inven.co.kr | Inven | 1,184 | ko | Hangul, Latin | wikidata magazine-independent Q12613375; wikidata online-magazine Q12613375 |
| sample | exclaim.ca | Exclaim! | 46,188 | en | Latin | wikidata magazine-independent Q664232; wikidata online-magazine Q664232 |
| sample | thenarwhal.ca | The Narwhal | 108,640 | en | Latin | wikidata magazine-independent Q110469456; wikidata online-magazine Q110469456 |

### `architecture-design`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | arup.com | (no English label) | 22,408 | en-US | Latin | wikidata architectural-firm Q716737 |
| leader | gensler.com | Gensler | 37,706 | en | Latin | wikidata architectural-firm Q3100834; wikidata architecture Q3100834; wplist architecture-firms Q3100834 |
| leader | fosterandpartners.com | Foster and Partners | 55,198 | – | unknown | wikidata architectural-firm Q1208016; wplist architecture-firms Q1208016 |
| leader | hdrinc.com | HDR, Inc. | 59,477 | en | Latin | wplist architecture-firms Q5629257 |
| leader | pentagram.com | Pentagram | 69,388 | en-US | Latin | wikidata architectural-firm Q7164989 |
| sample | davidchipperfield.com | David Chipperfield Architects | 379,069 | en-GB | Latin | wikidata architectural-firm Q51137078 |
| sample | artcom.de | ART+COM | 387,432 | de-DE | Latin | wikidata design-agency Q2632380 |
| sample | sgh.com | Simpson Gumpertz & Heger Inc. | 578,511 | en-US | Latin | wikidata architecture Q7521099 |
| sample | basedesign.com | Base | 707,381 | en | Latin | wikidata graphic-design Q4866356 |
| sample | perkinswill.com | Perkins & Will | 128,961 | en-US | Latin | wikidata architectural-firm Q5818919; wikidata architecture Q5818919; wplist architecture-firms Q5818919 |
| sample | hopkins.co.uk | Hopkins Architects | 655,279 | en | Latin | wikidata architectural-firm Q11682592 |
| sample | studiomakkinkbey.nl | Studio Makkink & Bey | 989,382 | en | Latin | wikidata architectural-firm Q7628200; wikidata design-agency Q7628200 |
| sample | watg.com | Wimberly Allison Tong & Goo | 372,559 | en-US | Latin | wikidata architectural-firm Q17143677; wikidata architecture Q17143677 |
| sample | ppt-design.com | PPT-Design | 914,961 | en | Latin | wikidata graphic-design Q141638973 |
| sample | hksinc.com | HKS | 170,489 | – | unknown | wikidata architectural-firm Q3123324; wikidata architecture Q3123324; wplist architecture-firms Q3123324 |

### `consumer-apps`

| Stratum | Site | Organization | Tranco | lang | Scripts | Found in |
|---|---|---|---|---|---|---|
| leader | pinterest.com | Pinterest, Inc. | 54 | en | Latin | appstore all 429047995 |
| leader | tiktok.com | TIKTOK PTE. LTD. | 61 | en | Latin | appstore all 6741796873 |
| leader | whatsapp.com | WhatsApp Inc. | 64 | en | Latin | appstore all 310633997 |
| leader | spotify.com | Spotify | 78 | en | Latin | appstore all 324684580 |
| leader | snapchat.com | Snap, Inc. | 158 | en-US | Latin | appstore all 447188370 |
| sample | suiteness.com | Suiteness | 313,487 | en | Latin | yc suiteness |
| sample | reelshort.com | New Leaf Publishing, Inc. | 18,271 | en | Latin | appstore all 1636235979 |
| sample | answerthis.io | AnswerThis | 419,038 | en | Latin | yc answerthis |
| sample | doordash.com | DoorDash | 2,331 | – | unknown | yc doordash; appstore all 719972451 |
| sample | type.ai | Type | 222,721 | en | Latin | yc type |
| sample | thebiblechat.com | Book Vitals Inc. | 167,726 | en | Latin | appstore all 6448849666 |
| sample | mosaic.so | Mosaic | 974,799 | en | Latin | yc mosaic-2 |
| sample | tonalenergy.com | TonalEnergy, Inc | 435,636 | en-US | Latin | appstore all 497716362 |
| sample | paxhistoria.co | Pax Historia | 46,982 | en | Latin | yc pax-historia |
| sample | mydramawave.com | SKYWORK AI PTE LTD | 2,423 | en | unknown | appstore all 6670430706 |

### Changes from the first proposal

Every site in `proposed-sites.v1.json` (protocol 1) and its status under protocol 2. Sites new in protocol 2 are the ones above that don't appear here as kept.

| Protocol 1 | Site | Status under protocol 2 |
|---|---|---|
| dev-tools leader | gitlab.com | kept: dev-tools leader |
| dev-tools leader | docker.com | kept: dev-tools leader |
| dev-tools leader | fontawesome.com | kept: dev-tools leader |
| dev-tools leader | sendbird.com | kept: dev-tools leader |
| dev-tools leader | replit.com | no longer a leader: new sources added higher-ranked sites |
| dev-tools sample | getshogun.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | deepnote.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | activeloop.ai | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | circuitlab.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | adam.new | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | influxdata.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | boat.dev | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | netmaker.io | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | tryfinch.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| dev-tools sample | tumult.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech leader | stripe.com | kept: fintech leader |
| fintech leader | kaspi.kz | kept: fintech leader |
| fintech leader | ycombinator.com | **struck**: startup accelerator and investor, not a financial-services technology company (asked by user) |
| fintech leader | affirm.com | kept: fintech leader |
| fintech leader | razorpay.com | no longer a leader: new sources added higher-ranked sites |
| fintech sample | tryjeeves.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | fintual.cl | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | freetrade.io | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | credible.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | aiprise.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | taulia.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | trulioo.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | wiipo.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| fintech sample | anglehealth.com | **struck**: health insurer; belongs to health, not fintech (asked by user) |
| fintech sample | pretto.fr | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health leader | boots.com | no longer a leader: new sources added higher-ranked sites |
| health leader | cochrane.org | no longer a leader: new sources added higher-ranked sites |
| health leader | centene.com | no longer a leader: new sources added higher-ranked sites |
| health leader | healthgrades.com | no longer a leader: new sources added higher-ranked sites |
| health leader | idexx.com | no longer a leader: new sources added higher-ranked sites |
| health sample | medicalib.fr | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | yashodahospitals.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | medpro.vn | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | mdhub.ai | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | ufhealth.org | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | bonjour-sante.ca | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | hopelab.org | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | dragarwal.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | mclaren.org | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| health sample | vituity.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion leader | patou.com | kept: luxury-fashion leader |
| luxury-fashion leader | hugoboss.com | kept: luxury-fashion leader |
| luxury-fashion leader | armani.com | not selected: domain listed by 3 organizations in one source |
| luxury-fashion leader | burberry.com | kept: luxury-fashion leader |
| luxury-fashion leader | pullandbear.com | **struck**: mass-market fast-fashion retailer (Inditex), not a high-end fashion house or luxury brand (asked by user) |
| luxury-fashion sample | telfar.net | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion sample | etro.com | kept: luxury-fashion sample |
| luxury-fashion sample | holzweileroslo.com | kept: luxury-fashion sample |
| luxury-fashion sample | bulgari.com | not selected: listed site is a page or subdomain, not its own domain's homepage |
| luxury-fashion sample | thombrowne.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion sample | balmain.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion sample | marcjacobs.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion sample | jaeger-lecoultre.com | kept: luxury-fashion sample |
| luxury-fashion sample | cerruti.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| luxury-fashion sample | alcltd.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality leader | ritzcarlton.com | not selected: domain listed by 10 organizations in one source |
| food-hospitality leader | chipotle.com | kept: food-hospitality leader |
| food-hospitality leader | fairmont.com | not selected: domain listed by 3 organizations in one source |
| food-hospitality leader | sixflags.com | **struck**: theme-park operator, not a restaurant, hotel or hospitality company (asked by user) |
| food-hospitality leader | mandarinoriental.com | not selected: domain listed by 40 organizations in one source |
| food-hospitality sample | chucksroadhouse.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | vapiano.de | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | carinos.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | chuckecheese.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | leonardo-hotels.de | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | bones.dk | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | huddlehouse.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | loewshotels.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | sourdoughandco.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| food-hospitality sample | billmillerbbq.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media leader | time.com | kept: editorial-media leader |
| editorial-media leader | telegraph.co.uk | no longer a leader: new sources added higher-ranked sites |
| editorial-media leader | hbr.org | no longer a leader: new sources added higher-ranked sites |
| editorial-media leader | nypost.com | no longer a leader: new sources added higher-ranked sites |
| editorial-media leader | fortune.com | no longer a leader: new sources added higher-ranked sites |
| editorial-media sample | valeursactuelles.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | relish.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | tampabay.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | prevention.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | wirralglobe.co.uk | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | fortworthbusiness.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | thefiscaltimes.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | lagrandeobserver.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | chinaeconomicreview.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| editorial-media sample | kenoshanews.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design leader | design.com | **struck**: logo-maker software, not an architecture firm or design agency (asked by user) |
| architecture-design leader | visme.co | **struck**: presentation and graphics software, not an architecture firm or design agency (asked by user) |
| architecture-design leader | arup.com | kept: architecture-design leader |
| architecture-design leader | biorender.com | **struck**: scientific-illustration software, not an architecture firm or design agency (asked by user) |
| architecture-design leader | gensler.com | kept: architecture-design leader |
| architecture-design sample | unstudio.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design sample | pentagram.com | kept: architecture-design leader |
| architecture-design sample | burohappold.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design sample | p22.com | **struck**: type foundry selling retail fonts, not an architecture firm or design agency (asked by user review, struck by Claude) |
| architecture-design sample | fatboy.com | **struck**: furniture and lifestyle product brand, not an architecture firm or design agency (asked by user review, struck by Claude) |
| architecture-design sample | rpbw.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design sample | akqa.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design sample | i-mad.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| architecture-design sample | smithgroup.com | not selected: listed site is a page or subdomain, not its own domain's homepage |
| architecture-design sample | artcom.de | kept: architecture-design sample |
| consumer-apps leader | matterport.com | no longer a leader: new sources added higher-ranked sites |
| consumer-apps leader | instacart.com | no longer a leader: new sources added higher-ranked sites |
| consumer-apps leader | buymeacoffee.com | no longer a leader: new sources added higher-ranked sites |
| consumer-apps leader | opensea.io | no longer a leader: new sources added higher-ranked sites |
| consumer-apps leader | 9gag.com | no longer a leader: new sources added higher-ranked sites |
| consumer-apps sample | rove.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | shoptiques.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | provenskincare.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | hypeandvice.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | wanderlog.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | lineleap.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | anythingllm.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | voiceos.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | tsenta.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
| consumer-apps sample | tagmango.com | not drawn: new sources and source-balanced sampling changed the pool and the draw |
