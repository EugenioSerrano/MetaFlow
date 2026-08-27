# The 39 blocking rules — validator coverage

Every `G` rule from `devflow/GUARDRAILS.md`, classified by whether a validator
can decide it from the repository alone.

**Method.** Each rule was read verbatim, its `§` references followed into the
methodology (the guardrail text is compressed; the enforceable condition often
lives there), then decomposed into predicates and classified by the evidence
each predicate needs:

| Evidence tier | Checkable |
|---------------|-----------|
| **Structured** — manifests, YAML frontmatter | Yes |
| **Filesystem** — existence, names, placement | Yes |
| **Git** — history, diffs | Yes, with repository context |
| **Prose** — MEM/SPEC/BUG narrative | Only presence and shape, never truth |
| **Human intent** — was the review diligent, is the slice right | No |

`full` = every predicate lands in the first three tiers · `partial` = some do ·
`none` = all land in prose or intent.

## Result

| Verdict | Count | |
|---------|-------|--|
| **`full`** | **23** | G01 G02 G03 G05 G08 G10 G12 G13 G14 G16 G17 G23 G25 G26 G27 G28 G29 G30 G32 G33 G35 G36 G37 |
| **`partial`** | **12** | G04 G07 G11 G15 G18 G19 G20 G22 G24 G31 G38 G39 |
| **`none`** | **4** | G06 G09 G21 G34 |

**59% fully decidable from the repository.** Two of the four `none` rules are
`none` for structurally different reasons — see *Two findings* at the end.

---

## Fully checkable (23)

