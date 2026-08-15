# Phase 1, steps 1–5 — measure, then research

**Load this alone.** `judge.md` is steps 6–11 and is loaded when you hold four inventories and a
catalogue; `standing.md` is steps 12–16 and is months away.

**Steps 1–4 are measured. Steps 7–9 are estimated.** Keeping that line visible is most of what makes
the record readable later: an inventory figure is a measurement and is stated as one, and only the
saving is ever banded.

---

## What is being audited, and what is not

**Token efficiency, and nothing else.** Security, compliance, licensing, quality and correctness are
not searched for. What is noticed anyway goes in the byproduct register and is never ranked.

**The ranking axis is context runway** — how long a session runs before it compacts. Cost in money
follows from runway and is not the axis. A finding that saves tokens without lengthening the runway is
still a finding, and it ranks below one that does both.

**No fact loses its only home.** Layering and load-on-demand are the instruments; deletion is not. A
finding whose gain depends on a rule becoming unfindable, a gate weakening, or a lesson disappearing
is recorded with that risk stated and ranks below everything else.

---

## The four surfaces, and the fifth thing that cuts across them

Every agent-driven repository has all four. **An audit that skips one ranks the other three against an
unknown denominator.**

| | Surface | What it holds | Why it is separate |
| :--- | :--- | :--- | :--- |
| **A** | **The load path** | What enters context without anyone asking — instruction or rule files at every scope, any persistent store the agent recalls from, whatever is carried over from the last session, the catalogue of capabilities the agent is offered, and the tool interface | Paid on **every** turn of **every** session, so a saving here compounds against all the others. Its items differ in **who controls them** |
| **B** | **The read path** | What a session must read to do one unit of work — the specification, the conventions, the lessons, the index, the work item, its neighbours, the source it edits | Paid once per session, and it grows with the project's age |
| **C** | **Tool output** | What commands print back — gate reports, per-row verdict listings, test suites, search results | Paid per invocation, and the only surface where a tool's own default decides the cost |
| **D** | **Write volume** | What a session produces — work-item prose, log rows, commit messages, the reconcile edits a closure owes | Paid twice: once written, and again when the next session reads it as surface B |

**E — workflow and tooling** cuts across all four: when a gate *must* run rather than *may*, whether a
suite runs whole or targeted, whether exploration searches or reads, whether read-heavy work is
delegated, how a session hands over. Its findings change **when** a cost is paid rather than how large
it is, so report E as its own section.

### Tiers, and why only surface A gets a budget

| Tier | Loaded | Membership rule |
| :--- | :--- | :--- |
| 1 | every turn | **What the harness loads without being asked.** A property of the tree, not a list someone updates |
| 2 | when work of a kind starts | What a packaged procedure or workflow document pulls in when it activates |
| 3 | when a phase or mode begins | What tier 2 loads one at a time, for the branch actually taken |

**Only tier 1 gets a budget.** Tiers 2 and 3 are not paid every turn, so a size limit there measures
the wrong cost; what constrains them is the load-one-at-a-time rule. **Say this explicitly** rather
than leaving it inferred — it is the visible price of budgeting tier 1 alone, and it means the tier-2
documents are allowed to grow.

**Express the budget as a relation, never as a constant.** Bound tier 1 against something else counted
from the same tree, so that re-measuring changes a measurement and leaves the rule alone.

**The relation's comparison set must be closed and stated.** Any document split out of tier 1 is
smaller than tier 1 was, so a bound against *the smallest document it defers to* ratchets down with
every remedy it prompts and becomes unsatisfiable by the one action it exists to cause. Name the set —
tier 2, or whatever the project's equivalent is — and say that its membership changes only by a
deliberate act.

**A document that asserts a load discipline the harness does not implement is worse than one over
budget**, because the claim cannot be falsified and content keeps being written on the strength of it.
Establish tier 1 **by observation**: read what the session was given before its first tool call. Do not
take a file's word for when it loads.

### Controllers — who can change a load-path item

**A tier says when an item is paid. A controller says who can stop paying it.** They are independent,
and the most expensive item on the load path can be the one nobody in the repository can touch. Every
item inventoried in step 1 gets one of three values.

| Controller | Who can change it | What a finding against it means |
| :--- | :--- | :--- |
| **project** | anyone who clones the repository | actionable work, rankable as it stands |
| **user** | the person running the agent, across all their projects | actionable, and **someone present can do it** — but the change lands outside the repository and no clone inherits it. Say so |
| **harness** | the agent, its vendor, or its account configuration | **may be unreachable, and that is a result rather than a low rank** |

**Why this is a field and not a remark.** Without it, an audit converts *I cannot reach this* into
*this is not worth doing*, and those read identically in a ranking while being different facts.

