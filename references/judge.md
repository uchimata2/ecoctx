# Phase 1, steps 6–11 — screen, band, rank, split, raise

**Load this alone**, holding four inventories and a catalogue with its search record. `measure.md` is
behind you; `standing.md` is months ahead and cannot be faked from here.

**Steps 1–4 were measured. Everything in this file is estimated**, and the difference is the single
most important thing the record carries.

---

## 6. Read the local precedent

Repositories where the same owner has already done this work are an input the internet cannot supply:
they are proof a technique survived contact with how this owner actually works.

**Patterns, structures and measurements only.** Nothing is copied across, and no path, machine name or
personal datum from a precedent repository enters the report.

Six patterns that carried over in the one recorded run, stated as structures rather than as files:

| | Pattern | What it buys |
| :--- | :--- | :--- |
| **P1** | **Stub, canon, depth** — a tiny per-agent instruction file points at one agent-neutral document, which points at heavy references | One copy of the rules for several agents. **Note honestly**: the stub saves little; the layer below it is what saves |
| **P2** | **One file per lifecycle phase**, each with preflight, do, do-not, close | A session in one phase loads that phase. Measured at 1.2–7 KB per phase against one document several times larger |
| **P3** | **Rationale in its own document**, cited from the operative steps | The F3 tension resolves without deleting anything |
| **P4** | **Evidence quoted forward** — a planning phase records verbatim signatures and `path:line`, so the audit phase searches instead of re-reading | The expensive re-read never happens |
| **P5** | **One body, thin per-agent front-ends** — the package lives once, each agent gets a 1–2 KB adapter naming only what differs | No drift between agents, no duplicated body |
| **P6** | **Spine plus one branch, never both** — a core document declares which branch a mode loads, and a run loads exactly one | Observed during the recorded audit: 10 KB present, 7 KB of one binding and 6 KB of the other branch not paid |

---

## 7. Screen for applicability

Each technique is **adopted**, **rejected**, or **deferred**. A rejection names the constraint it
collides with; a deferral names what would close it.

**The three are a partition, and a technique in none of them fails the audit.** A silent fourth
category is how an account that looks complete gets shipped.

**The partition is not a coverage claim, and it reads like one.** *Adopted + rejected + deferred =
every technique gathered* is arithmetic over what you happened to gather. In the one recorded run it
summed correctly, and read as complete, over **nineteen entries of a catalogue that turned out to hold
35** — right about a bit over half. Step 5's search record is the only guard, and it is weaker than
the partition: a search record can be read and judged, but nothing can prove a survey complete.

---

## 8. Estimate gain and effort

**Estimate the gain; do not measure it.** Measuring a saving requires building it, which is the work
the ranking exists to decide on.

**Ask *is this a saving at all* before asking *how big*.** Two of the six bands below exist because the
first run needed them and the four-value table could not express a gain that is not a saving.

| Band | Meaning |
| :--- | :--- |
| `XL` | removes more than about a third of a session's cost **on the surface it names** |
| `L` | roughly a tenth to a third |
| `M` | a few per cent |
| `S` | under a per cent, or unquantifiable but real |
| `enabler` | it saves nothing and makes a later saving decidable. **Its gain is the finding it unblocks, named** |
| `bimodal` | it costs one surface to save another. **Both figures are stated, and the trade is argued rather than netted** |

**A band is always read against its own surface.** `L` on the load path and `L` on the read path are
different quantities, and the record says which.

**Name the mechanism before writing the band.** A band written off the size of a surface prices the
wrong thing: one finding in the recorded run was banded on how big its subject was rather than on how
much of it could be changed, and the reachable share was about a ninth.

### The band prices the finding, not the remedy — and the remedy is where a ranking goes wrong

In the fully graded run, **eleven of thirteen bands missed**: four on magnitude, three on the *shape*
of the change, one on its direction, one on a false premise. **Every error was in the `Change` cell and
none in the `Finding` cell.** The inventory said where the weight was and was right thirteen times out
of thirteen; the proposed remedy said what removing it was worth and was wrong more often than not.

- **`Change` is a hypothesis and is read as one.** It is written with the same authority as `Finding`
  and does not deserve it. **Re-measure a remedy before carrying it out, and let the measurement
  refuse it.** Four rows were refused exactly that way; a ranking obeyed instead would have deleted
  two tools' payloads, rebuilt one finding on a timer, and split a small document into four smaller
  ones.
