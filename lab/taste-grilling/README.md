# taste-grilling

Design and discovery tests for `/taste`, the design-director skill in [`direction/`](../../direction/).

**Status:** the skill ships under `direction/skills/taste/` (fast mode primary; guided mode experimental). The
documents here are the discovery test design. Persona-B calibration has not run; guided mode stays labelled
experimental until those transcripts are reviewed by hand.

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
| [`direction-spec.md`](direction-spec.md) | Pointer to the skill's creative-direction template | Anyone |
| [`../../direction/skills/taste/references/direction-template.md`](../../direction/skills/taste/references/direction-template.md) | The live format: principles, provenance, template, writing rules | The skill and anyone editing the format |
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
4. Drop the experimental label on guided mode only after that review.
5. Lab condition **D** (`/taste` in fast mode) against C measures orchestration on the existing briefs; see
   [`lab/README.md`](../README.md).
