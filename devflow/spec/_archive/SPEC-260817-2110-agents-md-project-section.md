---
id: "SPEC-260817-2110"
title: "The project section of the root AGENTS.md survives every methodology upgrade"
date: "2026-08-17"
author: "eugenio.serrano"
llm: "claude-opus-5[1m]"
status: "approved" # draft | approved | blocked | obsolete
origin: "ADR-001"
bolt: "US-000.BOLT-001"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3" # default for medium (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-18T10:38:44-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-18T10:38:44-03:00"
  decided_at: "2026-08-18T10:50:35-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 2 reviewed as Dev-validator, after raising the five findings that produced it. The material change is finding 4: the install step now excludes AGENTS.md so the file is never destroyed, and recovery from the last commit is demoted to the fallback for a project that copies everything anyway. Both paths documented with an explicit hierarchy. AC-2 generalized to the property rather than one paragraph, AC-9 and AC-10 added for the new scope. Approved as drafted."
---

# SPEC-260817-2110 — The project section of the root AGENTS.md survives every methodology upgrade

| Field | Value |
|-------|-------|
| **Origin** | ADR-001 |
| **Bolt** | US-000.BOLT-001 |
| **ADRs** | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 6 and 7 |
| **Risk Class** | medium |
| **Revision** | 2 |

---

## 1. Objective

Avenga DevFlow ships an `AGENTS.md` that ends by inviting the adopting project
to extend it — *"Project-specific conventions can be added below this line"* —
and then, at upgrade time, provides no rule that protects what the project
wrote there. §5.16 governs the migration of `devflow/` in exhaustive detail and
says nothing about the root `AGENTS.md`; the reconciliation walk that must give
every file a disposition only walks `devflowOLD/`, and this file is not inside
it. The result is that the one place the methodology tells a project to put its
own conventions is the one place an upgrade silently destroys.

This SPEC closes that hole in the product: it gives the file a machine-readable
boundary, states the merge rule normatively, projects it into the blocking
rules, propagates it to the four platform agent definitions, stops those
definitions from directing project content into files that an upgrade
overwrites, and brings this repository's own `AGENTS.md` into the shape the
rule assumes.

If it is not implemented, every adopting project loses its `AGENTS.md`
conventions on every upgrade — and this repository loses its authoring contract
on its first release migration, which is the single operation ADR-001 makes the
backbone of the release loop.

---

## 2. Context

The defect surfaced while preparing this repository to govern itself. ADR-001
established two trees — `distribution-kit/` as the product, the root `devflow/`
as the installed methodology that governs the work — and made the §5.16 release
migration the only mechanism that replaces the root tree. Walking through that
migration concretely exposed the collision: installing the kit puts its generic
`AGENTS.md` over a root `AGENTS.md` that carries the two-tree map, the release
loop, the four-agent synchronization procedure, the preamble parity matrix and
the version bump procedure.

ADR-001 rule 6 records the decision that resolves it: the agent definitions are
pure framework and are overwritten, while `AGENTS.md` is merged at a project
marker — replaced above, preserved below. Rule 7 places the affected paths in
the product zone, so the change travels the full Bolt → SPEC → V-Bounce path.

