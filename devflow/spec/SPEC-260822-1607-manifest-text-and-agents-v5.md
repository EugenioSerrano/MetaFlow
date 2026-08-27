---
id: "SPEC-260822-1607"
title: "Align the methodology text + four agents to the v5 manifest (§3.12, G23, projection maps, schema refs, agents' Manifest Family)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-020"
bolt: "US-020.BOLT-002"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1546"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T16:07:33-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T16:12:25-03:00"
  decided_at: "2026-08-22T16:12:25-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Phrase family + full location set + the §5.16-conversion allowlist declared (ADR-005); the substantive §3.12/agents shape rewrite (mode + actor+model) separated from the mechanical renames; checkpoint names kept HITL-* (rename is a separate US). Prereq BOLT-001 Done. Kit-only, medium/L3. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root untouched. ADR-005 phrase-family sweep discipline.
  This Bolt aligns the DESCRIBING text to the v5 schema (BOLT-001, Done); it
  does NOT rename checkpoints (HITL→AITL, separate US) and does NOT touch the
  §5.16 conversion recipe (BOLT-003).
-->

# SPEC-260822-1607 — Align the methodology text + four agents to the v5 manifest

| Field | Value |
|-------|-------|
| **Origin** | [US-020](../functional/user-stories/US-020-manifest-aitl-evolution.md) (approved) |
| **Bolt** | [US-020.BOLT-002](../functional/bolts/US-020.BOLT-002-manifest-text-and-agents.md) (approved) |
| **ADRs** | ADR-008/007 (v5 shape), ADR-005 (sweep discipline), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 |
| **Revision** | 1 · **Prerequisite:** SPEC-260822-1546 (BOLT-001, Done) |

---

## 1. Objective

