#!/usr/bin/env node
// check-layout: render a page in Chrome and report which overused layout patterns it shows.
//
// Usage:
//   node check_layout.mjs <file.html | http://localhost:3000/> [--screenshot out.png] [--full]
//                         [--width 1440] [--height 900] [--json]
//
// Needs Node 22+ (for its built-in WebSocket) and Google Chrome, Chromium, Edge or Brave. No install. Set
// CHROME_PATH to use a specific browser. Reads the rendered page's computed styles, so it works on any stack.
// Exit code is 0 whether or not patterns are found: the report is advice, read with the brief in hand.

import { spawn, execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { measure, PATTERNS } from "./patterns.mjs";

const argv = process.argv.slice(2);
const opt = (name, fallback) => {
  const i = argv.indexOf(name);
  if (i === -1) return fallback;
  const v = argv[i + 1];
  argv.splice(i, 2);
  return v;
};
const flag = (name) => (argv.includes(name) ? (argv.splice(argv.indexOf(name), 1), true) : false);
const screenshot = opt("--screenshot", null);
const width = Number(opt("--width", 1440));
const height = Number(opt("--height", 900));
const full = flag("--full");
const asJson = flag("--json");
const target = argv[0];

function fail(message) {
  console.error(`check-layout: ${message}`);
  process.exit(2);
}
if (!target) fail("give a page: node check_layout.mjs page.html (or a URL)");
if (typeof WebSocket === "undefined") fail(`needs Node 22 or later (this is ${process.version})`);
const url = /^https?:\/\//.test(target) ? target : pathToFileURL(resolve(target)).href;
if (url.startsWith("file:") && !existsSync(resolve(target))) fail(`no such file: ${target}`);

function findChrome() {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  const mac = ["Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser"]
    .map((n) => `/Applications/${n}.app/Contents/MacOS/${n}`);
  const win = ["C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"];
  for (const p of [...mac, ...win]) if (existsSync(p)) return p;
  for (const name of ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"]) {
    try { return execFileSync("which", [name], { encoding: "utf8" }).trim(); } catch {}
  }
  fail("no Chrome, Chromium, Edge or Brave found. Install one or set CHROME_PATH.");
}

const profile = mkdtempSync(join(tmpdir(), "check-layout-"));
const chrome = spawn(findChrome(), ["--headless=new", "--remote-debugging-port=0", `--user-data-dir=${profile}`,
  "--no-first-run", "--no-default-browser-check", "--hide-scrollbars", "--mute-audio", "about:blank"],
  { stdio: ["ignore", "ignore", "pipe"] });
const cleanup = () => { try { chrome.kill(); } catch {} try { rmSync(profile, { recursive: true, force: true }); } catch {} };
process.on("exit", cleanup);

const wsUrl = await new Promise((ok, no) => {
  let buf = "";
  const timer = setTimeout(() => no(new Error("Chrome didn't start within 20 s")), 20000);
  chrome.stderr.on("data", (d) => {
    buf += d;
    const m = buf.match(/DevTools listening on (ws:\/\/\S+)/);
    if (m) { clearTimeout(timer); ok(m[1]); }
  });
  chrome.on("exit", (code) => no(new Error(`Chrome exited (${code})`)));
}).catch((e) => fail(e.message));

// Minimal DevTools protocol client.
const ws = new WebSocket(wsUrl);
await new Promise((ok, no) => { ws.onopen = ok; ws.onerror = () => no(new Error("couldn't connect to Chrome")); })
  .catch((e) => fail(e.message));
let nextId = 0;
const pending = new Map();
const listeners = [];
ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id && pending.has(msg.id)) {
    const { ok, no } = pending.get(msg.id);
    pending.delete(msg.id);
    msg.error ? no(new Error(msg.error.message)) : ok(msg.result);
  } else if (msg.method) listeners.forEach((l) => l(msg));
};
const send = (method, params = {}, sessionId) => new Promise((ok, no) => {
  const id = ++nextId;
  pending.set(id, { ok, no });
  ws.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
});
const once = (method, sessionId, ms) => new Promise((ok) => {
  const timer = setTimeout(ok, ms);
  listeners.push((m) => { if (m.method === method && m.sessionId === sessionId) { clearTimeout(timer); ok(); } });
});

try {
  const { targetId } = await send("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await send("Target.attachToTarget", { targetId, flatten: true });
  await send("Page.enable", {}, sessionId);
  await send("Emulation.setDeviceMetricsOverride", { width, height, deviceScaleFactor: 1, mobile: width < 600 }, sessionId);
  const loaded = once("Page.loadEventFired", sessionId, 30000);
  await send("Page.navigate", { url }, sessionId);
  await loaded;
  await new Promise((r) => setTimeout(r, 1500)); // late scripts, web fonts and entrance animations
  const { result, exceptionDetails } = await send("Runtime.evaluate", {
    expression: `document.fonts.ready.then(() => JSON.stringify((${measure.toString()})()))`,
    awaitPromise: true, returnByValue: true,
  }, sessionId);
  if (exceptionDetails) throw new Error(exceptionDetails.exception?.description || "measurement failed in the page");
  const report = JSON.parse(result.value);

  if (screenshot) {
    let clip;
    if (full) {
      const { cssContentSize } = await send("Page.getLayoutMetrics", {}, sessionId);
      clip = { x: 0, y: 0, width, height: Math.min(cssContentSize.height, 12000), scale: 1 };
    }
    const { data } = await send("Page.captureScreenshot", { format: "png", captureBeyondViewport: full, ...(clip ? { clip } : {}) }, sessionId);
    writeFileSync(screenshot, Buffer.from(data, "base64"));
  }

  const hits = Object.entries(report.patterns).filter(([, v]) => v.hit);
  if (asJson) {
    console.log(JSON.stringify({ url, width, ...report, hits: hits.map(([k]) => k) }, null, 2));
  } else {
    const evidence = (k, v) => ({
      centeredHero: `heading "${v.heading}" is centered`,
      threeCardRow: `${v.rows} row(s) of three similar cards`,
      gradient: `${v.backgrounds} large gradient background(s), ${v.text} gradient text`,
      emojiIcons: `${v.count} emoji used as icons`,
      roundedEverything: `${v.rounded} of ${v.boxes} boxes rounded 8px or more`,
      uniformSpacing: `${v.sharedPadding} of ${v.sections} sections share one padding`,
      purpleAccent: `main button "${v.cta}" has hue ${v.hue}°`,
      pillBadge: `"${v.text}"`,
      statsRow: `${v.rows} row(s) of big numbers`,
    })[k];
    console.log(`check-layout: ${url} at ${width}×${height}`);
    console.log(`Fonts: heading ${report.fonts.heading || "?"}, body ${report.fonts.body || "?"}`);
    if (!hits.length) console.log("\nNone of the nine overused patterns found.");
    else {
      console.log(`\n${hits.length} of 9 overused patterns found:`);
      for (const [k, v] of hits) console.log(`  - ${PATTERNS[k]} (${k}): ${evidence(k, v)}`);
      console.log("\nFor each: change it, or keep it and say in one line why this brief needs it. See SKILL.md.");
    }
    if (screenshot) console.log(`\nScreenshot: ${screenshot}`);
  }
} catch (e) {
  fail(e.message);
} finally {
  ws.close();
  cleanup();
}
process.exit(0);
