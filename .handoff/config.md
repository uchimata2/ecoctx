# Handoff config — ecoctx

Read by the handoff core (`handoff.core.md` §0). Plain Markdown, no parser, so the `key: value`
shape stays simple. Nothing validates this file automatically — ask the skill to **check** it after
any edit.

## Core keys

- `handoff_file`: .handoff/HANDOFF.md
- `tracker`: github-issues
- `tracker_status`: label:status:
- `tracker_status_done`: done
- `tracker_workflow`: the taskmd method, `plugin/skills/taskmd/docs/METHOD.md` in the taskmd repository
- `project_docs`: README.md, skills/ecoctx/SKILL.md, skills/ecoctx/references/
- `reconcile_targets`: README.md, .taskmd/config.md, assets/, GitHub Issues on uchimata2/ecoctx

`memory` is not a project key. Claude Code supplies `memory: claude` from its own stub.

## Why the live handoff is not tracked and this file is

`.gitignore` drops `.handoff/HANDOFF.md`, `processed_*` and `discarded_*`, and keeps this file.
A handoff is one session's state on one machine; the config is a fact about the project. The
consumed handoffs accumulate at roughly one file per session and are never deleted, so that folder
grows locally and stays out of the history.

## `tracker: none` was provisional, and it has been resolved

**The binding this section was waiting for shipped on 2026-08-16**, one day after the section was
written. `bindings/github-issues.md` in the handoff skill implements the contract's five operations
through `gh`, and the four keys above are taskmd's own recipe for joining the two
(`plugin/skills/taskmd/docs/HANDOFF.md`, the GitHub section). The join needs no translation layer:
taskmd writes each enumerated field as a `<field>:<value>` label, and `label:status:` reads exactly
that.

*The paragraph this replaced is kept below, because the reasoning was right and only its premise
expired — and because a premise that expires in silence is the thing this file exists to catch:*

> Work here is tracked as GitHub Issues under taskmd's binding, but the handoff skill ships bindings
> for Notion and for two local-Markdown shapes only. There is no GitHub Issues binding, so no value
> of `tracker` names one, and `none` is the only honest setting today. […] **So the exception is
> refused in this project.** Task facts go to the issue by hand, with `gh`, and the snapshot carries
> a reference to the issue and nothing more.

**The consequence of the change is that §7.1 no longer applies here.** A task home is now visible to
the skill, so the exception that let task-specific facts sit in the snapshot is not merely refused by
policy — it does not arise. Facts go to the issue because the binding puts them there.

`reconcile_targets` still names the issue list, which was always a floor rather than a ceiling and
never depended on a binding existing.

## What goes stale silently here

The three named in `reconcile_targets`, and each for a different reason:

- **README.md** carries measured byte counts and an installed-cost table. **The figures are no
  longer among them**: #24 landed `tools/check_readme.py` on 2026-09-04, which re-measures all
  five rows and the arithmetic identity on every run of `check_all.py`, in bytes on LF. It caught
  #3's edit to `SKILL.md` in the same batch, before a reader did. What is still hand-kept is the
  README's **prose** — the recorded run's counts, the claims about what the method cannot do.
  **Two more instruments landed on 2026-09-05**, and neither closes that: `check_charts.py` fails
  when a chart in `assets/` draws a figure the prose does not state, and `check_prose.py` fails on
  an em dash, a curly quote or an inflated word. Both cover mechanics. **What a sentence claims is
  still hand-kept**, and every miss recorded here was a claim rather than a character.
  **It fired twice more on 2026-09-05**, in the same batch that gave `check_readme.py` its count
  rules: *it refuses four things* had been five since #39, and *nobody has performed a release* had
  been false since 1.1.0. Neither is a figure, so no instrument could see either — and the first is
  a **count**, of which `check_readme.py` now checks five. A sixth with no rule written for it is
  invisible, and that file's docstring says so out loud.
  **This fired on 2026-09-04**, one batch after it was written: the
  *Status* section still said the method had one recorded run, on the repository where it was
  invented. The batch that made both halves false was two commits from shipping it, and
  `check_all.py` stayed green the whole way, because every figure it checks was still correct.
  Only the sweep caught it.

  *The original entry read: "Any edit to `SKILL.md` or a reference changes numbers that the README
  states as fact and nothing recomputes." It was right for as long as it was true, and it is kept
  here because it is the entry that produced the issue that retired it.*
- **.taskmd/config.md** enumerates the vocabularies, and every value is a GitHub label. Adding a
  value without creating its label fails the next write that uses it.
- **GitHub Issues** renders `state` from the `status:` label, and carries `related` edges that this
  backend derives no inverse for. **Both are now checked** by `tools/check_tracker.py`, the second
  since #81. What is still unchecked here is an edge nobody wrote at either end, which no view can
  see and no checker can either.
