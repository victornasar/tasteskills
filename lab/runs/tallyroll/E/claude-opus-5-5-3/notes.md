I built the Tallyroll page and saved `index.html` and `DIRECTION.md` in the project. The layout checker found none of its nine overused patterns on desktop or phone. I did two fix rounds, the cap you set, and the results are logged in §13 of `DIRECTION.md`. The spec was never approved because this run couldn't stop to ask, so it stays a draft with the gaps listed under Open decisions.



- **Invoice in the first screen:** the hero is the example invoice line, not a dashboard mock. On desktop it starts open on the 31 daily totals, which add up to 1,204,388; on phone it starts closed. The daily figures are made up and labelled "illustrative". That and the open-by-default choice are tagged as needing your OK.
- **Fonts:** IBM Plex Serif for headings, IBM Plex Sans for text and Commit Mono for numbers and code, all free (OFL) and all from find-font. I skipped its first headline pick, Technor, because the tool describes it as "sci-fi", which works against "calm". The fonts load from the jsdelivr CDN because downloading them to embed needed an approval this run couldn't give. Host them yourself before launch.
- **Colours:** find-color's Graphite and Signal: off-white background, near-black text, and blue only on buttons, the step line and highlighted data. One dark band holds the engineering and pricing sections.
- **Copy:** the finance and engineering features show only the brief's wording. I removed my own descriptions in fix round 1 because they made claims the brief doesn't. The sample event payload and pricing rule are marked "illustrative".
- **Still open:** `fennel-street.md` isn't in the project, so the "opposite" register rests on the brief's three words. The demo and footer links point nowhere yet.
