"""The find-font engine must follow AGENTS.md's rules and keep different briefs apart.

Run: python3 -m unittest discover -s tests
No Claude calls: these feed fixed readings of each brief straight to the script.
"""
import itertools
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills" / "find-font" / "scripts"))
sys.path.insert(0, str(ROOT / "scripts"))
import find_font as ff  # noqa: E402
import eval as ev  # noqa: E402

DATA = ff.load()
FEELS = list(DATA["vocab"]["feel"])
BRIEFS = json.loads((ROOT / "evals" / "briefs.json").read_text())["briefs"]
# Every feel alone, and every ordered pair of feels: 100 readings of a brief.
FEEL_READINGS = [[a] for a in FEELS] + [[a, b] for a, b in itertools.permutations(FEELS, 2)]
OPPOSITES = [("warm", "technical"), ("elegant", "loud"), ("literary", "playful"),
             ("neutral", "experimental"), ("editorial", "retro")]
MAX_TOP_SHARE = 0.30  # no font may be the top pick for more than this share of feel readings in a role


def run(engine):
    return ff.recommend(DATA, engine["roles"], engine.get("feel", []), engine.get("scripts", []),
                        engine.get("public_repo", False), engine.get("replaces"), engine.get("category"))


class EvalBriefs(unittest.TestCase):
    def test_engine_passes_every_eval_brief(self):
        for b in BRIEFS:
            with self.subTest(brief=b["id"]):
                result = run(b["engine"])
                answer = "```json\n" + json.dumps(result["picks"]) + "\n```"
                self.assertEqual(ev.score(b, answer), [])


class Rules(unittest.TestCase):
    def test_every_pick_passes_the_filter(self):
        for role in DATA["vocab"]["use"]:
            for feels in FEEL_READINGS[:len(FEELS)]:
                for p in run({"roles": [role], "feel": feels})["roles"][0]["picks"]:
                    font = next(f for f in DATA["fonts"] if f["id"] == p["id"])
                    self.assertTrue(ff.passes(font, role, []), (role, feels, p["id"]))

    def test_headline_body_pairs_follow_the_rules(self):
        for feels in FEEL_READINGS:
            with self.subTest(feels=feels):
                result = run({"roles": ["headlines", "body"], "feel": feels})
                self.assertEqual(result["pair"]["bends"], [])
                self.assertEqual(result["pair"]["ids"], [r["picks"][0]["id"] for r in result["roles"]])

    def test_public_repo_drops_fontshare_when_open_fonts_fit(self):
        result = run({"roles": ["headlines"], "feel": ["editorial"], "public_repo": True})
        self.assertTrue(all(p["license"] == "OFL" for p in result["roles"][0]["picks"]))

    def test_same_input_same_output(self):
        engine = {"roles": ["headlines", "body"], "feel": ["warm", "literary"]}
        self.assertEqual(run(engine), run(engine))


class Diversity(unittest.TestCase):
    def test_opposite_feels_get_different_top_picks(self):
        for role in ("headlines", "body", "ui", "posters", "logos", "code"):
            for a, b in OPPOSITES:
                with self.subTest(role=role, feels=(a, b)):
                    top_a = run({"roles": [role], "feel": [a]})["roles"][0]["picks"][0]["id"]
                    top_b = run({"roles": [role], "feel": [b]})["roles"][0]["picks"][0]["id"]
                    self.assertNotEqual(top_a, top_b)

    def test_no_font_dominates_a_role(self):
        for roles in (["headlines", "body"], ["ui"], ["posters"], ["logos"], ["code"]):
            tops = [Counter() for _ in roles]
            for feels in FEEL_READINGS:
                for i, r in enumerate(run({"roles": roles, "feel": feels})["roles"]):
                    tops[i][r["picks"][0]["id"]] += 1
            for role, counts in zip(roles, tops):
                font, n = counts.most_common(1)[0]
                with self.subTest(role=role):
                    self.assertLessEqual(n / len(FEEL_READINGS), MAX_TOP_SHARE,
                                         f"{font} is the top {role} pick for {n} of {len(FEEL_READINGS)} readings")


if __name__ == "__main__":
    unittest.main()
