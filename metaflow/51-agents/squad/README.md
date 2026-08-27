# squad/ — your project's live agents

This is the **live workspace** of the `51-agents/` family: one folder per
agent (`squad/<agent-id>/` — `agent.yaml` + `prompt.md`, the same
definition contract as everywhere, see [`../README.md`](../README.md)).

**The rules:**

- **The Coordinator writes here.** Ask your MetaFlow MainAgent to
  create an agent ("create me a reviewer agent") and it scaffolds the
  definition from [`../TEMPLATE-new-role/`](../TEMPLATE-new-role/) + the
  closest [`../examples/`](../examples/) reference into this folder — then
  installs the platform wrapper into your tool's spawn folder
  (`.claude/agents/`, `.opencode/agents/`, `.github/agents/`,
  `.codex/agents/`) per the mapping in
  [`../VERIFICATION.md`](../VERIFICATION.md).
- **The only roster-referenced folder.** The roster's (`53-actors/`)
  `definition:` pointers reference `51-agents/squad/<id>/…` — never
  `examples/`.
- **Ships empty.** The kit delivers no live agents — your squad is yours.
  List each agent in [`../INDEX.md`](../INDEX.md) and add its actor entry
  to the roster.

Reuse is expected: several actors may share one definition (N:1) — each
distinct by its actor `id`, each with its own per-instance `model`.

## The lifecycle consistency contract

Every lifecycle act (install · create · delete) must leave the four legs
agreeing — and under N:1 reuse the **cardinality matters**:

- **Every installed wrapper belongs to ONE actor-instance** and points at
  one live definition in `squad/` — two actors sharing a definition have
  **two wrappers** (each with its own actor `id` and per-instance model).
  **Wrapper files are named by the actor `id`** — under N:1, two actors
  produce two distinctly-named wrappers (naming by the definition would
  collide in the spawn folder).
- **Every definition in `squad/`** has its row in [`../INDEX.md`](../INDEX.md)
  and **≥1 actor** referencing it — zero referencing actors makes it a
  deletion candidate (or it gets flagged; never a silent ghost).
- **Every agent actor** (`metaflow/53-actors/<id>.yaml` with a `definition:`)
  is **listed in `roster.yaml`** — an unlisted actor file is not in the
  team: flag it to the human, never silently adopt it.

**The reference check (before any delete)** — per the shared body: check
`roster.yaml` and the actor files first. Concretely: enumerate every
actor file whose `definition:` points at the target
`squad/<id>/agent.yaml`, and each one's `roster.yaml` listing. Then:

- **Deleting an actor** removes ITS wrapper, its actor file and its
  roster listing — the definition stays while ANY other listed actor
  references it.
- **The definition falls only at zero**: when the enumeration finds no
  remaining referencing actor, the definition (and its INDEX row) may go
  with it.
- **Wrapper-only removal is legitimate**: the actor stops being spawnable
  on that platform until reinstalled; the definition and the roster entry
  stay.

**Edge cases:**

- *Shared definition (N:1):* deleting one actor removes its wrapper +
  actor file + listing; the definition and the other actors' wrappers
  stay.
- *The last actor:* the enumeration hits zero — the definition and its
  INDEX row may go with it.
- *Orphans* (a wrapper without a definition; a definition without an
  INDEX row): repair toward the invariants — reinstall or list — or
  remove; never leave a leg dangling.
- *An unlisted actor file:* outside the team (`roster.yaml` is the
  membership authority) — flag it to the human; the lifecycle never
  adopts it silently.
