---
name: performance
description: Make a website fast to load, stable while it loads and responsive to input, as part of how it feels, not an afterthought. Covers perceived performance, loading states, Core Web Vitals (LCP, INP, CLS), image optimisation and delivery, asset and script loading, font loading without layout shift, layout stability, animation and rendering performance, and measuring with lab and field tools. Use when building or reviewing a page's loading and runtime behaviour, adding images, fonts, scripts or third-party embeds, or when a site feels slow, jumps while loading or lags on input. Not for which loading states exist (`interaction`) or motion design choices (`motion`).
argument-hint: "[page or concern, e.g. hero image LCP]"
---

# performance

Speed is part of the design. A page that shows its main content quickly, doesn't jump while loading and responds
the instant someone taps feels well made; the same design delivered slowly feels broken. Most performance is
decided by design choices: how big the hero image is, how many fonts load, what animates, which third-party
scripts are added. Make those choices with their cost in view, then measure.

Page or concern:

$ARGUMENTS

If this is empty, measure the current project's main pages and fix the biggest problems first.

## Where this sits

- `interaction` decides the loading and feedback states; this skill makes the real waits short and the
  perceived ones shorter.
- `images` decides what images show; this skill delivers them efficiently. `fonts` chooses the faces and
  says to self-host and subset; this skill loads them without shift.
- `motion` decides what moves; this skill keeps it smooth.

## Principles

1. **Core Web Vitals describe what users feel.** Measured at the 75th percentile of real visits:
   **LCP** (Largest Contentful Paint: when the main content appears) at or under 2.5s; **INP** (Interaction to
   Next Paint: how quickly the page responds to input) at or under 200ms; **CLS** (Cumulative Layout Shift: how
   much things jump) at or under 0.1.
2. **Perceived speed counts too.** Show something useful fast: real content before decoration, the layout before
   the details, skeletons shaped like the result. A page that paints its headline and hours instantly feels faster
   than one that waits for a carousel.
3. **The heaviest thing is usually the design's choice.** A full-bleed hero video, five font files, an animated
   background, a chat widget and analytics scripts. Each needs a reason that outweighs its cost.
4. **Reserve space for everything that loads later.** Images, embeds, ads, fonts and late-injected banners cause
   layout shift when they arrive without reserved space.
5. **Keep the main thread free.** Long JavaScript tasks (over 50ms) delay every tap. Less JavaScript is the most
   reliable fix.
6. **Measure on the devices your audience uses.** A mid-range Android phone on a mobile network, not a developer
   laptop on fibre.

## How to work

### 1. Budget the design

Before building, list the page's heavy items and their job: hero media, fonts (families × weights × styles),
scripts, embeds, third-party tags. Set a rough budget, for example: LCP image under ~200KB on mobile, two or three
font files, no third-party script on the critical path. If the direction asks for something heavy (a video hero),
plan how to deliver it (poster image, lazy video, no autoplay on mobile data).

### 2. Images

The usual LCP element, and the usual weight.

- Modern formats (AVIF or WebP with a fallback), compressed to the visual quality the image needs.
- Responsive sizes: `srcset` with widths and an accurate `sizes`, so phones don't download desktop images. Art
  direction (different crops) via `<picture>`, as `images` decides.
- `width` and `height` attributes (or CSS `aspect-ratio`) on every image, to reserve space.
- The LCP image: not lazy-loaded, `fetchpriority="high"`, discoverable in the HTML (not a CSS background or
  injected by JavaScript), and preloaded if it can't be.
- Everything below the first screen: `loading="lazy"` and `decoding="async"`.
- SVG for icons and simple illustration, optimised (SVGO); no PNG icons at 2×.
- Video: `preload="none"` or `"metadata"`, a poster image, no autoplay on phones unless it's essential and muted.

### 3. Fonts

- Self-host (`fonts`' rule), WOFF2, subset to the scripts the site needs, only the weights and styles used. A
  variable font can replace several static files when several weights are used.
- `font-display: swap` (or `optional` for non-essential faces) so text shows immediately.
- Preload the one or two files used above the fold.
- Reduce the swap shift by matching the fallback's metrics: `size-adjust`, `ascent-override`,
  `descent-override` and `line-gap-override` on a fallback `@font-face` built from a local system font.

### 4. CSS and JavaScript

- Inline or prioritise the CSS for the first screen; don't block rendering on large unused stylesheets.
- Ship less JavaScript: static HTML for static content, islands or server rendering for interactive parts, no
  framework for a page that doesn't need one.
- `defer` or `type="module"` for scripts; `async` only for independent ones. No render-blocking third-party
  scripts in `<head>`.
- Load third-party embeds (maps, video, chat, social) on interaction or when near the viewport, with a static
  placeholder of the same size (a "facade").
- Break up long tasks: yield to the main thread between chunks of work (for example `await scheduler.yield()`
  where supported, or `setTimeout`), debounce input handlers, move heavy work off the main thread.
- Give interactions instant visual feedback before the expensive work (update the pressed state, then compute).

### 5. Layout stability

- Reserve space for images, embeds, ads and anything injected (cookie banners as overlays, not pushed content).
- Don't insert content above what the user is reading unless they asked for it.
- Skeletons and placeholders match the final size.
- Fonts: metric-matched fallbacks (above).
- Animations use `transform`, which never shifts layout.

### 6. Rendering and animation

- Animate `transform` and `opacity` (handled by the compositor), not `width`, `height`, `top`, `left`, `margin` or
  `box-shadow` every frame.
- `will-change` only on elements about to animate, removed afterwards; not on everything.
- `content-visibility: auto` with `contain-intrinsic-size` for long pages with many off-screen sections.
- Avoid large `backdrop-filter` blurs and huge fixed backgrounds on mobile; they're expensive to composite while
  scrolling.
- Virtualise very long lists.

### 7. Measure

Use lab tools to diagnose and field data to judge. `references/measuring.md` has commands and how to read them.

1. **Lighthouse** (Chrome devtools or CLI) with mobile emulation and throttling: LCP, CLS, Total Blocking Time (a
   lab stand-in for INP), and the opportunities list.
2. **Performance panel:** record a load and an interaction. Find the LCP element, long tasks, layout shifts (shown
   with the elements that moved) and slow interactions.
3. **Network panel** with throttling ("Fast 4G" or slower) and the cache disabled: what loads, in what order, how
   heavy.
4. **Field data** when the site is live: Chrome UX Report (PageSpeed Insights), or the `web-vitals` library
   reporting to analytics.
5. **Look at it load:** a throttled filmstrip or screen recording. What appears first? Does anything jump? Is
   there a blank moment?

Report the vitals before and after, the LCP element and how it's delivered, the page weight by type, and the
design trade-offs you flagged (anything heavy kept on purpose, and why).

## Mistakes agents make

- Lazy-loading the hero image, or making it a CSS background or JavaScript-injected, so it loads late.
- One huge image served to every screen size; PNG photographs; no `width` and `height`.
- Five or more font files, Google Fonts links instead of self-hosting, no `font-display`, no metric-matched
  fallback.
- A full-page client-side framework for a static marketing page.
- Third-party chat, analytics and embed scripts loaded synchronously on every page.
- Content that fades in on scroll via JavaScript, delaying LCP and causing shifts.
- Animating layout properties; `will-change` on everything; giant blurred fixed backgrounds.
- Cookie banners and promo bars that push content down after load.
- Measuring only on a fast laptop, or optimising a Lighthouse score instead of real users' experience.
