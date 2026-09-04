# Phase 2, steps 12–16 — establish standing operation

**Load this alone, and only after the raised work is implemented.** At ranking there is nothing to
measure against, and a phase 2 run from memory produces the audit's own opinion of itself.

**The gate is implementation. Elapsed time is not part of it.** Where this method says the phases are
months apart it is describing the usual case, not setting a bound: a project that implements quickly
opens phase 2 quickly, and is right to proceed. What that costs is step 15, which needs its second null
shape when the delta window is short.

**An audit is a measurement taken at one moment, and a cleaned repository resumes growing at the rate
that produced the findings.** Phase 1 ends with work raised and, later, done. Nothing in it makes the
*next* year cheaper: the rules that would prevent regrowth are still in the auditor's head, the bands
that turned out wrong still read as right, and the technique catalogue starts ageing the day it is
written.

## The standing risk, named before the steps

**This is the phase where an audit becomes a second policy author for a project it is a guest in** —
writing rules beside the project's own, in its own vocabulary, with its own priorities. That is the F2
family at the level of documents rather than sentences, and it is committed by a well-meaning closing
pass more often than by anything in phase 1. **Step 16 exists mostly to prevent it.**

---

## 12. Close the loop on every finding: predicted against measured

**Check the version before the first row.** The report records the version the run was performed under
(`SKILL.md`); compare it with the one in front of you. Where the rubric numbers differ, **name what
moved and qualify the grading — never refuse it, and never re-classify.** Re-banding a phase 1 finding
under a later rubric manufactures a band nobody assigned, which is a derived value doing a measured
one's job. Where the run predates rubric 1 it carries no version at all, and the comparison is
**unversioned**: say so, rather than reading a match into a blank.

**Two blanks look identical and are not.** Rubric 1 was written on **2026-09-04** (`SKILL.md`). A report
dated **before** that carries no version because none existed — the exemption above. A report dated
**after** it carries none because the run omitted a line the method requires, which is a **friction
entry**, not an exemption. Say which one you found. A requirement whose absence is indistinguishable
from a defined exemption is not a requirement.

**Not a re-read of the findings.** For each one implemented, the band it carried set against what it
actually bought, **with the original kept and the correction marked.**

**This is the only evidence that improves the next audit's rubric, and it is rarely a match.** From the
one fully graded run: one finding understated itself twenty-fold, one was 48% wrong as a forecast of
bytes, one saved no bytes at all and bought a gate instead, one measured a unit that did not exist.
**Two of thirteen bands held as written.**

**A withdrawn finding is a result and is reported as one**, never as a gap in delivery. In the graded
run the clearest case was a finding whose remedy was refused and where **the refusal was the
deliverable**.

**Read the byproduct register for a shape, not only row by row.** This is the register's largest
return and nothing else in the method ever reads it back. Eight defects surfaced in passing during the
recorded run, each filed as an unrelated row, and **six of the eight were one class: text a reader
follows and no checker reads** — a link label stating a wrong path beside a working target, a bare
section mark left behind by an extraction, a citation of an id never allocated, a dangling pointer in
a store outside the tree. Row by row, eight small defects. As a class, a gap in what the project's
gates can see at all — worth a work item, which no single row was.

**Read every occasion's rows, and name the ones you read.** The register is one concept with four
occasions and they do not share a document (`judge.md`, *The byproduct register*): this run's report,
the closing report, and wherever the method's own work is tracked. A read-back over one of them is
not a read-back over the register — and a shape that spans occasions is exactly the kind this step
exists to find. Say which you read, so a blind spot is declared rather than discovered.

**Split the record's reliability visibly.** A reader who trusts `Finding` and `Change` equally will
obey a ranking. Say which half held.

---

## 13. Report what the remedies cost, not only what they saved

**Every remedy has a bill**: a document that did not exist, a gate to run, a rule somebody now reads.

**Splits move bytes off the load path and usually increase the repository.** A closing report that
shows only savings teaches its reader that the method is free, and the first person to check the total
concludes it failed. In the recorded run, tier 1 fell 4,214 bytes; the destinations gained 1,117 and a
new 10 KB document.

**Name any remedy that manufactured new work of another family** — a split that created duplication by
giving content a new home while leaving the old statement in place.

**And name the growth the audit itself caused.** In the recorded run, **3,012 of 3,405 bytes** added to
tier 1 came from the two findings written to govern tier 1. That is step 16's warning, committed by
the run that produced it, before step 16 existed.

---

## 14. Reconcile the method against what this run did to it

The run is a test of the rubric, the checklist and the record format. For each: **did it hold, did it
stay silent where it should have fired, did it fire where nothing was wrong.**

**The output is a change to the method, not to the project**, and the two must not be confused — a
project-specific finding written into the method is how a portable method acquires one repository's
habits.

