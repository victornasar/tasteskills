---
name: conversion
description: Audit a website, landing page or flow from the side of the visitor who should act. Works out who they are, how ready they arrive, what they need to believe and what worries them, then walks the whole path from first screen to confirmation. Maps objections to evidence, counts friction, checks trust, and recommends changes tied to this audience and its evidence rather than generic CRO tactics, with no dark patterns. Use when a page isn't converting, before launching a landing page, sign-up, pricing page or checkout, or when asked for a conversion or CRO review. Not for writing the copy (`content`), ranking emphasis (`hierarchy`), choosing sections (`layout`) or designing form behaviour (`interaction`); it diagnoses and routes each fix to them.
argument-hint: "[page or flow, and its goal if known]"
---

# conversion

A page converts when the right visitor understands the offer, believes it, sees how to act, and finds acting
easy and safe. Most pages that don't convert fail one of those for a reason you can see once you look from the
visitor's side. Generic advice skips that step: urgency timers, bigger buttons, "add social proof" and "put it
above the fold" get applied to every page, and help only by accident. Work out who this visitor is and what
stops them, then fix that.

Page or flow:

$ARGUMENTS

If this is empty, audit the current project's main page and its primary action. Read `DIRECTION.md` if it exists:
its audience, the page's one job and the positioning are the starting point.

## Where this sits

- `layout` orders the sections by the visitor's questions; `content` writes the answers and the calls to action;
  `hierarchy` makes the decisive facts and the action prominent; `interaction` designs forms, steps and errors;
  `performance` makes it fast. Each owns its fix.
- This skill owns the diagnosis across them: the goal, the visitor's readiness, the objections and the evidence
  that answers them, the friction along the whole path, and trust. It names whose area each fix falls in and
  makes it with that skill's rules.
- taste's copy rule applies: never invent testimonials, numbers, logos, guarantees or scarcity.

## Principles

1. **One goal, one visitor first.** Name the action (book, buy, sign up, call, ask for a quote) and the visitor
   it's for. A page built for everyone persuades no one; other audiences get a clear path, not the page.
2. **Readiness decides what the page must do.** Someone who already knows what they want needs the price,
   availability and the button. Someone who doesn't yet know the category exists needs the problem first.
   Eugene Schwartz's stages of awareness are a useful frame. Mismatch is the commonest failure: asking for a
   demo before saying what the product does, or burying "Book" under an essay for returning customers.
3. **Objections are specific and answerable.** "Will it work for a team my size?", "What happens after I
   submit?", "Does the price go up after the trial?" Each has an answer the page can give, with evidence, at the
   moment the question comes up. A generic trust badge answers none of them.
4. **Evidence beats assertion.** A named testimonial that says something specific, a visible price, a real photo
   of the place, a sample of the output, the returns policy in one sentence. "Trusted by thousands" is not
   evidence.
5. **Friction adds up, and most of it is unnecessary.** Every field, step, required account, surprise cost and
   unclear label loses some visitors. Baymard Institute's checkout research has found, year after year, that
   unexpected extra costs, forced account creation and long or complicated checkouts are among the top reasons
   people abandon. Remove friction before adding persuasion.
6. **Persuade honestly.** No fake scarcity or countdowns, pre-ticked add-ons, costs revealed at the last step,
   confirmshaming ("No thanks, I don't like saving money"), cancellation made harder than sign-up, or invented
   social proof. Regulators in the EU (the Digital Services Act) and the US (FTC enforcement) treat many of these
   as unlawful, and all of them spend the trust the page is trying to earn.

## How to work

### 1. Define the goal and the visitor

Write down:

- **The action**, and what counts as done: a submitted form, a paid order, a phone call.
- **The visitor it's for, and how they arrive:** searching for a known need, clicking an ad with a promise,
  referred by a friend, returning to buy again. Where they come from sets how ready they are.
- **Secondary actions and audiences**, which get quieter paths.

If the page has no single goal, that's the first finding.

### 2. Walk the path as the visitor

