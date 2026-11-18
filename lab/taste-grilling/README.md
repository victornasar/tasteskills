# taste-grilling

Design for a skill that helps people work out what they want their website to look like, before and during
building, without the agent swapping in its own taste.

**Status:** design documents only. There is no skill to install and no experiment has run.

## The idea

Most people describe a website in a handful of words they've seen elsewhere: "minimal", "premium", "clean".
An agent that takes those words literally builds the generic version. An agent that ignores them and builds
what *it* finds tasteful replaces the client's taste with its own default.

taste-grilling sits between those. It asks questions, looks at references and shows contrasting options until
the client's real values are clear, then writes them into a short **creative direction** that the build
follows and screenshots are checked against.

The rule underneath: **values belong to the client; the words for a look are open.** "Minimal" might mean
"little on the page", or it might mean "nothing careless". The agent finds out which instead of assuming.

## Files

Read them in this order:

| File | What it is | Who reads it |
| --- | --- | --- |
| [`direction-spec.md`](direction-spec.md) | The creative direction format: five principles, who may change what, a one-page template and writing rules | Anyone; the eventual skill |
| [`examples.md`](examples.md) | Three worked examples: one brief, one fictional product (Tallyroll), three clients whose wants differ | Graders only |
| [`persona-b.md`](persona-b.md) | A test: a simulated client whose words and references disagree, and how to grade the agent | Client simulator and graders only |

**Keep `examples.md` and `persona-b.md` away from the agent being tested.** They show the answers. An agent
that has seen them copies them, and the test would then measure copying instead of discovery.

## The test in one paragraph

A simulated client opens with "a minimal, premium SaaS website" but hands over references that point
elsewhere. Six facts about what they actually want are hidden, each revealed only by the right kind of
question. The agent is graded on three things, separately: **discovery quality** (did it find the facts),
**discovery integrity** (did it find them without leading the client, for example by naming a style before
the client did) and **intent preservation** (did the finished site still match once built).

## What's next

1. An independent designer reviews `persona-b.md`.
2. Build the client simulator and three scripted agents (leading, careful but unhelpful, curious) to calibrate
   it.
3. Read the calibration transcripts by hand before trusting any score.
4. Only then write the skill.
