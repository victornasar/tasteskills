# corpus

Websites built by AI models from generic one-line briefs, with no skills and no personal settings. It's the
evidence for what "AI slop" looks like, and the "no skills" baseline other experiments compare against.

| Path | What it is |
|---|---|
| `manifest.json` | The 30 briefs: 6 kinds of site (landing page, portfolio, blog, dashboard, docs, shop) × 5 subjects |
| `sites/<model>/` | One HTML file per brief, as the model returned it |
| `detect.json` | What `../tools/detect.mjs` found on each rendered page |
| `layout-slop.md` | The summary: how often each layout pattern appears, by model and kind of site |
| `generate.py` | Builds the sites. Skips files that exist, so it can be re-run to fill gaps |
| `report.py` | Turns `detect.json` into `layout-slop.md` and `layout-slop.json` |

The same briefs drive `typography/scripts/measure_slop.py`, so the font measurement can use this corpus too:
`python3 typography/scripts/measure_slop.py --corpus lab/corpus/sites`.

## Rebuild

```bash
python3 lab/corpus/generate.py                                   # needs the claude CLI; about an hour
node lab/tools/detect.mjs lab/corpus/sites --out lab/corpus/detect.json
python3 lab/corpus/report.py
```

## Limits

- Models from one company only (Claude Opus 5.5, Sonnet 5.5 and Haiku 5.5). Fable 5.2 needed paid usage credits
  and other providers weren't installed. Add another model's sites as a new folder under `sites/` and rerun the
  detector and report.
- One page per model per brief: enough to see which patterns are common, not to rank models against each other.
