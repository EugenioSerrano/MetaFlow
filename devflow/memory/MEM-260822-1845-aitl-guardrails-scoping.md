---
id: "MEM-260822-1845"
title: "AITL guardrails scoping — G05/G18/G24 (count 39 unchanged) (US-021.BOLT-002)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-021.BOLT-002"
spec: "SPEC-260822-1839"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-021.BOLT-002-aitl-guardrails-scoping.json"
diff_ref: ""
review_ready_at: "2026-08-22T18:45:40-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T18:47:27-03:00"
  decided_at: "2026-08-22T18:47:27-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the GUARDRAILS + 4 agents diff (only G05/G18/G24), the rule-count invariant (39x5, no rule added/removed/renumbered), four-agent row sync, §3.0 G37/handoff intact, kit-only. G18/G24 scoped per ADR-008 §3.4 without dissolving the guarantee. V-Bounce GREEN."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records stay 4.2 (HITL-*, schema 4.0).
-->

# MEM-260822-1845 — AITL guardrails scoping (US-021.BOLT-002)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-021.BOLT-002](../functional/bolts/US-021.BOLT-002-aitl-guardrails-scoping.md) |
| **SPEC**        | [SPEC-260822-1839](../spec/SPEC-260822-1839-aitl-guardrails-scoping.md) revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (§3.1 G05, §3.4 G18/G24), ADR-005 (boundary), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce scoped the three identity/naming guardrails for AITL — the second of
US-021's four Bolts — so the guardrails now enforce the precept BOLT-001 stated.
**G05** was evolved so the canonical checkpoint vocabulary is `AITL-<CODE>-Approval`
and `HITL-*` joins `H1–H6` as a legacy prefix (preserved only in migrated history,
G36). **G18** and **G24** were scoped per ADR-008 §3.4 from "the AI never approves"
to "the AI never approves **unless** an explicit valid virtual-approver
configuration exists **and** the independence rule holds (approver actor ≠ executor
actor)", keeping the safe default (absent/invalid config → human-only) and the hard
guarantee that the record **never fabricates a human** (a virtual approval is
`agent:<id>`/`model:<id>`). The §3.0 exclusion of G37 + the handoff from any
no-holder fallback (already present from US-014) was referenced, not duplicated.
The change was applied to `GUARDRAILS.md` (full text) and the four platform agents'
compressed guardrail table (byte-identical). The outcome is GREEN: the
**blocking-rule count is exactly 39** (distinct G-numbers, in GUARDRAILS and 39×5
across the agents — no rule added, removed or renumbered), the diff touched **only
the G05/G18/G24 rows**, and the change is kit-only (root untouched). No guarantee
was dissolved — the scoping narrows *when* an AI may approve and never lets an
executor approve its own work or the record name a human that did not sign.

---

## 2. Implemented phases

### Phase A — GUARDRAILS.md
Rewrote the full text of **G05** (canonical `AITL-*`, `HITL-*` legacy with H1–H6,
G36 history), **G18** (never approve own work; AI approval only under explicit valid
config with independence; absent/invalid → human-only; record never fabricates a
human — `agent:<id>`/`model:<id>`) and **G24** (no delegation to an AI approver
without explicit valid config/independence; no fabricated decision; a configured
independent AI approver is the permitted AITL path).

### Phase B — the four agents
Applied the matching **compressed G05/G18/G24 rows** to `CLAUDE.md`, `SKILL.md`,
`AvengaDevFlow.agent.md`, `AvengaDevFlow.md` — **byte-identical** across the four.

---

## 3. Files created / 5. Files renamed / 6. Files deleted

_(none)_

---

## 4. Files modified

