---
id: "SPEC-260823-1600"
title: "DevFlow Agent contract and producer-first charters — the devflow/agents/ family: agent.yaml contract, the shipped Coordinator and the five role charter templates"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-023"
bolt: "US-023.BOLT-001" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
prerequisites: [] # Prior SPECs this one depends on
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T16:00:00-03:00"
review: # AITL-SPEC-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobado x4") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T16:09:00-03:00"
  decided_at: "2026-08-23T16:10:15-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (agents/ family — contract, Coordinator, five producer-first charters with the approver ceiling T0/T1 + MCP allowlist default, AC-7/8 closed end-to-end per the review); grounded, feasible, testable. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-023 approved ✓;
  ADR-007/008/010 accepted ✓; DISC-002 approved ✓; US-022 active ✓;
  0 open OQs (G35).
-->

# SPEC-260823-1600 — DevFlow Agent contract and charters (US-023.BOLT-001)

| Field | Value |
|-------|-------|
| **Origin** | [US-023](../functional/user-stories/US-023-devflow-agent-definition-and-deployment.md) (approved) |
| **Bolt** | [US-023.BOLT-001](../functional/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.md) (approved) |
| **ADRs** | ADR-007 (identity), ADR-008 (precept + separation of duties + approver ceiling), ADR-010 (grammar) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Create the kit's `distribution-kit/devflow/agents/` family (G30-sanctioned
by US-023): the **canonical definition contract** (`agent.yaml` — the
fields of DISC-002 §5.1 with `executor` as the first-class default mode),
the shipped **Coordinator** (definition + charter — routes, delegates
production, spawns, records, **never signs**), and the **five role charter
templates** (functional-analyst, architect, developer, qa, reviewer) —
each **enumerating its role's productive outputs** (FA→US, architect→ADR,
developer→SPEC+code, QA→TC/tests), emphasizing `modes: [executor]`, and
**encoding the approver capability ceiling (T0/T1) and the
`mcp_servers: []` default allowlist** — the security rules of AC-7/AC-8.

**Why:** this is where "DevFlow Agents are true actors" becomes operative —
the charters define what each agent PRODUCES (US-022 producer+approver
reframe), and the contract's structured fields carry the authority and the
security constraints. **If not done:** the generator (BOLT-002), the
deployment (BOLT-003) and the smoke (BOLT-004) have no canonical input, and
the approver ceiling + MCP allowlist have no home.

---

## 2. Context

US-023 (approved, 8 SP) defines the agent as a governed identity with a
role charter that states what it produces; ADR-007 fixes the identity model
(authority in structured fields — `modes`/`approves`/`capabilities`), the
Coordinator's existence and the never-signs separation of duties (ADR-008);
DISC-002 §5.1 specifies the contract fields and §5.5 the product split.
The role→outputs mapping already exists canonically in the §3.0.1 of the
methodology (US-022 delivered) — the templates enumerate it per role. This
is documentation, kit-only (ADR-004).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-023.BOLT-001-devflow-agent-contract-and-charters.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-023-devflow-agent-definition-and-deployment.md | AITL-US-Approval ✓ (2026-08-23, 8 SP) |
| ADRs | ADR-007, ADR-008, ADR-010 | accepted ✓ |
| DISC evidence | DISC-002 (contract §5.1, product split §5.5) | approved ✓ |
| Prior work | US-022 (delivered — the Actor concept + §3.0.1 mapping), US-016 (approved) | delivered/approved ✓ |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; no active-ADR
conflict; 0 open OQs (G35).

---

## 4. Scope

### In scope (kit, documentation only)

- `distribution-kit/devflow/agents/coordinator/` — the Coordinator's
  `agent.yaml` + `charter.md` (never signs).
- `distribution-kit/devflow/agents/roles/<role>/` — five charter templates
  (`functional-analyst`, `architect`, `developer`, `qa`, `reviewer`):
  `agent.yaml` + `prompt.md` (charter body) per role.
- `distribution-kit/devflow/agents/README.md` — the family's explanatory
  README (disambiguation vs `actors/`, the contract at a glance).

### Out of scope

- The wrapper generator + parity check (BOLT-002); the deployed wrappers
  (BOLT-003); the smoke test (BOLT-004); the roster schema/contents
  (US-024); the root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- US-022 delivered (the Actor concept + §3.0.1 mapping the templates
  enumerate); US-016 approved (audit tool — used by BOLT-002, not here).
- Baseline commit `45d553f`; kit at version 5.1.
- No prior SPEC prerequisite (first of US-023).

---

## 6. Phases

