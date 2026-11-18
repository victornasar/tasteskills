/**
 * Static checks for the /taste skill. No model calls.
 *
 * - Sibling commands named in SKILL.md exist on the sibling scripts
 * - The direction template has the sections the skill refers to
 * - SKILL.md (and interviewing.md) do not steer picks with catalog font or color names
 * - Provenance tags and the two-round critique cap are present
 */
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, it } from "node:test";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const REPO = join(ROOT, "..");
const SKILL = join(ROOT, "skills", "taste");
const SKILL_MD = join(SKILL, "SKILL.md");
const TEMPLATE = join(SKILL, "references", "direction-template.md");
const INTERVIEWING = join(SKILL, "references", "interviewing.md");

const FIND_FONT = join(REPO, "typography", "skills", "find-font", "scripts", "find_font.py");
const FIND_COLOR = join(REPO, "color", "skills", "find-color", "scripts", "find-color.mjs");
const CHECK_LAYOUT = join(REPO, "layout", "skills", "check-layout", "scripts", "check_layout.mjs");

function read(path) {
  return readFileSync(path, "utf8");
}

describe("taste skill files", () => {
  it("ships SKILL.md and both reference files", () => {
    assert.ok(existsSync(SKILL_MD), "SKILL.md missing");
    assert.ok(existsSync(TEMPLATE), "direction-template.md missing");
    assert.ok(existsSync(INTERVIEWING), "interviewing.md missing");
  });

  it("has skill frontmatter name taste", () => {
    const md = read(SKILL_MD);
    assert.match(md, /^---\nname: taste\n/m);
    assert.match(md, /^description: /m);
  });
});

describe("sibling engines the skill coordinates", () => {
  it("find-font, find-color and check-layout scripts exist in the repo", () => {
    assert.ok(existsSync(FIND_FONT), FIND_FONT);
    assert.ok(existsSync(FIND_COLOR), FIND_COLOR);
    assert.ok(existsSync(CHECK_LAYOUT), CHECK_LAYOUT);
  });

  it("SKILL.md only names sibling commands that the scripts accept", () => {
    const md = read(SKILL_MD);
    // Commands the conductor tells the agent to run via the sibling skills.
    const fontCmds = ["recommend", "vocab", "avoid", "get"];
    const colorCmds = ["recommend", "apply", "get", "classify", "domains", "conventions"];
    for (const cmd of ["recommend", "vocab", "avoid"]) {
      if (new RegExp(`\\b${cmd}\\b`).test(md) && md.includes("find-font")) {
        assert.ok(fontCmds.includes(cmd), `unknown find-font command: ${cmd}`);
      }
    }
    // Probe the real CLIs so a renamed subcommand fails this area's tests.
    const fontHelp = spawnSync("python3", [FIND_FONT, "-h"], { encoding: "utf8" });
    assert.equal(fontHelp.status, 0, fontHelp.stderr);
    for (const cmd of ["recommend", "vocab", "avoid"]) {
      assert.match(fontHelp.stdout, new RegExp(`\\b${cmd}\\b`), `find_font.py missing ${cmd}`);
    }
    const colorHelp = spawnSync("node", [FIND_COLOR], { encoding: "utf8" });
    // find-color prints usage on no args; exit may be non-zero.
    const colorOut = (colorHelp.stdout || "") + (colorHelp.stderr || "");
    for (const cmd of ["recommend", "apply", "domains"]) {
      if (md.includes(cmd) && md.includes("find-color")) {
        assert.match(colorOut, new RegExp(`\\b${cmd}\\b`), `find-color.mjs missing ${cmd}`);
      }
    }
    assert.ok(colorCmds.includes("recommend"));
    const layoutHelp = spawnSync("node", [CHECK_LAYOUT], { encoding: "utf8" });
    const layoutOut = (layoutHelp.stdout || "") + (layoutHelp.stderr || "");
    assert.match(layoutOut, /check-layout|page\.html|give a page/i);
  });
});

