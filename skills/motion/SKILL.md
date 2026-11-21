---
name: motion
description: Decide whether, where and how things move on a website so motion explains change, gives feedback and directs attention instead of decorating. Covers when not to animate, motion hierarchy, timing and duration, easing, transitions between states and views, micro-interactions, scroll-based motion, loading animations, choreography of several elements, a brand's motion character, and reduced-motion preferences. Use when adding or reviewing animation, transitions, hover and press effects, page transitions, scroll effects or loaders, or when a site feels slow, jittery or over-animated. Not for which states exist (`interaction`) or frame-rate problems (`performance`).
argument-hint: "[component, page or effect]"
---

# motion

Motion is information over time. It can show where something came from and went, confirm that an action
registered, connect two states, and point at what changed. It can also slow every interaction, distract from
reading, and make some people physically ill. Every animation needs a job; most interfaces need less motion than
agents add.

Component, page or effect:

$ARGUMENTS

If this is empty, review the motion in the current project.

## Where this sits

- `interaction` decides the states and feedback; this skill decides how transitions between them move.
- `performance` keeps animation smooth (composited properties, main-thread work). `a11y` sets
  the requirements for reduced motion, flashing and auto-playing content.
- `taste` may set a motion character as part of the direction's Surface axis ("quick, mechanical motion").

## Principles

1. **Motion needs a job.** The legitimate jobs: **feedback** (the press registered), **continuity** (this panel
   came from that button), **orientation** (you moved forward a step), **attention** (this changed, look here),
   **status** (still working), and occasionally **character** (a brand moment, once). "It looks nicer" is not a
   job on its own.
2. **Frequency sets the budget.** Something people do hundreds of times a day (typing, opening a menu, switching
   tabs) should be instant or nearly so. Something seen once (a first-run moment) can take longer. Keyboard-driven
   actions usually shouldn't animate at all.
3. **Fast by default.** Most interface transitions sit between about 100 and 300ms. Longer motion has to be
   worth the wait, because the user is waiting.
4. **Easing explains physics.** Things entering decelerate (ease-out) because they arrive; things leaving
   accelerate (ease-in) because they depart; things moving on screen ease in and out. Linear motion looks
   mechanical except for continuous things (progress, rotation of a spinner).
5. **Hierarchy applies to motion.** One thing moves most; related things follow; everything else stays still.
   Several elements animating with equal emphasis is noise.
6. **Respect reduced motion.** When `prefers-reduced-motion: reduce` is set, remove movement that isn't essential
   (slides, parallax, zooms, scroll effects) and keep meaning with fades or instant changes. Vestibular disorders
   are real; parallax and large zooms can trigger nausea.
7. **Interruptible.** A user can act mid-animation; motion must not block input or finish a state the user has
   already reversed.

## How to work

### 1. Audit what wants to move

List each candidate animation with its job, its frequency (once, per visit, per action, constant) and its trigger
(user action, system event, scroll, time). Remove those without a job, and those triggered by time alone that
loop forever (WCAG 2.2.2 requires a pause or stop for anything moving more than five seconds).

### 2. Decide the motion character

The brand's motion should be consistent: one set of durations and easings, used by role. A calm, precise brand
might use short, subtle fades and small offsets; an energetic one might use quicker, springier movement with
more travel. Write it as a few tokens (see `references/timing-and-easing.md`), not per-component improvisation.

### 3. Choose timing and easing

| Change | Typical duration | Easing |
| --- | --- | --- |
| Hover, press, focus feedback | 80–150ms (press can be near-instant) | ease-out |
| Small element appears (tooltip, dropdown) | 120–200ms | ease-out; exit faster than entry |
| Panel, drawer, sheet | 200–350ms, scaled by distance | ease-out on entry, ease-in on exit |
| Modal | 150–250ms | ease-out with a slight scale (0.96 → 1) or fade |
| Page or view transition | 200–400ms | ease-in-out; shorter when frequent |
| Attention cue (a changed value) | 300–800ms, once | ease-out |

Distance and size matter: larger movement needs a little more time, and a phone screen needs less than a large
desktop movement of the same element. Exits are usually faster than entrances; the user has already moved on.

### 4. Build

- Animate `transform` and `opacity`. Animating `width`, `height`, `top`, `left` or `margin` triggers layout and
  stutters (`performance` covers why).
- Use CSS transitions for state changes, keyframes for loops and multi-step sequences, the View Transitions API
  for transitions between views where supported (as progressive enhancement), and a JS library only for physics,
  gestures or complex choreography.
- Write motion tokens as custom properties (`--duration-quick`, `--ease-out`) and use them everywhere.
- Wrap movement in a reduced-motion query:

  ```css
  @media (prefers-reduced-motion: no-preference) {
    .drawer { transition: transform var(--duration-panel) var(--ease-out); }
  }
  ```

  or reduce it explicitly in a `reduce` block. Keep opacity changes and state colour changes; drop travel, scale,
  parallax and scroll-linked movement.
- For scroll-linked motion, prefer CSS scroll-driven animations (`animation-timeline: view()`) with a fallback
  that shows the content in its final state; never hide content until it animates in, because if the script or
  animation fails, it stays hidden.
- Never animate on page load anything the user needs to read first. Content that fades in as you scroll slows
  reading and makes screenshots, anchors and Find-in-page unreliable.

### 5. Choreograph several elements

When several things move together: decide the lead element, move related elements in the same direction with a
short stagger (20–50ms between items, capped so the last item starts within about 200ms), and keep everything
else still. Shared direction reads as one motion; random directions read as chaos.

### 6. Loading motion

- Under about a second: no loader at all, or a delayed one (show only after ~300–500ms) so it doesn't flash.
- Content loading: skeletons shaped like the result, with at most a subtle shimmer.
- Unknown waits over a few seconds: a spinner plus words saying what's happening.
- Long, measurable work: a determinate progress bar.
- Never a fake progress bar that lies.

### 7. Check it

Watch it, don't just read the CSS. In a browser tool, use the animation inspector or slow animations down
(devtools can play them at 10% or 25%) and:

1. Trigger each animation. Can you say its job in one sentence?
2. Repeat the most frequent interaction twenty times. Does the motion start to feel slow?
3. Interrupt: click again mid-animation, reverse, press Escape. Does it respond immediately and stay coherent?
4. Turn on reduced motion (devtools rendering emulation, or the OS setting). Does everything still work and make
   sense, with no movement left that isn't essential?
5. Record or watch at real speed on a phone-sized viewport: any jank, layout shift or content that appears late?
6. Is there more than one thing competing for attention at once?
7. Does anything loop or auto-play for more than five seconds without a pause control? Does anything flash more
   than three times a second (WCAG 2.3.1)?

Report each animation's job, duration and easing, what you removed, and what reduced motion does.

## Mistakes agents make

- Fade-and-slide-up on every section as it scrolls into view.
- Hover effects that scale, lift and glow cards that aren't clickable.
- 500–800ms transitions on menus and tabs used constantly.
- Linear or default `ease` on everything; the same easing for entering and leaving.
- Staggering long lists so the last item appears a second later.
- Parallax backgrounds and scroll-jacking that override the user's scroll.
- Animating `height`, `top` or `box-shadow` every frame.
- Ignoring `prefers-reduced-motion`, or handling it by removing feedback that carried meaning.
- Spinners that flash for 50ms; skeletons that don't match the layout and cause a shift.
- Infinite decorative animations (floating blobs, pulsing badges, gradient sweeps).
