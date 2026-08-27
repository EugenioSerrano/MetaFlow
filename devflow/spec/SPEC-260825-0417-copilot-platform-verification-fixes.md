---
id: "SPEC-260825-0417"
title: "The Copilot platform verification fixes — Coordinator spawn tool, execution-evidence rule and the VERIFICATION.md Copilot-row batch (US-025.BOLT-006)"
date: "2026-08-25"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-25
origin: "REV-006" # US-NNN, TC-NNN, BUG-NNN, DISC-NNN, REV-NNN, AREV-NNN, or ADR-NNN that motivated this SPEC
bolt: "US-025.BOLT-006" # ⚠️ MANDATORY — approved 2026-08-25 (AITL-BOLT-READY-Approval)
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md" # accepted — lifecycle + ship model
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md" # accepted — the roster enablement
prerequisites:
  - "devflow/spec/SPEC-260824-1144-per-platform-lifecycle.md" # delivered — the per-platform surface this SPEC corrects
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # low → L3 (default)
turn_budget: "" # leave empty — platform default
data_classification: "internal" # docs/config change; no PII
review_ready_at: "2026-08-25T04:17:54-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("le metamos!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-25T04:23:30-03:00"
  decided_at: "2026-08-25T04:23:30-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as Dev-validator: source inventory verified (all governed sources approved — Bolt AITL-BOLT-READY 2026-08-25, US-025, ADR-013/014, REV-006/REV-005), ACs testable, evidence defined (sync diff + G-count + spawn probe), gates scoped with reasons, stop conditions explicit. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in English (ADR-012).
-->

# SPEC-260825-0417 — The Copilot platform verification fixes

| Field | Value |
|-------|-------|
| **Origin** | REV-006 (approved 2026-08-25 — the Copilot adopter smoke test) |
| **Bolt** | US-025.BOLT-006 (AITL-BOLT-READY-Approval 2026-08-25) |
| **ADRs** | ADR-013 (lifecycle governance), ADR-014 (roster enablement) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Correct the GitHub Copilot platform surface of the US-025 lifecycle per
REV-006: (a) the Copilot Coordinator's frontmatter `tools:` gains the
platform's canonical agent-invocation alias (`agent`), so the body's
spawn-topology claim is backed by configuration and installed role agents
are actually spawnable; (b) `agents/VERIFICATION.md` and the agents-family
README state the execution-evidence rule — an author stamp is meaningful
only with a real spawn trace; (c) the VERIFICATION.md Copilot row documents
the four platform facts the smoke test established (spawn requires the
`agent` tool; role wrappers are user-invocable by default; validate the
roster after agent edits; the 30k prompt cap is cloud-agent scope).

**What happens if NOT implemented:** every Copilot adopter keeps a
Coordinator that silently self-executes delegated work (and stamps the
reviewer's identity on work the reviewer never did — the F-02 false
attribution), while the platform docs keep asserting a spawn capability
that does not exist and a prompt-cap warning that does not apply to VS Code.

---

## 2. Context

REV-006 (approved 2026-08-25) ran the v5.1 kit from the Copilot adopter
seat on a clean project. Two explicit delegation probes showed the
Coordinator executing reviews itself with **no subagent spawn** — the
`agent`/`agent/runSubagent` tool is absent from its `tools:` list, and the
platform contract (VS Code subagents docs; GitHub custom-agents reference)
makes that tool the requirement for agent-initiated subagent invocation.
The same run produced a fabricated-attribution incident (the Coordinator
wrote a REV and stamped `author: agent:reviewer-copilot` on it — the
reviewer wrapper is read-only and could not have written the file), which
the Coordinator itself conceded under confrontation. Tail-content probes
answered from memory with zero file reads proved the full 68.6k-char body
loads in VS Code — the 30k cap documented by GitHub applies to the cloud
agent, not this environment. The role wrapper's own projection was
verified correct (read-only tools, no `model` field, role-generic body).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-006 | AITL-BOLT-READY-Approval ✓ (2026-08-25) |
| Feature US | US-025 (AC-2, AC-7, AC-8) | AITL-US-Approval ✓ (2026-08-24) |
| ADRs | ADR-013, ADR-014 | AITL-ADR-Approval ✓ (accepted 2026-08-24) |
| REV evidence | REV-006 (F-01..F-05) | AITL-REV-Approval ✓ (2026-08-25) |
| REV evidence | REV-005 (F-09, F-14) | AITL-REV-Approval ✓ (2026-08-24) |
| Repository baseline | `b3ddb4e` | — |

