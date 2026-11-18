// Find a loadable stylesheet for every catalog font, for rendering lab pages only.
//
// Pages built with find-font self-host their fonts, but the lab has no font files, so a screenshot would show
// fallback fonts and misrepresent the design. detect.mjs uses this map to swap in a hosted copy at render time.
// Hosted CSS is fine here: these are local screenshots, not pages served to visitors.
//
// Usage: node resolve-fonts.mjs   → writes font-sources.json

import { readFileSync, writeFileSync } from "node:fs";

const catalog = JSON.parse(readFileSync(new URL("../../typography/fonts.json", import.meta.url)));

const names = (f) => {
  const parts = f.name.split(" / ").map((p) => p.trim());
  const first = parts[0].split(" ");
  return [parts[0], ...parts.slice(1).map((p) => (p.includes(" ") ? p : [...first.slice(0, -1), p].join(" ")))];
};

async function ok(url) {
  try {
    const r = await fetch(url, { headers: { "user-agent": "Mozilla/5.0 Chrome/130" } });
    const text = await r.text();
    return r.ok && text.includes("@font-face");
  } catch {
    return false;
  }
}

// Fontsource publishes some catalog fonts under other ids.
const FONTSOURCE_ALIASES = {
  "Libertinus": "libertinus-serif", "Monaspace": "monaspace-neon",
  "iA Writer Mono": "ia-writer-mono", "iA Writer Duo": "ia-writer-duo", "iA Writer Quattro": "ia-writer-quattro",
};

const sources = {};
for (const f of catalog.fonts) {
  const tries = [];
  const fs = f.url.match(/fontshare\.com\/fonts\/([a-z0-9-]+)/);
  if (fs) tries.push(`https://api.fontshare.com/v2/css?f[]=${fs[1]}@${f.weights.join(",")}&display=swap`);
  for (const n of names(f)) {
    const fam = n.replace(/ /g, "+");
    const w = f.weights.length > 1 ? `:ital,wght@${f.weights.map((x) => `0,${x}`).join(";")}${f.italics ? ";" + f.weights.map((x) => `1,${x}`).join(";") : ""}` : "";
    tries.push(`https://fonts.googleapis.com/css2?family=${fam}${w}&display=swap`);
    tries.push(`https://fonts.googleapis.com/css2?family=${fam}&display=swap`);
  }
  for (const n of names(f)) if (FONTSOURCE_ALIASES[n]) tries.push(`https://cdn.jsdelivr.net/npm/@fontsource/${FONTSOURCE_ALIASES[n]}/index.css`);
  tries.push(`https://cdn.jsdelivr.net/npm/@fontsource-variable/${f.id}/index.css`);
  tries.push(`https://cdn.jsdelivr.net/npm/@fontsource/${f.id}/index.css`);
  let found = null;
  for (const url of tries) if (await ok(url)) { found = url; break; }
  for (const n of names(f)) sources[n] = found;
  console.log(`${found ? "ok  " : "NONE"} ${f.name}${found ? "" : ""}`);
}
writeFileSync(new URL("./font-sources.json", import.meta.url), JSON.stringify(sources, null, 2) + "\n");
const missing = Object.entries(sources).filter(([, v]) => !v).map(([k]) => k);
console.log(`\n${Object.keys(sources).length - missing.length} of ${Object.keys(sources).length} names resolved. Missing: ${missing.join(", ") || "none"}`);
