---
id: "SPEC-260823-1601"
title: "Wrapper generator and N×4 parity check — the maintainer tool that projects canonical agent definitions into the four platform wrapper shapes"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-023"
bolt: "US-023.BOLT-002" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md" # the canonical definitions the generator projects
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T16:01:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (the wrapper generator + N×4 parity check integrated with the US-016 discipline, platform mapping re-verified at implementation); grounded, feasible, testable (unit + integration). Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-023 approved ✓;
  DISC-002 approved ✓; US-016 approved ✓; ADR-004 accepted ✓; 0 open OQs.
-->

# SPEC-260823-1601 — Wrapper generator and N×4 parity check (US-023.BOLT-002)

| Field | Value |
|-------|-------|
| **Origin** | [US-023](../functional/user-stories/US-023-devflow-agent-definition-and-deployment.md) (approved) |
| **Bolt** | [US-023.BOLT-002](../functional/bolts/US-023.BOLT-002-wrapper-generator-and-parity.md) (approved) |
| **ADRs** | ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Build the **wrapper generator** in `tools/`: a maintainer-run tool that
projects a canonical DevFlow Agent definition
(`distribution-kit/devflow/agents/roles/<id>/agent.yaml`, delivered by
BOLT-001) into the **four platform wrapper shapes** — Claude Code
`.claude/agents/*.md`, OpenCode `.opencode/agents/*.md`, GitHub Copilot
`.github/agents/*.agent.md`, Codex `agents/*.toml` — plus the **N×4
parity check**: the four-agent sync philosophy (AGENTS.md procedure)
extended to N roles × 4 platforms, integrated with the US-016 audit tool
so the parity invariant is mechanically verified.

**Why:** the wrappers must stay in sync with the canonical definitions
forever — a hand-maintained set would drift (the AREV-001 F-01 failure
mode made mechanical). **If not done:** BOLT-003 has nothing to deploy and
the N×4 parity has no mechanism.

---

## 2. Context

