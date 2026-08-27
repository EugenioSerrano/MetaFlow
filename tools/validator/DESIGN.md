# DevFlow validator — design

**Status:** specification. The implementation lives beside it in `tools/`;
what ships to a project is the compiled executable in `devflow/bin/`.

## It is not a new concept — it is a missing implementation

Two things in the methodology already describe this tool and have no code
behind them:

- **§3.6** lists **`Bolt-manifest validation`** among the conditional AI-native
  gates: *"the manifest must be present, valid against the manifest schema, and
  contain the applicable lifecycle decisions."*
- **§3.12** states that timestamp ordering is *"a validation error **enforced by
  tooling**, since no JSON Schema can express ordering"*, and **§3.0** states
  that a mismatch between an artifact's `review:` contract and its manifest
  projection *"is a validation error"*.

So the methodology already names two validation errors and one gate with no
implementation. The validator fills that hole. It invents nothing.

## Hard constraints

1. **Optional by contract.** `devflow/reports/README.md` promises that no
   tooling is required. The validator can never become a dependency: if it is
   absent, DevFlow works exactly as documented.
2. **Strictly read-only, like every tool here.** It reports; it never writes.
   **There is no `--fix`** — not for an artifact, not for framework hygiene,
   not for anything. It names the defect and the agent decides what to do,
   which is what keeps every change visible in the diff a human reviews.
3. **Rules are a projection, never a source.** Every rule maps to a `G`/`W`/`N`/`T`
   identifier that already exists. A rule with no identifier is a methodology
   change first.
4. **No mandatory runtime.** A single self-contained binary per platform (Go or
   Rust) removes the "install Python 3.x" problem that made the previous
   generator awkward, and matches the `devflow/bin/` delivery shape: a project
   receives an executable, never a toolchain.
5. **Cheap enough to actually run.** Verifying one rule by hand costs an agent a
   dozen file reads; the same rule as code costs one command. That difference is
   what turns a rule from aspirational into governing — see `tools/README.md`.

## Two modes, one engine

Conflating them produces a validator that demands Bolts from the methodology
repository and version markers from a project.

| Mode | Subject | Checks |
|------|---------|--------|
| `--project` | A repository that *uses* DevFlow | Manifests, artifact naming and routing, traceability, HITL coverage, document `status`, OQ readiness |
| `--framework` | The repository where DevFlow is *authored* | Four-agent body sync, guardrail count invariant, 69/69 version markers, `§` resolution, `status` table vs templates, and **no sentence in `devflow/` that is false inside a project** |

`--framework` is not governance validation — it is **lint of the distributable**.
Its question is *"is this template complete, internally consistent and safe to
copy?"*, not *"does this project comply?"*.

## Rules as data, with a coverage manifest

Each rule declares `id`, `severity`, `mode`, `verdict` (`full` / `partial` /
`none`), the signal it reads, and its exclusions. That makes the killer feature
possible:

```
devflow-validate --coverage
```

emits the rule inventory, and **CI fails when `GUARDRAILS.md` gains a rule the
validator has not classified**. It does not demand implementation — it demands a
declared decision. That single check is what prevents the drift this repository
has repeatedly had to repair by hand.

See [`RULES-G.md`](RULES-G.md) for the classification of all 39 blocking rules:
**23 `full`, 12 `partial`, 4 `none`**.

## First slice — seven checks, not thirty-six

Ordered by (value × lack of ambiguity) ÷ cost:

| # | Check | Why first |
|---|-------|-----------|
| 1 | Manifests against the three v4 schemas | The gate §3.6 already mandates. **Trap: a repository holds exactly one manifest family (§3.12) — an older `schema_version` is an unfinished migration (§5.16), reported as such and not as a schema error** |
| 2 | Timestamp monotonicity `created_at ≤ review_ready_at ≤ review_started_at ≤ decided_at` | Named by §3.12 as a validation error JSON Schema cannot express |
| 3 | Artifact `review:` block vs its manifest projection | The other error §3.0 already names, with no implementation |
| 4 | Document `status` against the §3.15 table | The table is normative and **nothing validates it** |
| 5 | Naming N01–N23 + routing (§5.15) | Regex plus folder. Cheap, catches a lot |
| 6 | Relative links and `§` references resolve | Found a broken cross-repo link and two ambiguous `§` refs in one pass |
| 7 | US/Bolt/TC ↔ manifest bijection, both directions | G33 plus the inverse case: an orphan manifest with no document |

## Traps specific to this methodology

- **Append-only** (`v_bounces[]`, `spec_revisions[]`, `hitl_approvals[]`) cannot
  be checked on a single snapshot — it requires comparing against git history.
  It is the only check that needs the repository's past.
- **`_archive/`**: never run lifecycle *progression* checks there. An archived
  document is finished, and flagging it for a step it will never take is pure
  noise (§5.4, W20). The single exception is **G38**, which asks the inverted
  question — not *did this document advance?* but *was it closed before it was
  moved?* Same folder, opposite predicate: progression rules stay off, the
  closure check stays on.
- **Templates play by different rules.** The nine "broken" links in `TEMPLATE-*`
  files are legitimate placeholders. A validator that flags them will be muted,
  and a muted validator catches nothing.
- **`US-000` breaks every pattern deliberately**: no manifest, no approval
  lifecycle, fixed `status: active`. Special-case it, as `functional/README.md`
  already warns.
- **Never auto-fix anything.** Reporting a defect and repairing it are two
  different acts, and only the second one needs a human watching.

## Output

- **Human:** `file:line` + rule id + **the verbatim message from
  `GUARDRAILS.md`**. Quoting rather than paraphrasing matters: two wordings of
  the same rule drift, and then the validator becomes a third source of truth.
- **Machine:** SARIF, so GitHub annotates pull requests inline.
- **Exit codes:** `0` clean · `1` warnings (`W`) · `2` blocking (`G`). Maps
  directly onto CI.

## Where it runs

1. **Pre-commit** — the fast subset (naming, schema, links).
2. **CI** — everything, as the implementation of the §3.6 gate.
3. **The agent, before pausing at `HITL-MEM-Approval`** — its output joins the
   package the human reviews. This is the most interesting one: it turns the
   validator into evidence rather than a side tool, which is precisely what
   §3.6 describes.
