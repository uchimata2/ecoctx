---
# ---------------------------------------------------------------- identity
id_field: id               # front-matter field holding the task id
id_prefix: #               # a GitHub issue number: #7, #41, #1024
id_width: none             # GitHub allocates ids; no width can describe them
title_field: title         # one-line name, shown in every generated view
tasks_dir: tasks           # unused on this backend; see "The folder that is not used"

# ------------------------------------------------------------------ status
status_field: status       # which vocabulary below carries open/closed meaning
open_statuses: [proposed, specified, planned, in_progress, blocked, review]
blocked_status: blocked    # the value meaning "held up"

# ------------------------------------------------------------- deliverables
deliverables_field: deliverables   # paths a task produces, relative to the project root

# ---------------------------------------------------------------- ordering
value_field: business_value  # estimated worth
effort_field: effort         # estimated cost

# ------------------------------------------------------------------- hooks
after_write: none          # taskmd writes nothing here — there are no task files

# ------------------------------------------------------------------- views
context_fields: [status, phase, type, work_package, owner]
index_columns: [work_package, status, phase]
---

# ecoctx — task schema

Work on this repository is one task per GitHub issue, under taskmd's **GitHub Issues** binding:
`taskmd/skills/taskmd/docs/bindings/github-issues.md` in the installed plugin. The binding defines
no fields and no vocabularies of its own — it reads this file, exactly as the local binding does.

## What is deliberately not copied here

The shipped default (`taskmd/defaults/config.md`) is the **only** description of what a key means,
and it says so. Copying its prose into this repository would be a second copy of one fact — the
drift the plugin exists to remove, and the drift this repository exists to measure. So this file
carries the values and the three things that are true *here*, and nothing else. Read the shipped
default for what any key means.

Two consequences of that choice, both accepted: `check` may report `CONFIG DRIFT` when a shipped
vocabulary gains a value this file does not carry, which is advisory and never a problem; and
adding a key to the shipped schema will fail this project on the next upgrade, with an error
naming the key. Both are documented there.

## The folder that is not used

`tasks_dir` names no folder that matters. The binding states it is unused — there are no task
files, because the issue list *is* the index, computed on demand. The key is still written because
a config **replaces** the shipped default rather than merging with it, so every key must be
present, and a missing one is an error naming the key.

The value is nevertheless checked against the filesystem whenever the config is read, so any
taskmd command run in this repository fails until `tasks/` exists. This project does not create it:
no local command has anything to read, and an empty folder committed to satisfy a validator would
be a fact about the tool rather than about the work. Ids, labels, edges and state all live in
GitHub, and `gh` is what reads them.

## Identity

`id_width: none` is the value that says ids are **allocated, not composed**. It is not the width
check switched off: where a project composes its own ids the width is what makes a mistyped one
reportable, and here an id cannot be mistyped because nothing ever composes one. `gh issue create`
returns it and the project reads it back.

Nothing in this repository may write a task id before its issue exists — not a branch name, not a
commit message, not a line in a document. That is the binding's first assumption, and the README
states it for readers who never open this file.

## Edges

`Derives` is the inverse, computed and never written down. Record a dependency on the task that is
blocked, not on the blocker.

On this backend `parent` and `blocked_by` have native carriers and are visible from both ends
without traversal. `related` has none: it lives in the `Related` line of the issue's property block
and nowhere else, which makes it the one edge a careless body rewrite deletes without error.

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

Every value below is a GitHub label named `<field>:<value>`. The labels are the setup: `gh` will
not invent one, and a mistyped label name fails the write rather than silently mislabelling.

The rows are the shipped defaults, kept whole rather than trimmed. Trimming would save labels that
cost nothing to hold and would drop this project out of drift reporting for any row it replaced.

Order is rank, best first: `critical` outranks `high`, and `xs` is cheaper than `s`.

| Field | Values |
| :--- | :--- |
| status | proposed, specified, planned, in_progress, blocked, review, done, cancelled |
| phase | specify, plan, implement, review |
| type | analysis, decision, deliverable, research, fix, admin, audit |
| business_value | critical, high, medium, low |
| effort | xs, s, m, l, xl |

## The one thing to get right

`status` is the fact; the open or closed state of an issue is a **rendering** of it, written from
the `status:` label and from nothing else. A status change is two writes:

```bash
gh issue edit <n> --remove-label "status:planned" --add-label "status:done" && gh issue close <n>
```

Never the second without the first. Closing an issue in the web interface changes the rendering
while the fact stays put, and no view will flag it.
