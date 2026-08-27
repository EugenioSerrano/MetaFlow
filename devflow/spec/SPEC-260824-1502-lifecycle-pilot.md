---
id: "SPEC-260824-1502"
title: "The lifecycle pilot — the run script for the maintainer's second adopter test (create → spawn → delete on OpenCode) and the evidence to bring back"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-025"
bolt: "US-025.BOLT-004"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260824-1101-mainagent-lifecycle-body.md"
  - "devflow/spec/SPEC-260824-1144-per-platform-lifecycle.md"
  - "devflow/spec/SPEC-260824-1423-delete-safe-consistency.md"
  - "devflow/spec/SPEC-260824-1447-kit-g07-scoping.md"
risk_class: "low"
autonomy_level: "L1" # the pilot is human-executed by design — the agent's role is the recording; L1: a bounded proposal (the script) executed by the human
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T15:03:51-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T15:06:02-03:00"
  decided_at: "2026-08-24T15:06:02-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the run script covers the three legs with the expected behaviors pinned against the delivered contracts (incl. the F-02 delta measured verbatim at Leg 1 and the F-13 registration checks at Leg 2), the evidence list is complete (extracts, trees, agent list, latencies per F-17), the observation-only discipline and the seed-commit recording are stop-conditioned, and the L1 autonomy correctly makes the human the executor. Authorizes the V-Bounce: the maintainer runs the pilot; the recording lands in the MEM."
---

# SPEC-260824-1502 — The lifecycle pilot (the run script)

| Field | Value |
|-------|-------|
| **Origin** | US-025 (approved 2026-08-24) |
| **Bolt** | US-025.BOLT-004 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-013, ADR-004 |
| **Risk Class** | low · **Autonomy L1** (human-executed pilot; the agent records) |
| **Revision** | 1 |

---

## 1. Objective

Run and record the second adopter test — the field proof of US-025's four
delivered Bolts. The maintainer executes; this SPEC is the run script (the
setup, the three legs, the expected behaviors, the evidence to bring back);
the V-Bounce is the execution + the recording.

## 2. Context

The REV-005 baseline ran BEFORE US-025 existed (docs-primary by model
diligence; the G07 gray zone resolved silently). This pilot re-runs the
same shape of test on the COMPLETE kit — the deltas ARE the measurement.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-004 | AITL-BOLT-READY-Approval ✓ (2026-08-24T15:02:24) |
| Feature US | US-025 | AITL-US-Approval ✓ |
| REV baseline | REV-005 | AITL-REV-Approval ✓ |
| The four sibling SPECs | 1101 / 1144 / 1423 / 1447 | AITL-SPEC-Approval ✓ (all delivered, MEMs approved) |
| Repository baseline / kit seed | `93cc94e` (or later) | — |

## 4. Scope

### In scope
- The pilot run (maintainer-executed, OpenCode TUI, a fresh scratch
  project outside this repo seeded from the current kit) + the recording
  (the MEM's evidence + a findings annex in `agents-data/claude/` if
  volume warrants).

### Out of scope
- Fixing anything found (findings route per the REV protocol); other
  platforms; headless re-verification beyond recording.

## 5. Prerequisites and baseline

- Scratch folder outside this repo (e.g. `AvengaDevFlow-test/open-code-v2/`),
  seeded with the CONTENT of `distribution-kit/` at commit `93cc94e` or
  later — **the seed commit recorded in the MEM**.
- OpenCode TUI session opened at the scratch root.

## 6. Phases

### Phase A — Setup (the human)

**Duration:** ~10min

Fresh folder outside the repo → copy the kit content → open OpenCode at
the scratch root → sanity ask: *"¿qué versión de AvengaDevFlow sos?"*
(expected: 5.1, verified from `devflow/VERSION` — the baseline behavior).

### Phase B — The three legs (the human asks; the agent under test acts)

**Duration:** ~45min

**Leg 1 — Create.** Ask (free wording): *"creame un agente `<role>`"*.
Expected against the delivered contract: scaffold from
`TEMPLATE-new-role/`/examples into `agents/squad/<id>/` (role-generic,
`content_language` charter); actor file + `roster.yaml` listing as
**executor-only draft**; `agents/INDEX.md` row; the wrapper installed to
`.opencode/agents/<actor-id>.md` (named by the ACTOR id); the reload
notice; the commit-is-the-record reminder; **no Bolt requested — ideally
the agent cites the scoped G07/living-data rule** (the F-02 delta: from
silent resolution to contract citation).

