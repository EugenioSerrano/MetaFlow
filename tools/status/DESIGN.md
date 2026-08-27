# status — walk the documents and report their state

**Status:** specification.

## The problem

To know where a folder stands, someone has to open every file in it and read
its frontmatter. `bugs/` with forty BUGs is forty file reads to answer *"which
ones are still `draft`?"* — cheap for a program, expensive for an agent, and
tedious for a human.

That is the whole job: **walk the documents, read the state each one already
records, and return it.**

## What it does

```
devflow status bugs/                      every BUG with its status
devflow status functional/bolts/          every Bolt in the folder
devflow status US-012.BOLT-003            one artifact
devflow status --pending                  everything waiting on a human
devflow status --json                     for the agent
```

Per artifact it reports the `status:` its frontmatter already holds — the same
value the document carries and the INDEX shows. Filterable by state, so
*"which TCs are still draft"* is one call.

**The `status:` field stays exactly where it is.** This tool reads; it is not a
replacement for storing state, and it never changes what a document says.

## Two states the methodology also derives

For two artifacts there is a second state that is deliberately **not** a field,
and the tool can surface it alongside the stored one — clearly labelled, and
still without writing anything:

| Artifact | Stored `status:` | Additional state, derived |
|----------|------------------|---------------------------|
| **Bolt** | `candidate` · `approved` · `deprecated` — its **approval** state | `In Development` · `Development Completed` · `Done` — its **development** state, derived from the manifest's approvals (§3.12) |
| **MEM** | *(none by design, §2.12)* | pending review · approved · `changes_requested`, derived from its `HITL-MEM-Approval` |

These are two different questions about the same Bolt — *"is it approved to
work on?"* versus *"how far along is it?"* — and the methodology answers the
first with a field and the second from the approvals. The tool shows both so a
reader does not have to open the manifest for the second.

## The `--json` shape

Agents parse this, so it is specified here rather than left to the
implementation. **One call returns everything an `INDEX.md` row needs** — which
is what makes refreshing an index cost one invocation instead of one file read
per artifact.

```json
{
  "tool": "status",
  "output_version": 1,
  "folder": "devflow/bugs/",
  "artifacts": [
    { "id": "BUG-004", "slug": "invoice-pdf-timeout",
      "file": "BUG-004-invoice-pdf-timeout.md",
      "status": "resolved", "derived": {}, "defects": [] },
    { "id": "BUG-005", "slug": "login-retry-loop",
      "file": "BUG-005-login-retry-loop.md",
      "status": "draft", "derived": {}, "defects": [] }
  ]
}
```

The envelope carries its own `output_version` because an agent written today
must not break when a field is added tomorrow. It is bumped when a field changes
meaning or disappears — never for an addition.

### Stored and derived never share a level

What the document itself records sits at the top of the entry. What the tool
worked out from somewhere else sits under `derived`. The distinction the
previous section makes in prose is therefore visible in the data, and a caller
that only wants recorded facts ignores one key:

```json
{ "id": "US-012.BOLT-003", "slug": "invoice-download",
  "file": "US-012.BOLT-003-invoice-download.md",
  "status": "approved",
  "derived": { "development": "Development Completed" },
  "defects": [] }
```

```json
{ "id": "MEM-260802-1015", "slug": "invoice-download",
  "file": "MEM-260802-1015-invoice-download.md",
  "status": null,
  "derived": { "review": "pending" },
  "defects": [] }
```

`"status": null` on a MEM is not a defect — §2.12 gives the MEM no status field
at all, which is why its state can only appear under `derived`.

### Every file gets an entry

A file that cannot be parsed, or whose name does not conform, still appears —
with `status: null` and the rule it breaks in `defects`:

```json
{ "id": null, "slug": null, "file": "bug-006 draft final.md",
  "status": null, "derived": {}, "defects": ["N11"] }
```

Reporting problems in a separate array would force every caller to merge two
lists before rendering an index, and the callers that forgot would silently drop
artifacts from it — the exact failure an index exists to prevent.

Defects are reported, never repaired, and never change the exit code: `status`
returns `0` even when every artifact in the folder is malformed. Deciding that
something is *wrong* is `validate`'s job, and it is the one with the failing
exit code.

