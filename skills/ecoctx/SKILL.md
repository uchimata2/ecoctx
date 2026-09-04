---
name: ecoctx
description: Audit what a coding agent loads on every turn — instruction files, indexes, skill descriptions — rank what can actually be changed, then grade each prediction against what it bought. Use when the user asks why a session starts expensive, wants an always-loaded instruction file cut down, asks what loads every turn or what a skill costs to have installed, wants per-session context cost measured, or wants an earlier audit's findings graded. Phase 2 runs after the fixes exist, not at ranking.
---

# ecoctx

**Sixteen steps in two phases. Phase 1 audits, phase 2 turns the audit into standing practice.**
Phase 2 runs **after the raised work is implemented**, not at ranking — at ranking there is nothing
yet to measure against.

## Load exactly one reference

Never load two. Each names its own steps and nothing outside them.

| You are | Load | It covers |
| :--- | :--- | :--- |
| Starting an audit | `references/measure.md` | Steps 1–5 — inventory the four surfaces, then research externally |
| Holding four inventories and a catalogue | `references/judge.md` | Steps 6–11 — screen, band, rank, split, raise work |
| Coming back after the raised work is done | `references/standing.md` | Steps 12–16 — grade every band, price the remedies, fix the method, write policy |

If the user has not said which, ask. *Audit my context* means step 1; *grade the audit* means step 12.
The second cannot be faked from the first: its gate is that the raised work is implemented, which is usually months and is never a clock.

## The four things this skill refuses to do

Stated here, on the body, because each one is where a run goes wrong and none of them survives being
kept in a reference the session may not load.

1. **Present a catalogue with no search record.** Step 5's output carries the queries run, the sources
   read, and an explicit statement that named tools were looked for by name. Two searches and two
   articles is a start, not a survey, and a step-5 output that does not say which it was is claiming
   the second while doing the first.
2. **Write a gain band before naming the mechanism.** *What is costing* comes before *how much*, and
   **is this a saving at all** comes before both — some findings are enablers and some trade one
   surface for another.
3. **Emit a standing policy without a governing document.** Step 16 will not write a rule until it has
   named the document that already governs the act, priced what the rule costs to load, and stated
   whether it **extends**, **narrows** or **replaces** the nearest existing rule.
4. **Resolve a collision with the project's own policy.** The method is a guest. Where a proposed rule
   collides with something the project has settled, the project's rule stands and the collision is
   reported for its owner.

## What the run produces

Two documents and two registers, and the split between them is by **who can act**, never by subject.

| Audience | Where it goes |
| :--- | :--- | 
| **Any project** | The portable half — findings stated so they stand alone |
| **This project** | The project's own report, ranked |
| **Upstream** | A section of that report, written to be handed over, never implemented locally |
| **This method** | The friction log, below — the one output addressed to the skill rather than to anyone who can act on the subject |

**The report carries the full step partition as a table**, one row per step, each *ran* or
*not run, with a stated reason*. A step in neither fails the audit, and a partition a reader has to
reconstruct is not one a later reader can check.

**The byproduct register is the fourth output and sits outside the ranking.** Checking every file for
one thing means seeing other things; record them, never band them, and read the register **for a
shape** at step 12 rather than only row by row.

**The friction log is the fifth output: what the run had to work out that these documents did not
say.** One entry per occasion — the step being run, what was missing, and what was done instead.
**Write each as it is met.** By the end of a run the friction of step 2 is a feeling rather than a
fact, which is how the one recorded external run produced no answer to this at all. **A nil return
is an output**: *nothing had to be worked out* is a result, and is only a result once written down.
Step 14 reads it, and its destination is this method's own tracker rather than the subject's.

**The run's own cost is what the audit consumed, and it is never the subject's load path.** Step 1
inventories the **subject's** load path; reporting that figure under the other name is how the one
externally assessed run recorded a criterion as met that it had not met. The audit's own consumption
is a **disclosure** — never screened, banded, ranked or raised — stated with the instrument that
produced it and what that instrument excludes. Where the harness offers none, say so rather than
substitute an artifact sum: unlabelled, it reads exactly like a measurement.

