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

**The axis's boundary marker is itself one of the most expensive events in a session, and the axis
must not be read as bounded by something free.** A compaction re-sends the whole conversation in order
to write its summary, leaves that summary behind as the new floor — priced at **12% of the summed
conversation to that point** in the harness's published model, read 2026-09-03 — and drops the cache
that had been making the re-send cheap. So the event this axis counts *up to* costs more than most of
what the axis ranks.

Two consequences, and the second is the one that catches an auditor out. **Lengthening the runway
defers that bill as well as the compaction**, so a runway finding is worth more than its own byte
count. And under #12's ruling compaction is **not** bandable: its cost side is money and a cache while
its benefit is a freed window, which is the runway-against-money trade and not a window against a
window. Name it, price it, keep it out of the ranked list.

**A cost that is only money is named, never ranked, and the silence is a decision rather than an
omission.** Some acts move a session's bill by an order of magnitude while leaving the window
untouched — the same bytes sit in it before and after — so this axis cannot rank them at all. An
audit that quietly scored them last would be reporting an accident of the rubric as a judgement.
Record them as F6 findings (`judge.md`), mark them `controller: user`, keep them out of the ranked
list, and **say in the report that you did.**

**The method names repricing acts and declines to price them**, which is the artifacts-not-sessions
boundary held rather than widened. Such an act changes no file and runs no command; it is entirely
how the session was driven, is inherited by no clone, and is reachable only by whoever is present.
Naming it costs nothing and is worth doing. Measuring it would need a rate model, and rates belong in
a run's report, where a date makes them honest.

**The worked example is delegation, and it earns its place because the two verdicts disagree while
every figure agrees.** Delegating read-heavy exploration keeps the file reads out of the main window
and returns a summary; the same events cost more in total than reading inline. Under context runway
that is an unambiguous win. Under money it is a loss. This method reports the runway win, records the
money cost beside it, and ranks only the first — so a reader who checks the total finds the
arithmetic already stated rather than concluding the method missed it.

**That is the runway-against-money trade, and delegation carries a second one that is not it.** The
delegate's own window is context, so main-window bytes against delegate-window bytes are two
measurements of the same quantity and **are** banded — `bimodal`, in `judge.md`, where the figures and
the three conditions live. Two trades, one subject, and the words for them are nearly identical: this
sentence exists so a reader meeting one does not think they have met the other.

**No fact loses its only home.** Layering and load-on-demand are the instruments; deletion is not. A
finding whose gain depends on a rule becoming unfindable, a gate weakening, or a lesson disappearing
is recorded with that risk stated and ranks below everything else.

---

## The four surfaces, and the fifth thing that cuts across them

Every agent-driven repository has all four. **An audit that skips one ranks the other three against an
unknown denominator.**

| | Surface | What it holds | Why it is separate |
| :--- | :--- | :--- | :--- |
| **A** | **The load path** | What enters context without anyone asking — instruction or rule files at every scope, any persistent store the agent recalls from, whatever is carried over from the last session, hooks that fire on tool events, the environment block the harness appends, every scheduled task, the catalogue of capabilities the agent is offered, and the tool interface | Its tier 1 is paid on **every** turn of **every** session; the rest is paid once per activation. Its items differ in **who controls them**, and in **how often each is paid** |
| **B** | **The read path** | What a session must read to do one unit of work — the specification, the conventions, the lessons, the index, the work item, its neighbours, the source it edits, **in whatever format each of them arrives in** | Paid on the turn it is read and on every turn after it, and it grows with the project's age |
| **C** | **Tool output** | What commands print back — gate reports, per-row verdict listings, test suites, search results | Paid on the invocation that produced it, and again on every turn after it, and the only surface where a tool's own default decides the cost |
| **D** | **Write volume** | What a session produces — work-item prose, log rows, commit messages, the reconcile edits a closure owes | Paid twice: once written, and again when the next session reads it as surface B |

**E — workflow and tooling** cuts across all four: when a gate *must* run rather than *may*, whether a
suite runs whole or targeted, whether exploration searches or reads, whether read-heavy work is
delegated, how a session hands over. Its findings change **when** a cost is paid rather than how large
it is, so report E as its own section.

**A payment rule above names one event. The cost is that event multiplied by how often it recurs**,
and the multiplier is the finding record's `Recurrence` field (`judge.md`), which names it and
declines to order it. Read the two together, because a rule read alone invites the wrong sum: a
conversation is re-sent from the top on every turn, so a 3,000-token tool output at turn 4 of a
40-turn session is not paid per invocation once — it is paid 37 more times.

**Compounding is a recurrence value, not a property of surface A.** A saving on B or C compounds too,
against the turns that follow it. What is unique to surface A's tier 1 is that its multiplier is
*every* turn of *every* session — the extreme case, not a different kind of case.

