#!/usr/bin/env python3
"""Draw the human-rated subset (methodology §9) from the frozen list. Run once, at freezing, before any
measurement; writes rated-subset.json. Standard library only."""
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = "20261118-ratings"
INDUSTRIES = ["dev-tools", "fintech", "health", "luxury-fashion", "food-hospitality", "editorial-media",
              "architecture-design", "consumer-apps"]  # §1 order
MODELS = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]  # §8 order
LEADERS, SAMPLED, AI = 2, 3, 5

raw = (HERE / "proposed-sites.json").read_bytes()
sites = json.loads(raw)["sites"]
assert list(sites) == INDUSTRIES
rng = random.Random(SEED)
drawn = rng.sample(INDUSTRIES, 4)
out = {"seed": SEED, "list_sha256": hashlib.sha256(raw).hexdigest(), "industries": {}}
for ind in INDUSTRIES:
    if ind not in drawn:
        continue
    leaders = sorted(s["domain"] for s in sites[ind] if s["role"] == "leader")
    sampled = sorted(s["domain"] for s in sites[ind] if s["role"] == "sample")
    slots = [f"{m}/run{r}" for m in MODELS for r in (1, 2, 3)]
    out["industries"][ind] = {"leaders": rng.sample(leaders, LEADERS), "sampled": rng.sample(sampled, SAMPLED),
                              "ai_pages": rng.sample(slots, AI)}
out["drawn_order"] = drawn
(HERE / "rated-subset.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
