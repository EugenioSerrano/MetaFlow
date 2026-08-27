---
id: "SPEC-260823-1603"
title: "Spawn smoke test — minimal proof on the pilot platform (Claude Code) that the deployed wrappers load, a role agent spawns, produces a trivial artifact and returns control"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-023"
bolt: "US-023.BOLT-004" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 2 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1602-wrapper-deployment.md" # the deployed wrappers under test
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T16:40:00-03:00"
review: # AITL-SPEC-Approval (rev 2) — recorded by the human reviewer (§3.0); revision dictated in conversation ("quitamos la smoke del bolt4 y la pruebo en otro entorno") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T16:40:30-03:00"
  decided_at: "2026-08-23T16:41:25-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 2 approved (G15 — rescope after the environment rabbit hole): the smoke EXECUTION is a human-run step in a trusted environment; this Bolt delivers the runbook + the recorded environment findings (5 honest runs across Claude Code CLI and OpenCode headless — custom agents not registered in headless sessions, OpenCode 1.18.21) + the evidence template. The spawn evidence is appended when the human runs it (or re-verified by the pilot US). The never-fabricate stop condition stands. Authorizes the V-Bounce against rev 2."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-023 approved ✓;
  DISC-001/002 approved ✓; ADR-004 accepted ✓; 0 open OQs.
-->

# SPEC-260823-1603 — Spawn smoke test (US-023.BOLT-004)

| Field | Value |
|-------|-------|
| **Origin** | [US-023](../functional/user-stories/US-023-devflow-agent-definition-and-deployment.md) (approved) |
| **Bolt** | [US-023.BOLT-004](../functional/bolts/US-023.BOLT-004-spawn-smoke-test.md) (approved) |
| **ADRs** | ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 2 |

---

## 1. Objective

Deliver the **smoke-test runbook** (`tools/agent-wrappers/smoke/README.md`)
and the **evidence template** for the minimal spawn proof on the pilot
platform (Claude Code — the only platform with full native coverage,
DISC-002 §5.6): the deployed wrapper loads; a role agent spawns with its
declared model/tools; the agent **takes the baton and produces a trivial
artifact of its role** (the executor side of the Actor — US-022 reframe,
US-023 AC-3); control returns via the spawn result. The **execution is a
human-run step in a trusted environment** (this repo's workspace must be
trusted and the session restarted, or an adopting project with the kit's
`.claude/agents/` on the path): this environment cannot register the
custom wrappers in headless sessions (recorded in §8), so the run happens
where the platform loads them — the human runs the runbook and the
evidence is appended.

**Why:** DISC-002 §7 #7 calls for a minimal spawn smoke as part of the
registry family — proof the machinery works before the full pilot US
(flow + red-team). **If not done:** the wrappers could be committed but
unspawnable, and the defect would surface only in the pilot.