The constraint is not specific to this repository. Every project that took the
methodology's invitation is exposed, which is why the fix lands in the
distributable and not in local tooling.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-000.BOLT-001` — [document](../functional/bolts/US-000.BOLT-001-agents-md-project-section.md) | `HITL-BOLT-READY-Approval` ✓ 2026-08-17T21:09:30-03:00, eugenio.serrano (architect) |
| Parent US | `US-000` — [container](../functional/user-stories/US-000-non-functional.md) | `status: active` — permanent container, no approval lifecycle (§3.2) |
| ADR | `ADR-001` — [document](../adrs/ADR-001-repository-layout-methodology-and-product.md) | `HITL-ADR-Approval` ✓ 2026-08-17T21:03:18-03:00, eugenio.serrano (architect) |
| DISC/REV/AREV | none | — |
| Repository baseline | `67a62ed` on branch `4.2`, plus the uncommitted working tree of the 4.2 reorganization | — |

**Pre-SPEC evidence gate (§2.4.1, G13):** every governed source above is
approved or is a container with no approval lifecycle. No `open` or
`in-validation` `OQ-NNN` exists in `analysis/open-questions/` (G35). No two
active ADRs conflict — ADR-001 is the only one. The gate passes.

---

## 4. Scope

### In scope

- The boundary marker in the `AGENTS.md` the distribution ships, and the
  relocation of the framework text that currently sits on the wrong side of the
  existing divider.
- The normative merge rule in §5.16 of the methodology, plus the §5.2 statement
  that makes the file's dual ownership explicit.
- The extension of blocking rule **G36** so that destroying the project section
  during a migration is a violation rather than an accident.
- The four platform agent definitions: the migration-protocol rule (shared
  body, verbatim) and the memory/project-instructions wording (platform
  preamble, per-tool).
- This repository's root `AGENTS.md`, restructured so that everything above the
  marker is byte-identical to the kit's and everything repo-specific sits
  below.
- **(rev 2)** The install step of the migration itself: `AGENTS.md` is excluded
  from the copy that installs the new version, so the file is never destroyed
  and reading from the last commit becomes the fallback rather than the
  mechanism.
- **(rev 2)** The precondition that the working tree is committed before a
  migration runs, stated in the normative text instead of assumed by it.

### Out of scope

- Running the actual release migration of this repository.
- Any version bump — the kit stays at 4.2.
- The removal of `CHANGELOG.md` from the distributable, already delivered.
- Committing an automated checker for the invariant; `tools/` is untouched.
  The verification in §8 is executed as commands and its output recorded in the
  MEM.

---

## 5. Prerequisites and baseline

- Branch `4.2`, baseline commit `67a62ed` plus the uncommitted 4.2
  reorganization already present in the working tree.
- The four agent definitions are **verified in sync before any edit**: their
  shared methodology bodies differ by exactly 2 lines each (the sanctioned
  `devflow/agents-data/<agent>/` path). Confirmed at 2026-08-17T21:10:20-03:00.
  Re-confirm before Phase D; a pre-existing mismatch is itself a defect and a
  stop condition.
- No prior SPEC. This is the repository's first.

---

## 6. Phases

### Phase A — Give the shipped `AGENTS.md` a machine-readable boundary

**Duration:** ~0.3h total cycle — **Complexity:** Low

#### A.1 Move the framework closing text above the boundary

`distribution-kit/AGENTS.md` currently ends with a `---` divider, the sentence
*"Project-specific conventions can be added below this line."*, and then a
framework paragraph about not appending personal preferences and routing
durable agent knowledge to `devflow/agents-data/<agent-name>/`.

That last paragraph is **framework advice given to every adopting project**. If
the boundary is placed where the divider is today, that paragraph lands on the
project side and freezes in every adopter, never updated by any future release.
Move it above the boundary, immediately after the *"Human checkpoints are not
yours to skip"* section, so it stays framework-owned.

#### A.2 Replace the prose divider with an explicit marker

The boundary is the **last line** of the shipped file, expressed as an HTML
comment so it is invisible when rendered, unambiguous to parse, and stable
across versions. The human-facing explanation goes **above** it, on the
framework side:

```
<!-- Everything below the marker that closes this file belongs to the project.
     A migration replaces only what is above it; your section survives byte for
     byte. Add your project's own conventions there. -->
