---
id: "SPEC-260823-1602"
title: "Wrapper deployment — generate and commit the per-platform wrappers with per-platform verification notes (Claude full coverage; Codex/Copilot re-verified with documented fallbacks)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-023"
bolt: "US-023.BOLT-003" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md" # the canonical definitions being deployed
  - "devflow/spec/SPEC-260823-1601-wrapper-generator-and-parity.md" # the generator producing the wrappers
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T16:02:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (generated + committed wrappers with the spawn-topology allowlists — AC-6 enforcement — and the per-platform verification notes, Codex/Copilot re-verified); grounded, feasible, testable (parity over the committed set). Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-023 approved ✓;
  DISC-002 approved ✓; ADR-004 accepted ✓; 0 open OQs.
-->

# SPEC-260823-1602 — Wrapper deployment and per-platform verification (US-023.BOLT-003)

| Field | Value |
|-------|-------|
| **Origin** | [US-023](../functional/user-stories/US-023-devflow-agent-definition-and-deployment.md) (approved) |
| **Bolt** | [US-023.BOLT-003](../functional/bolts/US-023.BOLT-003-wrapper-deployment.md) (approved) |
| **ADRs** | ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Deploy the per-platform wrappers for the canonical DevFlow Agents: run the
BOLT-002 generator and **commit its output** into the kit's platform agent
folders — `.claude/agents/*.md` (Claude Code), `.opencode/agents/*.md`
(OpenCode), `.github/agents/*.agent.md` (GitHub Copilot),
`.codex/agents/*.toml` (Codex) — plus **per-platform verification notes**:
Claude Code receives full native coverage; Codex (open invocation issues
#14579/#15250) and Copilot (env-dependent `model`/`mcp-servers`) are
**re-verified against current docs** at implementation and use documented
fallbacks (DISC-002 rec #6, §7 #1). The committed wrappers also **set the
spawn allowlists** that enforce the spawn topology — approver agents
spawnable only by the Coordinator (US-023 AC-6).

**Why:** adopters copy the kit wholesale — the wrappers must ship
pre-built (no adoption-time build), honest about each platform's current
capabilities. **If not done:** the canonical definitions exist but no
platform can spawn a role agent.

---

## 2. Context

US-023 AC-9/AC-10/AC-6: generated + committed wrappers with a passing N×4
parity, per-platform verification notes, and the spawn-topology allowlists.
DISC-002 §4.2 documents the four contracts (re-verify at implementation),
§5.6 the Claude-pilot rationale, rec #6 the Codex/Copilot re-verification.
The kit's platform folders today hold only the four main agent files —
the role wrappers land alongside them (`.claude/agents/` and `.codex/`
are new folders; G30-sanctioned by US-023).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-023.BOLT-003-wrapper-deployment.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-023-devflow-agent-definition-and-deployment.md | AITL-US-Approval ✓ (2026-08-23, 8 SP) |
| DISC evidence | DISC-002 (§4.2 matrix, §5.6 pilot, rec #6) | approved ✓ |
| ADR | ADR-004 (kit-only) | accepted ✓ |
| Prior SPECs | SPEC-260823-1600 (definitions), SPEC-260823-1601 (generator) | prerequisites |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; 0 open OQs.

---

## 4. Scope

### In scope (kit deployment)

- The generated wrapper files committed under `.claude/agents/`,
  `.opencode/agents/`, `.github/agents/`, `.codex/agents/` (per role +
  the Coordinator wrapper where the platform models it).
- The per-platform verification notes (recorded in
  `devflow/agents/VERIFICATION.md` or the family README): Claude full
  coverage; Codex/Copilot re-verified with fallbacks.
- The N×4 parity check over the **committed set** (passes).

### Out of scope

- The generator itself (BOLT-002); the smoke test (BOLT-004); the
  canonical definitions (BOLT-001); the root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- SPEC-260823-1600 (BOLT-001) delivered — the canonical definitions.
- SPEC-260823-1601 (BOLT-002) delivered — the generator + parity gate.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — Generate and commit

**Duration:** ~2h total cycle — **Complexity:** Low

#### A.1 Run the generator

Run the BOLT-002 generator over the canonical definitions; inspect the
output set (one wrapper per role × platform + the Coordinator where
applicable). Commit the generated files into the kit's platform folders:
`.claude/agents/*.md`, `.opencode/agents/*.md`,
`.github/agents/*.agent.md`, `.codex/agents/*.toml`.

**Files created:**
- `distribution-kit/.claude/agents/<role>.md` (×5 + coordinator)
- `distribution-kit/.opencode/agents/<role>.md` (×5 + coordinator)
- `distribution-kit/.github/agents/<role>.agent.md` (×5 + coordinator)
- `distribution-kit/.codex/agents/<role>.toml` (×5 + coordinator)

#### A.2 The spawn-topology allowlists

Verify the committed wrappers carry the spawn restrictions that enforce
"approver agents spawnable only by the Coordinator": Claude Code
`Agent(...)` allowlists (executors get no approver-spawn capability),
OpenCode `permission.task` denials, Copilot tool omission, Codex role
config + parent instruction (US-023 AC-6 — the enforcement side; BOLT-004
confirms at smoke level).

### Phase B — Per-platform verification notes

**Duration:** ~1.5h total cycle — **Complexity:** Low–Medium

#### B.1 Re-verify the platform contracts

Re-check Codex (issues #14579/#15250 — named custom-agent invocation from
tool-backed sessions) and Copilot (`model`/`mcp-servers` environment
dependence) against current docs; record per platform: what works
natively, what needs a fallback (e.g., Codex generic `agent_type` +
explicit overrides), and the Claude full-coverage statement.

**Files created:**
- `distribution-kit/devflow/agents/VERIFICATION.md` — the per-platform
  notes (also referenced from the family README)

### Phase C — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 Evidence collection

Run: (a) the four wrapper trees present; (b) the parity check passes over
the committed set (N×4, 0 drift); (c) the spawn-topology allowlists spot
check; (d) the verification notes present (Claude full; Codex/Copilot
re-verified + fallbacks); (e) `git status` kit-only; (f) encoding clean.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: Wrappers committed

**Given** the generator output,
**When** the deployment lands,
**Then** the four platform folders carry the generated wrappers (per role
+ Coordinator) and the N×4 parity check passes over the committed set
(US-023 AC-9 — the committed facet).

### AC-2: Spawn topology enforced in the wrappers

**Given** the deployed wrappers,
**When** the spawn allowlists are inspected,
**Then** approver agents are spawnable only by the Coordinator — encoded
per platform (Claude `Agent(...)`, OpenCode `permission.task`, Copilot
tool omission, Codex role config) (US-023 AC-6).

### AC-3: Verification notes recorded

**Given** the platform verification status,
**When** the notes are read,
**Then** Claude Code receives full native coverage; Codex and Copilot are
re-verified against current docs with documented fallbacks, recorded per
platform (US-023 AC-10).

### AC-4: Kit-only

**Given** the diff,
**When** the Bolt lands,
**Then** only `distribution-kit/` changes (US-023 AC-11).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-023 AC-9 (committed facet) | generated + committed wrappers, parity over the set | AC-1 |
| US-023 AC-6 | spawn-topology allowlists in the wrappers | AC-2 spot check |
| US-023 AC-10 | per-platform verification notes + re-verification | AC-3 |
| US-023 AC-11 | scope | AC-4 git status |

---

## 8. Testing strategy

Deterministic (deployment + verification):

- **RED (before):** no role wrappers in the platform folders; no
  verification notes.
- **GREEN (after):** AC-1..AC-4 — trees present, parity passes over the
  committed set, allowlists spot-checked, notes present, kit-only.
- **Edge cases:** Codex/Copilot gaps — recorded as fallbacks, never
  silently assumed; a wrapper that cannot express a restriction is noted
  per platform (DISC-002 §4.2 known-gaps column).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — deployment of generated files (the generator's tests are BOLT-002's) |
| SAST / SBOM | — | n/a — no new runtime code |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — static generated files; no external content |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | refs resolve | pass — platform refs re-verified at implementation |
| IP / license provenance | — | n/a — generated from the kit's own definitions |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — deployment; parity + presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass — parity over the committed set reproduces |
| Bolt-manifest validation | validates | pass — BOLT-003 manifest + spec_revisions[] |

---

## 10. Security and data

The committed wrappers encode the spawn-topology allowlists (the
injection-forged-approval defense's operational half) and the approver
ceiling; the verification notes record each platform's honest capability
status. Data classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** new wrapper files + folders (`.claude/agents/`,
  `.codex/`); additive.
- **Compatibility:** the four main agent files are untouched; new paths
  only.
- **Rollback:** delete the generated wrapper files/folders; root
  untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Codex/Copilot contracts changed since DISC-002 | 3 | 3 | Re-verification at implementation (rec #6) + fallbacks recorded |
| Spawn allowlists omitted from a wrapper | 2 | 4 | AC-2 spot check per platform |
| Parity drift after commit | 1 | 4 | Parity over the committed set (AC-1) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Wrappers committed pre-built | Adopters copy wholesale — no adoption-time build (DISC-002 §5.5) |
| Verification notes live in `devflow/agents/VERIFICATION.md` | One place per platform status; referenced from the family README |
| `.claude/agents/` and `.codex/` are new kit folders | G30-sanctioned by US-023; the platform contract requires those paths |

---

## 14. Stop conditions

- A platform wrapper cannot express a required restriction and no
  fallback is documented → stop, record, resolve (never silently omit).
- The parity check fails over the committed set → stop, fix, re-commit
  (never hand-edit wrappers to pass).
- Any file outside `distribution-kit/` in the diff → stop, revert
  (ADR-004).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-4 pass
- [ ] GREEN evidence (trees, parity over the set, allowlists, notes, kit-only)
- [ ] Codex/Copilot re-verified against current docs (DISC-002 rec #6)
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-023 (approved), US-023.BOLT-003 (approved)
- DISC-002 §4.2 (matrix), §5.6 (pilot), rec #6; ADR-004 (kit-only)
- SPEC-260823-1600 (definitions), SPEC-260823-1601 (generator)

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
| **review_ready_at** | `2026-08-23T16:02:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
