---
id: "MEM-260822-1617"
title: "Align the methodology text + four agents to the v5 manifest — US-020.BOLT-002"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-020.BOLT-002"
spec: "SPEC-260822-1607"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-020.BOLT-002-manifest-text-and-agents.json"
diff_ref: ""
review_ready_at: "2026-08-22T16:17:48-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T16:20:16-03:00"
  decided_at: "2026-08-22T16:20:16-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the 8-file kit diff and the §9 sweep: zero stale v4 manifest-description outside the conversion allowlist, §5.16/upgrade recipe preserved for BOLT-003, §3.12 + the four agents describe the v5 shape (mode + actor+model), no HITL->AITL leak, four agents byte-synced (identical entry bullet) with G-count 39x5, kit-only. Bolt now Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Documentation V-Bounce (ADR-002 class-1 style) → evidence is deterministic
  grep/diff. Kit-only (ADR-004); root framework untouched.
-->

# MEM-260822-1617 — Align the methodology text + four agents to the v5 manifest (US-020.BOLT-002)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-020.BOLT-002](../functional/bolts/US-020.BOLT-002-manifest-text-and-agents.md) |
| **SPEC**        | [SPEC-260822-1607](../spec/SPEC-260822-1607-manifest-text-and-agents-v5.md) — revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008/007 (v5 shape), ADR-005 (sweep), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce brings every place in the kit that **describes** the manifest into
agreement with the v5 schema BOLT-001 shipped, closing the self-contradiction the
ADR-005 discipline guards against. Two kinds of edit were applied: a
**mechanical phrase-family rename** (`hitl_approvals`→`checkpoint_approvals`,
`manifest-v4`→`manifest-v5`, `schema_version "4.0"`→`"5.0"`, "Manifest Family
v4"→"v5") done with a deterministic Python pass that **skipped the conversion
sections** (§5.16 in the methodology and the "Methodology Upgrade Protocol" in
each agent — those belong to BOLT-003), and a **substantive shape rewrite** of
§3.12, the §3.0/GUARDRAILS projection maps and the four agents' "Manifest Family"
section to teach the new record: `checkpoint_approvals[]` with `mode`
(`human`|`virtual`) and a `{actor, role, model}` approver (model null for humans,
the model id for agents). The checkpoint identifier names were deliberately left
`HITL-*` (the HITL→AITL rename is a separate US; the field name is already
neutral). Outcome: zero stale v4 manifest-description survives outside the
conversion allowlist; the §5.16 conversion recipe is preserved intact for
BOLT-003; §3.12 and all four agents describe the v5 shape; the four agents stay
byte-synced (the new entry bullet is identical across all four) with the G-rule
count unchanged at 39×5; and no `AITL-*` leaked into the kit. Kit-only (ADR-004):
the root `devflow/` framework is untouched.

---

## 2. Implemented phases

### Phase A — Methodology (`Avenga-DevFlow.md`), excluding §5.16
Mechanical renames across §3.12, the §3.0 projection map, the schema-file
references, the folder map and the §5.15 routing table (22 lines). Substantive
rewrite of §3.12's approval-record description (added `mode` + the
`{actor, role, model}` approver) and of the §3.0 projection map (reviewers
projected as actors). The §5.16 conversion section (lines ~4439–4702) was left
untouched — BOLT-003's territory.

### Phase B — GUARDRAILS
Renames on G23, N09, T07 and the manifest references (8 lines); substantive note
on the manifest-projection line (decided_by as actors + mode).

### Phase C — The four agents (identical edits)
Mechanical renames (5 lines each) and the rewritten `## Manifest Family v5`
section, plus a new **`checkpoint_approvals[]` entry** bullet describing
`mode`/`actor`/`model` — byte-identical across `CLAUDE.md`, `SKILL.md`,
`AvengaDevFlow.agent.md`, `AvengaDevFlow.md`. Each agent's "Methodology Upgrade
Protocol" section (the conversion recipe) was skipped (BOLT-003).

### Phase D — README + ONBOARDING
Manifest-reference renames (README 5 lines, ONBOARDING 3 lines).

