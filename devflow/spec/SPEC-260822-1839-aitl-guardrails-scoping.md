---
id: "SPEC-260822-1839"
title: "Scope G05/G18/G24 for AITL (canonical AITL-*, HITL-* legacy; AI-approves-only-if-configured) — count 39 unchanged"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-021"
bolt: "US-021.BOLT-002"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1817"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T18:39:52-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T18:43:04-03:00"
  decided_at: "2026-08-22T18:43:04-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. G05/G18/G24 scoped for AITL per ADR-008 §3.1/§3.4 (canonical AITL-*, HITL-* legacy; AI-approves-only-if-configured-with-independence; record never fabricates a human; safe default human-only). Count stays 39; BOLT-002 owns these three rules, BOLT-004 allowlists them; only G05/G18/G24 change. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root operating methodology stays v4.2. Dogfooding split:
  this SPEC's own checkpoints are HITL-*. BOUNDARY: this Bolt fully owns the TEXT of
  G05, G18, G24 (their AITL/HITL tokens are the semantic); BOLT-004's sweep
  ALLOWLISTS these three rules. It does NOT touch other rules, the identifier sweep
  (BOLT-004), the schema enum (BOLT-003) or the precept prose (BOLT-001, Done).
-->

# SPEC-260822-1839 — AITL guardrails scoping (US-021.BOLT-002)

| Field | Value |
|-------|-------|
| **Origin** | [US-021](../functional/user-stories/US-021-hitl-to-aitl-evolution.md) (approved) |
| **Bolt** | [US-021.BOLT-002](../functional/bolts/US-021.BOLT-002-aitl-guardrails-scoping.md) (approved) |
| **ADRs** | ADR-008 (§3.1 G05, §3.4 G18/G24/G37/handoff), ADR-005 (boundary), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 · **Revision** 1 |

---

## 1. Objective

Evolve the **semantics** of the three identity/naming guardrails for AITL, per
ADR-008: **G05** (canonical vocabulary), **G18/G24** (AI-approves-only-if-configured,
record never fabricates a human), aligned with the **G37/handoff no-fallback**
exclusion already stated in §3.0. This scopes *what the rules mean* under
human-by-default/agent-by-explicit-configuration — **without adding, removing or
renumbering any rule** (count stays **39**).

**Why:** BOLT-001 stated the AITL precept; the guardrails must now enforce it
precisely (an AI actor may occupy an approval only under explicit valid config with
independence). **If not done:** G18/G24 still forbid *all* AI approval outright,
contradicting the AITL precept BOLT-001 introduced.

---

## 2. Context

`GUARDRAILS.md` carries the full G05 (line 61), G18 (95), G24 (106); the four
agents carry the compressed table rows (CLAUDE.md 221/234/240 + peers). §3.0
already excludes G37 + the handoff from any no-holder fallback (line ~1388, from
US-014) — this Bolt aligns G18/G24 to it, it does not duplicate it.

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-021.BOLT-002-aitl-guardrails-scoping.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-021-hitl-to-aitl-evolution.md` | HITL-US-Approval ✓ |
| ADRs | ADR-008 (§3.1/§3.4), ADR-005, ADR-004 | accepted ✓ |
| Prior Bolt | US-021.BOLT-001 (concept) | **Done** ✓ |

Pre-SPEC evidence gate: **all governed sources approved.** No active-ADR conflict.

---

## 4. The scoping to apply (RED → GREEN)

### G05 — canonical vocabulary (ADR-008 §3.1)
- **Now:** canonical is `HITL-*`; H1–H6 legacy.
- **Scoped:** canonical is **`AITL-<CODE>-Approval`**; **`HITL-*` joins H1–H6 as a
  legacy prefix** — invalid for new approvals, preserved only in migrated history
  (G36).

### G18 — no self-approval, scoped (ADR-008 §3.2–§3.4)
- **Now:** "self-approve the MEM / skip human review / 'AI says it's fine'" — the AI
  never approves.
- **Scoped:** the agent **never approves its own work** (approver actor ≠ executor
  actor); an **AI actor may approve only under an explicit valid virtual-approver
  configuration with independence**; absent/invalid config → **human-only**; **the
  record never fabricates a human** — a virtual approval is `agent:<id>`/`model:<id>`.

### G24 — no un-configured delegation / no fabrication (ADR-008 §3.4)
- **Now:** "delegate a human checkpoint to AI or fabricate a reviewer decision."
- **Scoped:** delegate a checkpoint to an AI approver **without explicit valid
  configuration (or without independence)**, or fabricate a reviewer decision. A
  *configured, independent* AI approver is permitted (that is the AITL path); the
  safe default stays human-only.

### G37 + handoff — already excluded (§3.0)
- No change to §3.0's existing exclusion; G18/G24's scoped text references it (the
  identity-separation rules are never subject to a no-holder fallback).

**Count invariant:** G05, G18, G24 keep their numbers; **no rule added, removed or
renumbered** → total stays **39**.

---

## 5. Scope

### In scope (kit)
- `distribution-kit/devflow/GUARDRAILS.md` — the full text of **G05, G18, G24**.
- `distribution-kit/CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
  `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md` —
  the **compressed G05/G18/G24 table rows** (byte-synced).

### Boundary (ADR-005)
- **This Bolt fully owns G05/G18/G24's text** — including the `AITL-*`/`HITL-*`
  tokens *inside those three rules* (they express the semantic). **BOLT-004's
  identifier/adjective sweep ALLOWLISTS these three rules.**
