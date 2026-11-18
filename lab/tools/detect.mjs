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

// Runs inside the page. Every check reads the rendered DOM and computed styles.
function measure() {
  const vw = innerWidth, vh = innerHeight;
  const visible = (el) => {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return r.width > 4 && r.height > 4 && s.visibility !== "hidden" && s.display !== "none" && +s.opacity > 0.05;
  };
  const all = [...document.body.querySelectorAll("*")].filter(visible);
  const rgb = (c) => (c.match(/[\d.]+/g) || []).map(Number);
  const transparent = (c) => !c || c === "transparent" || (rgb(c).length === 4 && rgb(c)[3] < 0.05);
  // OKLCH hue and chroma. HSL can't separate blue from indigo (both near 240°); OKLCH puts blue near 262°,
  // indigo 277°, violet 293° and purple 303°.
  const oklch = (c) => {
    const lin = (x) => (x /= 255) <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4;
    const [r, g, b] = rgb(c).slice(0, 3).map(lin);
    const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
    const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
    const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
    const A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s;
    const B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;
    return { c: Math.hypot(A, B), h: (Math.atan2(B, A) * 180 / Math.PI + 360) % 360 };
  };
  const hue = (c) => { const o = oklch(c); return o.c < 0.06 ? null : o.h; };
  const boxy = (el) => {
    const s = getComputedStyle(el);
    const parentBg = el.parentElement ? getComputedStyle(el.parentElement).backgroundColor : "";
    return (!transparent(s.backgroundColor) && s.backgroundColor !== parentBg) ||
      parseFloat(s.borderTopWidth) > 0 || (s.boxShadow && s.boxShadow !== "none");
  };
  const radius = (el) => parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0;
  const firstFont = (el) => el ? getComputedStyle(el).fontFamily.split(",")[0].replace(/["']/g, "").trim() : null;
  const bodySize = parseFloat(getComputedStyle(document.body).fontSize) || 16;
  const found = {};

  // 1. Centered hero: the page's main heading is centered in the first screen.
  const h1 = all.find((el) => el.tagName === "H1") ||
    all.filter((el) => /^H[1-3]$/.test(el.tagName) && el.getBoundingClientRect().top < vh)
      .sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
  if (h1 && h1.getBoundingClientRect().top < vh) {
    const r = h1.getBoundingClientRect();
    const centered = getComputedStyle(h1).textAlign === "center" ||
      (Math.abs(r.left + r.width / 2 - vw / 2) < vw * 0.03 && r.width < vw * 0.8);
    found.centeredHero = { hit: centered, heading: h1.textContent.trim().slice(0, 80) };
  } else found.centeredHero = { hit: false, heading: null };

  // 2. Three-card row: three similar boxed siblings side by side, each with real text.
  let cardRows = 0;
  for (const parent of new Set(all.map((el) => el.parentElement).filter(Boolean))) {
    const cards = [...parent.children].filter((c) => visible(c) && boxy(c) && c.textContent.trim().length > 40);
    const rows = {};
    for (const c of cards) {
      const r = c.getBoundingClientRect();
      (rows[Math.round(r.top / 12)] ||= []).push(r.width);
    }
    for (const widths of Object.values(rows)) {
      if (widths.length === 3 && Math.max(...widths) / Math.min(...widths) < 1.15 && widths[0] > vw * 0.15) cardRows++;
    }
  }
  found.threeCardRow = { hit: cardRows > 0, rows: cardRows };

  // 3. Decorative gradients: large colourful gradient backgrounds, or gradient-filled text. Dark or neutral
  // scrims over photos are functional and don't count: a gradient counts only with two or more chromatic
  // stops, or one chromatic stop and no image under it.
  const chromaticStops = (bg) => (bg.match(/rgba?\([^)]+\)/g) || []).filter((c) => {
    const a = rgb(c)[3];
    return (a === undefined || a >= 0.3) && oklch(c).c >= 0.06;
  }).length;
  let bigGradients = 0, gradientText = 0;
  for (const el of all) {
    const s = getComputedStyle(el);
    if (!s.backgroundImage.includes("gradient")) continue;
    const stops = chromaticStops(s.backgroundImage);
    const decorative = stops >= 2 || (stops >= 1 && !s.backgroundImage.includes("url("));
    if (!decorative) continue;
    const r = el.getBoundingClientRect();
    if (s.webkitBackgroundClip === "text" || s.backgroundClip === "text") gradientText++;
    else if (r.width * r.height > vw * vh * 0.15) bigGradients++;
  }
  found.gradient = { hit: bigGradients + gradientText > 0, backgrounds: bigGradients, text: gradientText };

  // 4. Emoji used as icons: elements whose whole text is one or two emoji.
  const emojiOnly = /^(\p{Extended_Pictographic}️?‍?){1,2}$/u;
  const emojiIcons = all.filter((el) => el.children.length === 0 && emojiOnly.test(el.textContent.trim())).length;
  found.emojiIcons = { hit: emojiIcons >= 3, count: emojiIcons };

  // 5. Rounded boxes everywhere: most boxed elements have a radius of 8px or more.
  const boxes = all.filter((el) => boxy(el) && el.getBoundingClientRect().width > 60);
  const rounded = boxes.filter((el) => radius(el) >= 8).length;
  found.roundedEverything = { hit: boxes.length >= 5 && rounded / boxes.length >= 0.6, rounded, boxes: boxes.length };

  // 6. Same spacing everywhere: most top-level sections share one vertical padding.
  const main = document.querySelector("main") || document.body;
  const sections = [...main.children].filter((el) => visible(el) && el.getBoundingClientRect().height > 200);
  const pads = sections.map((el) => getComputedStyle(el).paddingTop).filter((p) => parseFloat(p) > 0);
  const commonest = Math.max(0, ...Object.values(pads.reduce((m, p) => ((m[p] = (m[p] || 0) + 1), m), {})));
  found.uniformSpacing = { hit: sections.length >= 4 && commonest / sections.length >= 0.75, sections: sections.length, sharedPadding: commonest };

  // 7. Purple or indigo primary action: the first prominent filled button is indigo, violet or purple.
  // A button's colour is its background colour, or its gradient's first colourful stop.
  const fill = (el) => {
    const s = getComputedStyle(el);
    if (!transparent(s.backgroundColor)) return s.backgroundColor;
    if (!s.backgroundImage.includes("gradient")) return null;
    return (s.backgroundImage.match(/rgba?\([^)]+\)/g) || []).find((c) => !transparent(c) && oklch(c).c >= 0.06) || null;
  };
  const buttons = all.filter((el) => (el.tagName === "BUTTON" || el.tagName === "A") && fill(el) &&
    el.getBoundingClientRect().height >= 28 && el.textContent.trim().length > 1);
  const cta = buttons[0];
  const ctaHue = cta ? hue(fill(cta)) : null;
  found.purpleAccent = { hit: ctaHue !== null && ctaHue >= 270 && ctaHue <= 320, hue: ctaHue && Math.round(ctaHue), cta: cta ? cta.textContent.trim().slice(0, 40) : null };

  // 8. Pill badge above the headline ("✨ New: …").
  let pill = null;
  if (h1) {
    const top = h1.getBoundingClientRect().top;
    pill = all.find((el) => {
      const r = el.getBoundingClientRect();
      return r.bottom <= top + 4 && top - r.bottom < 120 && r.height < 44 && r.height > 14 &&
        radius(el) >= r.height / 2 - 1 && boxy(el) && el.textContent.trim().length < 60 && el.textContent.trim().length > 2;
    });
  }
  found.pillBadge = { hit: !!pill, text: pill ? pill.textContent.trim().slice(0, 60) : null };

  // 9. Stats row: three or more siblings each led by a big number ("10k+", "99.9%").
  let statRows = 0;
  for (const parent of new Set(all.map((el) => el.parentElement).filter(Boolean))) {
    const kids = [...parent.children].filter(visible);
    const stats = kids.filter((k) => {
      const big = [k, ...k.querySelectorAll("*")].find((x) => /^[$€£]?\d[\d.,]*\s?[kKmMbB%+×x]*\+?$/.test(x.textContent.trim()) &&
        parseFloat(getComputedStyle(x).fontSize) >= bodySize * 1.6);
      return !!big;
    });
    if (stats.length >= 3 && stats.length === kids.length) statRows++;
  }
  found.statsRow = { hit: statRows > 0, rows: statRows };

  // Page ground: the first non-transparent background of body or html, as OKLCH lightness.
  const groundColor = [document.body, document.documentElement].map((el) => getComputedStyle(el).backgroundColor)
    .find((c) => !transparent(c)) || "rgb(255, 255, 255)";
  const lightness = (() => {
    const lin = (x) => (x /= 255) <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4;
    const [r, g, b] = rgb(groundColor).slice(0, 3).map(lin);
    const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
    const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
    const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
    return 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s;
  })();

  return {
    patterns: found,
    ground: { color: groundColor, lightness: Math.round(lightness * 100) / 100 },
    fonts: { heading: firstFont(h1), body: firstFont(document.querySelector("p") || document.body) },
    height: document.documentElement.scrollHeight,
  };
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