**Unattended execution is an item class on surface A, reported here under E.** A scheduled task, a
background job or a running agent team — a cron entry, a timed routine, a subagent left working —
fires with nobody present and re-sends the whole context on every fire. Nothing on the filesystem changes when its interval does, so **no byte count reaches it**:
its cost is `per-activation` where the activation is a clock. It earns no surface and no family of its
own — a new one has to name a unit none of the existing ones takes (`judge.md`, *F6's unit*), and a
scheduled task's unit is the load path it re-sends. Surfaces A-D also rest on *every agent-driven
repository has all four*; most have no scheduled task, so a fifth surface would be empty in the common
case and an audit skipping it would be skipping nothing.

**Set each interval against the cache lifetime and state the result in `Cache` vocabulary.** A task
firing less often than the cache lives is paid **cold** on every fire; one firing inside it is paid
**warm**. That is the whole relation, it needs no lifetime figure, and a figure is refused here for
the reason this method refuses every rate. The consequence is worth stating because it reads
backwards: **running a task more often can be cheaper.** Reported behaviour, not measured here.

### Tiers, and why only surface A gets a budget

| Tier | Loaded | Membership rule |
| :--- | :--- | :--- |
| 1 | every turn | **What the harness loads without being asked.** A property of the tree, not a list someone updates |
| 2 | when an activity of a kind starts | What a packaged procedure or workflow document pulls in when it activates, and anything else an **event** triggers: a hook firing on a tool call, a rule that loads because of what is being edited |
| 3 | when a phase or mode begins | What tier 2 loads one at a time, for the branch actually taken |

**Only tier 1 gets a budget.** Tiers 2 and 3 are not paid every turn, so a size limit there measures
the wrong cost; what constrains them is the load-one-at-a-time rule. **Say this explicitly** rather
than leaving it inferred — it is the visible price of budgeting tier 1 alone, and it means the tier-2
documents are allowed to grow.

**A tier says when an item loads; recurrence says how often that happens.** They are different
questions, and the tier model answers only the first. Tiers 2 and 3 are paid **per activation**, so
their cost is size times activations — a product no byte count reaches, because the number of
activations belongs to the activity and not to any file.

**A per-turn audit therefore reports a tier-2 file as free, and the arithmetic is the smaller half of
the error.** One config read on every run of a single procedure went unmeasured for months at 16,159
bytes, of which 13,031 was narrative no schema asked for. The worse half is that most of it
**duplicated the always-loaded file** — so a session could act on the stale on-demand copy while the
fresh authoritative one sat in its context, and nothing reads such a file between runs, so nothing
could catch it. Measured 2026-08-23 in a sibling repository, and dated because it is one file.

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

**A controller says who can change an item. It never says the item's size is fixed.** The environment
block a harness appends — working directory, platform, shell, and a summary of the repository's
version-control state — is `harness` by controller and **sized by the project**. A project can
therefore influence a cost it cannot control, and a reader who takes `harness` to mean *nothing here
moves* will not look.

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

1. **Inventory the load path (A).** Everything that enters context unasked, with its size, its
   controller and its recurrence. Whatever your agent calls them, look for: instruction or rule files
   at every scope; any persistent store the agent recalls from by itself; anything carried over from a
   previous session; **rules that load because of what is being edited**, which arrive mid-session and
   unasked; **hooks that fire on tool events**, whose output enters context; **the environment block
   the harness appends** — working directory, platform, shell, and a summary of the repository's
   version-control state; **every scheduled task or background job, with its interval**; **the
   catalogue of capabilities the agent is offered** — the name-and-description listing of whatever it
   can invoke, paid whether or not the project could use one; and how much of the tool interface is
   present before a tool is chosen. **The item you cannot change still belongs in the inventory,
   marked.**

   **Establish membership by observation — and observe the right thing.** Most of what loads at
   startup is invisible in the terminal: hook output prints nothing, and the environment block and the
   tool catalogue scroll past nobody. So the observation is of the agent's **own report of its
   context**, never of what was displayed. A load path read off the screen is a list of the items that
   happened to be loud.

   **Unattended execution is the one item on this list that observation does not reach**, and it is
   worth knowing before the inventory starts. A context report describes the session in front of you;
   a schedule that fires when nobody is there appears in none of it. That item is **queried**, from
   whatever the harness offers for listing scheduled tasks and running jobs — and where nothing offers
   it, the inventory records that the item could not be enumerated rather than that there were none.
   An unobservable item recorded as absent is the one error on this step that looks like a clean
   result.

   **Extending that rule to the tool interface: record whether deferred loading is active, and read it
   from that same report rather than inferring it from any byte count.** A harness that defers tool
   schemas lists the deferred pool separately and excludes it from the percentage, so the state is a
   line to read rather than a quantity to deduce. Then check for an override: a base-URL, auth-token or
   gateway variable routing the agent through a proxy can turn deferral off **with no warning**, and so
   can the harness's own switch for it — on one harness, `ENABLE_TOOL_SEARCH`, documented with three
   settings. Two byte-for-byte identical trees can differ by tens of thousands of tokens per turn on
   this alone, and **nothing in either tree records which one you are on.**

   **The same rule reaches a persistent store from the other side: record whether the harness caps
   what it loads from that store, and where it does, inventory the cap rather than the file.** Such a
   store is measurable in the ordinary way — its size is a fact about a file, and anyone can check it.
   What is visible nowhere is that the harness may load only the first part of it: nothing in the
   store records the cap, and the file's own size cannot reflect it. A project whose store has grown
   past that bound pays the cap while its inventory reports the file, and the excess buys nothing.
   **The cap is looked up, never measured**, so a run that cannot find it records it as
   **undetermined** rather than as absent — *no cap* and *cap unknown* are different findings, and
   only one of them is safe to act on. Name it by class, never by the harness, the setting or the
   number, all three of which date within a release (step 16).

2. **Inventory the read path (B)** for one representative unit of work, **chosen before the audit
   starts and named in the report.** Record what was opened, **in what format**, how much of it was
   needed, and how much was history rather than operative rule.

   **Format changes the price of identical content**, so an inventory of sizes alone prices the wrong
   thing. A screenshot is charged as an image, whatever it depicts; a PDF page arriving as both its
   text and an image of itself is paid twice for one reading. Record the format even when it is plain text, so that
   *text* is an observation rather than an assumption — and note that the remedy is neither a split nor
   a deletion but a conversion, which is why it is filed under F4 rather than F1 (`judge.md`).

3. **Inventory tool output (C).** For each gate or command a unit of work runs, the size of what it
   prints on a **green** run. The failing case is rare and its verbosity is usually earned.

   **Then say what could be removed without losing the failure signal.** Measuring what a command
   prints is not a remedy, and this surface is the one where a tool's own default decides the cost, so
   an inventory that stops at the size has found the whole cost and proposed nothing. The remedy class
   is F4 (`judge.md`), and it is the one remedy in the method whose demonstration is a matched pair on
   a live invocation rather than a recomputed figure.

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
| **C** | **the harness's own documented mechanisms** | it found three techniques and had never been treated as a source at all. Its published model of what a session loads is also the only external check on step 1's enumeration: run one against the other, and take the **taxonomy** rather than the figures, which are usually illustrative and sized to a window that has since moved |

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

**A known-good case is not always enough, and the case that proves it was a mechanical prose-versus-
rules ratio.** It was proposed as a cheap check that would rank files without anyone arguing about
prose, built, and run over a sibling tree: dates per KB, and lines carrying changelog phrasing. The
calibration refused it. The file cut from 16,159 bytes to 1,845 that same morning scored **mid-table**,
above a document nobody had touched — because the permitted shape for a historical fact ends in a
date, so a fully compliant file is dense in exactly the token the metric counts. The second signal
misled the other way: two 25 KB configs carry one date between them and would rank near the bottom,
and their bulk is guide prose the rule keeps. Ranking by either number and editing the top edits the
wrong files. Measured 2026-08-23.

**So the check is declined, and the declination is the result.** This scan *had* its known-good case
and still could not be read as a finding, because a compliant file and a defective one score alike.
What survives is a ranking for a person to read, reporting what it counted beside the count and saying
in its own output that a compliant file scores high — and that is not a check, so it moves no exit
status. **A scan that cannot separate its known-good case from its target is not measuring the thing
its name claims.**

**A file's size on disk is not what a session pays, and the error runs one way.** A harness may strip
regions before injecting: one always-loaded instruction file carried 1,839 characters of block comment
that never reached the session. An audit ranking by raw size therefore **overstates**, always. Subtract
the stripped regions or report them as their own column — the difference is also a lever, since moving
an argument into a stripped region costs the file and not the session. Observed 2026-08-16.

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

**Prompt length is a rounding error; prompt vagueness is not.** Typed input has been reported at
around 0.01% of a session's spend, so shortening what a person types is not a finding at any band. A
**vague** prompt is expensive, and by a different mechanism entirely: it is paid in the reads,
searches and re-reads it sets off, every one of which is surface B or C at `turns-remaining`. An audit
that reaches for prompt length has found the cheapest thing in the session; the expensive version of
the same observation is unmeasured here and is worth stating as such rather than banding.

---

## Before you leave for `judge.md`

You should be holding four inventories, each with figures and a date; a catalogue with a search record
covering three axes and its empty rounds; and a byproduct register that has been collecting since step
1. **If the catalogue has no search record, step 5 is not finished** — go back rather than forward,
because everything downstream will read as complete over whatever you gathered.
