---
id: "SPEC-260822-0053"
title: "Role routing as guidance, never a gate — operability principle, role multiplicity, no-holder fallback"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-014"
bolt: "US-014.BOLT-001" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium" # mirrors the Bolt
autonomy_level: "L3" # medium → L3 default
turn_budget: "" # platform default
data_classification: "internal"
review_ready_at: "2026-08-22T00:53:56-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:01:19-03:00"
  decided_at: "2026-08-22T01:01:19-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed revision 1 against US-014 (approved), the Bolt US-014.BOLT-001 and ADR-004: the D1/D2/D3 approach is faithful to the approved policy, the §3.3 MEM-approver boundary (deferred to BOLT-003) is correct, the identity-rule exclusions are explicit and verified by AC-4, and the completeness grep guarantees no role-gated route without a fallback. Approved as drafted — authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  Kit-only edits (ADR-004); the root devflow/ is untouched. Documentation
  change — verification is a deterministic grep/consistency suite.
-->

# SPEC-260822-0053 — Role routing as guidance, never a gate

| Field | Value |
|-------|-------|
| **Origin** | [US-014](../functional/user-stories/US-014-role-availability-policy.md) (approved) |
| **Bolt** | [US-014.BOLT-001](../functional/bolts/US-014.BOLT-001-role-guidance-not-gate.md) (approved) |
| **ADRs** | [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Implement the **role dimension** of US-014 (D1, D2, D3) in the distributable:
state the single-operator operability principle once as a governing default
(D1), define role multiplicity with recorded self-assignment (D2), and remove
the role-availability **block** from every named-role checkpoint route while
keeping the named role as guidance (D3) — preserving the identity-separation
rules as the only exceptions.

**If not implemented:** the methodology stays structurally unsatisfiable for
small teams (the confirmed AREV-001 blockers on the critical BUG route,
acceptance pairing and TC), and future checkpoints keep being written
role-first (no governing default to inherit from).

---

## 2. Context

US-014 (approved, `HITL-US-Approval`) records the maintainer policy D1–D7 for
single-operator operability. This Bolt implements the role dimension; D5 (AREV)
is US-014.BOLT-002 and D7 (approver counts) is US-014.BOLT-003. To avoid
double-editing the §3.3 MEM-approver area, **this SPEC does not touch the MEM
approver rule** (owned wholesale by BOLT-003/D7); it establishes the principle
and the fallback pattern that BOLT-003 then follows. Kit-only (ADR-004).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-014.BOLT-001-role-guidance-not-gate.md` | HITL-BOLT-READY-Approval ✓ (2026-08-22T00:47:31-03:00) |
| Parent US | `devflow/functional/user-stories/US-014-role-availability-policy.md` | HITL-US-Approval ✓ (2026-08-22T00:37:30-03:00) |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| Route inventory | US-014 §3 (single-role-route enumeration) | — |
| Repository baseline | branch `4.2`, HEAD `0c7f40d` | — |

Pre-SPEC evidence gate: **all governed sources approved**.

---

## 4. Scope

### In scope (kit only, `distribution-kit/`)

- **D1** — the operability principle as a governing statement.
- **D2** — role multiplicity + recorded self-assignment.
- **D3** — the no-holder fallback on every single-role route of the US-014 §3
  enumeration **except the MEM approver rule**: the §3.0 checkpoint-table owner
  cells (US, TC, BOLT-READY, ADR, SPEC, BOLT-DONE, UNIT, UAT — note UNIT/UAT
  are being removed by US-015, so touch only if still present), the §3.11
  work-category acceptance table (`infra`→TL+SRE, `hardening`→TL+Sec, etc.),
  the critical non-functional BUG route, the two-role TC route, the GUARDRAILS
  checkpoint map + work-category table, and the four agents' HITL tables +
  acceptance bullets.

### Out of scope

- **The §3.3 MEM approver rule (role + counts)** → US-014.BOLT-003 (D7) rewrites it wholesale.
- D5 AREV operability → US-014.BOLT-002.
- UNIT/UAT machinery removal → US-015.
- The team-roster mechanism → US-001.
- The root `devflow/` tree (ADR-004 — next §5.16 migration).

---

## 5. Prerequisites and baseline

- US-014 approved; US-014.BOLT-001 approved (readiness).
- The four agent definitions in sync before the edit (whole-body diff = sanctioned divergence only); if pre-existing drift → stop, reconcile first.
- Baseline: branch `4.2`, HEAD `0c7f40d`.

---

## 6. Phases

### Phase A — D1: the operability principle (governing statement)

**Duration:** ~0.75h — **Complexity:** Medium

Add a governing paragraph to the §3.0 HITL Charter (after the "load-bearing
principle" intro, ~line 1360) stating: *role routing informs who should
review; availability never blocks; every HITL checkpoint is satisfiable by the
qualified human(s) actually present; the named role is kept as guidance, never
as a gate; the only exceptions are the identity-separation rules (handoff
incoming-executor, G37 Judge-model neutrality, G18/G24 no AI self-approval).*
Mirror a compact one-line version in `GUARDRAILS.md` (near the checkpoint map)
and in the four agents' HITL Checkpoints section (identical text).

**Files modified:** kit methodology §3.0; `GUARDRAILS.md`; the four agents.

### Phase B — D2: role multiplicity + recorded self-assignment

**Duration:** ~0.5h — **Complexity:** Low

Add a clause (in the §3.0 charter, near the checkpoint table) stating: *one
person may hold several roles simultaneously; when a person approves acting in
a role they hold, the approval records the self-assigned role (e.g. "approved
as QA: <user>"), until the team roster (US-001) provides the resolution layer;
role assignment is living data, not a decision requiring approval.* Mirror
compactly in the four agents + `GUARDRAILS.md`.

**Files modified:** kit methodology §3.0; `GUARDRAILS.md`; the four agents.

### Phase C — D3: no-holder fallback on every single-role route (except MEM)

**Duration:** ~1.5h — **Complexity:** Medium

For each single-role Owner cell in the US-014 §3 enumeration (except the MEM
rule), keep the named role as the **default/recommended** approver and append
the fallback: *"— or, when no holder exists, the available qualified human
records it, noting the self-assigned role (D2)."* Apply to:
- §3.0 checkpoint table owner cells (US, TC, BOLT-READY, ADR, SPEC, BOLT-DONE; UNIT/UAT only if still present).
- The critical non-functional BUG route (make it satisfiable — the AREV-001 F-02 blocker) while keeping "Architect/Tech Lead" as the default and self-approval prohibited only where an alternate approver exists.
- §3.11 work-category acceptance table (`infra`→TL+SRE, `hardening`→TL+Sec, `refactor`/`debt`→TL, `qa_automation`→QA Lead) — pairs kept as default, fallback added.
- The two-role TC route (QA + owner as default; fallback).
- `GUARDRAILS.md` checkpoint map + work-category table; the four agents' HITL tables + acceptance bullets — identical treatment.

**Explicitly NOT changed (identity rules):** the handoff incoming-executor rule (§3.3), G37, and G18/G24 — verified untouched.

**Files modified:** kit methodology §3.0/§3.11/§2.16; `GUARDRAILS.md`; the four agents.

### Phase D — Verification

**Duration:** ~0.5h — **Complexity:** Low

Run and record the §8 verification suite (grep, four-agent sync, G-count, root untouched).

---

## 7. Acceptance criteria

### AC-1: Operability principle stated once as governing default (D1)
**Given** the edited kit, **When** grepping the §3.0 charter, **Then** the
operability principle appears as a governing statement, mirrored (compact) in
GUARDRAILS and the four agents.

### AC-2: Role multiplicity + self-assignment present (D2)
**Given** the edited kit, **When** grepping the charter, **Then** the
multiplicity/self-assignment clause is present and mirrored.

### AC-3: Every single-role route (except MEM) carries the fallback (D3)
**Given** the edited kit, **When** grepping every single-role Owner cell in the
US-014 §3 enumeration (excluding the §3.3 MEM rule), **Then** each states the
role as default **and** carries the no-holder fallback — zero role-gated routes
without a fallback remain.

### AC-4: Identity rules untouched
**Given** the edited kit, **When** diffing the handoff rule (§3.3), G37 and
G18/G24, **Then** they are byte-unchanged.

### AC-5: Four-agent sync + G-count
**Given** the edited agents, **When** running the whole-body diff and the
G-count, **Then** they differ only by the sanctioned line and each counts 39;
GUARDRAILS counts 39.

### AC-6: Root untouched
**Given** the V-Bounce, **When** `git status`, **Then** only `distribution-kit/`
files (plus this Bolt's governance records) changed.

### AC-7: Bolt-manifest validation
**Given** the updated manifest, **When** validated, **Then** 0 errors.

### AC mapping to source

| US-014 AC | How satisfied | Evidence |
|-----------|---------------|----------|
| AC-1 (available human records approval) | Phase C fallback | AC-3 |
| AC-2 (role as guidance never block) | Phases A + C | AC-1, AC-3 |
| AC-3 (critical BUG / infra-hardening / TC) — role half | Phase C | AC-3 |
| AC-7 (identity rules excluded) | Phase C exclusion | AC-4 |
| AC-8 (complete enumeration) | Phase C + grep | AC-3 |

---

## 8. Testing strategy

Deterministic, no runtime:
- **Principle/multiplicity present (AC-1, AC-2):** grep the charter + mirrors.
- **Fallback coverage (AC-3):** grep every single-role Owner cell (US-014 §3 list) for the fallback clause; assert zero role-gated-without-fallback (excluding the MEM rule, out of scope).
- **Identity rules intact (AC-4):** targeted diff/grep of the handoff rule, G37, G18/G24 → unchanged.
- **Sync (AC-5):** four-agent whole-body diff + `grep -cE '^\| G[0-9]{2} '` = 39.
- **Root check (AC-6):** `git status --short`.
- **Manifest (AC-7):** schema validation.
- **Edge cases:** escaped pipes in table cells; CRLF/LF normalization; UNIT/UAT rows may already be gone (US-015) — treat as "touch only if present".

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only |
| SAST / SBOM | — | `n/a` — no code/deps |
| Perf-smoke | — | `n/a` — no runtime |
| Prompt-injection scan | — | `pass` — text authored here |
| Secret-leak scan | — | `pass` |
| Hallucination lint | — | `pass` — every path/§-reference resolves |
| IP / license provenance | — | `n/a` |
| PII / DLP | — | `n/a` — internal, no personal data |
| Dependency-confusion | — | `n/a` |
| Test-first evidence | — | `n/a` — not a BUG Bolt (policy feature; grep verification) |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff |
| Bolt-manifest validation | — | `pass` |

---

## 10. Security and data

Changes governance-routing text only; no security boundary, credential or data
path. The identity-separation rules (which carry the real segregation-of-duty
protection) are explicitly preserved. Data classification `internal`.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §8 suite is the observability; output captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none here; adopters receive it at their next §5.16 migration.
- **Compatibility:** G-count stays 39; checkpoint vocabulary unchanged; roles still named (as guidance) so no consumer breaks.
- **Rollback:** revert the kit commit(s); root untouched.

---

## 13. Risk matrix

| Risk | Prob (1-5) | Impact (1-5) | Mitigation |
|------|-----------|--------------|------------|
| A route missed | 2 | 3 | US-014 §3 checklist + AC-3 grep asserts zero role-gated-without-fallback |
| Fallback weakens an identity rule | 2 | 4 | Explicit exclusion list; AC-4 verifies handoff/G37/G18/G24 unchanged |
| Collision with BOLT-003 (§3.3 MEM) | 2 | 3 | §3.3 MEM rule explicitly out of scope here; BOLT-003 owns it |
| Four-agent drift | 2 | 3 | Identical edits; AC-5 sync |
| Root edited by mistake | 1 | 4 | Kit-only; AC-6 check |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| MEM approver rule left to BOLT-003 | Avoids two Bolts editing the same §3.3 area; BOLT-003 rewrites it wholesale (D7) |
| Keep the named role as default + add fallback (not delete the role) | US-014 D1/D3: role stays as guidance, never removed |
| Principle stated once + mirrored compactly | Single source of truth; avoids the drift BUG-001 documented |
| UNIT/UAT rows "touch only if present" | US-015 removes them; avoid conflicting with that Bolt |

---

## 15. Stop conditions

- Pre-existing four-agent drift before Phase C → stop, reconcile, record.
- Any root `devflow/` methodology file in the diff → stop, revert, record.
- AC-3 still shows a role-gated route without a fallback → stop, sweep again.
- An identity rule would need to change to satisfy a route → stop (that is a design change, not this Bolt).
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] Phases A–D implemented
- [ ] AC-1..AC-7 pass
- [ ] Verification GREEN (principle+multiplicity present; every route has fallback; identity rules unchanged; sync 39×5; root untouched; manifest 0 errors)
- [ ] Follows ADR-004 (kit-only)
- [ ] Gates pass / n/a per §9
- [ ] MEM created (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- US-014 (approved), US-014.BOLT-001 (approved), US-014 §3 enumeration
- ADR-004 (kit-only), AGENTS.md (four-agent sync)
- US-014.BOLT-003 (the §3.3 MEM rule owner), US-015 (UNIT/UAT), US-001 (roster)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial revision 1 (draft) |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval` (in the `review` block). Bolt approval authorizes SPEC
> preparation; **SPEC approval** authorizes the V-Bounce. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-22T00:53:56-03:00` |
| **review.started_at** | `2026-08-22T01:01:19-03:00` |
| **review.decided_at** | `2026-08-22T01:01:19-03:00` |