- **The inventory is what survives.** A finding whose inventory figure is sound and whose remedy is
  refused is **still a good finding**, and *shape refused, still worth doing* is an outcome the record
  should be able to hold. It happened four times in thirteen.

**A carve-out estimate for any F1 split.** What share of the named region is load-bearing and has to
stay? One finding forecast a 6,980-byte extraction and 3,619 came out, because the rest was operative
rules. A size names a region; the region is not the change.

**Some remedies reduce nothing, by design.** Surfaces A and B measure **what is paid per turn**, not
repository size. In the recorded run tier 1 fell 4,214 bytes while the destinations gained 1,117 and a
new 10 KB document. **Say so in the band's definition**, or a reader who checks the total concludes
the method failed.

**Effort uses whatever scale the project already has for work items.** A band with no inventory behind
it is a guess wearing a table.

**Risk is a veto, not a term.** A finding that costs a fact its only home does not rank higher by
being cheap.

---

## The taxonomy — walk it, do not skim it

**A family with no finding against it is a result and is reported as one.**

| | Family | What it looks for |
| :--- | :--- | :--- |
| **F1** | **What loads, and when** | Anything paid every turn that is needed on few of them. Dynamic and on-demand loading; separating operative instruction from historical narrative |
| **F2** | **Redundancy and contradiction in the record** | The same fact in several homes, or two statements that cannot both be current. Cumulative rules consolidated into one statement with no detail lost; stale and deprecated information; records the project does not own |
| **F3** | **Prose that is not doing work** | Text that neither states a fact nor decides a future question |
| **F4** | **Model work that should be deterministic** | Anything the model does per session that a program could do once. A script that lists or processes instead of the model reading and reasoning; installing an existing component rather than re-deriving it; simplifying structures **wherever no human reads them** |
| **F5** | **Tool and workflow economics** | When a cost is paid rather than how large it is. Gate output on a green run; a gate that must run per task against one that may run per release; targeted runs against whole suites; delegating read-heavy exploration |
| **F6** | **Acts that reprice the context** | Something done mid-session that changes no file and re-charges the whole window: switching model or effort level, toggling fast mode, connecting a tool source whose catalogue loads up front, enabling a plugin that ships one, compacting, upgrading the harness and resuming a long session. Also where a subject sits against the cache — paid warm, paid cold, or re-written every turn |

### F3 needs a line drawn, and drawing it is part of the work

A project may keep rationale on purpose — a rule whose reason is lost gets undone by the next person
who finds it inconvenient. **So the test is not *is this justification* but *does it decide anything
future*.**

- **Decides something:** why a rule exists; what it cost to learn; what would close an excusal; what
  was rejected and why; the constraint a later change will collide with.
- **Decides nothing:** a defence of a choice nobody is contesting; the same reason restated in a third
  place; an account of how carefully the author worked.

**An F3 finding that cannot name what the prose would stop deciding is not a finding, and is recorded
as rejected.** F3 is the family that can damage a record, and this is the guard rail against declining
to draw the line.

**A second guard rail comes first: prove the bytes you counted are prose.** A share-of-file figure
does not establish it. One F3 finding survived ranking, publication and citation in five documents on
a count of triple-quoted string tokens; the file it named as 85% prose is **3.2%** prose and the lowest
in its tree, and the relocation it proposed would have deleted a tool's payload. **An F3 finding is
the one most likely to be acted on destructively, which is why its measurement gets the strictest
reading rather than the loosest.**

**Relocation beats deletion.** The strongest F3 result is usually an F1 move: rationale keeps its
home, in a document the operative path never loads.

### F2's first question is which document should have had it

**Not which copies to delete.** Restatement spreads where the governing home is missing, so the count
of copies is a symptom. In the recorded run, five documents restated one rule and the document that
*governs* the behaviour was the only one not stating it.

Two consequences:

- **A rule with no declared home gets copied by whoever needs it next**, by people acting correctly.
  Deleting copies without declaring the home regenerates them — one task wrote a fresh copy of a rule
  hours before another task's survey caught it.
- **Ask how many rules there are before assigning a home.** A cumulative rule that resists a single
  home is usually two wearing one sentence, binding at different moments, which is why nothing had
  ever been able to own it.

**A survey is evidence about the day it was taken.** One inherited survey was wrong in both directions
— it named a document that had never stated the rule and missed a copy inside the file the rule was
being cut from. **Re-measure before editing**, and never inherit a remainder from a closed task
without doing so.

**Sweep for existing homes before writing a new destination.** Otherwise an F1 split manufactures F2
duplication: three paragraphs in one split's scope needed no new home at all, because their content
was already in two other documents.