describe("direction template", () => {
  const requiredHeadings = [
    "## 1. Context",
    "## 2. Values",
    "## 3. Opening vocabulary",
    "## 4. References",
    "## 5. Directions explored",
    "## 6. Selected direction",
    "## 7. Design system",
    "## 8. Constraints",
    "## 9. Avoid",
    "## 10. Decisions log",
    "## 11. Open decisions",
    "## 12. Checkpoints",
  ];

  it("defines every section the skill workflow writes", () => {
    const t = read(TEMPLATE);
    for (const h of requiredHeadings) {
      assert.ok(t.includes(h), `template missing ${h}`);
    }
  });

  it("defines the five provenance tags", () => {
    const t = read(TEMPLATE);
    for (const tag of ["client", "inferred", "engine", "agent", "approved"]) {
      assert.match(t, new RegExp(`\`${tag}\`|\\b${tag}\\b`));
    }
  });

  it("encodes fast-mode and diversity writing rules", () => {
    const t = read(TEMPLATE);
    assert.match(t, /Fast mode/i);
    assert.match(t, /diversity rule/i);
    assert.match(t, /Never invent engine output/i);
  });
});

describe("SKILL.md conductor rules", () => {
  it("names the five phases and three gates", () => {
    const md = read(SKILL_MD);
    for (const phase of [
      "Phase 1 — Discover",
      "Phase 2 — Directions",
      "Phase 3 — Spec",
      "Phase 4 — Build",
      "Phase 5 — Critique",
    ]) {
      assert.ok(md.includes(phase), `missing ${phase}`);
    }
    for (const gate of ["Gate 1", "Gate 2", "Gate 3"]) {
      assert.ok(md.includes(gate), `missing ${gate}`);
    }
  });

  it("caps critique at two rounds", () => {
    const md = read(SKILL_MD);
    assert.match(md, /two|2/i);
    assert.match(md, /Critique/);
    assert.match(md, /at most \*\*two\*\* rounds|two-round critique|Fix at most \*\*two\*\*/i);
  });

  it("forbids inventing engine output when siblings are missing", () => {
    const md = read(SKILL_MD);
    assert.match(md, /Never invent|never guess fonts/i);
    assert.match(md, /DIRECTION\.md/);
  });

  it("marks guided mode experimental", () => {
    const md = read(SKILL_MD);
    assert.match(md, /Experimental/i);
    assert.match(md, /guided/i);
  });
});

describe("no steered catalog picks in conductor prose", () => {
  function catalogNames() {
    const fonts = JSON.parse(read(join(REPO, "typography", "fonts.json")));
    const names = new Set();
    for (const f of fonts.fonts) {
      names.add(f.name.toLowerCase());
      if (f.id) names.add(String(f.id).toLowerCase());
    }
    for (const a of fonts.avoid) {
      names.add(a.name.toLowerCase());
    }
    // Common CDN defaults the typography skill also rejects in CSS — keep the conductor clean of them.
    for (const extra of ["inter", "geist", "poppins", "roboto", "arial", "helvetica", "montserrat", "open sans"]) {
      names.add(extra);
    }
    const directions = JSON.parse(read(join(REPO, "color", "library", "directions.json")));
    const list = directions.directions || [];
    for (const d of list) {
      if (d && d.name) names.add(String(d.name).toLowerCase());
      if (d && d.id) names.add(String(d.id).toLowerCase());
    }
    return names;
  }

  it("SKILL.md contains no curated font or color-direction names", () => {
    const md = read(SKILL_MD).toLowerCase();
    // Strip code fences and install URLs so path segments don't false-positive.
    const prose = md
      .replace(/```[\s\S]*?```/g, " ")
      .replace(/https?:\/\/\S+/g, " ")
      .replace(/`[^`]+`/g, " ");
    const hits = [];
    for (const name of catalogNames()) {
      if (name.length < 4) continue; // short ids collide with English
      // Word-boundary-ish: avoid matching inside longer words when possible.
      const re = new RegExp(`(^|[^a-z0-9-])${name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}([^a-z0-9-]|$)`);
      if (re.test(prose)) hits.push(name);
    }
    assert.deepEqual(hits, [], `SKILL.md steers engines with: ${hits.join(", ")}`);
  });
});

describe("interviewing rules", () => {
  it("bans style-label choices and recommended answers on values", () => {
    const md = read(INTERVIEWING);
    assert.match(md, /No style labels/i);
    assert.match(md, /No recommended answer/i);
    assert.match(md, /Silence is not approval/i);
    assert.match(md, /experimental/i);
  });
});
