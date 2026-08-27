# examples/ — shipped role definitions (read-only references)

The five example role definitions — `functional-analyst/`, `architect/`,
`developer/`, `qa/`, `reviewer/` — each an `agent.yaml` + `prompt.md`
following the definition contract (see [`../README.md`](../README.md)).

**The rules:**

- **Copy, never edit in place.** These are references: instantiate your
  own agent by copying the closest example (or
  [`../TEMPLATE-new-role/`](../TEMPLATE-new-role/)) into
  [`../squad/`](../squad/) and adapting it there.
- **Never referenced by the roster.** The roster's (`actors/`)
  `definition:` pointers reference `agents/squad/<id>/…` only — an example
  carries no identity in your team.
- **Never installed.** The Coordinator projects wrappers from `squad/`,
  not from here.

The five examples are references, never a closed enum — your squad defines
the roles your project needs.
