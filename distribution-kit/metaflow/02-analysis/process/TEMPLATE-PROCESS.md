---
id: "PROC-NNN"
process: ""
date: "YYYY-MM-DD"          # document date — a process is not a point-in-time event
author: ""              # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""                 # LLM used (e.g. "Claude Sonnet", "GPT")
status: "draft"         # draft | active | deprecated (process/ uses active, not stable — see README)
participants: []        # roles involved
domain_entities: []     # entities touched (from domain-model/)
sources: []             # INT-NNN, documentation references
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — descriptions,
  steps, decisions, exceptions — goes in the project's content_language.
  See metaflow/README.md -> Language policy.
  `CP-*-Approval` codes are never translated.
-->

# PROC-NNN — [Process name]

## 1. Description

[What this process achieves and when it is triggered.]

## 2. Trigger

[Event or condition that starts the process.]

## 3. Participants

- **[Role 1]** — what they do in this process.
- **[Role 2]** — what they do in this process.

## 4. Domain entities involved

| Entity     | Operation (CRUD) | Notes |
|------------|:----------------:|-------|
| `Entity1`  | C/R/U/D          |       |
| `Entity2`  | R                |       |

> Link entities to `../domain-model/entities/<Entity>.md`.

## 5. BPMN diagram (Mermaid)

```mermaid
flowchart TB
    A["Start"] --> B{"Decision?"}
    B -->|Yes| C["Activity C"]
    B -->|No|  D["Activity D"]
    C --> E["End"]
    D --> E
```

## 6. Business rules

- [Rule 1 — link to `../glossary/` if it introduces a term]
- [Rule 2]

## 7. Exceptions and alternative paths

- **[Exception 1]** — what triggers it, how it is handled, who intervenes.
- **[Exception 2]** — …

## 8. Process metrics

| Metric                     | Target            | Measurement frequency |
|----------------------------|-------------------|-----------------------|
| Average execution time     | [X min / hours]   | daily / weekly        |
| Success rate               | [%]               | weekly                |
| Volume                     | [N per period]    | daily                 |

## 9. Traceability

- **Derived User Stories:** US-NNN, US-NNN
- **Related ADRs:** ADR-NNN
- **Source interviews:** `../../01-input/interviews/INT-NNN.md`

## 10. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial draft | @user |
