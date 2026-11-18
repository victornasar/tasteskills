// Download catalog fonts that no font host serves, straight from their upstream repos, for lab renders only.
//
// All of them are OFL. Files go to .font-cache/ (not committed) and font-local.json lists them, so detect.mjs
// can inline them into a page as data URLs.
//
// Usage: node fetch-fonts.mjs

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const UPSTREAM = {
  "Karrik": "gitlab:phantomfoundry/karrik_fonts",
  "Sporting Grotesque": "gitlab:velvetyne/Sporting-Grotesque",
  "Junicode": "github:psb1558/Junicode-font",
  "Avara": "gitlab:velvetyne/Avara",
  "Happy Times at the IKOB": "gitlab:velvetyne/Happy-Times-at-the-IKOB",
  "Ouroboros": "gitlab:velvetyne/ouroboros",
  "Basteleur": "gitlab:velvetyne/basteleur",
  "Terminal Grotesque": "github:StudioTriple/Terminal-Grotesque",
  "Le Murmure": "gitlab:velvetyne/murmure",
  "Sligoil": "gitlab:velvetyne/sligoil",
  "Departure Mono": "github:rektdeckard/departure-mono",
  "Steps Mono": "github:raphaelbastide/steps-mono",
};
const WEIGHTS = [["hairline", 100], ["thin", 100], ["extralight", 200], ["ultralight", 200], ["light", 300],
  ["book", 400], ["regular", 400], ["medium", 500], ["semibold", 600], ["demibold", 600], ["extrabold", 800],
  ["ultrabold", 800], ["bold", 700], ["black", 900], ["heavy", 900]];
const FORMATS = [["woff2", "woff2"], ["woff", "woff"], ["otf", "opentype"], ["ttf", "truetype"]];
const CACHE = new URL("./.font-cache/", import.meta.url).pathname;

async function json(url, tries = 5) {
  const r = await fetch(url, { headers: { "user-agent": "tasteskills-lab" } });
  if (r.status === 429 && tries > 0) {  // GitLab rate limit: back off and retry
    await new Promise((ok) => setTimeout(ok, 20000));
    return json(url, tries - 1);
  }
  if (!r.ok) throw new Error(`${r.status} ${url}`);
  return r.json();
}

async function listFiles(spec) {
  const [host, path] = spec.split(":");
  if (host === "github") {
    const repo = await json(`https://api.github.com/repos/${path}`);
    const tree = await json(`https://api.github.com/repos/${path}/git/trees/${repo.default_branch}?recursive=1`);
    return tree.tree.filter((t) => t.type === "blob").map((t) => ({
      path: t.path, raw: `https://raw.githubusercontent.com/${path}/${repo.default_branch}/${t.path}` }));
  }
  const id = encodeURIComponent(path);
  const project = await json(`https://gitlab.com/api/v4/projects/${id}`);
  const files = [];
  for (let page = 1; page < 20; page++) {
    const batch = await json(`https://gitlab.com/api/v4/projects/${id}/repository/tree?recursive=true&per_page=100&page=${page}`);
    files.push(...batch.filter((t) => t.type === "blob"));
    if (batch.length < 100) break;
  }
  return files.map((t) => ({ path: t.path, raw: `https://gitlab.com/${path}/-/raw/${project.default_branch}/${t.path}` }));
}

const known = new URL("./font-local.json", import.meta.url);
const local = existsSync(known) ? JSON.parse(readFileSync(known)) : {};
for (const [family, spec] of Object.entries(UPSTREAM)) {
  if (local[family]?.length) { console.log(`have ${family}`); continue; }
  try {
    const files = await listFiles(spec);
    let chosen = [];
    for (const [ext, format] of FORMATS) {
      chosen = files.filter((f) => f.path.toLowerCase().endsWith("." + ext) && !/test|specimen|old|archive|source|variable/i.test(f.path))
        .map((f) => ({ ...f, format }));
      if (chosen.length) break;
    }
    const faces = new Map();
    for (const f of chosen) {
      const name = f.path.split("/").pop().toLowerCase().replace(/[-_ ]/g, "");
      const style = /italic|oblique/.test(name) ? "italic" : "normal";
      const weight = (WEIGHTS.find(([w]) => name.includes(w)) || [null, 400])[1];
      const key = `${weight}-${style}`;
      if (!faces.has(key)) faces.set(key, { ...f, weight, style });
    }
    const dir = join(CACHE, family.replace(/ /g, "-"));
    mkdirSync(dir, { recursive: true });
    local[family] = [];
    for (const face of faces.values()) {
      const dest = join(dir, face.path.split("/").pop());
      if (!existsSync(dest)) {
        const r = await fetch(face.raw);
        if (!r.ok) continue;
        writeFileSync(dest, Buffer.from(await r.arrayBuffer()));
      }
      local[family].push({ file: dest, format: face.format, weight: face.weight, style: face.style });
    }
    console.log(`${local[family].length ? "ok  " : "NONE"} ${family}: ${local[family].length} faces`);
  } catch (e) {
    console.log(`FAIL ${family}: ${e.message}`);
  }
}
writeFileSync(new URL("./font-local.json", import.meta.url), JSON.stringify(local, null, 2) + "\n");