Bring every place in the kit that **describes** the manifest into agreement with
the v5 schema BOLT-001 shipped, so the kit does not contradict itself — the
ADR-005 partial-sweep guard applied to the manifest change. Two kinds of edit:
**(a) mechanical renames** (`hitl_approvals`→`checkpoint_approvals`,
`manifest-v4`→`manifest-v5`, `schema_version "4.0"`→`"5.0"`, "Manifest Family
v4"→"v5"); **(b) a substantive shape rewrite** of §3.12 and the agents' Manifest
Family section to describe the new record — `checkpoint_approvals[]` with `mode`
(`human`|`virtual`) and an approver of `{actor, role, model}`.

**If not done:** the kit ships a v5 schema while its own methodology and agents
describe v4 — a self-contradiction, and an auto-loaded agent would instruct
against the shipped schema.

---

## 2. Context

BOLT-001 (Done) shipped the v5 schemas + templates. This is **BOLT-002**
(depends on BOLT-001). The §5.16 conversion recipe is **BOLT-003** — this SPEC
excludes the entire §5.16 manifest-conversion section. The checkpoint-name rename
(`HITL-*`→`AITL-*`) is a separate US — this SPEC keeps the checkpoint names as-is
and touches only the manifest **structure** description. Kit-only (ADR-004).

---

## 3. Source inventory and approval references (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-020.BOLT-002-manifest-text-and-agents.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-020-manifest-aitl-evolution.md` | HITL-US-Approval ✓ |
| Prereq Bolt | US-020.BOLT-001 (v5 schemas + templates) | **Done** ✓ |
| ADRs | ADR-008, ADR-007, ADR-005, ADR-004 | accepted ✓ |
| Baseline | branch `5.0`, HEAD `97125e7` (+ BOLT-001 kit changes in the working tree) | — |

Pre-SPEC evidence gate: **all governed sources approved; BOLT-001 Done.**

---

## 4. ADR-005 sweep contract

### 4.1 Phrase family (v4 manifest description → v5)
- `hitl_approvals` → `checkpoint_approvals`
- `manifest-v4` → `manifest-v5` (and `manifest-v4*.schema.json` → `manifest-v5*.schema.json`)
- `schema_version` `"4.0"` → `"5.0"` (in prose/examples that describe the manifest)
- `Manifest Family v4` / `Manifest v4` → `v5`
- approver shape `{user, role}` → `{actor, role, model}`; add `mode` (`human|virtual`)

### 4.2 Location set (swept in full; kit only)
`devflow/avenga-devflow/Avenga-DevFlow.md` (§3.0 projection maps ~1601–1603, ~2068,
~2390; §3.12 Manifest Family ~3097–3229 incl. the example manifest ~3004; schema
refs ~2847–2849, ~3140–3163; folder map ~4080–4082; §5.15 routing ~4312, ~4380) ·
`devflow/GUARDRAILS.md` (G23 line 105, N09 159, T07 240, projection 268, refs
478–480) · the four agents `CLAUDE.md` / `SKILL.md` / `AvengaDevFlow.agent.md` /
`AvengaDevFlow.md` (G23 row, manifest-template line, the `## Manifest Family v4`
section, the append-only line, the review→approvals projection, the
`schema_version "4.0"` line) · `devflow/README.md` · `devflow/ONBOARDING.md`.

### 4.3 Substantive rewrite (not just rename)
§3.12 (and the agents' `## Manifest Family` section) must **describe the v5
record**: `checkpoint_approvals[]` replaces `hitl_approvals[]`; each entry carries
`mode` (`human`|`virtual`); each `decided_by[]` is `{actor: human:<user> |
agent:<id>, role, model}` (model null for humans, the model id for agents); the
safe default (human) records equivalently to v4. The §3.0 projection maps update
`review.reviewers → checkpoint_approvals[].decided_by` (as actors).

### 4.4 Allowlist — NOT touched by this Bolt
- **The entire §5.16 manifest-conversion section** (~lines 4590–4700: the
  `3.0`→`4.0` example, "`hitl_approvals[]` crosses unchanged", the disposition
  table's `hitl_approvals[]` row, "converted to the current `schema_version`") →
  **BOLT-003** owns the v4.0→v5.0 conversion recipe there.
- **The `HITL-*` checkpoint identifier names** → the separate rename US.
- **The root `devflow/`** (operating v4.2) → untouched (ADR-004).

> Over-editing the §5.16 conversion lines or renaming checkpoint values is a
> failure of this Bolt (AC-2/AC-4).

---

## 5. Phases

- **Phase A — §3.12 + §3.0 projection maps + schema/folder/routing refs** in
  `Avenga-DevFlow.md` (the substantive shape rewrite + the renames), excluding
  §5.16. ~1.5h.
- **Phase B — GUARDRAILS** (G23, N09, T07, projection, refs). ~0.5h.
- **Phase C — the four agents** (identical edits: G23 row, template line, the
  `## Manifest Family` section rewritten to v5, append-only, projection,
  schema_version line). ~1h.
- **Phase D — README + ONBOARDING** manifest mentions. ~0.25h.
- **Phase E — Verification (GREEN)** (§6).

---

## 6. Acceptance criteria

- **AC-1 (no stale v4 description):** the §4.1 phrase family returns **zero
  matches** across the §4.2 location set, **outside the §4.4 allowlist** (i.e.
  excluding the §5.16 conversion section and checkpoint-name values).
- **AC-2 (§5.16 untouched):** the §5.16 conversion section is unchanged by this
  Bolt (BOLT-003's territory); `git diff` shows no edits in ~lines 4590–4700.
- **AC-3 (substantive shape):** §3.12 and each agent's `## Manifest Family`
  section describe `checkpoint_approvals[]` with `mode` and the
  `{actor, role, model}` approver; the §3.0 projection maps reference
  `checkpoint_approvals[].decided_by` as actors.
- **AC-4 (checkpoint names kept):** no `HITL-*` checkpoint value renamed to
  `AITL-*` (separate US).
- **AC-5 (four-agent sync + G-count):** whole-body diff = sanctioned divergence
  only; `grep -cE '^\| G[0-9][0-9] '` equal across the four agents + GUARDRAILS
  (unchanged count).
- **AC-6 (kit-only):** `git status` shows only `distribution-kit/` files +
  governance records; root `devflow/` untouched.
- **AC-7 (manifest):** the BOLT-002 manifest gets its `v_bounces[]` entry and
  validates.

---

## 7. Testing strategy

Deterministic grep/diff (documentation change, ADR-002 class-1 style):
- **RED (before):** the §4.1 family present across §4.2 (the inventory).
- **GREEN (after):** the family returns zero matches outside the §4.4 allowlist;
  §3.12 + agents show the v5 shape (grep `checkpoint_approvals`, `mode`, `actor`);
  §5.16 diff empty; four-agent diff sanctioned-only; G-count unchanged; `git
  status` kit-only. Record commands + output in the MEM.

---

## 8. Quality gates

Documentation/internal → unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. Prompt-injection, secret-leak,
hallucination-lint (every §-ref/path resolves; the v5 schema files exist from
BOLT-001), behavioral-reproducibility (deterministic grep/diff),
bolt-manifest-validation: `pass`.

---

## 9. Security and data

Governance text only; no runtime/security boundary. Data `internal`.

---

## 10. Migration, compatibility, rollback

- Migration: none here (the §5.16 recipe is BOLT-003). Compatibility: the text
  now matches the v5 schema BOLT-001 shipped; checkpoint names unchanged so no
  downstream break. Rollback: revert the kit commit; root untouched.

---

## 11. Monitoring and observability

`n/a` — the §7 sweep is the observability; captured in the MEM.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Partial sweep (a v4 description survives) | 3 | 3 | ADR-005 sweep over the full §4.2 set; AC-1 absence assertion |
| Over-reach into §5.16 (BOLT-003's territory) | 3 | 2 | AC-2 asserts §5.16 unchanged; explicit allowlist §4.4 |
| Accidental checkpoint-value rename | 2 | 2 | AC-4 keeps `HITL-*`; the rename is a separate US |
| Four-agent drift | 2 | 3 | Identical edits; AC-5 diff + G-count |
| Root edited | 1 | 4 | Kit-only; AC-6 |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| §5.16 excluded, left to BOLT-003 | Clean boundary: BOLT-002 describes the manifest *structure*; BOLT-003 owns the *conversion recipe* |
| Substantive rewrite of §3.12 + agents' Manifest Family (not just rename) | The v5 record has new semantics (mode, actor, model) that the text must teach, not only relabel |
| Keep `HITL-*` checkpoint values | Structure vs names split; the rename is a separate US |

---

## 14. Stop conditions

- A v4 reference cannot be classified as BOLT-002 vs §5.16/BOLT-003 → stop, ask.
- Any root `devflow/` file in the diff → stop, revert, record.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress, resume.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–E · AC-1..AC-7 pass
- [ ] GREEN sweep (zero stale v4 outside allowlist; §3.12 + agents show v5 shape; §5.16 untouched; sync + G-count; root untouched)
- [ ] Follows ADR-005 (sweep) + ADR-004 (kit-only)
- [ ] MEM created · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 16. References

- US-020, US-020.BOLT-002 (approved); US-020.BOLT-001 (Done — the v5 schemas)
- ADR-004/005/007/008; §3.12 (Manifest Family), §3.0 (projection), §5.15 (routing)
- The §5.16 conversion recipe → BOLT-003 (not this Bolt)

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T16:07:33-03:00` |
| **review.started_at** | `2026-08-22T16:12:25-03:00` |
| **review.decided_at** | `2026-08-22T16:12:25-03:00` |
