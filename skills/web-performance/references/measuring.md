# Measuring performance

## Lab and field

| | Lab (Lighthouse, devtools, WebPageTest) | Field (CrUX, `web-vitals` in analytics) |
| --- | --- | --- |
| Tells you | Why something is slow, reproducibly | What real users experience |
| Conditions | Simulated device and network | Real devices, networks, caches |
| Measures INP? | No (Total Blocking Time is a proxy) | Yes |
| Use for | Diagnosing and checking fixes | Judging whether the fix mattered |

A new site has no field data; use lab measurements on a throttled mobile profile and treat them as estimates.

## Commands

```bash
# Lighthouse CLI against a local or deployed page, mobile emulation (the default)
npx lighthouse http://localhost:3000 --only-categories=performance --view

# Save JSON to compare before and after
npx lighthouse http://localhost:3000 --only-categories=performance --output=json --output-path=./lh.json
```

```js
// Find the LCP element and layout shifts in the page (paste into the console or page.evaluate)
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) console.log('LCP', Math.round(e.startTime), e.element);
}).observe({ type: 'largest-contentful-paint', buffered: true });

new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (!e.hadRecentInput) console.log('CLS', e.value.toFixed(3), e.sources?.map((s) => s.node));
  }
}).observe({ type: 'layout-shift', buffered: true });
```

```js
// Field reporting with the web-vitals library (npm i web-vitals)
import { onLCP, onINP, onCLS } from 'web-vitals';
const send = (m) => navigator.sendBeacon('/vitals', JSON.stringify({ name: m.name, value: m.value, id: m.id }));
onLCP(send); onINP(send); onCLS(send);
```

## Reading the results

**LCP is slow.** Break it into parts (Lighthouse and the Performance panel show them):

| Part | Cause | Fix |
| --- | --- | --- |
| Time to first byte | Slow server, no caching, redirects | Cache HTML at the edge, static generation, remove redirects |
| Resource load delay | LCP image discovered late (CSS background, JS-injected, lazy-loaded) | Put it in the HTML, `fetchpriority="high"`, preload |
| Resource load time | Image too heavy | Right size via `srcset`, AVIF/WebP, compression |
| Render delay | Render-blocking CSS/JS, fonts hiding text, client-side rendering | Inline critical CSS, defer JS, `font-display: swap`, server-render |

**CLS is high.** The layout-shift entries name the elements that moved. Usual causes: images or embeds without
dimensions, fonts swapping with different metrics, banners injected at the top, content inserted above the
viewport, skeletons of the wrong size.

**INP is high** (field) or **TBT is high** (lab). Record an interaction in the Performance panel. Look for long
tasks during input handling, large re-renders, layout thrashing (reading and writing layout in a loop), and heavy
third-party scripts. Fix by doing less, yielding, deferring non-urgent work, and showing feedback before the
work.

## Page weight

Check the Network panel with the cache disabled, filtered by type. Rough guidance for a content or marketing page
on mobile:

- HTML + CSS for the first screen: small enough to arrive in the first few round trips.
- Fonts: two or three WOFF2 files, typically tens of KB each when subset.
- LCP image: as small as its displayed size and quality allow, often under ~200KB.
- JavaScript: as little as the interactivity needs. Static pages may need almost none.
- Third parties: list each one, its weight and whether it blocks rendering.

These are not thresholds to hit; they're the places to look first.

## Throttling profiles

Test with Chrome devtools' network throttling (Fast 4G or Slow 4G) and CPU throttling (4× or 6× slowdown) to
approximate a mid-range phone. Look at the filmstrip (Performance panel screenshots) as well as the numbers: a
page can score well and still show a blank white screen for a second, or score poorly while showing useful
content early.

## Images checklist

- [ ] Format: AVIF or WebP, with a fallback if needed
- [ ] `srcset` widths cover phone to wide desktop; `sizes` matches the layout
- [ ] `width` and `height` (or `aspect-ratio`) on every image
- [ ] LCP image: eager, `fetchpriority="high"`, in the HTML
- [ ] Below-the-fold images: `loading="lazy"`, `decoding="async"`
- [ ] No image larger than about twice its largest displayed size
- [ ] SVGs optimised; no raster icons

## Fonts checklist

- [ ] Self-hosted WOFF2, subset, only used weights and styles
- [ ] `font-display: swap` or `optional`
- [ ] Above-the-fold files preloaded (`<link rel="preload" as="font" type="font/woff2" crossorigin>`)
- [ ] Fallback metrics adjusted to limit the swap shift
