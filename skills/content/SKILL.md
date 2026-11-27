---
name: content
description: Write and structure the words on a website so they say something specific, in the brand's own voice, in the order visitors need. Covers the messaging hierarchy, headlines, specificity and evidence, clarity and plain language, brand voice, content structure and scannable writing, calls to action, microcopy (labels, errors, empty states, confirmations), storytelling, removing generic AI-generated marketing language, and cutting UI text that over-explains. Use when writing or editing site copy, headlines, CTAs, product descriptions, error messages or UI text, when a page sounds like every other AI-written site, or when an interface has too much text. Not for how prominent each piece looks (`hierarchy`) or which sections exist (`layout`).
argument-hint: "[page, brief or copy to write or edit]"
---

# content

Visitors came with a question. The words either answer it, specifically, in a voice that sounds like this
business, or they fill space. Most AI-written copy fills space: it could describe any company, promises outcomes
nobody can check, and uses the same handful of words on every site. Write from the facts of the brief, in the
order of the visitor's questions, and cut everything that would fit a competitor equally well.

Page, brief or copy:

$ARGUMENTS

If this is empty, review the copy on the current project's pages. Read `DIRECTION.md` if it exists: its values,
positioning and "differentiate on" line are the raw material.

## Where this sits

- `layout` decides which sections exist from the visitor's questions; this skill writes what each one says.
- `hierarchy` decides how prominent each piece is; this skill makes sure the prominent pieces are worth it.
- `interaction` decides when labels, errors and confirmations appear; this skill writes them.
- `conversion` audits whether the page gets its visitor to act, and routes copy fixes here.
- taste's copy rule applies throughout: don't invent claims, customers, numbers or testimonials the brief doesn't
  make.

## Principles

1. **Specific beats impressive.** "Fresh sourdough from 7am, until it runs out (usually by 2)" says more than
   "Artisanal baked goods crafted with passion." Specific copy contains things that could be checked: numbers,
   names, places, times, prices, materials, steps.
2. **Answer the visitor's question, in their words.** Use the words visitors would type into a search, not the
   company's internal names. "Fix a leaking tap" not "Water ingress solutions".
3. **Lead with the point.** Inverted pyramid: the most important thing first in the page, the section, the
   paragraph, the sentence, the button. People read a fraction of the words; make it the right fraction.
4. **Plain language is not dumbing down.** Short sentences, common words, active voice, one idea per paragraph.
   Experts prefer it too: they're busy.
5. **Voice is consistent choices, not adjectives.** "Friendly but professional" is not a voice. A voice is
   decisions: contractions or not, "we" and "you" or not, humour or none, jargon level, sentence length, what the
   brand never says.
6. **Every claim needs evidence on the page, or it goes.** "Trusted by thousands" without names or numbers is
   noise; one real, attributed detail beats ten adjectives. Never invent the evidence.
7. **Fewer words.** AI-written interfaces over-explain: every screen describes itself, answers questions nobody
   asked and covers edge cases up front. The fix is cutting, not rephrasing more briefly. A word stays only if
   the visitor would miss it.

## How to work

### 1. Build the messaging hierarchy

Before writing, write down:

- **The one thing** this page must get across (one sentence; the brief's "differentiate on" if there is one).
- **The visitor's questions**, in order (from `layout`'s plan if it exists).
- **The proof** available for each answer: facts, numbers, names, examples, the product itself. Mark what's
  missing; ask the user for it or leave a clearly marked gap, never fabricate.
- **The action** the page asks for, and what the visitor needs to believe before taking it.

### 2. Write headlines

A headline is the answer or the claim, not a label or a mood. Test each against:

- **Specific:** would it be false for a competitor? If it would be equally true for them, rewrite it.
- **Concrete:** does it contain something you could picture or check?
- **Short enough:** often under about ten words for a hero; it has to stay readable at display size on a phone.
- **In the voice:** would the owner say this out loud to a customer?

Write five to ten options, then pick. Section headings follow the same rule: "Open until 4pm today" beats
"Opening hours"; "Pay only for the API calls you make" beats "Flexible pricing". Some sections are better with
a plain label (Menu, Contact, Prices) because people hunt for the word; use labels where the visitor is looking for
a known thing, claims where they need persuading.

### 3. Write the body

- Front-load sentences and paragraphs.
- One idea per paragraph; two to four sentences.
- Lists for parallel items; tables for comparable ones; numbered steps for sequences.
- Replace adjectives with the facts behind them ("handmade" → "shaped by hand, 40 loaves a morning").
- Cut warm-up sentences ("In today's world…", "We believe that…") and wind-downs ("…and so much more").
- Read it aloud. Rewrite anything you wouldn't say.