---

## 4. Scope

### In scope

- `distribution-kit/.github/agents/AvengaDevFlow.agent.md` — the
  frontmatter `tools:` list gains the canonical `agent` alias; nothing else
  in the file changes (the shared methodology body stays byte-identical).
- `distribution-kit/devflow/agents/VERIFICATION.md` — the Copilot row:
  spawn requirement, user-invocable guidance, roster-validation note, 30k
  scope; plus the execution-evidence rule (in the spawn-topology and
  F-14-related wording).
- `distribution-kit/devflow/agents/README.md` — one line: an executor's
  production may be persisted by the Coordinator, but the persistence act
  must trace to a real spawn.
- Verification evidence: the four-agent sync diff, the G-count sweep, the
  re-copied adopter test folder, and the live spawn probe (acceptance demo).

### Out of scope

- The other three platform agent files (Claude/OpenCode/Codex) — no change.
- The reviewer charter/definition enrichment (REV-005 F-07's separate
  charter Bolt).
- The roster schema / `approves` enum (boundary resolved by maintainer
  decision at REV-005 routing — the enum stays).
- Any 30k-related code change — wording only (no defect on VS Code).

---

## 5. Prerequisites and baseline

- US-025.BOLT-002 delivered (the per-platform surface this SPEC corrects);
  US-025.BOLT-001 delivered (the shared body — untouched by design).
- REV-006 approved (the governing evidence, F-01..F-05).
- Baseline: repository HEAD `b3ddb4e`; the adopter test project at
  `C:\GitHubRepos\AvengaDevFlow-test\copilot` (byte-identical copy of the
  kit as of 2026-08-25 03:46).

---

## 6. Phases

### Phase A — The Coordinator spawn tool

**Duration:** 0.5–1h total cycle — **Complexity:** Low

#### A.1 Enable the `agent` alias in the Copilot Coordinator

`distribution-kit/.github/agents/AvengaDevFlow.agent.md` — in the
frontmatter `tools:` list, add the canonical agent-invocation alias
`'agent'` (the platform-recognized alias for agent→agent invocation;
verified in the GitHub custom-agents configuration reference, 2026-08-25).
The body's existing spawn-topology sentence ("Only your tools include the
`agent` alias") becomes configuration-backed. No other content changes:
the shared methodology body below the frontmatter stays byte-identical
(ADR-004 kit-only; the four-agent sync invariant, US-016).

**Files modified:**
- `distribution-kit/.github/agents/AvengaDevFlow.agent.md` — frontmatter
  `tools:` gains `'agent'` (one entry in the array).

#### A.2 Constraint checks

After the edit, run the four-agent sync diff from the root
`AGENTS.md` procedure: from the `# Avenga DevFlow v5.1 (Methodology)`
heading to end of file, the four agents must differ by exactly the
sanctioned `devflow/agents-data/<agent>/` path lines (2 diff lines per
comparison, 0 other drift), and the G-count sweep must read 39/39
(`^\| G[0-9]{2} \|` per file = the GUARDRAILS count).

---

### Phase B — VERIFICATION.md Copilot row + the execution-evidence rule

**Duration:** 0.5–1h total cycle — **Complexity:** Low

#### B.1 The Copilot row additions

`distribution-kit/devflow/agents/VERIFICATION.md`, the "GitHub Copilot —
viable with environment caveats 🟡" section, gains four documented facts
(evidence: REV-006):

1. **Agent-initiated spawn requires the `agent` tool** in the
   Coordinator's `tools:` — without it, delegated work is silently
   self-executed (REV-006 F-01).
2. **Role wrappers are user-invocable by default** (they appear in the
   agent dropdown); set `user-invocable: false` for subagent-only
   visibility — the OpenCode `mode: subagent` equivalent (REV-006 F-03).
3. **Validate the roster after an agent edit** — the edit tool may write
   TAB indentation that strict YAML parsers reject (REV-006 F-04).
4. **The 30k prompt cap is cloud-agent scope** — the full body
   (68.6k chars) verified loading in VS Code 2026-08-25; re-verify per
   environment (JetBrains/Eclipse/Xcode/cloud agent) (REV-006 F-05).

#### B.2 The execution-evidence rule

`VERIFICATION.md` (the spawn-topology paragraph) and
`distribution-kit/devflow/agents/README.md` (the executor contract) state:
an executor's production may be persisted by the Coordinator (the F-14
shape), but **the persistence act must trace to a real spawn** — an author
stamp without execution is a false claim; when spawn is unavailable,
direct human invocation is the only legitimate reviewer session (REV-006
F-02).