<!-- AVENGA-DEVFLOW:PROJECT-SECTION -->
```

**(rev 2 — corrects revision 1.)** Revision 1 put the explanation *below* the
token, which stranded 244 bytes of framework text on the project side: a future
release improving that wording would never reach a project already carrying the
marker. That is the same defect this Bolt exists to fix, at smaller scale. The
split point is now the token line and nothing else, so everything the framework
owns — the explanation included — updates on every upgrade. The merge still
matches the token as a prefix, so the token line's own trailing text may vary
without breaking existing projects.

#### A.3 A hard handoff into the project section

**(rev 2 — strengthened.)** Revision 1 ended the framework block with a note
that the project section is binding. That is too soft for the case this
repository itself represents: an agent reading top-down meets ~55 lines of
unqualified framework text — including a bare *"Source of truth:
`devflow/…`"* — before learning that this repository has two trees and that the
root one is not the thing to edit. The wrong model gets planted first and
corrected later.

The framework block therefore ends with an **instruction, not a courtesy**: the
project section may add constraints specific to this repository and may qualify
anything above it, the source-of-truth line included, and it is not optional
reading. The text stays generic — every adopter benefits from the same
statement — so it belongs above the marker.

**Files modified:**
- `distribution-kit/AGENTS.md` — boundary marker added at the end; framework
  closing paragraph relocated above it; pointer line added.

---

### Phase B — State the merge rule normatively

**Duration:** ~0.5h total cycle — **Complexity:** Medium

#### B.1 §5.16 — the migration rule

§5.16 already carries the shape this rule needs: the `LANGUAGE` exception,
which explains that a file ships with the framework but is configured by the
project and therefore keeps its old value. Add the `AGENTS.md` rule as its
sibling, stating that:

- the root `AGENTS.md` is **merged, never replaced**: everything above the
  project marker comes from the new version, everything from the marker
  onward is preserved byte for byte;
- the merge is part of the migration, not an optional cleanup step;
- the invariant is checkable — after the merge, the text above the marker is
  byte-identical to the new version's `AGENTS.md` above its own marker, and a
  diff of the file must show no change below it;
- a file whose marker is absent stops the migration and is reported, rather
  than being resolved by judgement (consistent with §5.16's *stop and ask,
  never guess*).

#### B.2 §5.16 — extend the reconciliation to the root files

The reconciliation walk gives every file of `devflowOLD/` exactly one
disposition, which structurally cannot see the root `AGENTS.md`. Add the
explicit statement that the migration also touches files outside `devflow/`,
and enumerate their dispositions: agent definitions overwritten from the new
version, `AGENTS.md` merged at the marker.

#### B.3 §5.2 — record the file's dual ownership

§5.2 describes what a project installs and treats `AGENTS.md` as a single
framework artifact. Add that the file has two parts with different owners, and
that the boundary between them is the marker.

#### B.4 The install step never destroys the file, and the precondition is stated **(rev 2)**

Revision 1 protected the project section by *recovering* it from the last commit
after the copy had already destroyed it. That works — the rehearsal proved it —
but it rests the entire guarantee on the human having committed at exactly the
right moment, and a guarantee that depends on human timing is a mitigation, not
a fix.

§5.16 therefore prescribes that the install step **excludes `AGENTS.md` from the
copy**. The file is never destroyed, the new framework block is merged into it
in place, and reading from the last commit is demoted to the **fallback** for a
file that was already clobbered by a blunt copy. Both paths stay documented,
because a project that does copy everything must still be able to recover.

§5.16 also gains the precondition it never stated: **the working tree is
committed before a migration runs.** Revision 1 depended on that commit existing
while never requiring it — a search of the normative text for the requirement
returns nothing. Stating it is what makes the fallback path trustworthy.

**Files modified:**
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` — §5.2 dual
  ownership; §5.16 merge rule beside the `LANGUAGE` exception; §5.16
  reconciliation extended to the root files; **(rev 2)** the install-step
  exclusion and the committed-tree precondition.

---

### Phase C — Project the rule into the blocking rules

**Duration:** ~0.2h total cycle — **Complexity:** Low

**G36** already blocks a migration from rewriting what the repository recorded
— approved MEMs and ADRs, recorded HITL decisions, `CHANGELOG.md` history — and
its rationale is that *"a version migration moves documentation and manifests
forward, never history"*. Destroying the project section of `AGENTS.md` is the
same failure with the same shape, so it extends G36's predicate rather than
claiming a fortieth rule number. Extending an existing row also avoids adding a
row to four agent files, since the row is already inline in all of them.

Both the predicate and the ❌ response text are updated so the agent knows what
to do instead of only what not to do: merge at the marker.

**Files modified:**
- `distribution-kit/devflow/GUARDRAILS.md` — G36 predicate and response.

---

### Phase D — Propagate to the four platform agent definitions

**Duration:** ~0.5h total cycle — **Complexity:** Medium

This phase touches two zones with different rules, and conflating them is the
main risk of the whole SPEC.

#### D.1 Shared methodology body — verbatim in all four

Inside *Methodology Upgrade Protocol*, next to the `LANGUAGE` and
`CHANGELOG.md` bullets, add the `AGENTS.md` merge bullet. Update the **G36 row**
so it matches the new GUARDRAILS predicate. Both edits are byte-identical
across the four files, applied in the same pass, and verified by the four-way
body diff — not by grepping the lines that were touched.

