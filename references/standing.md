# Phase 2, steps 12–16 — establish standing operation

**Load this alone, and only after the raised work is implemented.** At ranking there is nothing to
measure against, and a phase 2 run from memory produces the audit's own opinion of itself.

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

**A null result is an output.** In the recorded re-run, re-running the research changed no finding: ten
of fourteen new techniques were addressed to the harness or the API and the one real local candidate
was unmeasured. That had to be written down, because a work item was blocked on the answer and *no new
finding* is only an answer once it is recorded as one.

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

**Leave at least one thing that re-measures without being asked** — a check that runs on a trigger the
project already has, or an explicit statement that none is possible and why. **A standing operation
that depends on somebody remembering to look is not standing**, and *review this annually* is that
dependency with a date attached.

**Wire the closure gate where a closure happens**, not into the release gate and not as a checklist. A
list is what goes unread; in the recorded run a finding's row read closed while its task was open, and
vice versa, invisibly, until a check failed in both directions and caught the session that wrote it.

---

## What to say about what the method cannot see

Put this in the closing report, so silence is not read as a clean bill.

- **It measures artifacts, not sessions.** File sizes are what a session *could* pay. What it actually
  paid needs harness instrumentation this method does not require. **That instrumentation now exists**,
  so this is a choice rather than an impossibility, and the reason to keep it is that artifact sizes
  are what a repository can change — a session total mixes them with how the session was driven.
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