**Revision 2 (material, G15):** the smoke **execution is rescoped to a
human-run step** — the V-Bounce delivers the runbook + the recorded
environment findings (5 honest runs: Claude Code CLI ×3 — untrusted
workspace/session-start registry; OpenCode headless ×2 + a dedicated
server — custom `.opencode/agents/*.md` not registered in headless
sessions, OpenCode 1.18.21, verified via the `/agent` registry) + the
evidence template. The spawn evidence is appended when the human runs it;
the pilot US re-verifies (DISC-002 §7 #1). The never-fabricate stop
condition stands.

---

## 2. Context

US-023 AC-3 (takes the baton and produces, control returns via the spawn
result — state = files) and AC-6 (spawn topology — smoke confirmation).
DISC-001 verified the Claude Code sub-agent mechanics (Agent tool, model
override, control return, usage in result); DISC-002 §5.6 confirms Claude
as the pilot. This Bolt is verification-only; the full pilot flow +
red-team AC is a separate, later US.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-023.BOLT-004-spawn-smoke-test.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-023-devflow-agent-definition-and-deployment.md | AITL-US-Approval ✓ (2026-08-23, 8 SP) |
| DISC evidence | DISC-001 (sub-agent mechanics), DISC-002 (§5.6 pilot, §7 #7) | approved ✓ |
| ADR | ADR-004 (kit-only) | accepted ✓ |
| Prior SPEC | SPEC-260823-1602 (the deployed wrappers under test) | prerequisite |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; 0 open OQs.

---

## 4. Scope

### In scope (verification)

- A smoke-test script/run on the pilot platform (Claude Code) using the
  deployed wrappers (BOLT-003): load a wrapper, spawn the role agent,
  have it produce a trivial artifact of its role, confirm control returns.
- The recorded evidence (spawn outcome, produced artifact, control-return
  note) in the MEM.

### Out of scope

- The full pilot flow + red-team AC (later US); smoke on the other three
  platforms (their wrappers are verified via parity + notes in BOLT-003);
  any change to the wrappers/charters; the root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- SPEC-260823-1602 (BOLT-003) delivered — the deployed wrappers exist.
- The pilot platform (Claude Code) available at execution time.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — The smoke runbook

**Duration:** ~1h total cycle — **Complexity:** Low

#### A.1 The runbook + evidence template

Deliver `tools/agent-wrappers/smoke/README.md` (what the smoke verifies,
the exact run command for Claude Code, the expected result, the recorded
findings from this environment) and an **evidence template** (the spawn
result, the produced artifact, the control-return note, the platform
variance) that the human fills when running the smoke in a trusted
environment.

**Files created:**
- `tools/agent-wrappers/smoke/README.md` — the runbook (delivered)
- `tools/agent-wrappers/smoke/EVIDENCE.template.md` — the evidence
  template the human-run fills and appends

### Phase B — Environment verification (this environment)

**Duration:** ~1h total cycle — **Complexity:** Low

#### B.1 The honest runs

Record the environment findings: Claude Code CLI ×3 (`claude -p` —
untrusted workspace, session-start registry, wrapper verified well-formed
with `model: inherit`); OpenCode headless ×2 + a dedicated server
(`opencode serve` on a temp adopting project) — the `/agent` registry
showed only the native agents (build, compaction, explore, general, plan,
summary, title); the custom `.opencode/agents/*.md` files were **not
registered in headless sessions** (OpenCode 1.18.21). The spawn mechanics
themselves were proven on OpenCode+Deepseek (task spawn → produce →
control return, with the built-in `general` agent). Findings recorded in
the runbook + VERIFICATION.md.

### Phase C — Handoff to the human

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 The execution path

Document the exact unblock path (trust the workspace / restart the
session / run in an adopting project with the kit's `.claude/agents/` on
the path) and hand the runbook to the human. The spawn evidence is
appended when the human runs it; the pilot US re-verifies (DISC-002 §7
#1).

**Files created (evidence):** none — the evidence template + findings
recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The runbook and evidence template are delivered

**Given** the deployed wrappers (BOLT-003),
**When** the smoke runbook + evidence template are inspected,
**Then** they document the exact Claude Code run, the expected result, and
the evidence fields (spawn result, produced artifact, control-return
note) — ready for the **human-run** execution in a trusted environment
(US-023 AC-3 — the takes-the-baton mechanics, proven by the human run;
the environment findings of this repo are recorded, never fabricated).

### AC-2: Topology documented

**Given** the executor spawn,
**When** the runbook documents the allowlists,
**Then** the spawn-capability expectations match the deployed wrapper's
restrictions — approver spawning stays Coordinator-only (US-023 AC-6 —
smoke confirmation; enforcement in BOLT-001/003).

### AC-3: Kit + tools only

**Given** the diff,
**When** the Bolt lands,
**Then** only `distribution-kit/` (and the smoke runbook in `tools/`)
change (US-023 AC-11).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-023 AC-3 | the runbook + evidence template; human-run execution | AC-1 — the runbook + the appended human evidence |
| US-023 AC-6 | topology documented in the runbook | AC-2 |
| US-023 AC-11 | scope | AC-3 git status |

---

## 8. Testing strategy

- **The smoke itself** is the test: wrapper load → spawn → produce →
  control return.
- **Edge cases:** platform variance (behavior differs from docs) —
  recorded, never assumed; a spawn that fails to load → the MEM records
  the failure + the resolution path (fix wrapper or record the platform
  gap).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — verification-only (the smoke IS the test) |
| SAST / SBOM | — | n/a — no new runtime code beyond the script |
| Perf-smoke (p95/p99) | — | n/a — not a perf exercise |
| Prompt-injection scan | — | pass — the smoke uses only repo files; no untrusted content |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | refs resolve | pass — wrapper/definition refs resolve |
| IP / license provenance | — | n/a — original script |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — verification Bolt; the smoke run is the evidence |
| Behavioral reproducibility | deterministic | pass — same wrappers → same smoke expectations |
| Bolt-manifest validation | validates | pass — BOLT-004 manifest + spec_revisions[] |

---

## 10. Security and data

The smoke runs a real spawn with the declared model — token/cost
awareness noted (DISC-002 §7 #3); no external content, no secrets. Data
classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** none (verification only + the smoke script).
- **Compatibility:** no impact.
- **Rollback:** remove the smoke script; root untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Platform behavior differs from docs | 3 | 2 | Recorded as evidence; the pilot US re-verifies (DISC-002 §7 #1) |
| Smoke spawn costs tokens | 4 | 1 | Minimal artifact; one spawn; budget noted |
| Wrapper fails to load | 2 | 3 | MEM records the failure + resolution path (never silent) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Smoke on Claude Code only | The pilot platform with full native coverage (DISC-002 §5.6); the other platforms are covered by parity + notes (BOLT-003) |
| Trivial artifact of the role | Proves the takes-the-baton mechanics without scope creep (the full flow is the pilot US) |
| The smoke script ships in `tools/agent-wrappers/smoke/` | Re-runnable evidence; part of the maintainer tooling surface |

---

## 14. Stop conditions

- The wrapper fails to load and the failure cannot be resolved in-repo →
  stop, MEM with the blocker (never fabricate the smoke result).
- Any file outside `distribution-kit/`/`tools/` in the diff → stop,
  revert (ADR-004).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (smoke run evidence)
- [ ] GREEN evidence (load, spawn, produce, control return; kit-only)
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-023 (approved), US-023.BOLT-004 (approved)
- DISC-001 (sub-agent mechanics), DISC-002 §5.6/§7 #7
- ADR-004 (kit-only); SPEC-260823-1602 (the wrappers under test)

---

## 17. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Revision 1 — initial |
| 2026-08-23 | eugenio.serrano | **Revision 2 (material, G15)** — rescope after the environment rabbit hole: the smoke EXECUTION is a human-run step in a trusted environment; the Bolt delivers the runbook + the recorded environment findings (Claude Code CLI ×3 — untrusted workspace/session-start registry; OpenCode headless + dedicated server — custom agents not registered in headless sessions, 1.18.21, verified via the `/agent` registry; the spawn mechanics proven on OpenCode+Deepseek with the built-in `general` agent) + the evidence template. The never-fabricate stop condition stands; the human appends the spawn evidence |

---

## 18. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval authorizes SPEC
> preparation; **SPEC approval authorizes the V-Bounce**. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** (rev 1) + **approved** (rev 2 — human-run rescope, 2026-08-23T16:41:25) |
| **review_ready_at** | rev 1 `2026-08-23T16:03:00-03:00` · rev 2 `2026-08-23T16:40:00-03:00` |
| **review.started_at** | rev 1 `2026-08-23T16:09:00-03:00` · rev 2 `2026-08-23T16:40:30-03:00` |
| **review.decided_at** | rev 1 `2026-08-23T16:10:15-03:00` · rev 2 `2026-08-23T16:41:25-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in the frontmatter `review:` block) |