#### D.2 Platform preamble — equivalent, not identical

Each definition's `# Memory` section currently tells the reader that project
instructions live in the platform definition itself — in the Claude file, *"**
Project instructions (shared, versioned):** this file (`CLAUDE.md` at the
repository root)"*. That is the same defect one level down: it directs
project-authored content into a file the upgrade overwrites wholesale.

The preamble is the **exempt zone** (parity matrix): the four legitimately word
this differently per platform, so this edit is **not** byte-identical and must
not be verified with the body diff. Each file states, in its own vocabulary,
that project instructions belong in the project section of the root `AGENTS.md`,
below the marker, and that the platform definition is framework the upgrade
replaces.

The parity matrix row for **Memory** is updated to record the new equivalence.

**Files modified:**
- `distribution-kit/CLAUDE.md`
- `distribution-kit/.agents/skills/avenga-devflow/SKILL.md`
- `distribution-kit/.github/agents/AvengaDevFlow.agent.md`
- `distribution-kit/.opencode/agents/AvengaDevFlow.md`
- `AGENTS.md` (root) — parity matrix, Memory row (also restructured in Phase E)

---

### Phase E — Bring this repository's `AGENTS.md` into the required shape

**Duration:** ~0.4h total cycle — **Complexity:** Low

The root `AGENTS.md` is 251 lines and entirely repository-specific, including a
customized version of what should be the generic framework block. Under the new
rule its structure becomes:

1. **Above the marker:** the framework block, byte-identical to
   `distribution-kit/AGENTS.md` above its own marker. Not paraphrased, not
   improved — identical, because that is the invariant the merge and its check
   depend on.
2. **The marker.**
3. **Below the marker:** everything this repository authored — the two-tree
   box, Part 1's repository-specific qualifications, *what counts as a code
   change here*, the release loop, the four-agent synchronization procedure,
   the preamble parity matrix and the version bump procedure.

Content that today sits in the framework zone as a customization (the source of
truth naming the installed release, the note that the root `CLAUDE.md` and
`.opencode/` are installed copies) moves below the marker, restated there.

**(rev 2)** The project section opens with a **compaction-proof paragraph** —
three or four lines, before any heading, carrying only what must never be lost:
that the product edited here is `distribution-kit/`, `tools/` and `prompts/`,
and that the root `devflow/` is the installed rulebook and is not edited. It
exists because position is fixed — nothing repository-specific may sit above the
marker without being eaten by the next upgrade — so salience is the only lever
left, and this is the text that has to survive a compacted context.

The release-loop text is corrected in the same pass: it currently says *"install
the kit (`cp -a distribution-kit/. .`)"*, which is precisely the blind copy this
Bolt exists to prevent. It becomes the explicit sequence, with the merge as its
own step.

**Files modified:**
- `AGENTS.md` (root) — restructured around the marker.

---

## 7. Acceptance criteria

### AC-1: The shipped file carries a parseable boundary

**Given** `distribution-kit/AGENTS.md`
**When** a migration tool or agent searches for the token `AVENGA-DEVFLOW:PROJECT-SECTION`
**Then** it matches exactly once, and everything after that match is the
project's section.

### AC-2: No framework text is stranded on the project side

**(rev 2 — generalized.)** Revision 1 verified this against one specific
paragraph and therefore missed the marker's own explanatory comment.

**Given** the shipped `AGENTS.md`
**When** every line from the marker token to end of file is inspected
**Then** none of them is framework text: the token line is the **last line of
the file**, so the distributed project section is empty by construction and no
future release can find its own text frozen on the project side.

### AC-3: The merge rule is normative

**Given** `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`
**When** §5.16 is read
**Then** it states that the root `AGENTS.md` is merged at the marker rather
than replaced, that the project side is preserved byte for byte, that the
migration also disposes of the files outside `devflow/`, and that a missing
marker stops the migration.

### AC-4: The rule is enforceable

**Given** `distribution-kit/devflow/GUARDRAILS.md`
**When** G36 is read
**Then** its predicate covers destroying the project section of the root
`AGENTS.md` during a migration, and its response names the merge as the correct
action.

### AC-5: The four agents stay in sync