| # | Signal the validator reads | Exclusions |
|---|----------------------------|------------|
| **G01** | For each `bolt_type: functional`, its parent US manifest holds `HITL-US-Approval` = `approved` with `decided_at` ≤ the Bolt's `generation.created_at` | US-000 has no approval lifecycle |
| **G02** | For each Bolt whose `bolt.sources` include a `BUG-NNN`, that BUG's `review.decision` = `approved` and `decided_at` ≤ Bolt `created_at` | — |
| **G03** | For each `TC-NNN.BOLT-NNN`, the parent TC manifest holds `HITL-TC-Approval` = `approved` before the Bolt's `created_at` | — |
| **G05** | Regex sweep for `HITL-[A-Z-]+-Approval`; every match must be one of the canonical 15. Plus `H1`–`H6` in approval context | Prose quoting the legacy names as invalid |
| **G08** | `bolt.type` ↔ `bolt.id` pattern (already enforced by the schema's conditionals) **plus** the `work_category` ↔ `bolt_type` mapping of §3.8, which the schema does not cover | — |
| **G10** | Every `spec_revisions[].generation.created_at` > the Bolt's `HITL-BOLT-READY-Approval.decided_at` | — |
| **G12** | SPEC frontmatter has a `bolt` field; it is scalar, not a list; grouping all active SPECs by `bolt` yields at most one each | Superseded SPECs with `status: obsolete` |
| **G13** | For each `spec_revisions[].sources`, every approval-bearing source is `approved` with `decided_at` ≤ that revision's `created_at` | Raw `input/` and `analysis/` files carry no approval |
| **G14** | Every `v_bounces[].code_generation.created_at` > the `HITL-SPEC-Approval.decided_at` of its referenced `spec_revision` | — |
| **G16** | `v_bounces[].spec_revision` is a single integer (schema-enforced); plus the V-Bounce window must not overlap a later revision's `created_at` | — |
| **G17** | Each `v_bounces[]` has exactly one `mem`; `mem.ref` resolves on disk; MEM file count for the Bolt equals its `v_bounces[]` count | — |
| **G23** | The three v4 schemas, `additionalProperties: false`, **plus what schema cannot express**: timestamp monotonicity, `spec_revision` referential integrity, `mem.ref` existence | A manifest on an older `schema_version` is an unfinished migration (§5.16), reported under G36 rather than as a G23 schema error |
| **G25** | Per AREV folder: `01` approved before `02`'s `review_ready_at`, `02` before `03`'s | — |
| **G26** | (a) No `sources` entry points at an ADR whose `status` ≠ `accepted`. (b) Git: no diff to an ADR file after its status became `accepted`, except the `status` field itself | Draft ADRs cited as context in prose, not in `sources` |
| **G27** | Same shape as G26 for DISC / REV / AREV: any such artifact in `sources` must carry its approval; an AREV needs all three phases | Optional mechanisms that were never initiated |
| **G28** | No `sources` entry resolves to `analysis/introduction/`, to `reports/`, or to a file with `derivative: true` | — |
| **G29** | BUG with `nature: non-functional`: if `severity: critical`, reviewer `role` ∈ {`architect`, `tech_lead`}; otherwise reviewer `user` ≠ BUG `owner`. The dedicated Bolt mirrors both | Functional BUGs route to the Functional Analyst regardless of severity |
| **G30** | Walk `devflow/`; every directory must appear in §5.1 or be a sanctioned exception: `agents-data/<agent>/`, `adversarial-reviews/AREV-NNN-*/`, any `_archive/` | — |
| **G32** | No `sources` entry starts with `agents-data/` | — |
| **G33** | Bijection: `functional/user-stories/US-NNN-*.md` ↔ `metrics/user-stories/*.json`, and `tests/test-cases/TC-NNN-*.md` ↔ `metrics/test-cases/*.json`. **Both directions** — an orphan manifest is also a defect | `US-000-non-functional.md` carries no manifest |
| **G35** | At each Bolt's `HITL-BOLT-READY-Approval.decided_at`, no `OQ-NNN` with `status` ∈ {`open`, `in-validation`} whose `targets` include that Bolt's parent or governing sources | Historical accuracy needs git; current-state is the practical approximation |
| **G36** | On a commit that changes `devflow/VERSION`: no modification to an approved MEM or ADR, to a recorded HITL decision, or to existing `CHANGELOG.md` lines; and every `metrics/**/*.json` declares the `schema_version` of the family `VERSION` now names | Appending a new CHANGELOG entry is expected. Manifests are *expected* to change on such a commit (§5.16), so the check is the shape of the change, not its absence: diff each manifest against its pre-commit version and require the new one to be a superset — every previous key and value present and equal, additions confined to the fields the new schema introduces, and those set to `null` |
| **G37** | Per AREV Verdict artifact: `judge_model` ∉ {`implementor_model`, `challenger_model`}, or it is `human:<name>` with the VERDICT stating why no third model was available (§3.13) | A human Verdict is valid; models compared by identifier |

## Partially checkable (12)

| # | What it **can** decide | What it **cannot** |
|---|------------------------|--------------------|
| **G04** | Exactly one Bolt references each approved BUG; the BUG and Bolt reference each other | Whether a fix actually happened inside some *other* Bolt's V-Bounce |
| **G07** | Every commit touching source is reachable from some manifest's `git_commit` | The link is weak: **nothing requires a commit to name its Bolt** — see *Two findings* |
| **G11** | Two `v_bounces[]` entries with overlapping `code_generation` windows and different `created_by` | Concurrency that never produced overlapping records |
| **G15** | Git: a governed source changed between a SPEC revision's approval and the V-Bounce that used it, with no new revision | Whether the change was **material** or cosmetic (§2.4.1 defines it, but semantically) |
| **G18** | `decided_by[].user` is a human identifier and is present; **minimum approver count per `risk_class`** (§3.3): low/medium 1, high 2, critical 3 | Whether the reviewer actually inspected the diff — "AI says it's fine" is review quality |
| **G19** | The MEM contains both a filled red section and a filled green section | That red genuinely preceded the production change — the evidence is prose |
| **G20** | Acceptance: `HITL-BOLT-DONE-Approval` requires a prior approved `HITL-MEM-Approval` on the latest V-Bounce | Merge and promotion: deployment data is **deliberately outside manifest v4** (§3.12) |
| **G22** | No artifact or INDEX row asserts `Done` without the acceptance decision | Bolt state is derived, never stored, so there is no field to contradict |
| **G24** | **The artifact `review:` block matches its manifest projection** — §3.0 already calls a mismatch a validation error, and nothing checks it today | Whether a recorded decision was fabricated by a human acting in bad faith |
| **G31** | Files exist under `devflow/input/` that no human deposited | Authorship: under G34 the human commits everything, so git author cannot distinguish agent from human. Mostly an **agent-behavior** rule |
| **G38** | Walk every `_archive/`: each document's frontmatter `status` must sit in the closed set for its family — ADR `superseded\|deprecated`, BUG closed, RISK retired, DISC/REV/AREV closed, Bolt `Done` with its `HITL-BOLT-DONE-Approval` recorded and its package (Bolt, SPEC, MEMs) present alongside it. An `accepted` ADR or an `open` BUG under `_archive/` is a defect | Whether a closed REV/DISC/AREV's findings were each **routed** to the artifacts they affect — routing lives in prose. And like G31 it is partly **agent behaviour**: the repository records where a file sits, never who moved it there |
| **G39** | Every document's frontmatter `status` belongs to its family's row of the §3.15 table — decidable per artifact type, with US-000 as the known exception (`status: active` outside every family) and the derived states (Bolt development state, MEM review state, US/TC progress) checked only for absence, never for correctness | Whether the family↔status mapping the validator assumes matches the routing the §5.15 table defines — the mapping is itself prose; and `status` vs the derived states is a semantic distinction that only misses when the document author mislabeled a field |

## Not checkable (4)

| # | Why | Best available heuristic |
|---|-----|--------------------------|
| **G06** | Whether an expected result was *derived from intent* or *copied from behavior* is intent, not structure | A TC created after the implementation it verifies is a smell, never proof |
| **G09** | Whether a Bolt sentence is "what" or "how" is semantic | Flag code fences, endpoint patterns and class names in a Bolt body — noisy, warning at most |
| **G21** | **Gate results are deliberately excluded from the manifest** (§3.12) and CI evidence is not standardized anywhere | None from the repository. See *Two findings* |
| **G34** | Post-hoc, nothing distinguishes a commit the human asked for from one the agent made unbidden | None. This is **agent-behavior**, enforceable only by the agent |

---

## Two findings the classification produces

**1 · Two rules are unverifiable because of a methodology decision, not because of ambiguity.**

- **G21** needs gate results. §3.12 excludes them on purpose (*"test and gate
  results … belong in the MEM and CI evidence"*), and no CI evidence format is
  standardized. The rule is not fuzzy — the data simply is not kept anywhere a
  validator can read.
- **G07** needs a link from a commit to the Bolt that authorized it. The
  manifest records `git_commit` as the **baseline** the work started from, not
  the commit the work produced, and nothing requires a commit message to name
  its Bolt (§3.15 governs language, not content).

Both would become `full` with a small methodology change — a standardized gate
evidence file, and a required Bolt reference in the commit or a
`produced_commit` field. **That is a product decision, not a coding one**, and
it is worth taking deliberately rather than discovering later that 2 of the 39
can never be enforced.

**2 · Two categories are mixed in the same catalogue.**

Most rules constrain **repository state** and a validator can decide them
post-hoc. But **G34** — and largely **G31** — constrain **agent behaviour**:
they describe what an agent must not *do*, and the repository afterwards looks
identical either way. No validator will ever enforce them; the agent
definitions are their only enforcement, which is exactly why every blocking
rule is now inline in all four agents.

Naming that boundary matters: it prevents the validator from ever being sold as
covering 100% of the blocking rules, when structurally its ceiling is **35 of
39** — 23 fully, 12 partially — and rises to 37 if the two methodology
decisions above are revisited.
