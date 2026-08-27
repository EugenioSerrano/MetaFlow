---
id: "MEM-260817-2123"
title: "The project section of the root AGENTS.md now survives every methodology upgrade"
date: "2026-08-17"
author: "eugenio.serrano"
llm: "claude-opus-5[1m]"
bolt: "US-000.BOLT-001"
spec: "SPEC-260817-2110"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "67a62ed"
applied_adrs:
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
manifest: "US-000.BOLT-001-agents-md-project-section.json"
diff_ref: ""
review_ready_at: "2026-08-17T21:23:10-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "changes_requested"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-17T21:23:10-03:00"
  decided_at: "2026-08-18T10:38:00-03:00"
  findings:
    - "1) The 244-byte marker block sits on the project side, so its framework explanation freezes in every adopting project and no future release can update it - the same defect class the Bolt set out to fix, reintroduced at smaller scale; AC-2 was verified against one specific paragraph instead of the general property. 2) The generic handoff into the project section is too soft: an agent reading top-down meets 55 lines of unqualified framework text, including an unqualified 'source of truth' line, before learning this repository has two trees. 3) No compaction-proof paragraph at the head of the project section. 4) DESIGN: the merge depends on the human having committed; excluding AGENTS.md from the install copy removes the failure mode instead of mitigating it, with git as fallback rather than mechanism. 5) The methodology never states the precondition that the tree must be committed before a migration - zero occurrences in the normative text; it lives only in this repository's own project section."
  acknowledged_without_comment: false
  acknowledgment_reason: ""
---

# MEM-260817-2123 — The project section of the root AGENTS.md now survives every methodology upgrade

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-001](../functional/bolts/US-000.BOLT-001-agents-md-project-section.md) |
| **SPEC**        | [SPEC-260817-2110](../spec/SPEC-260817-2110-agents-md-project-section.md), revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 6 and 7 |

---

## 1. Executive summary

This V-Bounce closed a defect that had been shipping in every release of Avenga
DevFlow: the distributed `AGENTS.md` invites each adopting project to write its
own conventions below a prose divider, and §5.16 — which governs the migration
of `devflow/` in exhaustive detail — said nothing about that file, so an upgrade
destroyed the project's content silently and irrecoverably from the working
tree. The fix gives the shipped file a machine-readable
`AVENGA-DEVFLOW:PROJECT-SECTION` marker, states the merge rule normatively in
§5.16 as a sibling of the existing `LANGUAGE` exception, extends blocking rule
**G36** so that overwriting the project section is a violation rather than an
accident, propagates both to the four platform agent definitions, and stops
those definitions from directing project-authored content into files an upgrade
overwrites whole. This repository's own `AGENTS.md` was then rebuilt around the
marker, with its framework block now a byte-identical copy of the kit's, so the
repository conforms to the rule it publishes.

All eight acceptance criteria pass. The decisive evidence is the migration
rehearsal: on a scratch git repository, a blind `cp -a` of the next version's
`AGENTS.md` **did** destroy the project section — confirming the defect is real
and not theoretical — and the prescribed merge then restored it byte-identically
from the last commit while the framework block correctly advanced to the new
version. Running the merge a second time on its own output produced an identical
file, proving idempotence, so the operation cannot drift across successive
releases. Five boundary cases were exercised and each behaved as the SPEC
prescribes: a missing marker on either side, a duplicated marker, an empty
project section and a CRLF-encoded input.

One deviation from the SPEC surfaced during execution and is recorded in §8: the
SPEC assumed all four agent definitions carried the misdirected
project-instructions pointer, but only the Claude one did — the other three
already pointed at `AGENTS.md` and needed only the marker precision added.

---

## 2. Implemented phases

### Phase A — A machine-readable boundary in the shipped `AGENTS.md`

The file previously ended with a `---` divider, the sentence *"Project-specific
conventions can be added below this line."*, and then a framework paragraph
about personal memory and `devflow/agents-data/<agent-name>/`. That last
paragraph is advice the framework gives every adopter, and it sat **on the
project side** of the divider — meaning that the moment the divider became a
real boundary, that advice would have frozen in every adopting project and never
been updated again. It was relocated above the boundary.

The divider was replaced by a two-part HTML comment: a first line carrying the
parseable token `AVENGA-DEVFLOW:PROJECT-SECTION`, and a second explaining the
contract to a human reader. The merge matches the token as a **prefix**, so a
future release can reword the human-facing explanation without breaking the
split for projects already carrying it. A pointer line was added at the end of
the framework block so a reader who stops there still learns that binding
project rules follow.

