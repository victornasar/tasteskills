# Methodology

**Protocol:** `industry-type/2` · **Selection date:** 2026-11-18 · **Status: Frozen 2026-11-19** (list approved
2026-11-19; `proposed-sites.json` SHA-256 `{{SITES_SHA}}`). The list, the industry scopes in §1 and the rated
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

{{RATED_SUBSET}}

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