| File | Change |
|------|--------|
| `distribution-kit/devflow/GUARDRAILS.md` | G05/G18/G24 full text scoped for AITL (§3.1/§3.4); count 39 unchanged |
| `distribution-kit/CLAUDE.md` | Compressed G05/G18/G24 rows scoped (byte-synced) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same (byte-synced) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same (byte-synced) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same (byte-synced) |
| `devflow/spec/SPEC-260822-1839*`, `metrics/bolts/US-021.BOLT-002*.json`, this MEM | Governance records (root, 4.2) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| BOLT-002 fully owns G05/G18/G24 text (tokens included) | Their `AITL-*`/`HITL-*` tokens *are* the semantic; BOLT-004's sweep allowlists these three rules |
| Follow ADR-008 §3.4 verbatim | G18/G24 must be scoped, never dissolved — the record never fabricates a human; the executor never approves its own work; safe default human-only |
| Reference §3.0's G37/handoff exclusion, not duplicate it | It already exists (US-014); duplication risks drift |
| Keep `HITL-*` as a named legacy prefix in G05 | ADR-008 §3.1 — migrated history keeps `HITL-*` (G36) |

---

## 8. Deviations and assumptions

- **Intentional mixed state:** G05 now declares `AITL-*` canonical, while ~1,119
  `HITL-<CODE>-Approval` identifiers still exist elsewhere — both close in
  **BOLT-004** (which allowlists G05/G18/G24). By design; each Bolt independently
  demonstrable.
- **Assumption:** enforcement of the safe-default/independence rules (the
  Coordinator, validators) is later US/Bolt work; this Bolt states the rules.
- No SPEC revision needed this V-Bounce (rev 1 executed clean).

---

## 9. Verification evidence

### Build / Tests
```
n/a — guardrails/documentation Bolt.
```

### Rule-count invariant (AC-5) + boundary (AC-6)
```
distinct G-numbers: GUARDRAILS.md 39 · CLAUDE 39 · SKILL 39 · AvengaDevFlow.agent 39 · AvengaDevFlow 39  (39×5, unchanged)
GUARDRAILS.md rule rows changed (git diff, line-initial | G## |): ONLY G05, G18, G24  (+/- pairs; no other rule; the "G36" in the diff is a reference inside G05's text, not a changed rule)
```

### Four-agent sync (AC-5)
```
G05 row: 1 unique across the four
G18 row: 1 unique across the four
G24 row: 1 unique across the four
```

### G37/handoff (AC-4) + kit-only (AC-7)
```
§3.0 identity-separation exclusion (handoff + G37 from no-holder fallback, from US-014): unchanged, referenced by scoped G18/G24.
git status: only distribution-kit/ (GUARDRAILS + 4 agents) + root governance records; root framework untouched.
```

### Gates
- unit/integration, SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first: **n/a** (guardrails/internal).
- hallucination-lint, behavioral-reproducibility, bolt-manifest-validation: **pass**.

### BUG V-Bounce evidence
n/a.

---

## 10. Manual interventions

None. All edits agent-generated; the human role was HITL-SPEC-Approval.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; 5.0 branch).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-021.BOLT-002-aitl-guardrails-scoping.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1h (three guardrails, GUARDRAILS + 4 agents) |
| V-Bounce number | 1 |
| Tests created | rule-count invariant (39×5) + boundary (only G05/G18/G24) + sync checks |
| AI-generated code | 100% (docs); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] **US-021.BOLT-003** — schema enum accepts `AITL-*` (SPEC/MEM conditionals both prefixes; keep `HITL-*`).
- [ ] **US-021.BOLT-004** — comprehensive kit-wide sweep: `HITL` adjective + `HITL-<CODE>-Approval` identifiers → AITL (allowlisting G05/G18/G24 already scoped here, and the §5.16 migration source).
- [ ] On all four Done → US-021 delivered (kit fully AITL).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent with no mutable status,
> **never self-approved**. The executing Dev-validator inspects the diff, the
> rule-count/boundary evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`. `approved`
> completes the V-Bounce and (latest MEM) marks the Bolt `Development Completed`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T18:45:40-03:00` |
| **review.started_at** | `2026-08-22T18:47:27-03:00` |
| **review.decided_at** | `2026-08-22T18:47:27-03:00` |
| **Review evidence** | GUARDRAILS + 4 agents diff (only G05/G18/G24), rule-count 39×5, four-agent row sync, §3.0 G37/handoff intact, kit-only, manifest |
| **Comments** | Approved; guardrail layer of HITL→AITL done |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN |
