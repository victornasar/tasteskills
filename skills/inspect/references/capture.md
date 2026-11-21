# Capturing views and measuring defects

Patterns for seeing every view that matters. Use whichever tool the project already has; these use Playwright
because it can set widths, trigger states and emulate settings in one place. Adapt them; they aren't a harness to
install for a one-off check.

## Widths and full pages

```js
for (const width of [320, 390, 768, 1024, 1440, 1920]) {
  await page.setViewportSize({ width, height: 900 });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `shots/${name}-${width}-first.png` });
  await page.screenshot({ path: `shots/${name}-${width}-full.png`, fullPage: true });
}
```

Full-page screenshots of long pages are tall: crop or step through them screen by screen to look at full size.
Without Playwright, headless Chrome takes a single view:

```bash
"<path to Chrome>" --headless --screenshot="$PWD/shot.png" --window-size=390,844 "http://localhost:3000/"
```

## States

Trigger them the way a person would, so the real CSS and script run.

```js
await page.hover('button.primary');                    // hover
await page.keyboard.press('Tab');                      // focus-visible: Tab, don't call .focus()
await page.click('form button[type=submit]');          // submit empty to see errors
await page.click('[aria-expanded="false"]');           // open menus, accordions, dialogs
await page.locator('.card').first().screenshot({ path: 'shots/card-hover.png' });
```

For loading states, slow the network or hold a request open:

```js
await page.route('**/api/**', async route => { await new Promise(r => setTimeout(r, 4000)); route.continue(); });
```

For empty, error and long-content states, use the app's own fixtures or mock the response with `page.route`
returning an empty list, an error status, or the longest real data.

## Settings

```js
await page.emulateMedia({ colorScheme: 'dark' });
await page.emulateMedia({ reducedMotion: 'reduce' });
await page.emulateMedia({ forcedColors: 'active' });
await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; }); // rough text-size check
```

## Measurements that find defects faster than looking

Run these in the page (`page.evaluate` or the devtools console). They point at where to look; the screenshot
still decides.

**Horizontal overflow** (anything wider than the viewport):

```js
[...document.querySelectorAll('body *')]
  .filter(el => el.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
  .map(el => el.tagName + '.' + el.className);
```

**Clipped text** (content larger than its box where overflow is hidden):

```js
[...document.querySelectorAll('body *')].filter(el => {
  const s = getComputedStyle(el);
  return (s.overflow.includes('hidden') || s.textOverflow === 'ellipsis') &&
    (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1);
}).map(el => el.textContent.trim().slice(0, 60));
```

**Did the chosen font load?** `document.fonts.check('16px "Face Name"')` returns false when the page is showing a
fallback. Check each family and weight the direction uses.

**Near-duplicate values** (the inconsistencies that are hard to see):

```js
const count = prop => {
  const seen = {};
  document.querySelectorAll('body *').forEach(el => {
    const v = getComputedStyle(el)[prop];
    seen[v] = (seen[v] || 0) + 1;
  });
  return Object.entries(seen).sort((a, b) => b[1] - a[1]);
};
count('fontSize'); count('color'); count('borderRadius'); count('boxShadow');
```

Values that appear once or twice next to a common neighbour (15px beside 16px, `#6b7280` beside `#6b7380`) are
usually drift. Compare them with the tokens before changing anything.

**Layout shift** while the page loads:

```js
new PerformanceObserver(list => list.getEntries().forEach(e =>
  console.log(e.value.toFixed(3), e.sources?.map(s => s.node))
)).observe({ type: 'layout-shift', buffered: true });
```

**Left edges** on a screen: collect `getBoundingClientRect().left` of visible text blocks, round to whole pixels
and count them. Edges a few pixels apart are almost always unintended.

## Before and after

Save the before screenshot of each finding under the same name pattern as the after (`card-390-hover-before.png`,
`card-390-hover-after.png`) and look at them side by side. A fix you can't show in a before-and-after pair hasn't
been verified.
