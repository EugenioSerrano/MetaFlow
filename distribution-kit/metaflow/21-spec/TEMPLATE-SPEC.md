---
id: "SPEC-YYMMDD-HHmm"
title: ""
date: "YYYY-MM-DD"
author: "" # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: "" # LLM model used (e.g. "Claude Sonnet", "GPT")
status: "draft" # draft | approved | blocked | obsolete
origin: "" # US-NNN, TC-NNN, BUG-NNN, DISC-NNN, REV-NNN, AREV-NNN, or ADR-NNN that motivated this SPEC
task: "" # ⚠️ MANDATORY — US-NNN.TASK-NNN | US-000.TASK-NNN | TC-NNN.TASK-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs: []
prerequisites: [] # Prior SPECs this one depends on
risk_class: "" # low | medium | high | critical (mirrors the TASK's risk_class)
autonomy_level: "" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3, high→L2, critical→L1; L4 requires an ADR (§3.3)
turn_budget: "" # OPTIONAL — agent loops without a green test suite before stop-and-ask (integer ≥ 1); leave empty to use the platform/agent default (§3.3)
data_classification: "internal" # public | internal | confidential | restricted — ordered (public < internal < confidential < restricted),
                                # normative definition in §3.6; mirrors the TASK's; this SPEC-declared value is the one the PII/DLP gate reads
review_ready_at: "" # When this version is submitted for review (§3.0) — ISO 8601 with seconds + offset, e.g. 2026-08-02T11:45:00-03:00
review: # CP-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: "" # ISO 8601 with seconds + offset
  decided_at: "" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  context, rationale, findings — goes in the project's content_language
  (declared in metaflow/LANGUAGE).

  ⚠️ MANDATORY TIMESTAMP: To generate the ID and filename:
  1. Run: Get-Date -Format "yyMMdd-HHmm" (PowerShell) or date +"%y%m%d-%H%M" (Bash)
  2. Use that ACTUAL value to replace YYMMDD-HHmm in the id, title and filename.
  3. NEVER invent or estimate the time.

  ⚠️ MANDATORY LLM: Fill the llm field with the exact model generating this document.
  ⚠️ MANDATORY TASK: The `task` field MUST reference an APPROVED TASK (CP-TASK-READY-Approval).
     A SPEC without a TASK reference is INVALID and cannot start implementation.
     Traceability: SPEC → TASK → manifest (spec_revisions[]).
  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): before generating, verify every governed source
     is approved (BUG/TC/TASK/US/ADR/DISC/REV/AREV). Any draft source → blocking
     report, never a partial SPEC.
  ⚠️ CP-SPEC-Approval: a draft SPEC cannot start a code-run or Delivery Loop. Material
     source changes invalidate the approval → stop, revise, re-approve (G15).
     One Delivery Loop never spans two SPEC revisions.
-->

# SPEC-YYMMDD-HHmm — [Descriptive title]

| Field | Value |
|-------|-------|
| **Origin** | [US-NNN / BUG-NNN / TC-NNN / DISC-NNN / REV-NNN / AREV-NNN / ADR-NNN] |
| **TASK** | [US-NNN.TASK-NNN] |
| **ADRs** | [links to associated ADRs] |
| **Risk Class** | [low / medium / high / critical] |
| **Revision** | [N] |

---

## 1. Objective

<!--
  ⚠️ MANDATORY: What is being built or modified. At least one paragraph.
  What problem does it solve? What happens if NOT implemented?
-->

[Concise description of what this SPEC will implement or modify.]

---

## 2. Context

<!--
  Where does this need come from? Reference the originating US/BUG/TC/DISC/REV/ADR and the
  approved TASK. What hardware, infrastructure, or system constraints exist?
-->

[Business and technical context that motivated this SPEC.]

---

## 3. Source inventory and approval references

<!--
  ⚠️ MANDATORY: from the pre-SPEC evidence gate — every governed source used,
  its approval status, and the repository baseline.
-->

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | [US-NNN.TASK-NNN] | CP-TASK-READY-Approval ✓ |
| Feature US / TC / BUG | [ref] | CITL-US / CITL-TC / CP-BUG-Approval ✓ |
| ADRs | [ADR-NNN] | CP-ADR-Approval ✓ |
| DISC/REV/AREV evidence | [ref] | approval ✓ |
| Repository baseline | [git commit] | — |

---

## 4. Scope

### In scope

- [What this SPEC covers]

### Out of scope

- [What this SPEC explicitly does NOT cover]

---

## 5. Prerequisites and baseline

<!--
  Current build state, prior SPECs that must be completed first,
  environment requirements.
-->

- [Prerequisite 1]
- [Prerequisite 2]

---

## 6. Phases