**Addressability is measured, never assumed — in both directions.** This method's first run got it
wrong twice, in opposite directions, on the same item: the largest thing on its load path was first
written off as untouchable by reasoning about where the files came from, then banded on the whole of
it once a setting was found, and the reachable share turned out to be about a ninth. **Write a
setting, restart, measure again.** A configuration schema documents what a key *means* and is silent
about which sources honour it at which scope.

**Two failed attempts is the signal to stop.** What survives is the boundary — which sources the
mechanism reached and which it did not — recorded so the next reader does not re-run the same tests.
That boundary is worth more than the tokens it failed to save.

---

## The steps

1. **Inventory the load path (A).** Everything that enters context unasked, with its size and its
   controller. Whatever your agent calls them, look for: instruction or rule files at every scope; any
   persistent store the agent recalls from by itself; anything carried over from a previous session;
   **the catalogue of capabilities the agent is offered** — the name-and-description listing of
   whatever it can invoke, paid whether or not the project could use one; and how much of the tool
   interface is present before a tool is chosen. Establish membership by observation. **The item you
   cannot change still belongs in the inventory, marked.**

2. **Inventory the read path (B)** for one representative unit of work, **chosen before the audit
   starts and named in the report.** Record what was opened, how much of it was needed, and how much
   was history rather than operative rule.

3. **Inventory tool output (C).** For each gate or command a unit of work runs, the size of what it
   prints on a **green** run. The failing case is rare and its verbosity is usually earned.

4. **Inventory write volume (D)** for the same representative unit.

5. **Research externally.** How practitioners reduce context and token use with coding agents. Produce
   a catalogue of *techniques*, each with what it costs and what it assumes.

### Step 5 owes a search record, and the record has rules

**A catalogue with no search record cannot be told apart from a short one.** Step 7's screening
partition then proves only that every gathered technique was judged — never that the gathering was
adequate.

**Three axes, and they are named here because leaving them to the auditor loses one:**

| Axis | What it searches | Why it is separate |
| :--- | :--- | :--- |
| **A** | ideas, articles, papers | the obvious axis, and the only one most surveys run |
| **B** | **named tools, by name** | searching for *ideas* never reaches a technique whose name is a product. Six of fourteen new techniques in the one recorded re-run came only from here, and so did its single largest correction |
| **C** | **the harness's own documented mechanisms** | it found three techniques and had never been treated as a source at all |

**Declare saturation per axis, and list the empty rounds.** An axis stops when a full round adds
nothing, **and the round that added nothing is written down.** Without that row a reader cannot judge
whether the axis stopped early, and the record documents an arbitrary stop.

**Expect an order of magnitude, not a handful.** The first pass of the one recorded run produced
nineteen entries and read as complete; under the coverage rule the catalogue reached **35**. A
catalogue that fits on one screen after a survey of a live tool space is the signal.

**Screen on the source of every figure.** A named tool advertised −54% code and −20% cost; an
independent 80-task benchmark measured −15% and −10.3%, concentrated on big builds and zero elsewhere.
A verdict resting on a vendor's number rests on their best case, and **where an effect concentrates
decides more screenings than its size.**

**A null result is an output.** A step that can produce nothing needs somewhere to say so; *the
research changed no finding* is only an answer once it is recorded as one.

---

## How to measure

**Measure with a program, not by reading.** Opening a file to find out how big it is spends the exact
budget under audit. Sizes come off the filesystem; command output is captured to a file whose length
is measured without printing it. **The script is throwaway and belongs outside the audited
repository.**

**Any scanning step owes a known-good case before its output is read as a finding.** A twenty-line
scan in the one recorded run named three defective rows and one of them was its own regular
expression. The scan was still the right move; one step was missing, not the tool.

**Prove the bytes you counted are what you say they are.** Comment markers, quote styles and block
delimiters are proxies for *kind*, and each holds until a file uses that syntax for something else — a
template, a fixture, an embedded payload. **Count by the structure that defines the unit** — a
parser's own notion of a docstring or comment, never a regular expression over quotes — and **name
that unit in the sentence reporting the share.**

**Record absolute bytes plus the date, and derive the share.** A share is two measurements and the
denominator usually moves faster than the numerator. One finding's share fell from 45% to 37.9% in a
day while the section it named had **grown**.

**State the token conversion once and apply it uniformly.** Bytes ÷ 4 is close enough for prose and
markdown, costs no dependency, and must be labelled an estimate. Never use it to separate two findings
that a byte count does not already separate.

---

## Before you leave for `judge.md`

You should be holding four inventories, each with figures and a date; a catalogue with a search record
covering three axes and its empty rounds; and a byproduct register that has been collecting since step
1. **If the catalogue has no search record, step 5 is not finished** — go back rather than forward,
because everything downstream will read as complete over whatever you gathered.
