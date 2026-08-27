---
id: "INC-NNN"
date: "YYYY-MM-DDTHH:mm:ss±HH:MM"  # point-in-time event: incident detection
severity: "sev3"    # sev1 | sev2 | sev3 | sev4
service: ""
author: ""          # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""             # LLM used for first draft (e.g. "Claude Sonnet")
status: "open"      # open | mitigated | closed
detected_at: ""     # ISO-8601 — detection (feeds D3 recovery time)
resolved_at: ""     # ISO-8601 — resolution (feeds D3 recovery time)
deployment_caused: false # true if this incident was caused by a deployment (feeds D4)
deployment_ref: ""  # deployment ID / tag that introduced the failure (if deployment_caused)
unplanned_rework: false # true if the fix was unplanned production rework (feeds D5)
caused_by_task: null # US-NNN.TASK-NNN if applicable — referential link, no manifest update
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — timeline,
  root cause, resolution — goes in the project's content_language
  (declared in metaflow/LANGUAGE).

  ⚠️ Manifest v1 (§3.12): the TASK manifest carries NO Delivery Flow or incident
  data. The INC links to the originating TASK and deployment referentially;
  Delivery Flow metrics are computed at deployment level from CI/CD + incidents
  (§3.7.1). No single-model attribution is forced (§5.12).
-->

# INC-NNN — [title]

## 1. Summary

[1–2 sentences: what failed, how it was detected, impact.]

## 2. Timeline

| Time (UTC) | Event |
|------------|-------|
| HH:mm | Detection |
| HH:mm | Triage |
| HH:mm | Mitigation |
| HH:mm | Resolution |

## 3. Impact

- Users affected: [#]
- Duration: [N min]
- SLO impacted: [yes/no, which]

## 4. Root cause

[Technical cause + process cause. Blameless.]

## 5. Why did the gates not catch it?

[Specific gap in gates / AREV / DoR / DoD that allowed the failure through.]

## 6. Actions (derived TASKs)

- [ ] US-000.TASK-NNN — [hardening (non-functional under US-000) / new gate / prompt fix / etc.]
- [ ] If a defect is confirmed → BUG → `CP-BUG-Approval` → dedicated TASK (§4.10)

## 7. Origin TASK link

If `caused_by_task` is not null, reference it here (US-NNN.TASK-NNN). The
link is **referential** — the TASK manifest carries no incident/Delivery Flow
fields (§3.12). Deployment-caused incident data feeds D3/D4/D5 from
CI/CD + `34-incidents/` (§3.7.1, §5.12).