<!--
  ⚠️ Each phase must be EXPLANATORY, not a telegram.
  Describe: what files are created/modified, what patterns are applied,
  how components interact, what ADRs constrain them.

  ⚠️ ONE TASK PER SPEC: All phases in this SPEC implement the SAME TASK
  (the one in the `task` frontmatter field). If your work spans multiple
  TASKs, create one SPEC per TASK.

  ⚠️ BUG SPECS (§3.3.1): prescribe strict TDD in ONE Delivery Loop — reproduction
  test (RED evidence) → production change → green. Production code may not
  change before red evidence exists.

  ⚠️ TEST TASK SPECS (§3.2.1): map exactly one approved parent TC to the QA
  Automation code; preserve the TC's expected results; no production-code
  changes.

  Format: Phase A — [Name]
  Duration: Xh total cycle — Complexity: Low/Medium/High
-->

### Phase A — [Name]

**Duration:** Xh total cycle — **Complexity:** Low / Medium / High

#### A.1 [Sub-step description]

[Detailed description of what is built: components, patterns, dependencies, ADR references.]

**Files created:**
- `path/to/file.ts` — Purpose in the system

**Files modified:**
- `path/to/file.ts` — Description of change

#### A.2 [Sub-step description]

[Same level of detail.]

---

### Phase B — [Name]

**Duration:** Xh total cycle — **Complexity:** Low / Medium / High

[Same structure as Phase A.]

---

## 7. Acceptance criteria

<!--
  ⚠️ Each AC must be testable. Use Given/When/Then format (BDD).
  Define inputs, expected outputs, and edge cases.
-->

### AC-1: [Short description]

**Given** [precondition]
**When** [action]
**Then** [expected result]

### AC-2: [Short description]

**Given** [precondition]
**When** [action]
**Then** [expected result]

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| [US AC-1 / technical outcome] | [implementation approach] | [test or evidence] |
| | | |

---

## 8. Testing strategy

<!--
  What types of tests will be created: unit, integration, e2e?
  What edge cases and error scenarios must be covered?
  For BUG SPECs: the reproduction test and its RED evidence come first (§3.3.1).
-->

- **Unit tests:** [what and how many]
- **Integration tests:** [what and how many]
- **E2E tests:** [what and how many, if applicable]
- **Edge cases:** [list]
- **BUG evidence:** [RED command/result → GREEN command/result]

---

## 9. Quality gates

<!--
  Applicable gates selected by this SPEC (§3.6): classic + AI-native.
  Each ends pass | waived (ADR-NNN) | n/a (with reason).
-->

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | | |
| SAST / SBOM | | |
| Perf-smoke (p95/p99) | | |
| Prompt-injection scan | | |
| Secret-leak scan | | |
| Hallucination lint | | |
| IP / license provenance | | |
| PII / DLP | | |
| Dependency-confusion | | |
| Test-first evidence | | |
| Behavioral reproducibility | | |
| TASK-manifest validation | | |

> Each gate ends `pass` / `waived` (ADR-NNN) / `n/a` (with reason) (§3.6).
> Non-applicable gates must still be listed with their `n/a` reason.

---

## 10. Security and data

<!--
  ⚠️ MANDATORY: security considerations (auth, authorization, data
  exposure, secrets) and data handling per the SPEC's `data_classification`
  (§3.2.1).
-->

- [Security control / threat considered]
- [Data handling / classification notes]

---

## 11. Monitoring and observability

<!--
  Logs, metrics, traces, alerts that must be added or modified.
-->

- [Log/metric/alert 1]
- [Log/metric/alert 2]

---

## 12. Migration, compatibility and rollback

<!--
  Schema changes, feature flags, compatibility and rollback procedure.
  If not applicable, state it explicitly (§3.2.1).
-->

- **Migration:** [steps or "N/A"]
- **Compatibility:** [notes or "N/A"]
- **Rollback:** [steps or "N/A"]

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
|      |                   |             |            |

---

## 14. Decisions and trade-offs

<!--
  Micro-decisions that do not warrant a full ADR.
  Why one approach over another, what alternatives were discarded.
-->

| Decision | Reason |
|----------|--------|
|          |        |

---

## 15. Stop conditions

<!--
  Explicit conditions that halt the Delivery Loop: an unresolved architectural
  decision → ADR lifecycle; unreproducible bug; material source change;
  conflicting, missing or ambiguous evidence → stop and request resolution
  (never fill the gap with an assumption, §2.4.1). The agent records the
  blocker in the MEM.
-->

- [Stop condition 1]

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented
- [ ] All acceptance criteria pass
- [ ] Tests GREEN (unit + integration + e2e where applicable); BUG: red + green evidence recorded
- [ ] Code follows applicable ADRs
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `metaflow/22-memory/` (exactly one per Delivery Loop)
- [ ] Manifest `delivery_loops[]` entry appended in `metaflow/23-metrics/tasks/`
- [ ] CP-MEM-Approval recorded

---

## 17. References

<!--
  Related documents: US, ADRs, DISCs, BUGs, RISKs, prior SPECs.
-->

- [Reference 1]
- [Reference 2]

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
|      |        |        |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `CP-SPEC-Approval`
> (in the `review` frontmatter block). TASK approval (`CP-TASK-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> Delivery Loop. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | [Dev-validator + applicable domain owner(s)] |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