### Phase B — The merge rule, stated normatively

§5.16 gained the rule as a sibling of the `LANGUAGE` exception, the existing
precedent for a file that ships with the framework but is owned by the project.
It states that the root `AGENTS.md` is merged rather than replaced; that the
previous content is read **from the last commit rather than the working tree**,
which is what keeps the operation correct even after the new file has already
been copied over it; that the result is checkable (framework block identical to
the new version's, nothing changed from the marker onward); and that a missing
or duplicated marker **stops** the migration for a human to place the boundary,
instead of being resolved by inference.

The reconciliation walk was extended. It gives every file of `devflowOLD/`
exactly one disposition and therefore structurally cannot see the root files, so
a second table now records what happens to them: agent definitions overwritten,
`AGENTS.md` merged. §5.2 was updated to record the file's dual ownership at the
point where a reader first learns what a project installs.

### Phase C — Enforcement

**G36** already blocks a migration from rewriting what the repository recorded —
approved MEMs and ADRs, HITL decisions, changelog history — on the rationale
that a migration moves documentation forward but never history. Destroying the
project section is the same failure with the same shape, so it extends that
predicate rather than claiming a fortieth rule number. The response text was
extended too, so the agent reads what to do instead of only what not to do. The
rule count stays at 39, which matters because each agent carries every row
inline.

### Phase D — The four platform agent definitions

Two zones with different rules, and conflating them was the main identified
risk. **D.1** (shared methodology body) added the merge bullet next to the
`LANGUAGE` and `CHANGELOG.md` bullets and updated the G36 row — byte-identical
in all four, applied in a single pass, verified by the whole-body diff rather
than by grepping the touched lines. **D.2** (platform preamble, the exempt zone)
was applied per tool in each one's own vocabulary and deliberately **not** made
identical; it is verified against the parity matrix instead. The matrix's
*Memory* row was updated to record the new equivalence.

### Phase E — This repository's `AGENTS.md`

Rebuilt by composition rather than by editing: the kit's file verbatim, then the
project section. That construction makes AC-7's byte-identity true by
construction instead of by care. Everything repository-specific moved below the
marker, including the qualifications that previously customized the framework
block. The release loop was corrected in the same pass — it read *"install the
kit (`cp -a distribution-kit/. .`)"*, which is precisely the blind copy this
Bolt exists to prevent, and is now the explicit six-step sequence with the merge
as its own step.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/spec/SPEC-260817-2110-agents-md-project-section.md` | Canonical SPEC of this Bolt: the implementation plan, its eight acceptance criteria and the verification that replaces a test suite in a repository with no runtime |
| `devflow/memory/MEM-260817-2123-agents-md-project-section.md` | This implementation memory — the V-Bounce record presented at `HITL-MEM-Approval` |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/AGENTS.md` | Framework closing paragraph relocated above the boundary; prose divider replaced by the `AVENGA-DEVFLOW:PROJECT-SECTION` marker; pointer line added so the reader is sent to the project section |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §5.2 dual ownership of `AGENTS.md`; §5.16 merge rule beside the `LANGUAGE` exception, with the read-from-commit rule, the checkable result and the two boundary cases; §5.16 reconciliation table for the files outside `devflow/` |
| `distribution-kit/devflow/GUARDRAILS.md` | G36 predicate and response extended to cover overwriting the project section instead of merging at the marker |
| `distribution-kit/CLAUDE.md` | D.1 merge bullet + G36 row (shared body); D.2 project-instructions pointer corrected — it named itself as the place for project instructions |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | D.1 merge bullet + G36 row; D.2 marker precision added to the existing `AGENTS.md` pointer |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | D.1 merge bullet + G36 row; D.2 marker precision, in this file's own wording |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | D.1 merge bullet + G36 row; D.2 marker precision added to the existing `AGENTS.md` pointer |
| `AGENTS.md` (root) | Rebuilt around the marker: framework block byte-identical to the kit's, project section carrying the two-tree map, the corrected release loop, the four-agent procedure, the parity matrix and the version bump procedure |
| `devflow/metrics/bolts/US-000.BOLT-001-agents-md-project-section.json` | `spec_revisions[]`, `hitl_approvals[]` for the Bolt and SPEC checkpoints, review timestamps, and this V-Bounce entry |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | None |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| — | None |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Extend **G36** instead of adding a G40 | Same failure mode — a migration destroying what the repository authored — and the row is already inline in all four agents, so no fortieth row has to be propagated to four files |
| HTML comment as the marker | Invisible in rendered Markdown, inert for every tool that consumes `AGENTS.md` as instructions, trivially greppable, stable across versions |
| Match the token as a **prefix** of the comment | Lets a future release reword the human-facing explanation beside it without breaking the merge for projects already carrying the marker |
| Marker at the very **end** of the shipped file | The distributed file has an empty project section by definition, so anything the framework wants to say must sit above it |
| Read the previous content from the **last commit**, not the working tree | Keeps the merge correct after a blind `cp -a` has already overwritten the file — which is the ergonomics the release loop actually wants to preserve |
| Build the root `AGENTS.md` by **composition** rather than by editing | Concatenating the kit's file with the project section makes AC-7's byte-identity true by construction; editing would have made every future merge a judgement call |
| Relocate the personal-memory paragraph above the boundary | It is framework advice; left below the marker it would freeze in every adopting project and never be updated by any future release |
| Missing or duplicated marker **stops** the migration | Consistent with §5.16's existing *stop and ask, never guess*; the framework/project boundary is not inferable from content |
| Verification kept as commands recorded here, not a committed checker | `tools/` is explicitly excluded by the Bolt; the invariant is defined in the SPEC so the tooling track can implement it later without re-deciding |

---

## 8. Deviations and assumptions

**Deviation — the D.2 defect was narrower than the SPEC assumed.** SPEC Phase
D.2 states that each definition's `# Memory` section *"currently tells the reader
that project instructions live in the platform definition itself"*. On
inspection only `distribution-kit/CLAUDE.md` did, with *"Project instructions
(shared, versioned): this file (`CLAUDE.md` at the repository root)"*. The other
three already pointed at the repository's `AGENTS.md` and were correct as far as
they went; they received only the added precision that project instructions
belong specifically **below** the marker. AC-6 is satisfied in full — no
definition now names itself as the place for project instructions — so the
outcome is unchanged and this is a narrowing of the work, not a material source
change requiring re-approval under G15.

**Assumption — `README.md`'s adoption command was left as is.** The root
`README.md` still tells a new adopter to run `cp -a distribution-kit/. <your-repo>/`.
That is correct for a **fresh install**, where no project `AGENTS.md` exists to
preserve; it is only the *upgrade* path that requires the merge, and that path is
documented in §5.16 and in this repository's release loop. Verified deliberately
rather than left unnoticed.

**Execution note.** Several large document writes could not be performed through
shell heredocs — the shell's parser failed on documents of that size — so the
SPEC, the Bolt, the MEM and the project section of `AGENTS.md` were written with
the direct file-write tool instead. No content was affected; it is recorded here
because it changed how the work was carried out, not what was produced.

**No unresolved risks** carried out of this V-Bounce.

---

## 9. Verification evidence

### Build

```
n/a — this repository has no runtime and no build. Per the Bolt's completion
evidence and SPEC §8, verification is the deterministic command set below.
```

### Tests

```
AC-1  marker token count in distribution-kit/AGENTS.md ................. 1        PASS
AC-2  agents-data framework paragraph at L49, marker at L57 ............ above    PASS
      lines after the marker in the shipped file ....................... 3 (comment block, empty project section)
AC-3  §5.16 "root AGENTS.md is merged, never replaced" ................. 1        PASS
      §5.16 "stops and reports it" (missing-marker case) ............... 1        PASS
      §5.16 marker "matched as a **prefix**" ........................... 1        PASS
      §5.16 "The files outside devflow/ are reconciled too" ............ 1        PASS
      §5.2  "Two owners, one file" .................................... 1        PASS
AC-4  GUARDRAILS G36 covers overwriting the project section ............ 1        PASS
      total G rules (unchanged) ....................................... 39       PASS
AC-5  shared-body diff vs claude:  codex 2 | ghcopilot 2 | opencode 2 lines      PASS
      G-rule count inline:  39/39 | 39/39 | 39/39 | 39/39                        PASS
AC-6  old Claude phrasing "this file (CLAUDE.md...)" .................. 0        PASS
      marker cited in each of the four definitions .................... 2 each   PASS
AC-7  framework block root vs kit ...................... identical, 2812 bytes    PASS
```

### Migration rehearsal (AC-8) — scratch git repository, run twice

```
baseline committed: e510359 (AGENTS.md with marker + project section)

after the blind `cp -a` of the next version's file:
   project section present? .................... NO — CLOBBERED   (defect confirmed)

pass 1 — merge, previous content read from HEAD:
   project section byte-identical to the commit ....... YES        PASS
   framework block equals the new version's ........... YES        PASS
   git diff --stat .................. AGENTS.md | 88 +++++-----    (all above the marker)

pass 2 — merge re-applied to its own output:
   result IDENTICAL to pass 1 ......................... YES        PASS (idempotent)

AC-8: PASS
```

### Boundary cases

```
existing file with no marker (project predating the rule) .. STOP: existing file has 0 markers
existing file with a duplicated marker ..................... STOP: existing file has 2 markers
incoming file with no marker ............................... STOP: incoming file has 0 markers
empty project section ...................................... OK — valid merge, framework only
existing file in CRLF ...................................... OK — normalized before the split
```

Each behaves exactly as SPEC §8 and the new §5.16 text prescribe. The scratch
repository was deleted after the run (W21 — temporary data is never committed).

### Gates

| Gate | Result |
|------|--------|
| Unit / integration | `n/a` — no executable code in scope; the command set above is the evidence |
| SAST / SBOM | `n/a` — no code and no dependencies added or changed |
| Perf-smoke (p95/p99) | `n/a` — documentation change, no runtime path |
| Prompt-injection scan | `pass` — all added text authored in this V-Bounce; no external content inlined |
| Secret-leak scan | `pass` — no credentials, tokens or endpoints in the diff |
| Hallucination lint | `pass` — every `§` reference and rule ID cited by the new text resolves on disk (§5.2, §5.16, §5.12, G07, G36 verified) |
| IP / license provenance | `n/a` — no third-party material introduced |
| PII / DLP | `n/a` — `data_classification: internal`, no personal data involved |
| Dependency-confusion | `n/a` — no package resolution involved |
| Test-first evidence | `n/a` — not a BUG Bolt; no red/green sequence prescribed (§3.3.1) |
| Behavioral reproducibility | `pass` — rehearsal run twice with identical output; every check is re-runnable |
| Bolt-manifest validation | `pass` — validates against `manifest-v4-bolt.schema.json` (jsonschema, Draft 2020-12), 0 errors |

---

## 10. Manual interventions

None. The agent produced every change; no human patch was applied.

---

## 11. Evidence links

- **Diff / PR:** none — nothing was staged or committed (G34; the human owns the commit)
- **Commit:** baseline `67a62ed` on branch `4.2`, plus the uncommitted 4.2 reorganization present in the working tree
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-001-agents-md-project-section.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~7 min (21:16 → 21:23 local), first V-Bounce of the repository |
| V-Bounce number | 1 |
| Tests created | n/a — no runtime; 8 acceptance criteria verified by 20 deterministic checks plus a 2-pass migration rehearsal and 5 boundary cases |
| AI-generated code | 100% — no human fallback |
| First-pass approval | pending `HITL-MEM-Approval` |

---

## 13. Pending items and stubs

- [ ] `HITL-BOLT-DONE-Approval` — acceptance routes to Tech Lead + Security by `work_category: hardening` (§3.11)
- [ ] The **G29 solo-maintainer finding**: a non-functional BUG at any severity requires an approver other than its author, which closes the entire BUG route for a single-person team. Surfaced during this Bolt's routing decision, unrelated to its content — it needs its own `OQ-NNN` or retro entry
- [ ] A `tools/` checker for the framework-block byte-identity invariant, deliberately excluded from this Bolt's scope
- [ ] The release migration of this repository itself, which will be the first real execution of §5.16

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff, the
> verification evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.
> `risk_class: medium` requires 1 approver (§3.3).

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | changes_requested |
| **review_ready_at** | `2026-08-17T21:23:10-03:00` |
| **review.started_at** | `2026-08-17T21:23:10-03:00` |
| **review.decided_at** | `2026-08-18T10:38:00-03:00` |
| **Review evidence** | Diff of the shipped `AGENTS.md`, §5.16, G36 and the four agent definitions; the §9 verification output; the merge traced byte by byte against both a simulated adopting project and this repository |
| **Comments** | Mechanism confirmed correct and stated in all three places, including the auto-loaded agent definition. Five findings, four of them surfaced by tracing the merge byte by byte during review. |
| **Findings** | 5 — recorded in the frontmatter `review.findings` |
| **acknowledged_without_comment** | false |
| **acknowledgment_reason** | n/a — findings recorded |
