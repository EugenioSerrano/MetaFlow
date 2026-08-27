# 51-agents/ — Index

**Methodology version:** 1.1

The MetaFlow Agent definitions family. The canonical contract and the
create-your-own-agent guide live in [README.md](README.md); the
per-platform wrappers are projected by the **Coordinator** (the
MetaFlow agent itself, one per tool) from the **live definitions in
[`squad/`](squad/)** into the project's platform folders
(`.claude/51-agents/`, `.opencode/51-agents/`, `.github/51-agents/`,
`.codex/51-agents/`) following the mapping in [VERIFICATION.md](VERIFICATION.md)
(N×4 parity verified) — the kit ships no pre-built role wrappers.

## Examples (shipped — read-only references)

| Example | Produces | Status |
|---------|----------|--------|
| examples/functional-analyst/ | feature US | shipped |
| examples/architect/ | ADR | shipped |
| examples/developer/ | SPEC + code + tests | shipped |
| examples/qa/ | TC/tests + MEM reviews | shipped |
| examples/reviewer/ | REV + MEM/DISC approvals | shipped |
| TEMPLATE-new-role/ | **generic template** — copy it (or an example) into `squad/` to create any project-defined role | template |

> Examples are **copied, never edited in place and never
> roster-referenced** — see [examples/README.md](examples/README.md).

## Squad (live — your project's agents)

| Agent | Role | Produces | Status |
|-------|------|----------|--------|
| —     | —    | —        | —      |

> The Coordinator creates agents here and installs their wrappers — see
> [squad/README.md](squad/README.md). List each agent in this table and
> add its actor entry to the roster (`53-actors/`).

## The Coordinator

**No separate folder** — the Coordinator is the MetaFlow agent
itself, shipped per platform (`CLAUDE.md`, `.51-agents/skills/…`,
`.github/51-agents/…`, `.opencode/51-agents/…`) and **evolved** to act as the
orchestrator: the shared body carries the "The Coordinator (the
orchestrator)" paragraph (routes, delegates production, spawns approvers,
records — **never signs**, `approves: []`), and each platform preamble
declares the spawn-topology mechanics. The wrappers are projections of
role agents only — no coordinator sub-agent exists.

## Notes

- **Examples are skeletons** — adopters copy them into `squad/` and
  instantiate; they never edit the kit's examples in place.
- **Project-defined agents** live in `squad/` and are listed in the Squad
  table above (the adopter's `51-agents/` family grows with their team).
- The **Coordinator is not generated** (MODEL Y): its projections are the
  four platform agent files; only role agents get wrappers.
- Per-platform capability status: [VERIFICATION.md](VERIFICATION.md).
