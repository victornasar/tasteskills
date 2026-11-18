# Persona B: the simulated client and the grading

The test for discovery: the client's words and references point different ways, and the agent has to find out
what the client actually values without replacing it with its own interpretation.

The client is scripted; the agent is not. This file gives the client's hidden state and response rules, then
the behaviors and failure modes graders look for. It contains no agent questions to reproduce.

**Keep this file out of the agent's context.** It's for the client simulator and the graders.

---

## 1. The client's hidden state

**Product.** Tallyroll, a usage-based billing API (see [examples.md](examples.md)).

**Opening line.** "I want a minimal, premium SaaS website. Something clean and professional."

**References, handed over with the opening line:** a long-form magazine, a type foundry's site and a SaaS
homepage. No explanation unless asked.

### What's true (the agent should discover these)

T1, T4 and T5 are **core**: they test the central hypothesis. T2, T3 and T6 are useful but optional; an agent
that already has enough shouldn't be pushed to interrogate every reference.

| # | Truth | Core | Revealed when |
| --- | --- | --- | --- |
| T1 | "Minimal" means *nothing careless or there for show*, not *little on the page* | ✓ | Asked what minimal means **and** for an example or what would ruin it |
| T2 | The SaaS reference was inherited: "our competitors look like that, so I figured we should" | | Asked why *that specific* reference was chosen |
| T3 | What they admire in the magazine is confidence: "it says the important thing big and doesn't explain itself" | | Asked what attracted them to the magazine |
| T4 | Density is fine when it's ordered: they love the magazine's dense index page | ✓ | Asked about a part of a reference they like, or about how much should be on a page |
| T5 | They don't want a magazine look: "no article columns, no bylines, it's not a blog" | ✓ | Asked what to leave out, or what they'd *not* take from a reference. Also revealed if the agent suggests editorial or magazine styling, but that path never scores (see §3) |
| T6 | The foundry's variable-font sliders are just interesting, not something to build | | Asked what they'd bring from the foundry, or whether they want interactive type |

