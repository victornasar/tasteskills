// The checker must catch every pattern on the slop fixture and none on the clean one, through the same script
// the skill ships. Run: node --test tests/   (needs Chrome and Node 22+)
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { PATTERNS } from "../skills/check-layout/scripts/patterns.mjs";

const here = (p) => fileURLToPath(new URL(p, import.meta.url));
const check = (page) => JSON.parse(execFileSync("node",
  [here("../skills/check-layout/scripts/check_layout.mjs"), here(page), "--json"], { encoding: "utf8" }));

test("slop fixture trips every pattern", () => {
  const r = check("fixtures/slop.html");
  assert.deepEqual(r.hits.sort(), Object.keys(PATTERNS).sort());
});

test("clean fixture trips none", () => {
  assert.deepEqual(check("fixtures/clean.html").hits, []);
});

test("phone width renders and reports", () => {
  const r = JSON.parse(execFileSync("node", [here("../skills/check-layout/scripts/check_layout.mjs"),
    here("fixtures/clean.html"), "--json", "--width", "390", "--height", "844"], { encoding: "utf8" }));
  assert.equal(r.width, 390);
  assert.deepEqual(r.hits, []);
});