### Phase A — The contract and the Coordinator

**Duration:** ~1.5h total cycle — **Complexity:** Low

#### A.1 The canonical `agent.yaml` contract

Create `distribution-kit/devflow/agents/roles/<id>/agent.yaml` as the
canonical shape (per DISC-002 §5.1): `id` (kebab-case), `role`,
`description` (when the Coordinator should delegate), `model` (declared,
constrained to the platform catalog), `modes` (`executor` first-class
default; `approver` configured), `approves` (checkpoint classes; empty =
executor-only), `capabilities` (tier T0–T3, least-privilege `tools`
allowlist, `mcp_servers` named + allowlisted, `[]` default), `escalation`,
`write_paths` (G30/G31 mirror). The template body documents each field —
**no implementation decisions invented** (the fields are fixed by ADR-007
and DISC-002 §5.1).

**Files created:**
- `distribution-kit/devflow/agents/roles/README.md` (contract reference) —
  the canonical field list + the producer-first rule (executor default,
  charter = WHAT I PRODUCE)

#### A.2 The Coordinator

Create `distribution-kit/devflow/agents/coordinator/agent.yaml` +
`charter.md`: the one shipped DevFlow Agent — resolves the roster, delegates
production to role agents (executor mode), spawns approver agents for
enabled checkpoints, enforces the escalation floor, records evidence —
and **never signs** (ADR-008 separation of duties; `approves: []`).

**Files created:**
- `distribution-kit/devflow/agents/coordinator/agent.yaml`
- `distribution-kit/devflow/agents/coordinator/charter.md`

### Phase B — The five producer-first charter templates

**Duration:** ~2h total cycle — **Complexity:** Low

#### B.1 Templates per role

For each of the five roles, create `agent.yaml` (role-specific: model
suggestion, `modes: [executor]`, `approves` per role policy — FA may
approve US, etc., `capabilities` tier, `mcp_servers: []` default) +
`prompt.md` (the charter body: who I am, **WHAT I PRODUCE** — the role's
outputs enumerated: functional-analyst → US, architect → ADR, developer →
SPEC + code, QA → TC/tests — what I check, how I decide, when I escalate,
what I may never do). **Each template encodes the approver capability
ceiling** (approver-mode agents run T0/T1, no write paths, no
transactional MCPs — AC-7) and the **MCP allowlist default** (`mcp_servers:
[]`, named + allowlisted — AC-8).

**Files created:**
- `distribution-kit/devflow/agents/roles/functional-analyst/{agent.yaml,prompt.md}`
- `distribution-kit/devflow/agents/roles/architect/{agent.yaml,prompt.md}`
- `distribution-kit/devflow/agents/roles/developer/{agent.yaml,prompt.md}`
- `distribution-kit/devflow/agents/roles/qa/{agent.yaml,prompt.md}`
- `distribution-kit/devflow/agents/roles/reviewer/{agent.yaml,prompt.md}`

#### B.2 The family README

Create `distribution-kit/devflow/agents/README.md`: what the family is
(canonical definitions — single source; the `actors/` folder is the team
map, US-024), the contract at a glance, the Coordinator-never-signs note,
and the "templates are copied by adopters, never edited in place" rule.

**Files created:**
- `distribution-kit/devflow/agents/README.md`

### Phase C — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 Evidence collection

Run: (a) the folder tree exists with all files; (b) each charter template
enumerates its role's productive outputs; (c) the templates encode the
approver ceiling (T0/T1, no write paths, no transactional MCPs) and the
`mcp_servers: []` default; (d) the Coordinator's `approves: []` (never
signs); (e) `git status` kit-only; (f) encoding clean (no BOM/mojibake).

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The agents/ family exists, producer-first

**Given** the kit's `devflow/agents/` folder,
**When** a maintainer inspects it,
**Then** it contains `coordinator/`, `roles/` with the five charter
templates and a README; each template enumerates its role's productive
outputs and emphasizes `modes: [executor]` (US-023 AC-1).

### AC-2: The contract is canonical

**Given** a DevFlow Agent definition,
**When** its `agent.yaml` is inspected,
**Then** it carries the DISC-002 §5.1 fields with `executor` (production)
as the first-class default and the charter body stating WHAT I PRODUCE
(US-023 AC-2).

### AC-3: Structured authority

**Given** the identity model,
**When** authority is expressed,
**Then** it lives in structured fields; the productive mandate is the
charter (US-023 AC-4).

### AC-4: The Coordinator never signs

**Given** the Coordinator,
**When** the kit ships it,
**Then** it delegates production, spawns, records — and never signs
(`approves: []`) (US-023 AC-5).

