---
id: "MEM-260824-1303"
title: "The per-platform lifecycle surface — the four preambles ship-model current (AC-9 complete) and the mapping made deterministic (US-025.BOLT-002, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-025.BOLT-002"
spec: "devflow/spec/SPEC-260824-1144-per-platform-lifecycle.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "848d6dc"
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-025.BOLT-002-per-platform-lifecycle.json"
diff_ref: ""
review_ready_at: "2026-08-24T13:03:22-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("aprobado! sigamos!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T14:08:13-03:00"
  decided_at: "2026-08-24T14:08:13-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the 5-file diff inspected against the approved SPEC — the four preambles verbatim per Phase A with the spawn controls preserved, AC-9 COMPLETE (zero maintenance references x4, live-swept), the shared body proven untouched by the pinned-hash comparison (cd24754c320d == reference, the reviewer-hardened gate), VERIFICATION.md carrying B.1-B.4 (the F-11 wrapper-half recorded bidirectionally; F-09 and F-13 and F-14 closed). V-Bounce 1 approved — BOLT-002 Development Completed; acceptance batched with the US-025 closure."
---

# MEM-260824-1303 — The per-platform lifecycle surface (US-025.BOLT-002, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-025.BOLT-002 (per-platform-lifecycle) |
| **SPEC**        | [SPEC-260824-1144](../spec/SPEC-260824-1144-per-platform-lifecycle.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 §3.9 (ship model), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce delivered the per-platform half of the lifecycle. The **four
platform preambles** were replaced verbatim per the approved SPEC: each now
names ITS spawn folder and wrapper format, wires the projection ("live
definitions from `devflow/agents/squad/` … per the mapping in
`devflow/agents/VERIFICATION.md`"), carries the reload notice (OpenCode's
additionally the ctrl+X / `opencode agent list` picker hint from the field
test), and **preserves its platform's spawn control** (the `Agent` tool /
`permission.task` + `task: deny` / the `agent` alias / instruction-based).
The pre-built-era text is gone (Claude's five-wrapper `Agent(…)` list;
Codex's "role agents live in `.codex/agents/*.toml`" sentence), and with
the preamble references cleaned (`ADR-007` ×4, `US-023` ×4, `DISC-002` in
Codex's), **US-025 AC-9 is COMPLETE: the four MainAgents now contain zero
maintenance-partition references** (the kit's own `US-000` and the naming
table's fictional examples stay — framework text). **VERIFICATION.md is
now deterministic**: the permission-block derivation (allowlist-only +
explicit deny-set — the field-proven `list: allow` drift would now violate
a written rule — plus the approver-class denies: the **deliberate partial
implementation of the REV-005 F-11 v2 spec**, wrapper-mapping half, so the
future hardening US implements only the schema half); the `model: inherit`
rule (**field omission** at projection — each platform's native
inheritance; this **closes REV-005 F-09**, resolved not pending) with the
pin-a-distinct-model guidance for reviewer-class agents; the OpenCode
picker/registration notes (**closing F-13**); and two internal consistency
touches (the install bullet now names `squad/` as the live source; the
Claude section drops the id-list allowlist wording). Verification is GREEN
on every gate, including the reviewer-hardened one: the shared lifecycle
body re-extracted with the **pinned convention** equals the BOLT-001
reference hash (`cd24754c320d…`) on all four files — untouched by
construction and proven by comparison.

## 2. Implemented phases

### Phase A — The four preambles

Old paragraphs asserted unique per file, then replaced with the approved
verbatim texts (the common checklist with platform values). Spawn controls
preserved; maintenance references and stale era-text removed.

### Phase B — VERIFICATION.md

B.1 the permission-block derivation (+ the approver-class deny clause —
F-11's wrapper half, deliberate and recorded); B.2 the `inherit` omission
rule + the model-diversity guidance (F-09 closed); B.3 the OpenCode picker
behavior note (F-13 closed); B.4 the `squad/`-as-source install bullet and
the Claude allowlist wording.

### Phase C — Verification (GREEN)

Shared-body hash ×4 == `cd24754c320d…` (the pinned convention — AC-3);
the preamble checklist PASS ×4 (folder + squad/ + mapping + reload);
maintenance references **ZERO ×4** (AC-9 complete); stale-text sweep
CLEAN; VERIFICATION.md carries B.1–B.4; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` | The Claude preamble → ship-model current (folder, format, wiring, reload; refs + stale list removed) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | The OpenCode preamble → idem + the picker hint (ctrl+X / agent list, not Tab) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | The Copilot preamble → idem |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | The Codex preamble → idem (the stale `.codex/agents/*.toml` role-agents sentence replaced; `DISC-002` ref removed) |
| `distribution-kit/devflow/agents/VERIFICATION.md` | B.1 permission derivation (+ approver-class denies) · B.2 `inherit` = field omission + model-diversity guidance · B.3 OpenCode notes · B.4 squad-as-source + Claude wording |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The hash gate compared against the BOLT-001 reference with the pinned §8 convention | The reviewer's finding: extraction boundaries differ legitimately — the gate is only meaningful like-with-like; the reviewer independently reproduced the reference value pre-approval |
| B.1's approver-class denies kept (the approver's decision at SPEC review) | Closes the field-proven `bash`-retention gap at projection level now; recorded bidirectionally (SPEC §14 + this §13) so the ADR-014 v2 backlog keeps only the schema half |
| `inherit` = omit the field, never write a resolved id | A written id freezes one session's model into the wrapper; omission delegates to platform-native inheritance — deterministic, portable, self-updating |

## 8. Deviations and assumptions

No deviations from SPEC-260824-1144 rev 1. No assumptions — every anchor
asserted on disk before editing.

## 9. Verification evidence

```
AC-3 shared-body hash x4:  cd24754c320df93c85339aadcddb1803 == reference (UNCHANGED)
AC-1 preamble checklist:   PASS x4 (folder · squad/ · VERIFICATION.md · reload)
AC-9 maintenance refs:     ZERO x4 — COMPLETE (US-000 + naming examples stay, framework)
Stale-text sweep:          CLEAN (no wrapper list; no codex role-agents sentence)
VERIFICATION.md:           B.1-B.4 present (byte-comparable · omits the model field ·
                           Tab picker · squad/ as source · pin a distinct model)
Encoding:                  no BOM
```

### Gates

Documentation Bolt: unit/integration/perf `n/a` (per the approved SPEC
§9); prompt-injection `pass`; secret-leak `pass`; hallucination-lint
`pass` (paths resolve); behavioral-reproducibility `pass` (the script +
checks re-run identically); bolt-manifest-validation `pass` (v_bounces[1]
appended, schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** working tree over baseline `848d6dc` (uncommitted —
  presented for review)
- **Commit:** baseline `848d6dc`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-025.BOLT-002-per-platform-lifecycle.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~12min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation; scripted evidence per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] **REV-005 routing progress:** F-09 (inherit) **closed** here; F-13
      (OpenCode notes) **closed** here; F-14 (permission spec) **closed**
      here; **F-11's v2 spec is now HALF-implemented** — the
      wrapper-mapping half lives in VERIFICATION.md B.1 (this Bolt); the
      **ADR-014 v2 backlog keeps only the schema half** (the `allOf`
      ceiling + the enablement checklist) — the future hardening US must
      not re-implement the wrapper half.
- [ ] BOLT-003 (delete-safe depth) · BOLT-005 (kit G07 scoping — F-02) ·
      BOLT-004 (the pilot).
- [ ] AITL-BOLT-DONE-Approval for BOLT-001 and BOLT-002 (batched with the
      US-025 closure).

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T13:03:22-03:00` |
| **review.started_at** | `2026-08-24T14:08:13-03:00` |
| **review.decided_at** | `2026-08-24T14:08:13-03:00` |
| **Review evidence** | the 5-file diff (4 preambles + VERIFICATION.md); the pinned-hash comparison; the AC-9 zero sweep; the stale-text sweep; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
