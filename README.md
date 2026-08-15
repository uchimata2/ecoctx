# ecoctx

**An audit of what your coding agent reads before it does anything.**

Every session an agent starts, it pays for a set of files it did not choose: the instructions the
harness loads unasked, the index it is handed, the skill descriptions it must read to know which one
to use. That cost is charged on every turn of every session, and almost nobody has measured theirs.
`ecoctx` measures it, ranks what can be changed, and writes the two documents that let the next
person check the work.

It is a skill, not a linter. It runs sixteen steps in two phases, produces a ranked register of
findings and a report, and then — this is the part that is unusual — **comes back after the fixes are
built and grades its own predictions against what they actually bought.**

## Why the second phase is the point

The method has been run once, end to end, on a real repository. Thirteen findings were raised,
ranked, turned into tasks, and implemented. Phase 2 then paired every finding against its outcome:

- **2 of 13 bands held as written.** Four were wrong on magnitude, three on shape, one on premise,
  one was measuring the wrong unit entirely and was withdrawn.
- **Every error was in the *remedy* half and none in the *observation* half.** The inventory said
  where the weight was and was right thirteen times out of thirteen. What it could not do was price
  the change.
- One finding understated its own effect by **twenty times**, because it compared two surfaces
  instead of measuring the question the agent actually asks.
- Two findings were worth doing for reasons their own rows never named, and one was worth doing by
  being **refused** — the refusal was the deliverable.

A method that only publishes its steps is asking to be trusted. The grading table is what makes this
one checkable, and it is why the rubric here marks a proposed remedy as a **hypothesis** at the
moment you write it, rather than in a paragraph you read afterwards.

## What it is not

- **Not a token-saving tool.** It finds where your bytes go. Some of what it recommends makes the
  repository *larger* — two of the largest findings in the one recorded run reduced nothing and were
  still right. If you check the total and expect it to fall, you will think the method failed.
- **Not a policy author.** The last step will not emit a rule without naming a document that already
  governs the thing, pricing what the rule costs to load, and stating whether it extends, narrows or
  replaces the nearest existing one. Where it collides with a policy you already have, it reports the
  collision instead of resolving it.
- **Not bound to one agent or harness.** No file of any one repository is named in the method, and
  nothing assumes a particular set of tools, plugins or configuration formats. That constraint is
  tested by running it somewhere else, not asserted.
- **Not a substitute for reading.** Every band it writes is a claim you can check, and several in the
  recorded run did not survive being checked.

## Status

**Pre-publication, and honest about why.** The method has one recorded end-to-end run, on the
repository where it was invented. Running it against a repository that is neither that one nor this
one is an acceptance criterion, not a nice-to-have: until that has happened, the first stranger to
run it would also be its first real test.

Improvements arrive two ways, and they are not the same channel. **Defects and requests belong in
GitHub Issues** once this is public. **The method itself improves from runs** — each one produces a
graded table like the one above, and that is the evidence a change to the rubric needs. An issue
saying a step feels thin is worth much less than a search record showing what the step missed.

## Licence

MIT. See [LICENSE](LICENSE).