- **NOT this Bolt:** every other rule and incidental `HITL-*` mention, the
  identifier sweep, the `HITL` adjective → BOLT-004; the schema enum → BOLT-003;
  the precept prose → BOLT-001 (Done).

### Out of scope
- Enabling virtual approvers / registry / Coordinator / roster / pilot (later USs);
  the root `devflow/` (ADR-004).

---

## 6. Phases

- **Phase A — GUARDRAILS.md:** rewrite G05, G18, G24 (full text). ~1h.
- **Phase B — the four agents:** the compressed G05/G18/G24 rows (byte-identical). ~0.5h.
- **Phase C — Verification (GREEN):** count 39×5; only G05/G18/G24 changed; sync. ~0.5h.

---

## 7. Acceptance criteria

- **AC-1 (G05 scoped):** G05 reads canonical `AITL-*`, `HITL-*` legacy (with H1–H6),
  preserved only in migrated history (G36) — in GUARDRAILS + the four agents.
- **AC-2 (G18 scoped):** G18 reads: agent never approves its own work; AI approval
  only under explicit valid config with independence; absent/invalid → human-only;
  record never fabricates a human (`agent:<id>`/`model:<id>`).
- **AC-3 (G24 scoped):** G24 reads: no delegation to an AI approver without explicit
  valid configuration/independence; no fabricated decision; a configured independent
  AI approver is the permitted AITL path.
- **AC-4 (G37/handoff intact):** §3.0's exclusion of G37 + handoff from any
  no-holder fallback is preserved and referenced by G18/G24.
- **AC-5 (count + sync):** the **blocking-rule count is exactly 39** (no rule
  added/removed/renumbered); the four agents' G05/G18/G24 rows are **byte-identical**;
  **G-count 39×5**.
- **AC-6 (boundary):** **only G05, G18, G24** are changed (diff inspection); no other
  guardrail, no incidental `HITL-*` elsewhere, is touched (those are BOLT-004).
- **AC-7 (kit-only):** `git status` shows only `distribution-kit/` + governance
  records; root untouched.
- **AC-8 (manifest):** the BOLT-002 manifest gets its `v_bounces[]` entry and validates.

---

## 8. Testing strategy

Deterministic (documentation/guardrails):
- **RED (before):** G05 canonical = HITL-*; G18/G24 forbid *all* AI approval.
- **GREEN (after):** AC-1..AC-4 present; the **G-number set is unchanged** —
  `grep -oE 'G[0-9]{2}'` distinct count = 39 in GUARDRAILS and 39 in each agent
  (39×5); the four agents' G05/G18/G24 rows identical; `git diff` shows only
  G05/G18/G24 lines changed; `git status` kit-only. Record the G-count + the
  "only three rules changed" diff summary in the MEM.

---

## 9. Quality gates

Documentation/internal → unit/integration, SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. hallucination-lint, behavioral-reproducibility,
bolt-manifest-validation: `pass`. prompt-injection, secret-leak: `pass`.

---

## 10. Security and data

These guardrails **are** the approval-integrity guarantees. The scoping follows
ADR-008 §3.4 verbatim — it narrows *when* an AI may approve; it never lets the
record fabricate a human, never lets an executor approve its own work, and keeps
the safe default human-only. Data `internal`.

---

## 11. Migration, compatibility, rollback

Additive/semantic; no rule added or removed (count 39). Rollback: revert the kit
commit; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Scoping dissolves G18/G24 | 2 | 5 | Follow ADR-008 §3.4 verbatim; AC-2/3 keep "never fabricate a human", "actor ≠ executor", human-only safe default |
| Rule count drifts | 1 | 4 | AC-5: G-number distinct count = 39 in GUARDRAILS + 39×5 agents |
| Bleed into other rules | 2 | 3 | AC-6: diff shows only G05/G18/G24 changed |
| Four-agent drift | 2 | 3 | Byte-identical rows; AC-5 sync |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| BOLT-002 fully owns G05/G18/G24 text (tokens included) | Their `AITL-*`/`HITL-*` tokens *are* the semantic; splitting them from BOLT-004 would fracture one rule across two Bolts |
| BOLT-004 allowlists G05/G18/G24 | They are already AITL-scoped here; the sweep must not re-touch them |
| Reference, not duplicate, the §3.0 G37/handoff exclusion | It already exists (US-014); duplication risks drift |
| Keep `HITL-*` as a named legacy prefix in G05 | ADR-008 §3.1 — migrated history keeps `HITL-*` (G36) |

---

## 14. Stop conditions

- The G-number count ≠ 39 (any agent or GUARDRAILS) → a rule was added/removed;
  stop, fix.
- The diff touches a rule other than G05/G18/G24 → stop, revert (BOLT-004's).
- Any root `devflow/` file in the diff → stop, revert, record.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–C · AC-1..AC-8 pass
- [ ] GREEN (G05/G18/G24 scoped; count 39×5; only three rules changed; kit-only)
- [ ] ADR-008 (§3.1/§3.4) + ADR-005 (boundary) + ADR-004 (kit-only) followed
- [ ] MEM (with G-count + "only three rules changed" evidence) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 16. References

- US-021, US-021.BOLT-002 (approved); US-021.BOLT-001 (Done)
- ADR-008 §3.1 (G05 vocabulary), §3.4 (G18/G24 scoping, G37/handoff no-fallback)
- GUARDRAILS.md G05/G18/G24; §3.0 identity-separation exclusion (line ~1388)

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T18:39:52-03:00` |
| **review.started_at** | `2026-08-22T18:43:04-03:00` |
| **review.decided_at** | `2026-08-22T18:43:04-03:00` |