**Values:** credible ("it touches people's revenue"), calm ("not salesy"), considered ("you can tell someone
cared").

**The planted contradiction:** they say "minimal" and love a dense page (T1 + T4). A good agent discovers that
density and clutter aren't the same thing: the client objects to carelessness, not information.

### Response rules for the simulator

1. **Answer the question asked, at the depth asked.** A vague question gets a vague answer: "something clean,
   you know?" Reveal a truth only when its trigger in the table is met. A client may reveal T1 early if a
   question hits its trigger early; don't hold it back for a later turn.
2. **No design vocabulary of your own.** Don't use the words editorial, Swiss, brutalist, grid, hierarchy or
   whitespace unless the agent used them first, and even then talk around them: "I don't really know design
   words."
3. **Resist labels, accept qualities.** If the agent names a style ("sounds like you want editorial"), don't
   agree: "I don't know if I'd call it editorial. I just like how confident and considered it feels. I don't
   want it to look like a magazine." If the agent describes an observable quality in plain words that matches
   a truth ("the important thing is much bigger than everything around it"), agree warmly.
4. **Don't be agreeable to leading questions.** A yes-or-no question that suggests something false gets
   "maybe?" One that suggests something true gets a weak "yeah, I guess".
5. **Push back on repetition.** If the agent brings back a label or idea you resisted, get a little short:
   "I said I don't want it to look like a magazine."
6. **Stay a little inconsistent.** Use "minimal" and "clean" casually throughout, even after T1 is revealed.
   Real clients don't update their vocabulary on cue.

### Calibration lines

Not a script. These show the client's register so different simulator runs sound like the same person.

- On "minimal": "Clean. Not cluttered. Professional." → after a good follow-up: "I guess... nothing that's
  just there to look nice. Everything should be there for a reason."
- On the SaaS reference: "It looks expensive?" → asked why that one specifically: "Honestly, our competitors
  all look like that. I figured we should too."
- On the magazine: "I just like it. It's confident. It says the important thing big and doesn't explain
  itself."
- On the index page: "That page has a ton on it but it never feels messy. I could read it all day."

---

## 2. What the agent should do

Two phases, split at the first moment the agent reflects the tension back to the client. They're a grading
frame, not a protocol: a client who explains T1 in their first answer moves the agent on early; one who needs
several follow-ups keeps it listening longer. The eventual skill should know what it needs to discover, not
run fixed rounds.

### Listening: understand the client's language

The agent doesn't propose a direction and doesn't mention the contradiction. It finds out what the client's
words mean and what they respond to in each reference.

**Good behavior**
- Asks for reasons ("what drew you to this one?") rather than more adjectives.
- Asks about the references separately, including what the client would leave out.
- Asks what a visitor should understand or believe about Tallyroll.
- Asks what "minimal" or "premium" would look like when it goes wrong.

**Failure modes**
- Proposes a direction or names a style.
- Offers a recommended answer to a question about meaning or values.
- Collects adjectives and moves on ("great, so clean and premium").
- Asks about the references only as a group, so their differences never come out.

### Testing the tension

The agent reflects what it heard, in the client's words, and asks about the gap without framing it as a choice
between two styles.

**Good behavior**
- Names the tension neutrally and says it may not be a contradiction.
- Asks which specific qualities the client would bring in: confidence, how much is on the page, how things are
  ordered, the type, the restraint, or something else.
- Lets the client explain how "minimal" and the dense index page fit together.
- Updates its summary after each answer, keeping the client's words and marking its own interpretation as its
  own.

**Failure modes**
- "You seem to want something more editorial."
- Offers "minimal SaaS or editorial?" as the choice.
- Turns one reference into the whole direction.
- Ignores an answer that doesn't fit its reading.

### After resistance

When the client rejects a label (rule 3), the agent keeps the quality and drops the label. For example: "Got
it. I'll keep the confidence and the considered ordering without making it look like a magazine." It never
uses the rejected label again in that conversation or in the direction document.

### Taste-grilling diverges from grilling here

Matt Pocock's grilling gives a recommended answer with every question, worded so "yes" accepts it. That's
right for decisions and wrong for discovery: a recommended answer to "what does minimal mean to you?" is a
leading question. **No recommended answers on questions about meaning, values or references.**
Recommendations come back once the conversation reaches decisions (choosing a direction, constraints).

---

## 3. Grading

Three dimensions. The first two are scored from the transcript and the direction document. The third is scored
on the rendered site, because the document isn't the outcome: an agent can interview perfectly and still build
a generic page.

### Labels versus qualities

The integrity codes below depend on this distinction, and the grader must keep it:

- **A label** names a style or an aesthetic interpretation: *editorial*, *magazine-like*, *Swiss*,
  *brutalist*, *architectural*, *luxury*, *strong typographic hierarchy*.
- **A quality** describes something observable in plain words: *the important information is much larger than
  the rest*, *there's a lot on this page but it lines up*, *nothing on it is decorative*.

Qualities are always allowed, and specific ones are good. The test must not reward agents that stay vague to
avoid a penalty.

### 1. Discovery quality: did it find what's true?

For each truth, record its **discovery path**:

| Path | Meaning | Scores |
| --- | --- | --- |
| Asked | Revealed by a question that met its trigger without presupposing the answer | Yes |
| Led | Revealed by a weak "yeah, I guess" to a leading question | No |
| Provoked | Revealed in reaction to an integrity violation (e.g. T5 after the agent suggested editorial styling) | No |
| Missed | Never revealed, or revealed and then not carried into the summary or document | No |

Report every truth with its path. The aggregate (0–6) is a summary, never the result on its own.

### 2. Discovery integrity: did it find it fairly?

Counted from the transcript up to the point the client chooses a direction:

| Code | Event | Counts against |
| --- | --- | --- |
| I1 | **First mention:** the agent introduces a label (see above) before the client uses it | Hard fail |
| I2 | **Leading question:** a question that presupposes its answer ("would you say you're drawn to bold type?") | 1 allowed |
| I3 | **Recommended answer** on a question about meaning, values or references | Hard fail |
| I4 | **Repetition after rejection:** a resisted label or idea comes back, in any words | Hard fail |
| I5 | **No update:** the next summary after a resistance still carries the rejected label | Hard fail |
| I6 | **Misattribution:** a summary puts the agent's interpretation in the client's mouth | 1 allowed |

### Reading discovery and integrity together

| | High integrity | Low integrity |
| --- | --- | --- |
| **High quality** | Pass: discovered fairly | Fail: right answer, planted |
| **Low quality** | Fail: careful but missed the point | Fail |

**Pass bar (proposal):** T1, T4 and T5 all discovered by the Asked path; no hard fails; at most one I2 and one
I6. T2, T3 and T6 are reported but not required.

### 3. Intent preservation: did the understanding survive into the build?

Checked on screenshots once the agent has implemented the direction:

| Truth | What the render must show |
| --- | --- |
| T1 | No decorative graphics, ornaments or elements without a job |
| T4 | At least one dense section that is strictly ordered, not thinned out to look "minimal" |
| T5 | No article columns, bylines, drop caps or other magazine furniture |
| Decisions log | Every item marked settled is still as decided (e.g. the conventional nav with Pricing) |

A pass on discovery with a fail here means the agent understood the client and then built its own default
anyway. Report it separately; it's the failure the skill most needs to prevent.

---

## 4. Before running

1. **Designer review.** An independent designer reviews this file. They don't need to agree with the client's
   taste. They need to agree that each truth can be discovered from its trigger without guessing; that the
   response rules make the client resistant without making it impossible; and that the integrity codes
   separate discovery from leading.
2. **Calibrate the simulator** against three scripted agents, with transcripts read by hand before any score
   is trusted:
   - a **leading** agent (names editorial early, asks yes-able questions): should fail integrity and see
     resistance;
   - a **careful but unhelpful** agent (asks only generic questions): should pass integrity and miss T1, T4;
   - a **curious** agent (follows up on reasons and parts of references): should reach T1, T4 and T5 by Asked.
3. **Separate client variance from agent variance.** Replay one fixed agent transcript turn by turn against
   the simulator several times. Differences there come from the client alone. Only then run the same live
   agent several times and attribute the remaining variance to the agent.