**A rubric that gets extended in the field is under-specified.** Two findings in the recorded run
carried bands the table did not define, invented at ranking time because nothing in a four-value table
fits a gain that is not a saving. Both are defined values now. That is what this step is for.

**Read the friction log, which has been collecting since step 1** (`SKILL.md`, *What the run
produces*). It carries the question this step cannot ask of itself: not *was the judgement right*,
which is what the three checks above test, but *did the documents say enough to make it*. A run
that arrives here with an empty log records that emptiness as the result it is, the same way step
15 records a null search.

**Implementing is a measurement pass, and the loop back belongs here.** Every closure in the recorded
run produced material the audit had not seen; collecting it took a separate work item because nothing
in the method said the loop existed.

---

## 15. Refresh the technique catalogue, with a search record

Techniques in this space move faster than any repository does, **so the catalogue's date is part of
it.**

**Step 5's recorded-search rule applies here unchanged**: the queries run, the sources read, and an
explicit statement that named tools were looked for by name — across all three axes, with saturation
declared per axis and the empty rounds listed.

**Bound it to the delta.** This is *what is new since the audit's step 5*, not a second survey. **A
closing phase that re-runs step 5 in full is another audit wearing a different number.**

**A null result is an output, and it has two shapes.**

| Shape | Written when | What the row carries |
| :--- | :--- | :--- |
| **searched, nothing new** | the axes were run and changed no finding | the queries, the sources, and what the survey found that did not matter |
| **not surveyed, window too short** | the delta window cannot hold a delta a survey would find | **the window**, and **what bounded it** — the date of step 5, the date of this phase |

In the recorded re-run, re-running the research changed no finding: ten of fourteen new techniques were
addressed to the harness or the API and the one real local candidate was unmeasured. That had to be
written down, because a work item was blocked on the answer and *no new finding* is only an answer once
it is recorded as one.

**The second shape exists because the gate is implementation, not elapsed time** — see the head of this
file. A project that implements in two sessions opens phase 2 a day after step 5, and issuing queries
across a one-day window to produce a record of having issued them is the theatre the *bound it to the
delta* rule already refuses. **An unsurveyed step 15 is not a skipped one**: it is this shape, written
down, and a run that leaves the step blank has skipped it.

---

## 16. Write the standing policy into the documents that already govern, and nowhere else

The output of phase 2 is **a small number of durable rules.** Four constraints on writing them, each
already paid for:

- **Decide which document governs each policy before writing it.** A rule with no governing home is
  copied by whoever needs it next, and the copies are all written by people acting correctly. **Where
  no document governs the act, *that* is the finding, and creating the home is the work.**
- **Price every policy against the load path the audit just cleaned.** A rule placed where it is read
  on every turn is paid on every turn — and that surface is usually the one phase 1 emptied. **An audit
  that closes by writing governance into the file it just cut has undone itself**, and the report will
  still show a saving.
- **Check non-contradiction; do not intend it.** For each proposed policy, name the nearest existing
  rule and state whether it **extends**, **narrows** or **replaces** it. A replacement names its
  predecessor and edits it. An unmarked replacement leaves two live rules that disagree, which is
  precisely the defect the audit was measuring.
- **The project's own policies win, and a collision is reported rather than resolved.** The method is a
  guest. Where a proposed policy collides with a rule the project has already settled, **the project's
  rule stands and the collision goes in the report for its owner to rule on.**

**Where a rule about the load path is written costs something either way, and both answers must be
priced.** Outside the file it governs, it goes unread. Inside it, it is charged on every turn and the
first thing it reports is itself: one such statement cost **2,690 bytes** of the budget it was
declaring, and pushed the file 4,555 bytes over its own bound — more than half of that the statement's
own text.

### The worked example: what may be written into a context-bearing file

This step states four constraints on writing a policy and, until now, gave no example of one that
satisfies them. Here is one, and it is worth adopting on its own account:

> **Config and instruction files carry what is true now** — keys, rules, and short notes on what
> something means or how to change it. Never a changelog, never how the current wording was reached.
>
> **Tasks, handoffs, commit messages and lessons may carry history**, in this shape: the fact, its
> source reference, the date, and one clause of why it is there. Not a justification, and never a
> detail copied out of the source it cites.
>
> Prose accreted the other way is unsupervisable, and it is paid for on every read.

**The distinction that makes it usable, and without which it gets reversed inside a month:** prose
**stays** when it is a general guide — what something means, how to use or update it. It **goes** when
it is update history or a log entry. Not *prose versus no prose*, which is the reading that produces
configs nobody can use.

Read against this step's four constraints, in order:

- **Which document governs.** Wherever the project already states what its own instruction files may
  contain. **Where nothing does, that absence is the finding and creating the home is the work** —
  this step's first constraint applied to its own example.
