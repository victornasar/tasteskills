# Voice, microcopy and generic language

## Defining a voice

A voice is a set of decisions you can check. Write it as a short table in `DIRECTION.md` or alongside the copy:

| Decision | Example position | Example position |
| --- | --- | --- |
| Person | "We" and "you" | Third person, institutional |
| Contractions | Always ("we're", "you'll") | Never |
| Sentence length | Short, often fragments | Full, measured sentences |
| Vocabulary | Everyday words, the trade's terms explained | Technical terms used precisely, not explained |
| Humour | Dry, occasional, never in errors | None |
| Confidence | States facts plainly, no hedging | Careful, qualified claims (medical, legal, financial) |
| Formality | Talks like the owner at the counter | Talks like a letter from a solicitor |
| Never says | "Delicious", "artisanal", exclamation marks | "Cheap", slang |

Derive each position from the brand's values and audience. Two bakeries can have opposite voices: one chatty and
local, one exact and quiet. Neither is "friendly but professional".

**Tone** varies within a voice by situation: celebratory on a confirmation, calm and plain on an error, direct on
a warning. The voice stays the same.

## Generic language check

Words, structures and claims that mark copy as generated or templated. None is banned; each needs a reason.
When you find one, replace it with the specific fact it was standing in for, or cut it.

**Words and phrases**

- elevate, unlock, unleash, empower, supercharge, revolutionise, transform, reimagine
- seamless, effortless, frictionless, hassle-free, intuitive, robust, powerful, cutting-edge, state-of-the-art,
  next-level, world-class, best-in-class, innovative, game-changing
- crafted, curated, bespoke, artisanal, passion, journey, story (as in "our story" with none), experience (as in
  "the X experience")
- "In today's fast-paced world", "In an ever-changing landscape", "Look no further", "Say goodbye to…", "Take your
  X to the next level", "We've got you covered", "Designed with you in mind", "And so much more"
- delve, tapestry, testament, realm, navigate (metaphorically), harness, leverage (as a verb), foster

**Structures**

- "Not just X. It's Y." / "More than just X."
- "Whether you're a A, B or C, …"
- Lists of exactly three adjectives ("fast, simple and secure").
- Rhetorical questions as headings ("Tired of slow invoices?").
- Every section starting with a one-word label and a colon, or an emoji.
- A headline, then a subheading that restates it with more adjectives.
- Ending paragraphs with an uplifting summary sentence.

**Claims**

- Superlatives without evidence ("the best coffee in town").
- Vague social proof ("Trusted by thousands", "Loved by teams everywhere").
- Unquantified outcomes ("Save time and money", "Boost productivity").
- Invented specifics: numbers, customers, testimonials, awards, press logos. Never write these unless the brief
  provides them.

**The test.** For each sentence: is there a fact in it a competitor couldn't also claim? If not, find the fact
(ask the user if needed) or cut the sentence.

## Before and after

| Generic | Specific (only with facts from the brief) |
| --- | --- |
| Elevate your morning with our artisanal, handcrafted breads. | Sourdough, rye and baguettes from 7am. Usually sold out by 2. |
| Seamless invoicing that empowers your business to thrive. | Send an invoice in under a minute. Get paid by card or bank transfer. |
| Not just a daycare — a second home. | Open 7:30 to 6. Twelve children, three qualified carers, a garden. |
| Get started | See prices · Book a visit · Create an account |
| Trusted by thousands of happy customers | "We've ordered our office bread here for six years." — Ana, Hill Street Dental |

## Over-explained and cut

| Over-explained | Cut |
| --- | --- |
| There are no notifications for you at this time. | No notifications |
| Your changes have been successfully saved. | Saved |
| Please enter your email address to continue. | Email address (as the label) |
| Here you can manage all of your account settings. | Account settings (as the heading) |
| Check your email. If there's a place for this address, a link is on its way. Nothing after a few minutes? Look in spam, or check the address. [Send again] | Check your email · sam@example.com · [Send again in 0:59] [Change address] |
| You're number 4 on the waitlist. Got an email saying you're in? Sign in with that address, or get a sign-in link sent to it. The link works once, for 30 minutes. | You're number 4. We'll email you when a place opens. [Already invited?] |

## Microcopy patterns

**Labels**

- Nouns for fields ("Email address"), verbs for buttons ("Save changes").
- Sentence case. Don't end with a colon in modern UIs unless it's the house style.
- Add a hint only where people would otherwise get it wrong ("Day, month, year"). Most fields need none.

**Buttons**

- Verb + object: "Send invoice", "Delete 3 files", "Book for Saturday".
- The button says what will happen, matching the heading or question it answers. A dialog titled "Delete
  invoice?" has a button "Delete invoice", not "Yes" or "OK".

**Errors** (what happened, why if useful, how to fix)

| Avoid | Prefer |
| --- | --- |
| Invalid input. | Enter a date in the future. |
| Error 422. | Couldn't save. Check your connection and try again. |
| Oops! Something went wrong 🙈 | Payment declined. You weren't charged. |
| You entered an incorrect password. | Wrong password. [Reset it] |

**Empty states**

- What's missing and the action that fills it: "No invoices yet. [Create invoice]". Explain why it's empty only
  when the reason isn't obvious (a filter, missing permission).
- For no search results: what was searched, and how to widen it: "No results for "sourdugh". [Clear filters]".

**Confirmations**

- What happened, with the specifics the person will check: "Booked: Sat 14 March, 3pm, 4 people." Routine
  actions need a word, or none when the change is visible: "Saved".

**Loading and progress**

- Say what's happening only when it takes more than a few seconds: "Checking availability…", "3 of 12".

**Consistency**

Keep a short glossary: one term per concept (booking or reservation, basket or cart, sign in or log in). Use it
everywhere, including the URL and the button.

## Plain language checks

- Average sentence length under about 20 words; no sentence over about 35 unless it's a list.
- Active voice by default ("We'll email you" not "You will be emailed").
- Common words: use, help, start, about, buy — over utilise, facilitate, commence, regarding, purchase, unless the
  voice calls for formality.
- Explain or cut jargon the audience doesn't use.
- Numbers as numerals ("3 days", "£12"); dates unambiguous ("Saturday 14 March").
- Link text that makes sense on its own: "Download the price list (PDF)" not "click here".

## Scannable structure

- Headings that summarise their section.
- Short paragraphs, front-loaded.
- Bulleted lists for three or more parallel items; keep bullets parallel in grammar.
- Bold sparingly for the words people scan for, consistently by role (`hierarchy` covers the visual side).
- Put the answer before the explanation: "Yes, we deliver within 5 miles. Orders before 11am arrive the same day."