### Order is part of the contract

`artifacts` is sorted by `id` ascending, gaps left as gaps, non-conforming names
last. Deterministic order is what makes the rendered `INDEX.md` deterministic:
the same folder always produces the same file, so a diff on an index shows only
what actually changed instead of a reshuffle nobody asked for.

### `--pending`

```json
{ "id": "US-012.BOLT-003",
  "file": "US-012.BOLT-003-invoice-download.md",
  "checkpoint": "HITL-MEM-Approval",
  "review_ready_at": "2026-08-14T09:12:00Z",
  "elapsed_hours": 51.3,
  "elapsed_basis": "wall_clock",
  "escalation": null }
```

**`elapsed_basis` is not a detail.** §3.0 measures the escalation thresholds in
**working time**, and a tool reading a repository has no calendar — it does not
know the team's hours, its holidays, or its timezone. So it reports wall clock
and says so.

Wall clock is an upper bound on working time, which makes it useful in exactly
one direction: **it can exonerate, never convict.** Under 4 h of wall clock the
review is certainly inside the target; over it, only a human or a configured
calendar can tell. `escalation` therefore stays `null` until such a calendar
exists — see the open decision at the end.

## The thing nobody computes today

§3.0 defines escalation thresholds for **Time-to-Human-Review** — ≥ 4 h a
process defect for the retro, ≥ 8 h escalate to the artifact owner, ≥ 24 h
escalate to the PO or Tech Lead. The timing contract has recorded
`review_ready_at` in every manifest since 4.0, and **nothing reads it**.

`status --pending` surfaces it in one call, which turns three documented
thresholds into something the team actually sees — with the honest caveat above
about wall clock versus working time.

## Boundaries

- **Read-only, always.** It never writes a `status`, never changes one, never
  persists a derived state anywhere.
- **It never invents.** A `status` value outside the §3.15 table is reported as
  such, not normalized. A missing manifest is reported as a G33 defect, not
  filled in.
- Where it derives, the rules come from §3.12 and §2.12 — read, not
  reinterpreted.

## Is this just the validator?

No — but it is the same binary, and it shares most of its engine.

| | `devflow validate` | `devflow status` |
|---|---|---|
| Question | Is anything **wrong**? | Where is everything **at**? |
| Output | Violations, each with its rule id | State, as recorded |
| Exit code | `2` blocking, `1` warnings — **fails CI** | Always `0`; reporting is not failing |
| Moment | Before *acting*: *"may I generate this SPEC?"* | Before *choosing*: *"what is there to work on?"* |

Both walk the same artifacts and read the same frontmatter, which is why they
are subcommands of one executable rather than two programs. The line between
them is the moment of use: an agent about to pick up work asks `status`; an
agent about to generate a SPEC asks `validate`, because that question has a
verdict and a blocking rule behind it (G13).

## Relationship to `indexer`

Same walk, different shape of output: **`status` prints the state as a list;
`indexer --render` prints it formatted as the folder's `INDEX.md`.** Neither
writes — the agent saves the rendered INDEX when it differs from the current
one. One traversal, two consumers, which is what guarantees the INDEX and the
live view can never disagree about how a document's state is read, only about
how fresh the INDEX is. That freshness gap is exactly what `indexer --check`
reports.

Build them together.

## Open decision: the working calendar

`escalation` cannot be filled without knowing what a working hour is for this
team. Three ways out, in order of appetite:

1. **Leave it `null`** and report wall clock only. Honest, zero configuration,
   and already useful — a review under 4 h of wall clock is provably within
   target, which covers the healthy majority.
2. **Read a calendar the project declares**, next to `LANGUAGE` — working days,
   working hours, timezone, holidays. Then `escalation` becomes computable and
   §3.0 is finally enforced as written.
3. **Report both**, wall clock always and working time when a calendar exists.

Option 2 is the only one that satisfies §3.0 literally, and it is also the only
one that adds a file to `devflow/` — so it is a methodology decision, not a
tooling one, and it does not belong to this repository's toolchain to make
unilaterally.