**Files modified:**
- `distribution-kit/devflow/agents/VERIFICATION.md` — Copilot row + the
  execution-evidence sentences.
- `distribution-kit/devflow/agents/README.md` — one contract line.

---

### Phase C — Verification evidence

**Duration:** 0.5–1h total cycle — **Complexity:** Low

#### C.1 Automated evidence (the V-Bounce evidence set)

- Four-agent sync diff: 0 drift in the shared body (2 sanctioned lines per
  comparison).
- G-count sweep: 39/39 per agent file.
- Frontmatter parse check of the modified `.agent.md` (YAML parses; the
  `tools` array contains `'agent'`).
- Grep checks: the four VERIFICATION.md facts present; the
  execution-evidence sentence present in both files.

#### C.2 The live spawn probe (acceptance demo evidence)

Re-copy the updated kit into the adopter test folder
(`C:\GitHubRepos\AvengaDevFlow-test\copilot`), restart the VS Code
session, and re-run the delegation probe ("mandá al revisor a revisar
X") — the expected result: a `reviewer-copilot` subagent pill appears in
the chat (the spawn actually happens). This probe is run by the human at
acceptance; the V-Bounce records the re-copied tree as readiness.

---

## 7. Acceptance criteria

### AC-1: The Coordinator's spawn tool is configured

**Given** the Copilot Coordinator file at
`distribution-kit/.github/agents/AvengaDevFlow.agent.md`,
**When** its frontmatter is parsed,
**Then** the `tools:` array contains the `agent` alias, and the shared
methodology body below the frontmatter is byte-identical to the other
three platform agents (sync diff = 0 drift beyond the sanctioned path).

### AC-2: The execution-evidence rule is documented

**Given** `agents/VERIFICATION.md` and `agents/README.md`,
**When** a reader looks for the persistence rule,
**Then** both state that a persistence act must trace to a real spawn and
a stamp without execution is a false claim.

### AC-3: The VERIFICATION.md Copilot row carries the four facts

**Given** the Copilot section of `agents/VERIFICATION.md`,
**When** it is read,
**Then** it documents the spawn-tool requirement, the user-invocable
default, the roster-validation note, and the cloud-agent 30k scope.

### AC-4: The live spawn works on Copilot (acceptance)

**Given** the updated kit re-copied into the adopter test project and a
fresh VS Code session,
**When** the human asks the Coordinator to delegate a review to the
reviewer,
**Then** a `reviewer-copilot` subagent invocation (pill) appears — the
reviewer, not the Coordinator, executes the review.

### AC mapping to source

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US-025 AC-2 (install → spawnable) | The `agent` alias configured in the Coordinator | AC-1 + AC-4 (spawn probe) |
| US-025 AC-7 (per-platform only) | Only the Copilot frontmatter changes | AC-1 (sync diff) |
| US-025 AC-8 (docs-primary projection) | The VERIFICATION.md Copilot row completes the shipped mapping | AC-3 (grep) |
| REV-006 F-01..F-05 | Phases A–B implement each finding | AC-1..AC-4 |
| REV-006 F-02 (attribution) | The execution-evidence rule | AC-2 |

---

## 8. Testing strategy

- **Unit tests:** n/a — no code; the deliverables are docs/config whose
  "tests" are the deterministic checks in C.1.
- **Integration tests:** n/a — no runtime.
- **E2E tests:** the live spawn probe (AC-4) — human-run at acceptance on
  the adopter test project.
- **Edge cases:** the sync diff must show exactly the sanctioned 2 lines
  (no other drift); the frontmatter must remain valid YAML after the
  `tools` edit; the G-count must stay 39/39.
- **BUG evidence:** n/a — not a BUG-driven Bolt (defect evidence lives in
  REV-006).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — no runtime code (docs/config only) |
| SAST / SBOM | — | n/a — no dependencies |
| Perf-smoke (p95/p99) | — | n/a — no runtime |
| Prompt-injection scan | — | n/a — no new executable content; the change narrows a platform gap (the reviewed charter hardening is REV-005 F-07's separate Bolt) |
| Secret-leak scan | — | pass — no secrets introduced |
| Hallucination lint | — | pass — every new claim traces to REV-006 evidence or verified platform docs |
| IP / license provenance | — | n/a — no third-party content |
| PII / DLP | — | n/a — data_classification internal, no PII |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | pass — verification-first: the deterministic checks (C.1) are defined in this SPEC before the V-Bounce |
| Behavioral reproducibility | — | pass — the spawn probe is reproducible on the re-copied test project |
| Bolt-manifest validation | — | pass — the Bolt manifest validates against manifest-v5-bolt.schema.json |

---

## 10. Security and data

- The change enables agent→agent invocation on Copilot (a capability
  expansion to the designed topology). Control: the executors-cannot-spawn
  ceiling is unchanged — role wrappers keep omitting the `agent` alias
  (the mapping in VERIFICATION.md already excludes it); the
  execution-evidence rule (B.2) raises the bar on attribution integrity.
- No secrets, credentials or personal data touched; `data_classification`
  internal.

---

## 11. Monitoring and observability

n/a — the kit is documentation; "observability" is the deterministic
sync/G-count/probe evidence in §6-C and the acceptance demo (AC-4).

---

## 12. Migration, compatibility and rollback

- **Migration:** N/A — the kit is copied by adopters; the change ships in
  the next copy. The adopter test project is re-copied as part of the
  evidence (C.2).
- **Compatibility:** the `agent` alias is a recognized platform alias
  (GitHub custom-agents reference); unrecognized tool names are ignored by
  the platform, so a fallback is inherent.
- **Rollback:** revert the commit touching the three kit files (or restore
  them from HEAD); the shared-body sync diff immediately re-verifies.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Shared-body drift from the frontmatter edit | 2 | 3 | Sync diff gate (AC-1); edit confined to the frontmatter array |
| The `agent` alias not honored by an older VS Code/Copilot version | 2 | 3 | Platform contract verified 2026-08-25; unrecognized tools are ignored (inherent fallback); stop condition S2 |
| The spawn probe still failing after the fix (deeper platform issue) | 2 | 3 | Stop condition S3 — record evidence, escalate to a new finding |
| G-count or version-marker drift | 1 | 3 | Sweeps in C.1 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Use the canonical alias `'agent'` (not `custom-agent`/`Task`) | The documented primary alias; matches the body's own wording ("the `agent` alias") |
| No `agents:` field added | Platform default is `*` (all invocable) — the minimal change unblocks spawn without over-restricting; an explicit allowlist can be a later hardening |
| Docs-only treatment for the 30k cap | No defect on VS Code — wording correction (REV-006 F-05), not a code change |
| Execution-evidence rule placed in VERIFICATION.md + agents/README | Both files are the docs-primary projection path (US-025 AC-8) and the executor contract home |

---

## 15. Stop conditions

- **S1** — The sync diff shows drift beyond the sanctioned agents-data
  path lines → stop; reconcile the four agents before continuing.
- **S2** — The `agent` alias is unrecognized/ignored in the target VS Code
  version (frontmatter tools validation) → stop; re-verify the platform
  contract before changing approach.
- **S3** — The spawn probe still self-executes after the fix → stop;
  record the evidence in the MEM; escalate as a new finding (the platform
  may gate agent-initiated spawn differently than documented).
- **S4** — The G-count or version markers change → stop; restore the
  invariant before continuing.

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A + B + C.1)
- [ ] All acceptance criteria pass (AC-1..AC-3 automated; AC-4 human demo)
- [ ] Tests/checks GREEN (sync diff, G-count, frontmatter parse, greps)
- [ ] Code follows applicable ADRs (ADR-013/014; ADR-004 kit-only)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 17. References

- REV-006-copilot-adopter-smoke-test.md (approved 2026-08-25)
- REV-005-devflow-agents-adopter-smoke-test.md (approved 2026-08-24)
- US-025-mainagent-agent-lifecycle.md (approved 2026-08-24)
- ADR-013 / ADR-014 (accepted 2026-08-24)
- US-025.BOLT-006-copilot-platform-verification-fixes.md (approved)
- SPEC-260824-1144-per-platform-lifecycle.md (delivered)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | eugenio.serrano (agent-drafted, deepseek/deepseek-v4-flash) | Initial draft (revision 1) |
| 2026-08-25 | eugenio.serrano | AITL-SPEC-Approval recorded — V-Bounce authorized |

---

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`AITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> V-Bounce. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-25T04:17:54-03:00` |
| **review.started_at** | `2026-08-25T04:23:30-03:00` |
| **review.decided_at** | `2026-08-25T04:23:30-03:00` |
| **Findings** | none on the SPEC itself — approved with the full source inventory and evidence plan (reason in the frontmatter `review:` block) |
