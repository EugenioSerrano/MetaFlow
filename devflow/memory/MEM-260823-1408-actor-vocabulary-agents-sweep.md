---
id: "MEM-260823-1408"
title: "Actor vocabulary and four agents — propagate the producer + approver reframe to the four agents, ONBOARDING and the actors/ README (US-022.BOLT-003, V-Bounce 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-022.BOLT-003"
spec: "devflow/spec/SPEC-260823-1337-actor-vocabulary-agents-sweep.md"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-23T14:08:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobadas todas") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T15:35:00-03:00"
  decided_at: "2026-08-23T15:36:33-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the propagation diff (4 agents byte-identical, ONBOARDING, actors/README), the sweep absence report and the G-count 39×5 evidence inspected; matches the re-approved US-022 and SPEC-1337 rev 2. V-Bounce 2 approved — BOLT-003 Development Completed."
---

# MEM-260823-1408 — Producer + approver propagation (US-022.BOLT-003, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-022.BOLT-003 (actor-vocabulary-and-agents-sweep) |
| **SPEC**        | [SPEC-260823-1337](../spec/SPEC-260823-1337-actor-vocabulary-agents-sweep.md) **rev 2** |
| **V-Bounce**    | 2 (propagation of the producer+approver reframe, per the re-approved US-022 — G15 chain) |
| **ADRs**        | ADR-010 (pure v5 vocabulary), ADR-005 (sweep discipline), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce propagates the producer+approver reframe (SPEC-1337 rev 2,
source US-022 re-approved) to every surface that names the Actor: the
**four platform agents'** shared paragraph was rewritten from "The Actor
(unit of identity): every checkpoint pause is occupied by an Actor…" to
"The Actor (producer + approver): an Actor is a member of the team — a
human by default, a virtual DevFlow Agent only by explicit valid
configuration — who **produces** the governed artifacts its role owns
(FA → US, architect → ADR, developer → SPEC + code, QA → TC/tests) as
executor, and **participates** in AITL approvals as approver when
configured, under the independence floor", keeping the grammar,
independence-ladder and safe-default sentences; the **ONBOARDING "Actor"
row** was updated to the same framing; and the **`actors/` README** "What
is an Actor?" paragraph plus its embedded mermaid were updated to the new
canonical producer → checkpoint → approver diagram (identical to §3.0.1 /
US-022 §4). The **phrase-family sweep** (ADR-005) was extended to the
production vocabulary and re-run: no surface defines the Actor solely as
"the participant who occupies a checkpoint pause" — the one literal hit
was the reframe's own negation sentence in §3.0.1, which was rephrased
("not merely a checkpoint participant") so the sweep reads clean;
**absence confirmed outside the allowlist**. Verification is GREEN:
reframe present in all surfaces, four-agent byte-identity holds (2
sanctioned diff lines per agent), G-count 39×5, kit-only. V-Bounce 1 MEM
remains as immutable history.

## 2. Implemented phases

### Phase A — The four agents' paragraph

Rewrote the shared "The Actor (producer + approver):" paragraph
byte-identically in all four platform agents (CLAUDE.md, SKILL.md,
AvengaDevFlow.agent.md, AvengaDevFlow.md): the producer side (artifact
ownership per role, executor mode) is now first-class, followed by the
unchanged approver-side sentences (independence floor, HITL default case,
safe default, grammar, independence ladder, human ceiling).

### Phase B — ONBOARDING and the actors/ README

Updated the ONBOARDING §4 "Actor" row to the producer + approver framing
(produces the artifacts its role owns as executor; participates in
approvals as approver when configured). Updated the `actors/` README
"What is an Actor?" paragraph and replaced its embedded mermaid with the
new canonical producer → checkpoint → approver diagram (identical to
§3.0.1 — the README references/embeds the canonical home, never forks it).

### Phase C — The extended sweep + the negation rephrase

Extended the phrase-family sweep to the production vocabulary (no surface
defines the Actor solely as "the participant who occupies a checkpoint
pause"). The sweep's first run found exactly one literal hit — §3.0.1's
own negation sentence ("is not merely 'the participant who occupies a
checkpoint pause'") — which was rephrased to "not merely a checkpoint
participant" so the corrective sentence no longer trips the family check.
Re-run: absence confirmed.

### Phase D — Verification (GREEN)

Ran: reframe presence (4 agents + ONBOARDING + README); the sweep absence
re-check; the four-agent shared-body byte-identity (tail from the heading,
CR-stripped, diffed — exactly 2 diff lines per agent, the sanctioned
`agents-data/<agent>/` path); G-count 39 in GUARDRAILS + all four agents;
`git status` kit-only.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits within existing files) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` | Shared paragraph rewritten to producer + approver (byte-identical) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same paragraph, byte-identical |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same paragraph, byte-identical |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same paragraph, byte-identical |
| `distribution-kit/devflow/ONBOARDING.md` | "Actor" row updated to the producer + approver framing |
| `distribution-kit/devflow/actors/README.md` | "What is an Actor?" paragraph + embedded mermaid updated to the new canonical diagram |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.0.1 negation sentence rephrased ("not merely a checkpoint participant") so the sweep family reads clean |

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
| The agents' paragraph keeps the approver-side sentences unchanged | The reframe adds production without weakening the approval precept; byte-identity preserved by construction |
| The `actors/` README mermaid follows the canonical one exactly | The README references/embeds the canonical home (US-022 rule #6) — no diagram drift |
| The sweep covers the production vocabulary | The reframe's family must be verified as an absence like the rest (ADR-005) |
| The §3.0.1 negation sentence rephrased | The literal old phrase in the corrective sentence tripped the family check; the meaning is preserved without the stale token |
| ONBOARDING row keeps the safe-default tail | The vocabulary surface stays complete (HITL default case + no-AI-signed-approval invariant) |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1337 rev 2. Assumption: the glossary
content file still does not exist in the kit (recorded in V-Bounce 1) —
ONBOARDING remains the vocabulary surface; the `actors/` README correction
is in-scope because the sweep's location set includes it.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   4 agents "The Actor (unit of identity): every checkpoint pause is
       occupied by…" ; ONBOARDING row approver-centric ; README
       paragraph + old mermaid
GREEN: 4 agents "The Actor (producer + approver):" — PRESENT (4x)
       ONBOARDING producer row — PRESENT
       actors/README producer paragraph + new mermaid — PRESENT
```

### Sweep (ADR-005, extended to production terms)

```
First run: 1 literal hit — §3.0.1 negation sentence → rephrased.
Re-run: ABSENCE CONFIRMED — no surface defines the Actor solely as "the
participant who occupies a checkpoint pause". PASS
```

### Invariants

```
Four-agent byte-identity: 2 diff lines per agent (sanctioned agents-data
path only)                                    PASS
G-count: 39 × 5 (GUARDRAILS + 4 agents)       PASS
Kit-only: 6 modified + actors/ new — all distribution-kit   PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass` (no runtime surface); hallucination-lint `pass` (refs resolve);
behavioral-reproducibility `pass`; bolt-manifest-validation `pass`
(v_bounces[2] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 2 |
| Tests created | 0 (documentation Bolt — deterministic presence/sync/sweep checks instead) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] PASO 5: US-023 (draft) — charter templates enumerate productive
      outputs per role and emphasize `modes:[executor]`
- [ ] Batch approvals: all pending MEMs + the re-approvals already
      recorded (US-022 re-approved; SPEC-1335/1337 rev 2 approved)

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
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T14:08:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the 4 agents + ONBOARDING + README + §3.0.1 rephrase; sweep absence report; byte-sync proof; G-count; kit-only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