US-023 AC-9 requires generated + committed wrappers with a passing N×4
parity check and no adoption-time build; DISC-002 §4.2 verified the four
platform wrapper contracts (re-check at implementation per §7 #1); US-016
(approved) automates the four-agent sync + G-count checks — the parity
check integrates with it (same diff-based discipline, N roles × 4
platforms). The generator is maintainer tooling in `tools/` (the existing
per-tool pattern: `tools/<tool>/DESIGN.md` + executable), kit-side per
ADR-004 (tools/ is part of the product work).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-023.BOLT-002-wrapper-generator-and-parity.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-023-devflow-agent-definition-and-deployment.md | AITL-US-Approval ✓ (2026-08-23, 8 SP) |
| Prior work | US-016 (audit tool), DISC-002 (§4.2 platform matrix) | approved ✓ |
| ADR | ADR-004 (kit-only) | accepted ✓ |
| Prior SPEC | SPEC-260823-1600 (BOLT-001 — the canonical inputs) | prerequisite |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; 0 open OQs.

---

## 4. Scope

### In scope (tooling)

- `tools/agent-wrappers/` — the generator + the parity check (following
  the `tools/<tool>/DESIGN.md` + executable pattern).
- The generator's mapping: canonical `agent.yaml` → the four wrapper
  shapes (per DISC-002 §4.2: frontmatter/TOML fields, tools/permissions,
  MCP config, spawn restrictions where the platform supports them).
- The N×4 parity check — a diff-based verification that each role's four
  wrappers match the canonical definition (extending the US-016 audit
  approach; wiring documented in the tool's DESIGN).

### Out of scope

- The committed wrapper files (BOLT-003); the canonical definitions
  (BOLT-001); per-platform verification notes (BOLT-003); the root
  `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- SPEC-260823-1600 (BOLT-001) delivered — the canonical `agent.yaml`
  inputs exist.
- US-016 delivered — the audit tool whose sync discipline the parity
  check extends.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — The generator

**Duration:** ~2.5h total cycle — **Complexity:** Medium

#### A.1 The tool

Create `tools/agent-wrappers/` with: a `DESIGN.md` (the mapping rules
canonical → 4 shapes, per DISC-002 §4.2, re-verified against current docs
at implementation — Codex TOML role files, Copilot `.agent.md`
frontmatter, OpenCode agent frontmatter, Claude Code frontmatter + tools +
mcpServers), and the generator executable (maintainer-run: input =
`agents/roles/*/agent.yaml` + the coordinator, output = the four wrapper
files). No runtime generation for adopters — the generated files are
committed (BOLT-003).

**Files created:**
- `tools/agent-wrappers/DESIGN.md` — the mapping + platform contract notes
- `tools/agent-wrappers/` — the generator executable + its tests

### Phase B — The N×4 parity check

**Duration:** ~1.5h total cycle — **Complexity:** Medium

#### B.1 The parity gate

Add the parity check to the same tool: for each role × 4 platforms, verify
the wrapper content matches the canonical definition (field mapping,
tools/permissions, MCP list, spawn restrictions) — the four-agent sync
discipline extended to N×4. Wire the invocation into the US-016 audit
surface (a shared check or a documented companion invocation).

**Files created:**
- `tools/agent-wrappers/parity-check` (or integrated in the generator CLI)
- US-016 integration note (how the audit tool calls/extends to N×4)

### Phase C — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 Evidence collection

Run: (a) the generator over the BOLT-001 definitions produces the four
wrapper shapes; (b) the parity check passes (N×4 consistent, 0 drift);
(c) the tool's tests pass; (d) `git status` shows only `distribution-kit/`
and `tools/`.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The generator runs

**Given** the canonical definitions (BOLT-001),
**When** the generator runs,
**Then** it produces the four platform wrapper shapes per role (US-023
AC-9 — the mechanism facet).

### AC-2: The N×4 parity check passes

**Given** the generated wrappers,
**When** the parity check runs,
**Then** each role's four wrappers match the canonical definition — N×4
consistent, 0 drift (US-023 AC-9).

### AC-3: Kit + tools only

**Given** the diff,
**When** the Bolt lands,
**Then** only `distribution-kit/` and `tools/` change (US-023 AC-11).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-023 AC-9 (mechanism) | the generator + parity gate | AC-1/AC-2 run results |
| US-023 AC-11 | scope | AC-3 git status |

---

## 8. Testing strategy

- **Unit tests:** the generator's field-mapping functions (per platform
  shape) — ~6-10 cases.
- **Integration:** the generator over the five BOLT-001 templates; the
  parity check over the produced set.
- **Edge cases:** an `agent.yaml` with `mcp_servers: []` (default), with
  named servers, with `approves: []`, with `modes: [approver]` (ceiling
  reflected in the wrapper), and a missing field (fail fast, no silent
  default).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | green | pass — the tool's tests |
| SAST / SBOM | — | n/a — internal tooling, no dependencies beyond the runtime |
| Perf-smoke (p95/p99) | — | n/a — batch maintainer tool |
| Prompt-injection scan | — | pass — the generator treats agent.yaml as data, not instructions; no external content processed |
| Secret-leak scan | — | pass — no secrets in tooling |
| Hallucination lint | refs resolve | pass — platform mapping refs verified |
| IP / license provenance | — | n/a — original code |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no third-party dependencies |
| Test-first evidence | — | n/a — tooling; the generator's tests are the evidence |
| Behavioral reproducibility | deterministic | pass — same input → same wrappers |
| Bolt-manifest validation | validates | pass — BOLT-002 manifest + spec_revisions[] |

---

## 10. Security and data

The generator processes only canonical repo files (no external content —
no injection surface); it never executes the definitions it projects.
Data classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** new tool in `tools/`; additive.
- **Compatibility:** no adopter impact (maintainer-run).
- **Rollback:** remove `tools/agent-wrappers/`; root untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Platform contracts drifted from DISC-002 §4.2 | 3 | 3 | Re-verify against current docs at implementation (DISC-002 rec #6); recorded in DESIGN.md |
| Generator drifts from canonical | 2 | 4 | The parity gate is the invariant; runs on every change |
| Codex/Copilot shapes unstable | 2 | 3 | Documented fallbacks in DESIGN.md (generic spawn path for Codex) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The generator + parity live in one tool (`tools/agent-wrappers/`) | One coherent maintainer surface; the parity is the generator's own gate |
| Parity integrates with the US-016 audit discipline | Reuses the proven four-agent sync approach instead of inventing a new one |
| No adoption-time generation | DISC-002 §5.5: the kit ships pre-built wrappers (committed in BOLT-003) |

---

## 14. Stop conditions

- A platform contract cannot be mapped with a documented fallback → stop,
  record, resolve (never guess).
- The parity check cannot pass on a generated set → stop, fix the
  generator (never hand-edit the wrappers to pass).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass
- [ ] Tests GREEN (generator + parity)
- [ ] Platform mapping re-verified against current docs (DISC-002 rec #6)
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-023 (approved), US-023.BOLT-002 (approved)
- DISC-002 §4.2 (platform matrix), §5.5 (product split), rec #6
- US-016 (approved — the audit tool), ADR-004 (kit-only)
- SPEC-260823-1600 (BOLT-001 — the canonical inputs)

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
| **review_ready_at** | `2026-08-23T16:01:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