**Given** the four platform agent definitions after Phase D
**When** their shared methodology bodies are diffed pairwise against the Claude
one
**Then** each differs by exactly 2 lines — the sanctioned
`devflow/agents-data/<agent>/` path — and each contains all 39 `G` rows.

### AC-6: No agent directs project content into an overwritten file

**Given** the four platform agent definitions
**When** their memory/project-instruction wording is read
**Then** none of them names the platform definition itself as the place for
project instructions; each points at the project section of the root
`AGENTS.md`.

### AC-7: This repository conforms to its own rule

**Given** the root `AGENTS.md` and `distribution-kit/AGENTS.md`
**When** the text above the marker is extracted from each and compared
**Then** the two are byte-identical.

### AC-8: A migration preserves the project section

**Given** a committed working tree and the kit installed over the repository
root as the release loop prescribes
**When** the merge step runs and `git diff AGENTS.md` is inspected
**Then** the diff contains changes only above the marker, and the bytes from
the marker onward are unchanged.

### AC-9: The install step does not destroy the file **(rev 2)**

**Given** the migration procedure as §5.16 prescribes it
**When** the new version is installed over a project root
**Then** `AGENTS.md` is excluded from that copy, the merge happens in place, and
the recovery-from-commit path is documented as the fallback for a file already
clobbered rather than as the mechanism.

### AC-10: The precondition is normative **(rev 2)**

**Given** the methodology text
**When** §5.16 is searched for the requirement that the tree be committed before
a migration
**Then** it is stated — where revision 1 returned zero occurrences — and the
consequence of ignoring it is named.

### AC mapping to measurable outcome (non-functional)

| Outcome (Bolt §2) | How this SPEC satisfies it | Verifying evidence |
|---|---|---|
| Project-authored part survives an upgrade byte for byte | Phase A boundary + Phase B rule + Phase C enforcement | AC-1, AC-3, AC-4, AC-8 |
| Boundary identifiable without human judgement | Phase A.2 machine-readable token matched as a prefix | AC-1 |
| Four agent definitions stay byte-identical in the shared body | Phase D.1 single synchronized pass, verified by whole-body diff | AC-5 |
| No agent directs project content into an overwritten file | Phase D.2, applied per platform in the exempt zone | AC-6 |
| No remaining statement contradicts the new rule | Phase E + repository-wide sweep | AC-2, AC-7 |

---

## 8. Testing strategy

This repository has no runtime; there is nothing to unit-test. Per the Bolt's
completion evidence, verification is a set of **deterministic, re-runnable
commands** whose output is recorded verbatim in the MEM. Committing them as a
checker is out of scope (§4).

- **Boundary checks (AC-1, AC-2):** count occurrences of the marker token in
  the shipped file (expect 1); assert the `agents-data/` personal-memory
  paragraph appears at a line number lower than the marker's.
- **Normative checks (AC-3, AC-4):** grep §5.16 and G36 for the new clauses;
  resolve every `§` reference and rule ID cited by the new text against the
  file on disk, so no citation is invented.
- **Four-agent sync (AC-5):** for each definition, slice from the
  `# Avenga DevFlow v<version> (Methodology)` heading to end of file, normalize
  CRLF, and diff against the Claude slice — expect exactly 2 differing lines
  each. Independently, count `^| G[0-9]{2} |` rows in each definition and in
  `GUARDRAILS.md` — expect N/N four times.
- **Preamble check (AC-6):** grep each definition for the old
  project-instructions phrasing (expect 0) and for the new one (expect 1 per
  file, wording differing per platform by design).
- **Conformance check (AC-7):** extract the text above the marker from the root
  `AGENTS.md` and from the kit's, and compare byte for byte after CRLF
  normalization.
- **Migration rehearsal (AC-8):** the decisive test. On a scratch copy of the
  repository, with a clean tree: copy the kit's `AGENTS.md` over the root one,
  run the merge as §5.16 now prescribes, then `git diff AGENTS.md` and assert
  every hunk lies above the marker. Run it **twice**, the second time on the
  output of the first, to prove idempotence — a merge that drifts on repeat
  application would corrupt the file over successive releases.
- **Edge cases:** marker absent from the incoming file; marker absent from the
  existing file; marker present more than once; a project section that is empty;
  CRLF versus LF on either side.
