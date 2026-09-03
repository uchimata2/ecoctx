# ecoctx

An audit of what your coding agent reads before it does anything.

Every session an agent starts, it pays for a set of files it did not choose: the instructions the
harness loads unasked, the index it is handed, the skill descriptions it must read to know which one
to use. That cost is charged on every turn of every session, and almost nobody has measured theirs.
`ecoctx` measures it, ranks what can be changed, and writes the two documents that let the next
person check the work.

It is a skill, not a linter. It runs sixteen steps in two phases and produces a ranked register of
findings and a report. Then, after the fixes are built, it comes back and grades its own predictions
against what they actually bought.

## Why the second phase is the point

The method has been run once, end to end, on a real repository. Thirteen findings were raised,
ranked, turned into tasks, and implemented. Phase 2 then paired every finding against its outcome.

Two of the thirteen bands held as written. Four were wrong on magnitude, three on the shape of the
change, one on its premise. One was measuring the wrong unit entirely and was withdrawn.

Every error sat in the proposed remedy, and none in the observation. The inventory said where the
weight was and was right thirteen times out of thirteen. What it could not do was price the change.
One finding understated its own effect by twenty times, because it compared two surfaces instead of
measuring the question the agent actually asks. Two were worth doing for reasons their own rows never
named. One was worth doing by being refused, and the refusal was the deliverable.

A method that only publishes its steps is asking to be trusted. The grading table is what makes this
one checkable. It is also why the rubric marks a proposed remedy as a hypothesis at the moment you
write it, rather than in a paragraph you read afterwards.

## What it is not

It does not save tokens on its own. It finds where your bytes go, and some of what it recommends
makes the repository larger. Two of the largest findings in the recorded run reduced nothing and were
still right, so a reader who checks the total and expects it to fall will think the method failed.

It does not write policy for you. The last step will not emit a rule until it has named a document
that already governs the thing, priced what the rule costs to load, and said whether it extends,
narrows or replaces the nearest existing rule. Where a proposed rule collides with one you already
have, it reports the collision instead of resolving it.

It is not bound to one agent or harness. No file of any one repository is named in the method, and
nothing assumes a particular set of tools, plugins or configuration formats. That constraint gets
tested by running the skill somewhere else, not by asserting it.

It is not a substitute for reading. Every band it writes is a claim you can check, and several in the
recorded run did not survive being checked.

## What it costs to have installed

A skill that audits context economy and is expensive to keep around is the joke that writes itself,
so here is the bill. Measured 2026-09-03, in bytes off the filesystem.

| Stage | Bytes | Paid |
| :--- | ---: | :--- |
| Routing description | 497 | every session, whether or not you use it |
| `SKILL.md` body | 5,260 | when the skill activates |
| `references/measure.md` | 24,587 | steps 1 to 5 only |
| `references/judge.md` | 31,581 | steps 6 to 11 only |
| `references/standing.md` | 12,636 | steps 12 to 16 only |

497 bytes is the only figure that compounds. Everything below it is paid once, by a session that
asked for it, and never two references at a time, because the body routes to exactly one. The largest
possible single-phase cost is 5,260 plus 31,581, or 36,841 bytes, and the common case is smaller.

The description started at 610 and lost 18.5% to duplication with every trigger kept. That trim is
the method applied to itself, and it is the first measurement this project made.

## Status

Pre-publication, and honest about why. The method has one recorded end-to-end run, on the repository
where it was invented. Running it against a repository that is neither that one nor this one is an
acceptance criterion rather than a nice-to-have: until that has happened, the first stranger to run
it would also be its first real test.

Work on this repository is tracked as GitHub Issues, using taskmd's issues backend. One task per
issue, and the issue number is the task id. Two consequences worth knowing before you open one:
`status:` is a label, and the open or closed state of an issue is written from that label, so closing
an issue in the web interface changes the rendering without changing the fact. Ids come from GitHub,
so nothing here writes a task id before its issue exists.

Improvements arrive two ways, and they are not the same channel. Defects and requests belong in
Issues. The method itself improves from runs, because each one produces a graded table like the one
above, and that is the evidence a change to the rubric needs. An issue saying a step feels thin is
worth much less than a search record showing what the step missed.

## Licence

MIT. See [LICENSE](LICENSE).