### F6's unit is an act, and that is why it is not F5

F1 through F5 each take a file or a command as their unit. A repricing act has neither: nothing in
the tree changes, nothing runs, and the next turn costs an order of magnitude more than the last.
Stretching F5 to cover it would make F5 mean *everything that is not a file*, which is how a taxonomy
stops discriminating.

**F6 findings are named, marked `controller: user`, and not banded.** This family is where the
artifacts-not-sessions boundary becomes visible: a repricing act is how the session was driven,
inherited by no clone, reachable only by whoever is present, and `controller: user` was defined to
say exactly that. The family reports what it sees and declines to measure it — which also keeps the
rubric out of a vendor's price list, where the rates change without notice and no band built on them
stays true.

**One dated measurement is why the family exists, and it is the only figure in it.** A single
session's usage readout: 5.8M tokens of cache read against 11.1k of fresh input, and 1.1M of cache
write — roughly 520 tokens re-sent from cache for every one charged at full price. A byte count over
the load path prices the 11.1k and is silent about the rest. Measured 2026-09-03, and stated with its
date because it is one session on one harness rather than a constant.

**The acts in the family row, and the magnitude claimed for them, are reported behaviour rather than
anything measured here.** They belong to one harness at one time. Read the row as what to look for,
re-check it against the vendor's own documentation before an audit rests on it, and record what you
found — the rule step 5 already applies to every catalogue entry.

**F6 findings are reported under surface E**, the one that already cuts across the other four and
collects costs that change *when* rather than *how much*. The taxonomy gains a family here, not a
sixth surface: the surfaces say where a cost sits and E is where a cost with no file sits, while the
family says what kind of thing it is.

---

## 9. Rank

Gain per unit of effort, **with risk as a veto rather than as a term.**

**Where a batch of findings shares one policy question, say so and name which task settles it.**
Specifying them independently produces inconsistent answers; in the recorded run the first one
specified settled the question and the other two cited it.

---

## 10. Split

Mark every finding **any project** or **this project**, and write the portable half so it stands
alone.

**The split is by who can act, not by what the finding is about.**

| Audience | Where it is reported |
| :--- | :--- |
| **Any project** | The portable half |
| **This project** | The project's own report, ranked |
| **Upstream** | That report, in its own section: components the project *uses* but does not own |

**One numbering space; each finding stated in full in exactly one document.** The ranked table lists
every id wherever it is stated. An audit about redundancy that prints its findings twice has answered
its own question.

**The upstream section is written to be handed over and is not implemented locally.** Two things it
owes:

- **Read the upstream backlog before proposing.** Their own precedent outranks the argument that
  arrived with the finding — it turned a proposal into an adoption twice in one session. **Say in each
  entry whether their backlog was read.**
- **A handed-over item carries the sender's labels.** Its priority is a guess about someone else's
  project: state the observation and let them place it.

**Prove which component failed before filing an observation upstream**, not after. One report was
addressed to the wrong owner for weeks: the mechanism that actually failed was a third component
entirely, and a local workaround that sidestepped it kept working while the attribution stayed wrong,
so nothing ever forced the question.

---

## 11. Raise child work

For the top of the ranked list — **at the owner's review, not before.**

**Re-measure the inventory figure when the work starts, not when the row was written.** Subjects keep
growing between ranking and implementation, and a saving computed against a stale denominator is not a
measurement. Three of thirteen moved: one board grew 33,676 → 36,559 before its task began, one share
fell 45% → 37.9% with the section unchanged, one went 61% → 69.0% by the day it was cut.

**Where the finding-to-task link lives is part of this step.** Put it on the **task**, in a structured
field a command can read without parsing English; parse the ranking table where it stands; and check
the two against each other. **The check fails in both directions** — a finding whose task closed while
the row still reads open, and a task naming a finding that does not exist, both stop the run. See
`tools/findings.py`.

**The subject needs `.ecoctx.json` before the tool will run, and writing it is part of this step.**
Its defaults describe this method's own conventions rather than the subject's, so a run that skips the
file gets `report not found at AUDIT.md` and stops — which is how the tool went unused in the first
external run. Write it at the **subject's** root, naming at least the report this run is about to
produce and the pattern of the ids it allocates:

```json
{ "report": "docs/audits/2026-01-01-context-economy.md", "id_pattern": "E-[0-9]+" }
```