### AC-5: Approver ceiling encoded

**Given** capability tiers,
**When** an agent acts as approver,
**Then** its template runs at T0 (at most T1 pinned), no write paths, no
transactional MCPs — encoded in the templates/fields this Bolt delivers
(US-023 AC-7).

### AC-6: MCP allowlist default

**Given** MCP access,
**When** an agent declares MCP servers,
**Then** each server is named and allowlisted (`mcp_servers: []` default) —
encoded in the contract and templates (US-023 AC-8).

### AC-7: Kit-only

**Given** the diff,
**When** the Bolt lands,
**Then** only `distribution-kit/` changes (US-023 AC-11).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-023 AC-1 | folder tree + charters enumerate outputs + modes:[executor] | AC-1 presence checks |
| US-023 AC-2 | canonical agent.yaml fields | AC-2 field-by-field check |
| US-023 AC-4 | structured authority | AC-3 |
| US-023 AC-5 | Coordinator never signs | AC-4 (`approves: []`) |
| US-023 AC-7 | approver ceiling in templates | AC-5 spot check |
| US-023 AC-8 | MCP allowlist default | AC-6 spot check |
| US-023 AC-11 | kit-only | AC-7 git status |

---

## 8. Testing strategy

Deterministic (documentation):

- **RED (before):** no `agents/` folder; no contract/Coordinator/templates.
- **GREEN (after):** AC-1..AC-7 — folder tree, per-role output
  enumeration, ceiling + MCP default encoded, Coordinator never signs,
  kit-only.
- **Edge cases:** a charter template must never carry authority prose
  (structured fields only — ADR-007); the templates are skeletons with
  placeholders, never project-specific content.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation-only, no runtime |
| SAST / SBOM | — | n/a — no dependencies, no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface; the templates state the safe-default + approver ceiling (they do not implement enforcement) |
| Secret-leak scan | — | pass — no secrets in documentation |
| Hallucination lint | refs resolve | pass — DISC-002/ADR references verified |
| IP / license provenance | — | n/a — no third-party code |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation; RED/GREEN presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass — same checks reproduce identically |
| Bolt-manifest validation | validates | pass — BOLT-001 manifest + spec_revisions[] |

---

## 10. Security and data

The templates **encode** the approver capability ceiling (T0/T1 — the
injection-forged-approval defense) and the MCP allowlist default as
structured fields; enforcement at runtime is the platform wrappers
(BOLT-003) and the Coordinator. Data classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** new kit folder; additive.
- **Compatibility:** no impact on adopters (new paths only; the four main
  agent files untouched).
- **Rollback:** delete `distribution-kit/devflow/agents/`; root untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Charter prose drifts into authority | 2 | 4 | AC-3/ADR-007 structured-fields rule + spot checks |
| Templates not producer-first | 2 | 3 | AC-1 enumeration requirement |
| Ceiling/MCP rules omitted | 2 | 4 | AC-5/AC-6 spot checks (the review-driven coverage) |
| Coordinator charters signs-by-prose | 1 | 5 | AC-4 `approves: []` + separation of duties (ADR-008) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The productive mandate lives in the charter body + per-role enumeration, not as a `produces` field in agent.yaml | Reconciled with US-024 (option a): the role → artifacts mapping is one source (the templates + §3.0.1); the roster derives from `role` |
| Approver ceiling + MCP allowlist encoded in the templates this Bolt delivers | AC-7/AC-8 claimed here (review finding) — the security rules of the contract need a home that builds them |
| Templates are skeletons (placeholders) | Adopters instantiate, never edit in place (DISC-002 §5.5) |

---

## 14. Stop conditions

- Any file outside `distribution-kit/` in the diff → stop, revert (ADR-004).
- A charter template carries authority prose → stop, fix (ADR-007).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-7 pass
- [ ] GREEN evidence (tree, enumeration, ceiling + MCP default, never-signs, kit-only)
- [ ] ADR-007/008/010 followed
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-023 (approved), US-023.BOLT-001 (approved)
- DISC-002 §5.1 (contract), §5.5 (product split); ADR-007 (identity),
  ADR-008 (precept + separation of duties), ADR-010 (grammar)
- US-022 (delivered — the Actor concept + §3.0.1 mapping)
- Example: SPEC-260823-1335 (US-022.BOLT-001 — same documentation pattern)

---

## 17. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Revision 1 — initial |

---

## 18. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval authorizes SPEC
> preparation; **SPEC approval authorizes the V-Bounce**. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator + applicable domain owner(s) |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T16:00:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