**Leg 2 — Spawn.** Reload the session → verify registration
(`opencode agent list` / ctrl+X — the F-13 notes verified in the field) →
have the Coordinator spawn the agent on a small task → it produces and
control returns.

**Leg 3 — Delete.** Ask: *"borra el agente `<id>`"*. Expected: the
reference check runs (the contract's enumeration — roster + actor files),
then wrapper + actor file + listing removed, the definition per the
zero-rule, `agents/INDEX.md` consistent — the four legs verified clean
after (`squad/`, INDEX, roster, spawn folder).

### Phase C — The recording (the executor agent, back in this repo)

**Duration:** ~30min

The maintainer brings back: transcript extracts per leg, the tree
before/after delete, the `agent list` output, latency notes per leg
(REV-005 F-17). The recording lands in the MEM (evidence section) + the
findings list (each finding named, severity-tagged and routed — the REV
protocol; an empty list is a valid result). No kit file changes in this
V-Bounce.

## 7. Acceptance criteria

### AC-1: The three legs observed
**Given** the run, **Then** create/spawn/delete each completed with the
expected behaviors — or the deviation recorded as a finding (a finding
does not fail the pilot; an unrecorded one does).

### AC-2: The G07 delta measured
**Given** Leg 1, **Then** the agent's governance stance is recorded
verbatim (Bolt requested? living-data cited? silent?) — the direct
before/after against REV-005 F-05/F-02.

### AC-3: The evidence complete
**Given** the MEM, **Then** it carries the per-leg extracts, the trees,
the registration output, the latencies and the findings list.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-025 AC-2/AC-3/AC-4 | Legs 1–3 exercise install/create/delete in the field | The per-leg evidence |
| US-025 AC-6 | The created agent stays executor-only unless the human grants | The Leg-1 roster extract |

## 8. Testing strategy

The pilot IS the test. Evidence-based observation, no assertions coded;
the four-leg consistency check after Leg 3 runs as a scripted listing in
the scratch (recorded, not committed there).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration / SAST / perf | n/a — observation pilot, no kit changes | n/a |
| Prompt-injection scan | n/a — no content shipped | n/a |
| Secret-leak scan | the recorded extracts carry no secrets | pass expected |
| Hallucination lint | the MEM's claims match the transcript extracts | pass expected |
| IP / license / PII / dependency | n/a / n/a — internal evidence | n/a |
| Test-first evidence | this script predates the run | pass expected |
| Behavioral reproducibility | the script is re-runnable on any fresh seed | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

The scratch is disposable and outside governance; nothing from it is
committed except the recorded evidence in the MEM. No secrets, no
personal data beyond the maintainer's own actor identity.

## 11. Monitoring and observability

The latency notes per leg are the observability (F-17's datapoint).

## 12. Migration, compatibility and rollback

n/a — observation only; the scratch is deleted by the human afterwards.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| The pilot finds a defect | 3 | 1 | By design: record + route (the REV protocol); never hotfix in the scratch |
| Stale seed invalidates the run | 1 | 3 | The seed commit recorded; seed ≥ 93cc94e |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Autonomy L1 (human-executed) | The pilot's value IS the human-run adopter experience; the agent's role is the faithful recording |
| Free wording in the asks | Scripted phrasing would test the script, not the kit — the baseline used natural asks and the comparison must too |
| Findings route, never fix | The scratch is outside governance; a hotfix there proves nothing and records nothing |

## 15. Stop conditions

- The seed turns out stale (< 93cc94e) → stop, reseed, restart the run.
- Any temptation to fix the kit mid-run → stop the fix, record the
  finding, continue the run.

## 16. Definition of Done (DoD)

- [ ] Phases A–C executed (the run + the recording)
- [ ] AC-1..AC-3 pass
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

US-025 · US-025.BOLT-004 (READY) · REV-005 (the baseline + F-17) · the
four sibling SPECs · ADR-013 · ADR-004.

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T15:03:51-03:00` |
| **review.started_at** | `2026-08-24T15:06:02-03:00` |
| **review.decided_at** | `2026-08-24T15:06:02-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in the frontmatter `review:` block) |