### Phase E — Verification (GREEN)
Phrase-family sweep, §5.16-preserved check, v5-shape presence, four-agent sync,
G-count, kit-only (§9).

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260822-1617-manifest-text-and-agents-v5.md` | This MEM |

---

## 4. Files modified (kit)

| File | Change |
|------|--------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.12 shape rewrite + §3.0 projection map + mechanical renames (§5.16 skipped) |
| `distribution-kit/devflow/GUARDRAILS.md` | G23/N09/T07 + manifest refs renamed; projection note (actors/mode) |
| `distribution-kit/CLAUDE.md` | `## Manifest Family v5` + new entry bullet + renames (upgrade §skipped) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/devflow/README.md` | Manifest references → v5 |
| `distribution-kit/devflow/ONBOARDING.md` | Manifest references → v5 |

> The working tree also carries BOLT-001's completion records (its MEM, Bolt doc,
> INDEX, and the v5 schema/template files) — pending the same US-020 commit; not
> a BOLT-002 change.

---

## 5. Files renamed / 6. Files deleted

None / none (the v4 schema files were removed by BOLT-001, not here).

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Mechanical renames via a section-skipping Python pass | Precision + speed across ~8 files; the skip ranges keep the §5.16/upgrade conversion recipe intact (BOLT-003) |
| Substantive rewrite (not just rename) of §3.12 + agents + projection maps | The v5 record has new semantics (mode, actor, model) that the text must teach, not only relabel |
| Kept the `HITL-*` checkpoint identifier names | The HITL→AITL rename is a separate US; `checkpoint_approvals` is already a neutral field name |
| Left §5.16 / the agents' Upgrade Protocol untouched | Clean boundary — the v4.0→v5.0 conversion recipe is BOLT-003 |

---

## 8. Deviations and assumptions

No deviations from the approved SPEC. All §4.2 locations swept; the §4.4 allowlist
(the conversion sections + checkpoint names) preserved.

**Note:** two agent files reported "modified on disk since last read" during the
substantive edits — that was this V-Bounce's own earlier Python rename pass, not a
concurrent writer; the anchor-based Edits applied cleanly and the four agents
remain byte-synced (verified §9).

---

## 9. Verification evidence

Documentation V-Bounce — deterministic grep/diff.

### RED (before)
The BOLT-002 inventory: the v4 manifest-description phrase family present across
the location set (§3.12, projection maps, schema refs, G23/N09/T07, the four
agents' Manifest Family, README/ONBOARDING).

### GREEN (after)
```
AC-1 stale v4 outside the conversion allowlist: 0
AC-2 §5.16 / upgrade sections still carry the conversion recipe: hitl_approvals present
     (Avenga-DevFlow.md ×2, each agent ×1) — preserved for BOLT-003
AC-3 v5 shape: §3.12 actor+mode addition present (1); the four agents' new
     checkpoint_approvals[] entry bullet present (1 each)
AC-4 no HITL->AITL leak: zero AITL- references in the kit (checkpoint names stay HITL-*)
AC-5 four-agent sync: the new entry bullet is byte-identical across the four
     (1 distinct version); G-count 39 · 39 · 39 · 39 · 39 (GUARDRAILS + 4 agents)
AC-6 kit-only: only distribution-kit/ + governance records changed; root framework untouched
```

### Gates
Documentation/internal → unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. Prompt-injection, secret-leak,
hallucination-lint (refs resolve; the v5 schemas exist from BOLT-001),
behavioral-reproducibility (deterministic sweep), bolt-manifest-validation: `pass`.

---

## 10. Manual interventions

None — mechanical renames (Python) + anchor-based Edits, all agent-generated.

---

## 11. Evidence links

- **Diff / PR:** uncommitted working tree at MEM time (kit + governance; includes BOLT-001's pending records)
- **Commit:** baseline `97125e7`; this V-Bounce's commit pending user request
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-020.BOLT-002-manifest-text-and-agents.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15 min |
| V-Bounce number | 1 |
| Tests created | 0 automated; deterministic grep/diff sweep (RED→GREEN) |
| AI-generated code | 100% |
| First-pass approval | pending |

---

## 13. Pending items and stubs

- [ ] **BOLT-003** — document the v4.0→v5.0 conversion in §5.16 (the recipe this Bolt deliberately preserved).
- [ ] **US-012 (validator tool)** — align the compiled validator to v5 (separate US).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, never self-approved. The
> executing Dev-validator inspects the diff and the §9 sweep. Risk medium → one approver.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator (risk medium → 1 approver) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T16:17:48-03:00` |
| **review.started_at** | `2026-08-22T16:20:16-03:00` |
| **review.decided_at** | `2026-08-22T16:20:16-03:00` |
| **Review evidence** | diff (8 kit files) + §9 GREEN/RED sweep + four-agent sync + manifest |
| **Findings** | none — `acknowledged_without_comment: true` |
