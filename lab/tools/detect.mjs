// Render pages in Chrome and detect the layout patterns AI-built sites overuse.
//
// Usage:
//   node detect.mjs <html file or folder>... [--out results.json] [--shots <folder>] [--full]
//
// Each page is opened at 1440×900, given up to 15 s for fonts and scripts, then measured on its computed
// styles, not its source. The result is one record per page: which patterns it shows and the evidence.
// --shots also saves an above-the-fold JPEG per page (--full adds a full-page one). Fonts a page self-hosts
// from the catalog are supplied from font-sources.json; `fonts.loaded` says whether heading and body fonts
// actually rendered. Uses the installed Google Chrome.

import { chromium } from "playwright-core";
import { readdirSync, statSync, writeFileSync, mkdirSync, readFileSync, existsSync } from "node:fs";
import { resolve, join, relative, basename, dirname } from "node:path";
import { pathToFileURL } from "node:url";
import { measure } from "../../layout/skills/check-layout/scripts/patterns.mjs";

const args = process.argv.slice(2);
const flag = (name) => {
  const i = args.indexOf(name);
  if (i === -1) return null;
  const value = args[i + 1];
  args.splice(i, 2);
  return value;
};
const out = flag("--out");
const shots = flag("--shots");
const full = args.includes("--full") ? (args.splice(args.indexOf("--full"), 1), true) : false;

// Pages that self-host catalog fonts reference files the lab doesn't have. Swap in hosted copies so the render
// shows the intended type (see resolve-fonts.mjs). Unresolvable fonts are reported, not hidden.
const sourcesFile = new URL("./font-sources.json", import.meta.url);
const SOURCES = existsSync(sourcesFile) ? JSON.parse(readFileSync(sourcesFile)) : {};
const localFile = new URL("./font-local.json", import.meta.url);
const LOCAL = existsSync(localFile) ? JSON.parse(readFileSync(localFile)) : {};  // see fetch-fonts.mjs
const cssCache = new Map();
async function hostedCss(family) {
  if (LOCAL[family]?.length) {
    return LOCAL[family].filter((f) => existsSync(f.file)).map((f) =>
      `@font-face { font-family: "${family}"; font-weight: ${f.weight}; font-style: ${f.style}; font-display: block; ` +
      `src: url("data:font/${f.format === "opentype" ? "otf" : f.format === "truetype" ? "ttf" : f.format};base64,` +
      `${readFileSync(f.file).toString("base64")}") format("${f.format}"); }`).join("\n");
  }
  const url = SOURCES[family];
  if (!url) return null;
  if (!cssCache.has(url)) {
    const r = await fetch(url, { headers: { "user-agent": "Mozilla/5.0 Chrome/130" } });
    cssCache.set(url, r.ok ? await r.text() : "");
  }
  return cssCache.get(url)
    .replace(/font-family:\s*['"]?[^;'"]+['"]?\s*;/g, `font-family: "${family}";`)
    .replace(/url\((['"]?)(?!https?:|data:)([^)'"]+)\1\)/g, (_, q, rel) => `url("${new URL(rel, url).href}")`);
}

async function supplyFonts(page) {
  // Remove @font-face rules that point at missing local files, and list the families the page asks for.
  const wanted = await page.evaluate(() => {
    const families = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      for (let i = rules.length - 1; i >= 0; i--) {
        const r = rules[i];
        if (r instanceof CSSFontFaceRule) {
          const src = r.style.getPropertyValue("src");
          if (!/url\(\s*["']?(https?:|data:)/.test(src)) {
            families.add(r.style.getPropertyValue("font-family").replace(/["']/g, "").trim());
            sheet.deleteRule(i);
          }
        } else if (r.style && r.style.fontFamily) {
          r.style.fontFamily.split(",").forEach((n) => families.add(n.replace(/["']/g, "").trim()));
        }
      }
    }
    return [...families];
  });
  const supplied = [];
  for (const family of wanted) {
    const loaded = await page.evaluate((f) => document.fonts.check(`16px "${f}"`) && [...document.fonts].some((x) => x.family.replace(/["']/g, "") === f && x.status === "loaded"), family);
    if (loaded) continue;
    const css = await hostedCss(family);
    if (css) {
      await page.addStyleTag({ content: css });
      supplied.push(family);
    }
  }
  return supplied;
}

const files = [];
for (const a of args) {
  const p = resolve(a);
  if (statSync(p).isDirectory()) {
    const walk = (d) => readdirSync(d).forEach((n) => {
      const q = join(d, n);
      statSync(q).isDirectory() ? walk(q) : n.endsWith(".html") && files.push(q);
    });
    walk(p);
  } else files.push(p);
}
files.sort();
if (!files.length) {
  console.error("no .html files given");
  process.exit(1);
}


const browser = await chromium.launch({ channel: "chrome" });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const results = [];
for (const file of files) {
  const record = { file: relative(process.cwd(), file) };
  try {
    await page.goto(pathToFileURL(file).href, { waitUntil: "load", timeout: 20000 });
    await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
    await page.evaluate(() => document.fonts.ready);
    record.suppliedFonts = await supplyFonts(page);
    await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
    await page.evaluate(() => document.fonts.ready);
    Object.assign(record, await page.evaluate(measure));
    record.fonts.loaded = await page.evaluate(({ heading, body }) => {
      const has = (f) => !f || [...document.fonts].some((x) => x.family.replace(/["']/g, "") === f && x.status === "loaded") ||
        /^(system-ui|-apple-system|georgia|times|helvetica|arial|ui-|sans-serif|serif|monospace|menlo|sf )/i.test(f);
      return { heading: has(heading), body: has(body) };
    }, record.fonts);
    if (shots) {
      const dest = join(resolve(shots), relative(resolve(args[0]), file).replace(/\.html$/, ".jpg"));
      mkdirSync(dirname(dest), { recursive: true });
      await page.screenshot({ path: dest, type: "jpeg", quality: 70 });
      if (full) await page.screenshot({ path: dest.replace(/\.jpg$/, "-full.jpg"), type: "jpeg", quality: 60, fullPage: true });
    }
    const hits = Object.entries(record.patterns).filter(([, v]) => v.hit).map(([k]) => k);
    console.log(`${basename(file)}: ${hits.join(", ") || "none"}`);
  } catch (e) {
    record.error = String(e.message || e).split("\n")[0];
    console.log(`${basename(file)}: ERROR ${record.error}`);
  }
  results.push(record);
}
await browser.close();
if (out) writeFileSync(out, JSON.stringify(results, null, 2) + "\n");
