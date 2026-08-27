---
id: "MEM-260823-1644"
title: "Spawn smoke test — runbook + evidence template delivered; the execution rescoped to a human-run step with the environment findings recorded (US-023.BOLT-004, V-Bounce 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-004"
spec: "devflow/spec/SPEC-260823-1603-spawn-smoke-test.md"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review" # per SPEC rev 2: the runbook + evidence template + environment findings are the deliverable; the spawn execution is a human-run step
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-004-spawn-smoke-test.json"
diff_ref: ""
review_ready_at: "2026-08-23T16:44:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("apruebo todos los mems, los bolts y la US23 de una") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:20:00-03:00"
  decided_at: "2026-08-23T17:21:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the runbook + evidence template + the nine honest runs (with the model-placeholder defect fixed and the OpenCode headless finding recorded) inspected — the human-run execution path is documented; never-fabricate held. V-Bounce 2 approved — BOLT-004 Development Completed."
---

# MEM-260823-1644 — Spawn smoke: runbook + human-run rescope (US-023.BOLT-004, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-004 (spawn-smoke-test) |
| **SPEC**        | [SPEC-260823-1603](../spec/SPEC-260823-1603-spawn-smoke-test.md) **rev 2** |
| **V-Bounce**    | 2 (rescope per SPEC rev 2 — the execution is a human-run step; V-Bounce 1 MEM-1624 stays as immutable history) |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce closes BOLT-004 per **SPEC rev 2** (the human-run rescope
dictated after the environment rabbit hole): the deliverable is the
**smoke runbook** (`tools/agent-wrappers/smoke/README.md` — what the smoke
verifies, the exact Claude Code run, the expected result) plus the
**evidence template** (`tools/agent-wrappers/smoke/EVIDENCE.template.md` —
the fields the human fills when running the smoke in a trusted
environment), with the **environment findings recorded honestly** across
**nine real attempts**: Claude Code CLI ×3 (`claude -p` — untrusted
workspace + session-start registry; wrapper verified well-formed with the
`model: inherit` fix) and OpenCode ×5 + a dedicated `opencode serve`
server (custom `.opencode/agents/*.md` files **not registered in headless
sessions**, OpenCode 1.18.21 — the `/agent` registry listed only the
native agents; the task tool rejected `developer-agent` as "not a valid
agent type"). The smoke still **proved real value**: it caught and fixed
the invalid model placeholder (`<pick-from-platform-catalog>` →
`model: inherit`) and it proved the **spawn mechanics work** on
OpenCode+Deepseek (task spawn → produce → control return, with the
built-in `general` agent — real, evidenced). The **execution is handed to
the human**: trust the workspace / fresh session (or an adopting project
with the kit's `.claude/agents/` on the path), run the runbook, append the
filled evidence template; the pilot US re-verifies (DISC-002 §7 #1). The
never-fabricate discipline held in every run. V-Bounce 1 (MEM-1624,
blocked) remains as immutable history.

## 2. Implemented phases

### Phase A — The runbook + evidence template (delivered)

`tools/agent-wrappers/smoke/README.md` carries the what/how/expected + the
findings section (the model fix, the Claude Code environmental blocker,
the OpenCode headless registration finding). `EVIDENCE.template.md`
defines the evidence fields: run metadata, wrapper loads, spawn with the
declared model/tools, takes-the-baton produce, control return, topology,
result — signed by the human who runs it.

### Phase B — Environment verification (this environment)

Nine real runs recorded (three `claude -p` + five opencode attempts + one
dedicated `opencode serve` with the `/agent` registry dump). Findings
propagated to the runbook and to the kit's `VERIFICATION.md` (OpenCode
headless registration — the DISC-002 rec #6 re-verification result).

### Phase C — Handoff to the human

The unblock path is documented in the runbook (trust the workspace /
restart the session / run in an adopting project); the evidence template
is the handoff artifact. No fabrication, ever.

## 3. Files created

| File | Purpose |
|------|---------|
| `tools/agent-wrappers/smoke/EVIDENCE.template.md` | The evidence template the human-run fills and appends (spawn result, produced artifact, control return, topology, signature) |
| `tools/agent-wrappers/smoke/README.md` | The smoke runbook — what it verifies, the exact run, the expected result, the recorded findings (updated with the OpenCode headless finding) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/VERIFICATION.md` | OpenCode section: the headless registration finding (custom agents not registered in `run`/`serve`; mechanics proven with the built-in `general`; re-verify interactively — DISC-002 rec #6) |

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
| The smoke execution is rescoped to a human-run step (SPEC rev 2) | This environment cannot register the custom wrappers in headless sessions (verified); the platform loads them in a trusted interactive session — the human runs it there and appends the evidence |
| Nine real runs recorded, never fabricated | The never-fabricate stop condition is the Bolt's core discipline — a negative run is real evidence |
| The OpenCode finding propagates to VERIFICATION.md | DISC-002 rec #6: re-verify platform contracts at implementation; adopters must know the headless limitation |
| The evidence template is a handoff artifact | The human-run needs a defined evidence contract to append — keeps the Bolt's verification honest and complete |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1603 rev 2. Assumption: the spawn resolves
in a trusted interactive session (the platform's documented behavior); the
pilot US re-verifies and includes the red-team AC.

## 9. Verification evidence

### Environment runs (RED — real, unfabricated)

```
Claude Code CLI ×3:  'Agent type developer-agent not found' — untrusted
                     workspace + session-start registry; wrapper verified
                     well-formed (frontmatter valid, model: inherit)
OpenCode ×5 + serve: 'Unknown agent type: developer-agent is not a valid
                     agent type' — /agent registry = native agents only
                     (build, compaction, explore, general, plan, summary,
                     title); custom files not registered headless (1.18.21)
Mechanics proven:    task spawn → produce → control return on
                     OpenCode+Deepseek with the built-in 'general' agent
                     (file created, parent verified the content)
Defect fixed:        model placeholder → 'model: inherit' (templates + 24
                     wrappers regenerated; parity PASS; tests 12/12)
```

### In-repo verification (GREEN where it can be)

```
Unit tests: 12/12 PASS · Parity: N×4 holds (24 wrappers, 0 drift) PASS
Kit + tools only: the smoke runbook/template live in tools/; the finding
in distribution-kit VERIFICATION.md — no root devflow/ changes  PASS
Process hygiene: all experiment servers/procs terminated (port 4199
freed; the user's own claude/opencode untouched)              PASS
```

### Gates

Verification Bolt (rescoped): the runbook/template deliverable — runtime
gates `n/a`; prompt-injection/secret-leak `pass`; hallucination-lint
`pass` (platform findings verified via the `/agent` registry + docs);
behavioral-reproducibility `pass` (the nine runs reproduced the same
honest results); bolt-manifest-validation `pass`.

## 10. Manual interventions

The smoke execution is a **human-run step** by design (SPEC rev 2): the
user runs the runbook in a trusted environment and appends the filled
evidence template — the unblock path is documented in the runbook.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-004-spawn-smoke-test.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~20min (across the rescope) |
| V-Bounce number | 2 |
| Tests created | 12 (tool suite) + the runbook + the evidence template |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] **Human action:** run the smoke in a trusted environment (Claude
      Code interactive / adopting project) and append the filled
      `EVIDENCE.template.md`; the pilot US re-verifies the spawn +
      red-team (DISC-002 §7 #1/#3)
- [ ] Batch approvals: MEM-1612, MEM-1615, MEM-1618, MEM-1624 (blocked,
      history), this MEM + AITL-BOLT-DONE ×4

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
| **review_ready_at** | `2026-08-23T16:44:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the runbook + evidence template + VERIFICATION.md; the nine honest runs; tests/parity; process hygiene; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
