# Timing, easing and motion tokens

## Why these numbers

- About **100ms** is the threshold where a response feels instantaneous; about **1 second** is where a user's
  flow of thought stays uninterrupted (Card, Moran and Newell; Nielsen's response-time limits). Feedback must
  start inside the first; transitions should finish well inside the second.
- Very short transitions (under ~100ms) are often imperceptible as motion and read as a flicker; very long ones
  (over ~500ms for frequent interactions) read as sluggish.
- Perceived duration depends on distance and size: a tooltip moving 4px and a sheet moving 600px can't share one
  duration and feel equally quick.

These are starting points to tune by watching, not rules.

## Easing curves

| Name | `cubic-bezier` | Use for |
| --- | --- | --- |
| Ease-out (decelerate) | `0.2, 0, 0, 1` or `0.16, 1, 0.3, 1` (stronger) | Elements entering; responses to user input |
| Ease-in (accelerate) | `0.4, 0, 1, 1` | Elements leaving the screen |
| Ease-in-out (standard) | `0.4, 0, 0.2, 1` | Elements moving from one place to another on screen |
| Linear | `0, 0, 1, 1` | Continuous motion: spinners, progress, marquee-like tickers |

CSS's built-in `ease` is a mild ease-in-out that's rarely the best choice; name your curves.

**Springs** (physics-based motion, via a JS library or CSS `linear()` approximations) suit direct manipulation:
dragging, flicking, sheets that follow a finger. They handle interruption naturally because they continue from
the current velocity. Keep bounce low for interface elements; overshoot reads as playful and gets tiring.

## Motion tokens

Define motion once, by role:

```css
:root {
  --duration-instant: 80ms;   /* press, toggle feedback */
  --duration-quick: 150ms;    /* hover, tooltips, small reveals */
  --duration-panel: 250ms;    /* menus, drawers, modals */
  --duration-view: 350ms;     /* view and page transitions */

  --ease-out: cubic-bezier(0.2, 0, 0, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
}
```

A brand's character changes the values, not the roles: a precise, quiet brand might shorten durations and reduce
travel; an energetic one might use stronger ease-out and a little more travel.

## Patterns

**Enter and exit asymmetry.** Entering elements take slightly longer and decelerate; exiting elements are faster
and accelerate. The user wants what they summoned, and wants what they dismissed gone.

**Origin.** Things should appear from where they were invoked: a menu grows from its button
(`transform-origin` at the trigger), a sheet slides from the edge it lives at. Elements scaling from their centre
when they came from a corner break continuity.

**Small travel.** Entrances need only a few pixels of movement (8–16px) with a fade to suggest direction. Large
travel is for things that really move across the screen.

**Shared element transitions.** When a thumbnail becomes a detail view, morphing the same element keeps the
user oriented. The View Transitions API (`view-transition-name`) supports this for same-document transitions in
current browsers; check support and treat it as enhancement.

**Attention without distraction.** To show that a value changed (a basket count, a total), a brief highlight
or a single pulse is enough. Never loop.

**Micro-interactions.** A micro-interaction has a trigger, rules, feedback and sometimes a loop or mode (Dan
Saffer's model). Good ones confirm an action in the place it happened: a toggle's knob slides, a copy button
briefly shows "Copied", a heart fills. They should be quick enough to be invisible on the hundredth use.

## Scroll-based motion

Acceptable when the motion explains something tied to position: a progress indicator for reading, a diagram that
builds as you reach each step, a sticky element that changes state at a section. Unacceptable when it delays
reading (content waits to fade in), hijacks scrolling speed or direction, or moves backgrounds at different
speeds for no reason (parallax is a common vestibular trigger).

Build it so the content is fully visible and usable without the effect, with reduced motion, and if JavaScript
fails.

## Reduced motion

`prefers-reduced-motion: reduce` means "reduce", not "remove all feedback". Under it:

| Keep | Replace or remove |
| --- | --- |
| Colour and opacity changes for state | Slides, zooms, scale-up entrances → fade or instant |
| Instant appearance of menus and dialogs | Parallax, scroll-linked movement → static |
| Determinate progress bars | Auto-playing video and animated backgrounds → paused, with a play control |
| Focus and pressed states | Spinning or bouncing decoration → static |

WCAG references: 2.2.2 Pause, Stop, Hide (A) for anything moving, blinking or scrolling for over five seconds;
2.3.1 Three Flashes or Below Threshold (A); 2.3.3 Animation from Interactions (AAA) for motion triggered by
interaction, which `prefers-reduced-motion` handling satisfies in practice.
