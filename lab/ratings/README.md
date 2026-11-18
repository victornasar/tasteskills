# ratings

Blind pairwise ratings of lab runs. Each pair is the condition A and condition B run with the same brief, model
and run number, shown as "left" and "right" in shuffled order.

**Rating page:** https://claude.ai/artifact/BvnH2kSuefhAdRLwhEwBaF (private: share it with raters from its Share
menu with access that lets them interact; viewers can look but not vote).

| File | What it is |
|---|---|
| `page.template.html` | The rating page. `build.py page` fills in the pairs to make `page.html` |
| `build.py` | `pairs` lists screenshots to upload and writes `key.json`; `page` builds the page; `score` scores votes |
| `key.json` | Which side of each pair was A and which was B. Never put this in the page |
| `uploads.json` | Each screenshot's address in the rating page's asset store |

## Scoring

Export the `votes` collection (one document per rater) as JSON, then:

```bash
python3 lab/ratings/build.py score votes.json     # writes results.md
```

Don't rate runs you made or watched being made. Raters should see neither the key nor `runs/measures.md` first.