- **BUG evidence:** n/a — this is not a BUG Bolt.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — no executable code in scope; the §8 verification commands are the evidence |
| SAST / SBOM | — | `n/a` — no code and no dependencies are added or changed |
| Perf-smoke (p95/p99) | — | `n/a` — documentation change, no runtime path |
| Prompt-injection scan | no untrusted content embedded in agent definitions | `pass` expected — all added text is authored here; no external content is inlined |
| Secret-leak scan | zero findings in the diff | `pass` expected |
| Hallucination lint | every `§` reference and rule ID cited by new text resolves on disk | `pass` expected — checked in §8 |
| IP / license provenance | — | `n/a` — no third-party material introduced |
| PII / DLP | — | `n/a` — `data_classification: internal`, no personal data involved |
| Dependency-confusion | — | `n/a` — no package resolution involved |
| Test-first evidence | — | `n/a` — not a BUG Bolt; no red/green sequence is prescribed (§3.3.1) |
| Behavioral reproducibility | verification commands produce identical output on re-run | `pass` expected — the rehearsal is run twice for idempotence |
| Bolt-manifest validation | validates against `manifest-v4-bolt.schema.json` | `pass` expected |

---

## 10. Security and data

- No credentials, tokens or endpoints are touched. The change is Markdown in
  the distributable plus this repository's own `AGENTS.md`.
- The relevant security property is **integrity of governance content**: the
  defect being fixed destroys human-authored rules silently. The marker plus
  G36 turn a silent loss into a blocked action.
- `data_classification: internal`, mirroring the Bolt. No personal data is
  read, written or transmitted; the PII/DLP gate is `n/a` on that basis.
- The merge described in §5.16 reads the previous file's content from committed
  git history rather than trusting the working tree, so an already-clobbered
  working copy cannot silently become the new project section.

---

## 11. Monitoring and observability

Not applicable in the runtime sense — there is no service. The equivalent
observability is the checkable invariant: the byte-identity of the framework
block between the root `AGENTS.md` and the kit's is a signal that either
someone customized where they must not, or the kit moved and the merge is
pending. It is recorded here so the next release can act on it and so the
future `tools/` checker (out of scope) has a defined predicate to implement.

---

## 12. Migration, compatibility and rollback

- **Migration:** none for existing adopters in this Bolt. Projects on an
  earlier version receive the marker when they upgrade; their first upgrade
  onto a marker-bearing version cannot merge on a marker their old file lacks,
  so §5.16 must state that a missing marker stops the migration and the human
  decides where the boundary lies. That statement is part of Phase B.2 and is
  what makes this change safe for repositories that predate it.
- **Compatibility:** the marker is an HTML comment, invisible in rendered
  Markdown and inert for every tool that reads `AGENTS.md` as instructions.
  Existing files without it are unaffected until they upgrade.
- **(rev 2) Precondition:** the migration requires a committed working tree. This is now normative rather than assumed, because the fallback path reads from the last commit and a project with uncommitted work has nothing there to read.
- **Rollback:** revert the working-tree changes. Nothing is committed by the
  agent (G34) and no state outside the repository is touched, so rollback is
  `git checkout` of the affected paths.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| A shared-body edit lands in fewer than four agent definitions | 3 | 4 | The whole-body four-way diff is mandatory evidence (AC-5), not a grep of the touched lines |