- **What it costs to load.** Three sentences, paid wherever they are written. They go in the document
  that governs writing, which a session loads when it writes — never in the always-loaded file whose
  growth the rule exists to stop.
- **Extends, narrows or replaces.** It **extends** F3. F3 asks *does this prose decide anything
  future* at audit time; this asks the same question at write time. Nothing in F3 changes, and a
  project adopting only one of the two still holds a coherent rule.
- **Collision.** None known. Where a project has already settled what its instruction files carry,
  that rule stands and this one is reported to its owner rather than merged over it.

**One measured instance, dated because it is one file:** a config read on every run of a single
procedure reached 16,159 bytes, of which the keys and their guidance were 3,128 and the other 13,031
was narrative no schema had asked for. The cut alone would have regrown; what made it durable was
adopting the rule the same day. Measured 2026-08-23 in a sibling repository.

**Leave at least one thing that re-measures without being asked** — a check that runs on a trigger the
project already has, or an explicit statement that none is possible and why. **A standing operation
that depends on somebody remembering to look is not standing**, and *review this annually* is that
dependency with a date attached.

**No instrument is standing by itself — the trigger is what makes it so, and the instrument is what
the trigger reads.** Four of the five classes below report only when somebody looks; the fifth is
written whether anyone does or not, and summing it is still an act somebody performs. A check needs
both halves, and naming an instrument in place of a trigger rebuilds the dependency this step has just
refused, with a tool instead of a date.

**Name the class, never the command.** Each is named by what it reports, so a reader can decide
whether their own harness has one:

- **A context readout** — what is in the window now, itemised, with sizes. Step 1 already depends on
  this one.
- **A usage attribution** — consumption charged to a named unit: a skill, a tool, a delegate, or a
  shape of session.
- **A re-read split** — how much of a session was history re-sent, against how much was new work.
- **A running meter** — the rate, while the session is going rather than after it.
- **A per-reply record** — what each reply cost, written down, so a session total is summed rather
  than estimated.

**The run binds each class to whatever it actually has and records the binding in its own output,
never in the method.** A harness's names date within a release and are wrong everywhere else; the
class outlives them. **A class with no instrument here is recorded as unavailable**, by step 1's rule
about an unobservable item recorded as absent. What a bound instrument owes when its figure is
reported — itself, and what it excludes — the body already states.

**A trigger qualifies when it fires on an act that changes what step 1 would find.** That is the
test, and it survives a harness whose acts nobody has written down: the entries are the method's own,
and the acts are whatever your project does to them. This **extends** the prohibition above rather
than softening it — a dated review fires whether or not anything changed, which is why it was
refused; these fire because something did.

- **The tool catalogue** — connecting a tool source, or enabling a plugin that ships one. Re-measure
  what the catalogue costs before a tool is chosen.
- **Unattended execution** — adding a scheduled task or a background job. Re-measure the interval and
  what each firing loads: it is the step 1 entry observation does not reach.
- **Instruction files at every scope** — an edit to one that loads without being asked. Re-measure the
  tier 1 total against the relation it is bound by.

Named from one harness at one time, and re-checked against your own before a check is wired to them —
the discipline step 5 already applies to every catalogue entry. **The acts age; the entries do not.**

**Wire the closure gate where a closure happens**, not into the release gate and not as a checklist. A
list is what goes unread; in the recorded run a finding's row read closed while its task was open, and
vice versa, invisibly, until a check failed in both directions and caught the session that wrote it.

---

## What to say about what the method cannot see

Put this in the closing report, so silence is not read as a clean bill.

- **It measures artifacts, not sessions.** File sizes are what a session *could* pay. What it actually
  paid needs harness instrumentation this method does not require. **That instrumentation now exists**, in the
  classes step 16 names, so this is a choice rather than an impossibility, and the reason to keep it is that artifact sizes
  are what a repository can change — a session total mixes them with how the session was driven.
  **That reason does not reach the run's own cost**, which nobody acts on; `SKILL.md` rules on it
  separately and requires a measurement there. The two are about different subjects, not in conflict.
- **It ranks on context runway, so a cost that is only money is out of the ranking.** Acts that
  reprice a session without changing what sits in the window are named as F6 findings, marked
  `controller: user`, and never banded. Name the ones you saw — the silence is a decision, and unsaid
  it reads as an omission.
- **It cannot separate operative prose from narrative mechanically.** Section sizes are measured; the
  split inside a section is a reader's judgement, and every F1 or F3 finding resting on one says so.
- **It does not price attention.** A shorter context is assumed better. Where a cut would make the
  agent guess, that is a risk field, not a measurement.
- **A green gate proves the gate ran, not that the saving is safe.** Every finding is a proposal for
  someone to review.
- **The screening partition says nothing about the catalogue's completeness**, and it reads like it
  does. It summed correctly, and read as complete, over 54% of one catalogue.
