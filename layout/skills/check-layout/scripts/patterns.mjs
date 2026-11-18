// The nine layout patterns AI-built pages overuse, measured on the rendered page.
//
// `measure` runs inside the page (it's serialized and evaluated there, so it must stay self-contained: no
// imports, no outside variables). It reads computed styles, not source. Evidence for each pattern:
// lab/findings.md and lab/corpus/layout-slop.md. Shared by check_layout.mjs (the skill) and lab/tools/detect.mjs.

export const PATTERNS = {
  centeredHero: "Centered hero headline",
  threeCardRow: "Row of three cards",
  gradient: "Decorative gradient (background or text)",
  emojiIcons: "Emoji used as icons",
  roundedEverything: "Rounded boxes everywhere",
  uniformSpacing: "Same padding on every section",
  purpleAccent: "Indigo, violet or purple main button",
  pillBadge: "Pill badge above the headline",
  statsRow: "Row of big numbers",
};

// Runs inside the page. Every check reads the rendered DOM and computed styles.
export function measure() {
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

  // Skeleton: one token per top-level section, so two pages' structures can be compared. A token is the number
  // of side-by-side columns in the section's content, plus "c" if centered and "b" if it has its own background.
  const pageBg = getComputedStyle(document.body).backgroundColor;
  const skeleton = [];
  const tops = [...(document.querySelector("main") || document.body).children]
    .flatMap((el) => (el.tagName === "MAIN" ? [...el.children] : [el]))
    .filter((el) => visible(el) && el.getBoundingClientRect().height > 120);
  for (const section of tops) {
    let box = section;
    for (let i = 0; i < 4; i++) {
      const kids = [...box.children].filter(visible);
      if (kids.length !== 1) break;
      box = kids[0];
    }
    const rows = {};
    for (const k of [...box.children].filter(visible)) (rows[Math.round(k.getBoundingClientRect().top / 20)] ||= []).push(k);
    const cols = Math.min(6, Math.max(1, ...Object.values(rows).map((r) => r.length)));
    const heading = section.querySelector("h1, h2, h3");
    const centered = getComputedStyle(box).textAlign === "center" || (heading && getComputedStyle(heading).textAlign === "center");
    const bg = getComputedStyle(section).backgroundColor;
    const own = (!transparent(bg) && bg !== pageBg) || getComputedStyle(section).backgroundImage !== "none";
    skeleton.push(`${cols}${centered ? "c" : ""}${own ? "b" : ""}`);
  }

  return {
    patterns: found,
    skeleton,
    ground: { color: groundColor, lightness: Math.round(lightness * 100) / 100 },
    fonts: { heading: firstFont(h1), body: firstFont(document.querySelector("p") || document.body) },
    height: document.documentElement.scrollHeight,
  };
}