Start where they start: the ad, search result or link, if you know it, because the page has to continue that
promise. Go through the first screen, to the action, and through every step after it: the form, the checkout,
the confirmation, the email that follows. Do it on a phone first when most visitors are on phones, then on
desktop. At each step, write what the visitor knows, what they're asking and what they have to do. Use the
rendered site, and complete the flow where it's safe (test mode, staging).

### 3. Map objections to evidence

List the likely objections from the brief, the category, and anything the user has: support questions,
reviews, sales calls. Most fall into a few families: does it fit me, does it work, what does it really cost,
what happens next, what if it goes wrong, and who is behind it.

| Objection | Evidence that answers it | Where it appears | Before the moment it's needed? |
| --- | --- | --- | --- |
| "Can I cancel?" | Monthly plan, cancel in settings | FAQ at the bottom | No: the trial button raises it first |

Where evidence is missing, ask the user for it or mark the gap. Never fabricate it.

### 4. Count the friction

For the whole path, list the steps, fields, choices, required accounts, surprise costs, unclear labels, errors
met, waits, distractions that lead off the path, and anything that breaks on a phone. For each, ask: is it
needed, is it needed now, and can it be removed, deferred, defaulted or made clearer? Some friction earns its
place: a postcode that pre-fills delivery options, a confirmation step before a large payment. Remove what isn't
needed, not everything.

### 5. Check clarity and the action

- **Five seconds on the first screen:** what is this, who is it for, what do I do next?
- **Message match:** does the page continue the promise that brought them?
- **The primary action:** one, named by what happens ("Book a table", not "Submit"), present where the visitor
  becomes ready (on a long page that's often more than once), and distinct from secondary actions.
- **Price and terms:** visible where the decision is made, as the total, with what's included.

### 6. Check trust

Is there a real name, place and people behind it? Is the proof near the claim it supports, and real? Are
policies plain and easy to find? Does everything work? A typo in the price, a broken image or a form error with
no message costs trust quickly. Is anything on the honesty list above present?

### 7. Recommend

For each recommendation, write: what you saw and where → why it costs this visitor (the objection or friction
it maps to) → the change → the skill whose area it is → how confident you are, and on what evidence. Rank by
likely effect on the goal and by effort. Prefer removing friction and supplying missing evidence over adding
persuasion.

### 8. Measure, if there's traffic to measure

- If analytics exist, find the step where visitors drop off and look there first. The data says where; walking
  the path says why.
- A/B tests need traffic. As an example, not a threshold: under the usual assumptions (5% significance, 80%
  power), detecting a 10% relative lift on a 3% conversion rate takes around 50,000 visitors per variant. The
  real number depends on the baseline, the size of change worth detecting and the test design, so work it out
  with a sample-size calculator for the case in hand. The order of magnitude is the point: most small sites
  can't run conclusive tests, so fix the clear problems, watch the numbers, and talk to customers instead.
- Decide a test's length and success measure before starting it. Don't stop it the first time it looks good.

Report the goal and visitor, the path you walked, the objection map with its gaps, the friction list, the ranked
recommendations with their owners, what the client needs to supply, and what you couldn't test.

## Generic advice to look past

- **Button colour as a strategy.** Contrast with the surroundings matters; a hue on its own doesn't.
- **Countdown timers and "only 2 left"** that aren't true.
- **"Everything above the fold."** People scroll when the first screen promises something worth scrolling for.
  What matters is that it answers the first question and the action is there when they're ready.
- **Logo walls and star ratings** with no source.
- **Pop-ups and chat widgets** covering the page on arrival.
- **Shortening every form** regardless of what the fields do later.
- **Copying a famous site's page** because it converts for them: their visitor, readiness and offer aren't yours.

## Mistakes agents make

- Auditing a page without naming the action or the visitor.
- Stopping at the button and never walking the form, checkout, confirmation or email.
- Recommending "add testimonials", then inventing them.
- Adding urgency, scarcity or pop-ups as fixes.
- Auditing on desktop for an audience that's mostly on phones.
- Hiding the price behind "contact us" when cost is the visitor's first question, with no reason.
- Several equally loud calls to action, so none of them is the action.
- Presenting a recommendation as proven: "this will increase conversions by 20%".
