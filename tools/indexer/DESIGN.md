# indexer — keep every INDEX true to its folder

**Status:** specification.

## The problem

An `INDEX.md` is not decoration: it is **where the next sequential number is
claimed** (§5.15). When it drifts from the folder, ID allocation drifts with
it, and two artifacts eventually claim the same number.

Two situations demand a rebuild:

- **Ordinary drift** — an artifact created and never indexed, or a `status`
  changed in the frontmatter and never reflected in its row.
- **Migration** — §5.16 requires every INDEX to be rebuilt from the migrated
  files, with **numbering continuity**: the next number continues from the
  highest migrated ID, gaps stay gaps, nothing is renumbered. An INDEX rebuilt
  as if the folder were new hands out a number the project already spent.

## What it does

```
metaflow index --check              -> diff between every INDEX and its folder
metaflow index --render <folder>    -> print the INDEX this folder should have
```

`--render` prints; it never writes. The agent compares the output against the
current `INDEX.md` and saves it when they differ — so the change lands as an
ordinary diff a human can read, not as a file that silently changed underneath.

The render reads each artifact's own frontmatter `status`, maps it onto the
section structure using the §3.15 status vocabulary and the emoji convention in
`GUARDRAILS.md` — 🟡 draft · 🔄 in motion · ✅ live and healthy · 🏁 terminal
and successful · ⛔ terminal and obsolete · ❌ rejected — and preserves the
`**Last updated:**` footer at the bottom, where the convention requires it.

## Boundaries

- **Writes nothing.** Even though an INDEX carries no HITL checkpoint, the tool
  still only prints: no file on disk changes without the agent putting it there
  (see `tools/README.md`).
- It never invents a status. The artifact's frontmatter is the source; a
  missing or non-conforming `status` is reported, never guessed.
- It never renumbers, never fills a gap, and never drops a row for an archived
  artifact without saying so.

## Open decision

The section structure differs per family — `open-questions/` has five states,
`risks/` four, `bugs/` five, and `analysis/` uses `stable` where others use
`approved`. That mapping needs one home, and the right one is the §3.15 status
table plus the GUARDRAILS emoji convention, **read** by the tool rather than
duplicated inside it. A tool carrying its own copy of the vocabulary is a
second source of truth, which is the defect this repository keeps having to
repair.