### 4. Write calls to action

- Name the action and, where useful, the outcome: "Book a table", "Get the price list (PDF, 2 pages)", "Start
  a 14-day trial — no card needed" (only if true).
- One primary call to action per view; secondary actions as quieter links.
- Match the visitor's readiness: "See how it works" before "Buy now" for a considered purchase.
- Avoid "Get started", "Learn more" and "Submit" when a specific verb exists; they say nothing about what happens.

### 5. Write microcopy

Labels, hints, errors, empty states, confirmations and loading text are where clarity matters most and voice
matters least. `references/voice-and-microcopy.md` has patterns. The core rules: say what happened and what to do
next, unless the screen already shows it; never blame the user; use the same word for the same thing
everywhere; keep jokes out of errors. Microcopy is the first place over-explaining shows up, so write the
shortest version first and add words only when something is missing.

### 6. Tell the story only if there is one

Storytelling works when there's a real sequence: a problem the customer recognises, a turning point, a result
with specifics. A founder story belongs on the page when it explains something the visitor cares about (why the
bread is made this way); otherwise it's padding. Customer stories need real customers, named with permission.

### 7. Remove generic language

Run the generic-language check in `references/voice-and-microcopy.md`: the words, structures and claims that mark
AI-written marketing copy. Then the copy swap test: put a competitor's name on the page. Every sentence that
still works is a candidate for rewriting with a specific fact or cutting.

### 8. Cut

Go screen by screen and count the words. Then cut, in this order:

1. **Text the screen already says.** A subheading that restates the heading, a sentence that repeats the label
   above it, "Check your email" followed by "We've sent a link to your email".
2. **Text the interface can show instead.** A disabled "Send again in 0:59" replaces "Nothing after a few
   minutes? You can request another link." A highlighted row replaces a sentence saying which plan is cheapest.
3. **Instructions for the obvious.** "Click the button below to…", "Enter your email address in the field",
   "Here you can manage…".
4. **Edge cases and fine print up front.** Move what few visitors need behind a disclosure, a link or the
   state where it applies: "Already invited?", "How we compared", a link's expiry time shown only on the expired
   link page.
5. **Filler and politeness.** "Please", "successfully", "simply", "just", "at this time", "Don't worry".
6. **Paragraphs where a phrase works.** "You haven't created any projects yet" → "No projects yet".

Keep the specific fact that answers the visitor's question (their place in line, the address the link went to,
"$19 vs $30"), the action, anything needed to decide, warnings and legal text. If a cut makes the screen
ambiguous, put the words back.

There's no target count, and the voice sets how terse the copy can be. But a task screen (sign-in, waitlist,
settings, confirmation) rarely needs more than a heading, one line and its actions. When an AI-written screen
loses half its words after this pass, that's normal.

### 9. Check it in place

Read the copy on the rendered page, not in a document:

1. **Headlines only.** Read just the headings and buttons. Do they tell the story and answer the first question?
2. **Five seconds.** What does the first screen say this business does, for whom, and what to do next?
3. **Fit.** Does the headline wrap well on a phone? Do buttons fit their labels? Does any text get truncated?
4. **Swap test** on every headline and the first paragraph of each section.
5. **Microcopy pass:** trigger every error, empty and success state and read what it says.
6. **Word count.** Count the words on each screen. For each sentence: would the visitor miss it? If not, cut it.
7. **Invented claims:** list every number, name, testimonial and superlative. Is each in the brief? If not, remove
   it or mark it for the client.

Report the messaging hierarchy, the voice decisions, what you cut (with word counts before and after), and what facts the client needs to supply.

## Mistakes agents make

- Copy that could describe any company in the category, or any category.
- The AI marketing vocabulary: "elevate", "unlock", "seamless", "empower", "revolutionise", "cutting-edge",
  "next-level", "crafted with passion", "your journey".
- Structures on repeat: "Not just X — it's Y", "Whether you're A or B, …", three-adjective lists, rhetorical
  questions as headings.
- Invented testimonials, customer logos, statistics ("10,000+ happy customers") and awards.
- Headings that are labels ("Our Features") where a claim was needed, or claims where people hunt for a label.
- "Learn more", "Get started", "Submit" everywhere.
- Long intros before the point; the important fact in the last sentence.
- Over-explaining: a description under every heading, helper text under every field, a sentence explaining
  each button, edge cases and methodology spelled out on the main screen.
- Saying in words what the interface already shows: a countdown, a disabled state, a highlighted row, the
  email address in the field.
- Friendly jokes in error messages; blaming the user ("You entered an invalid…").
- Inconsistent terms for the same thing (booking, reservation, appointment on one page).
- Title Case Headlines Everywhere when the brand's voice is plain.