## Version, and what it means for a phase 2

**rubric 2, revision 3**, and rubric 1 was written on **2026-09-04**. Written as words: two dot-separated integers would be read as SemVer, whose
question is not this one — nothing here breaks at run time, and what can break is a comparison taken
months apart. `.claude-plugin/plugin.json` carries the same version rendered as semver — rubric as the
major, revision as the minor, patch always zero — because the platform refuses anything else: `claude
plugin tag` rejects a non-semver version, and dependency resolution then ignores the tag. That manifest
field is a **rendering**; this line is the version's home, and naming the mapping rather than today's
value is what keeps it one.

**This line describes the tip of `master`, not the last release.** Every merge that changes a shipping
file moves it, and what a release shipped is the value this line held when its tag was cut, which is
what the tag records. So `master` standing ahead of the newest tag is the ordinary state, never a
stale number.

**The rubric number's only job is to say whether a run was graded under the rubric it ran under.** *The
rubric* is what a run's outputs cite — the closed value sets, the finding record's fields, the step
partition — and the number moves when **what a run is required to record** changes: a value added to,
removed from or redefined in a closed set; a field added to or removed from the finding record; a step
added, removed or moved between references; a rule that changes what gets written down. **Stating an
unchanged requirement more findably is not a rubric change.** Without that clause every clarification
moves the number, and a number that moves on everything discriminates nothing.

**The revision number is everything else** — prose, rationale, worked examples, the README, the tools —
and resets to 0 when the rubric moves. Changes landing together bump once, to the higher class.

**Every run's report records the version it ran under**, beside the step partition. Step 12 reads it
back (`standing.md`), and tells a report that omitted the line from one that predates rubric 1 by the
date above.

## Two rules that decide most disagreements

**Only tier 1 gets a budget, and express it as a relation rather than a constant.** Tier 1 is what the
harness loads without being asked — a property of the tree, established by observation, never by a
file's claim about itself. A number and the arithmetic that justified it must be edited together, and
the number wins that argument by staying put.

**The inventory survives; the remedy is a hypothesis.** In the one fully graded run, every band error
was in the proposed change and none in the observation. Re-measure a remedy before carrying it out and
let the measurement refuse it — a ranking obeyed instead would have deleted two tools' payloads.

## Measuring

**Measure with a program, not by reading.** Opening a file to find out how big it is spends the exact
budget under audit. Sizes come off the filesystem; command output is captured to a file whose length
is measured without printing it. The script is throwaway and belongs outside the audited repository.

**State the token conversion once and apply it uniformly.** Bytes ÷ 4 is close enough for prose and
markdown, costs no dependency, and is labelled an estimate. Never use it to separate two findings a
byte count does not already separate.

**`tools/findings.py` ships with the method** and answers *which finding is which task, and what state
is it in* without reading the audit, failing in both directions. The other programs beside it check the
skill's own repository and are not part of an install; `README.md` says which is which.
**`tools/check_all.py` is that repository's gate**, and it is the partition this method asks for
everywhere else, applied to checkers instead of steps: each **ran**, **was skipped with a stated
reason**, or **failed**, and one in none of the three fails the run.

## What this method cannot see

Say this in the report, so silence is not read as a clean bill. It measures the subject in
**artifacts, not sessions** — file sizes are what a session *could* pay. It **ranks on context runway alone**, so an
act that reprices a session without changing what sits in the window — family F6 — is named, marked
`controller: user`, and never banded. It **cannot separate operative prose from
narrative mechanically**. It **does not price attention**: a shorter context is assumed better, and
where a cut would make the agent guess, that is a risk field rather than a measurement. And the
screening partition in step 7 **says nothing about the catalogue's completeness** — it summed
correctly, and read as complete, over a bit more than half of one.