Every key has a default and only the differing ones need writing. `tasks_glob`, `task_finding_field`,
`task_status_field` and `closed_statuses` say where the subject keeps its work items and how one reads
as closed; `closed_marker` is how the report strikes a closed row, and setting it to `""` turns off
half the check and prints that it has.

**Where a subject's tasks are not files** — an issue tracker, a board — `tasks_glob` matches nothing,
every finding lists as having no task, and the check then passes having compared nothing. Read the
counted summary line rather than the exit status, and record the limitation instead of working around
it.

**The listing must not become a second board.** Key on findings and reference tasks; never mirror
them.

**Raise phase 2 as a work item now, blocked on the audit's own repairs.** A phase that runs once,
later, on a trigger nobody watches is a phase that does not run.

---

## The byproduct register

**Checking every file for one thing means seeing other things.** Record them; keep them out of the
ranking. Anything noticed that is not token efficiency goes in the register, with the file and what
was seen.

**One register, several occasions.** A row goes in the output of whatever occasion produced it — not,
as this section said until 2026-09-03, only at the end of a phase 1 run. A second register for the
other occasions would be the F2 defect this method exists to measure, so the concept stays single and
each occasion names its destination instead:

| Occasion | Where its rows go |
| :--- | :--- |
| A phase 1 run | The project's report, in its register section |
| A step 12 grading pass | The closing report's register section, beside the grading table |
| A step 15 catalogue refresh | The same closing report — the refresh has no report of its own |
| Work on the method itself | Wherever the method's own work is tracked, marked *register row, not ranked* so an unranked entry reads as deliberate rather than as an omission |

**The last row is the one that was missing, and leaving it out cost something.** An observation made
while developing the method has no run to attach it to, so it goes into a tracker whose every other
entry is ranked — and reads as an under-specified task rather than a deliberately unranked one. That
is this section's own warning arrived at backwards: instead of an unranked row leaking into a ranked
list, an unranked row is **forced** into one because nowhere else exists.

- **Never ranked, never banded, never a finding id.** Mixing them puts an unranked observation into a
  list someone is using to buy work.
- A register entry that is really a defect is raised as its own work item at review, and the row then
  points at it.
- **Record everything.** What an observation is worth is the receiving project's call, not the
  reporter's. Three of nine in one session would have been dropped as marginal by a filter asking *can
  I see what they would do with this* — which is the reporter deciding with less information than the
  reader has.
- **The register needs a home for an owner you have no section for.** One report went to the wrong
  owner because the register's shape offered only wrong ones, and a missing slot is where a wrong
  owner comes from.

---

## The finding record — twelve fields, all of them

**Operative or it is decoration.** A reader must be able to act on a finding without the audit's
author present.

| Field | What it holds |
| :--- | :--- |
| id | stable, cited from child work and from other projects reusing this method |
| Surface | A, B, C, D or E |
| Family | F1–F6 |
| Cache | `warm`, `cold`, `rewritten` or `n/a` — how the subject is paid |
| Finding | what is costing, stated as a fact about the repository |
| Change | what to do — **a hypothesis** |
| Gain | a band, with the inventory figure it rests on |
| Effort | the project's own scale |
| Risk | what it could cost. **`none` is a legitimate value and must be written** |
| Applies to | `any`, `this project`, or `upstream: <component>` — **who implements the change** |
| Controller | `project`, `user` or `harness` — **who can reach the cost** |
| Source | external research, local precedent, or this audit |

**`Applies to` and `Controller` are deliberately two fields.** One says who does the work, the other
whether the work is possible from here; a single field forces one of those answers to be a guess. A
finding can be `any` and `harness` at once — every project pays it and no project can change it.

**`Cache` orders and never prices.** `warm`, `cold` and `rewritten` say *how* a subject is paid, not
how much: three subjects of identical size are charged differently depending on whether each is
re-sent from cache every turn, read fresh once a session, or invalidated and re-written — precisely
the distinction a byte count cannot make. It stays ordinal, as the bands are. A finding whose subject
never enters the context window writes `n/a`, which like `Risk: none` is a value and not a blank.

**A per-item band is a first-class value.** A finding that closes per instance breaks *closed means
finished*, which every status check assumes. One record carried `xs` **each** since the day it was
written and nothing read it, because the marker existed and the schema for reading it did not.

**The record has no field for what the finding bought, and it should not gain one.** A field serving
one step that runs once is paid by every finding written. **What the closure owes instead is
one line** — the measured outcome, in the record that already exists, written on the day it is known.
Reconstructing thirteen outcomes afterwards cost 80,721 bytes across fourteen closed records and is
the most expensive step in the method.
