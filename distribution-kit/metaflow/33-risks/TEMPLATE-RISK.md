---
id: "RISK-NNN"
title: ""
date: "YYYY-MM-DD"
author: "" # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: "" # LLM model used (e.g. "Claude Sonnet", "GPT")
category: "" # technical | integration | security | performance | team | process
probability: "" # high | medium | low
impact: "" # critical | high | medium | low
overall_severity: "" # low | medium | high | critical (probability × impact)
status: "open" # open | mitigated | materialized | closed
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  mitigation plans — goes in the project's content_language (declared in
  metaflow/LANGUAGE).
-->

# RISK-NNN — [Descriptive title]

| Field           | Value |
|-----------------|-------|
| **Category**    | [technical / integration / security / performance / team / process] |
| **Probability** | [🔴 High / 🟡 Medium / 🟢 Low] |
| **Impact**      | [🔴 Critical / 🔴 High / 🟡 Medium / 🟢 Low] |
| **Overall severity** | [low / medium / high / critical (probability × impact)] |
| **Status**      | [open / mitigated / materialized / closed] |

---

## 1. Description

[What could happen and in which context. Clear risk description.]

---

## 2. Analysis

[Justification for the assigned probability and impact. Evidence.]

---

## 3. Mitigation plan

[Proactive actions to reduce probability or impact.]

1. [Action 1]
2. [Action 2]

---

## 4. Contingency plan

[What to do if the risk materializes.]

1. [Reactive action 1]
2. [Reactive action 2]

---

## 5. Impact on TASK risk class (§3.3)

If this risk applies to a specific TASK or set of TASKs, it influences the
TASK's `risk_class`, assigned during **`CP-TASK-READY-Approval`** (as part of its
DoR) and recorded in the **TASK frontmatter**. `risk_class` may be escalated
at any subsequent review (QA/Sec); it can **never be reduced after the first
MEM approval** without formal re-review and re-approval of the TASK; every
reassignment appends to `risk_history` (§3.3, GUARDRAILS W14). The manifest
does not duplicate risk data (§3.12):

| TASK risk_class | Default autonomy | Min approvers at CP-MEM-Approval | AREV |
|-----------------|-----------------|-------------------------------------|------|
| low        | L3 (Autonomous) | 1 (executing Dev-validator) | optional |
| medium     | L3 (Autonomous) | 1 (executing Dev-validator) | optional |
| high       | L2 (Bounded)    | 1 (the executing Dev-validator; QA/Sec optional) | optional |
| critical   | L1 (Suggest)    | 1 (the executing Dev-validator; QA/Sec optional) | optional |

> AREV is optional for all risk classes — stakeholder-triggered, never
> automatic (§2.15).

---

## 6. Relations

- **Related DISCs:** [links]
- **Related ADRs:** [links]
- **Related REVs:** [links]
- **Related BUGs:** [links]
- **Related INCs:** [links if risk materialized]