| Phase D.2 is treated as shared content and forced byte-identical, breaking the platform preamble | 3 | 3 | The SPEC separates D.1 and D.2 explicitly; D.2 is verified by the parity matrix, never by the body diff |
| The marker is placed so framework text lands on the project side, freezing it in every adopter | 2 | 5 | AC-2 asserts the personal-memory paragraph is above the marker; the rehearsal must show the framework block actually updating |
| The merge is not idempotent and corrupts the file across releases | 2 | 5 | The rehearsal is run twice, the second time on the first run's output (§8) |
| Projects predating the marker cannot merge on upgrade | 3 | 3 | §5.16 states a missing marker stops the migration and the human places the boundary (Phase B.2) |
| **(rev 2)** Two documented paths — exclude-from-copy and recover-from-commit — read as two competing procedures | 2 | 3 | §5.16 names one as the prescribed step and the other explicitly as the fallback for an already-clobbered file; Phase B.4 states the hierarchy in the same paragraph |
| G36's predicate grows broad enough to become unclear | 2 | 2 | The predicate names the artifact explicitly; the response text names the corrective action |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Extend **G36** instead of adding G40 | Same failure mode — a migration destroying what the repository authored — and the row is already inline in all four agents, so no fortieth row has to be propagated. A new number would also renumber nothing but would add a rule where an existing one already carries the rationale |
| HTML comment as the marker | Invisible in rendered Markdown, inert for every tool that consumes `AGENTS.md` as instructions, trivially greppable, and stable across versions |
| Match the token as a **prefix**, not the whole comment | Lets future versions reword the human-facing explanation without breaking every existing project's merge |
| Marker at the **end** of the shipped file, with its explanation **above** the token | The distributed project section is empty by construction, so nothing the framework owns can freeze on the project side. Revision 1 placed the explanation below the token and stranded 244 bytes — corrected in rev 2 |
| **(rev 2)** git is the **fallback**, not the mechanism: the install step excludes `AGENTS.md` so the file is never destroyed | Revision 1 rested the whole guarantee on the human having committed at the right moment. Excluding the file from the copy removes the failure mode instead of mitigating it; the git path stays documented for a project that copies everything anyway |
| Restate repo-specific qualifications below the marker rather than customizing the framework block | AC-7's byte-identity is what makes the invariant checkable; a customized framework block would make every future merge a judgement call |
| No committed checker in `tools/` | Explicitly excluded by the Bolt; the invariant is defined here so the tooling track can implement it later without re-deciding |

---

## 15. Stop conditions

- The four agent definitions are **not** in sync when Phase D begins — that
  mismatch is itself a defect and must be reconciled under its own governance
  before this Bolt continues.
- Placing the marker requires deciding the ownership of text whose side is
  genuinely ambiguous — stop and ask rather than guessing (§2.4.1).
- ADR-001 changes materially while this SPEC is open — G15: stop, revise the
  SPEC, re-approve.
- The migration rehearsal (AC-8) cannot be performed without committing, or
  cannot be made idempotent — record the blocker in the MEM and pause.
- The turn budget is exhausted without the verification passing — MEM with the
  blocker first, then stop and ask (§3.0).

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented
- [ ] All acceptance criteria pass (AC-1 … AC-8)
- [ ] Verification commands of §8 run and their output recorded verbatim in the MEM
- [ ] Migration rehearsal run **twice**, idempotence demonstrated
- [ ] Change follows ADR-001 (rules 6 and 7)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — two-tree layout; rule 6 (files installed outside `devflow/`), rule 7 (repository zone partition)
- [US-000.BOLT-001](../functional/bolts/US-000.BOLT-001-agents-md-project-section.md) — the approved Bolt this SPEC implements
- [US-000](../functional/user-stories/US-000-non-functional.md) — non-functional container
- `devflow/avenga-devflow/Avenga-DevFlow.md` §5.2, §5.16 — the sections the product change modifies, read here in their installed 4.1 form
- `devflow/GUARDRAILS.md` G36, G07, G34 — enforcement context
- `AGENTS.md` (root) — four-agent synchronization procedure and preamble parity matrix, the verification this SPEC reuses

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-17 | eugenio.serrano | Revision 1 — initial canonical SPEC for US-000.BOLT-001 |
| 2026-08-18 | eugenio.serrano | Revision 2 — material revision after `changes_requested` on MEM-260817-2123 (5 findings). Marker explanation moved above the token so no framework text is stranded (F1); the handoff into the project section becomes an instruction (F2); a compaction-proof paragraph opens the project section (F3); the install step excludes `AGENTS.md`, demoting git to fallback (F4 — material, this is what forced the revision under G15); the committed-tree precondition becomes normative (F5). AC-2 generalized; AC-9 and AC-10 added |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `HITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`HITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> V-Bounce. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved (revision 2) |
| **review_ready_at** | `2026-08-18T10:38:44-03:00` |
| **review.started_at** | `2026-08-18T10:38:44-03:00` |
| **review.decided_at** | `2026-08-18T10:50:35-03:00` |
| **Findings** | none — `acknowledged_without_comment: true`; reason in the frontmatter `review:` block |
