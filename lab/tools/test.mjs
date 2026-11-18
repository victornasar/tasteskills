// Calibration: the slop fixture must trip every detector and the clean fixture none. Run: npm test
import { execFileSync } from "node:child_process";
import { readFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const out = join(mkdtempSync(join(tmpdir(), "detect-")), "r.json");
execFileSync("node", ["detect.mjs", "../../layout/tests/fixtures", "--out", out], { stdio: "inherit" });
const results = JSON.parse(readFileSync(out, "utf8"));
let failed = 0;
for (const r of results) {
  const expectHit = r.file.endsWith("slop.html");
  for (const [name, v] of Object.entries(r.patterns)) {
    if (v.hit !== expectHit) {
      console.error(`✗ ${r.file}: ${name} should ${expectHit ? "" : "not "}fire`);
      failed++;
    }
  }
}
console.log(failed ? `${failed} calibration failures` : "✓ calibration: slop fixture trips all detectors, clean fixture none");
process.exit(failed ? 1 : 0);
