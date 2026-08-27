---
topic: ""           # stakeholders | market | competitors | compliance | business-model | success-metrics
date: "YYYY-MM-DD"
author: ""          # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""             # LLM used for the first draft
status: "draft"     # draft | stable | deprecated
sources: []         # interview IDs, document refs
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — descriptions,
  context, rationale, placeholder text — goes in the project's
  content_language. See devflow/README.md -> Language policy.
  `AITL-*-Approval` codes are never translated.
-->

# [Topic] — [Short title]

## 1. Summary

[One paragraph: what this document covers and why it matters now.]

## 2. Content

> Pick the structure that fits the topic. Examples below.

### Stakeholders example

| Stakeholder | Role (sponsor/user/impacted/regulator) | Influence (H/M/L) | Interest (H/M/L) | Key concern |
|-------------|----------------------------------------|:----------------:|:----------------:|-------------|
|             |                                        |                  |                  |             |

### Success metrics example

| Metric | Linked vision outcome | Definition | Baseline | Target | Owner |
|--------|-----------------------|------------|----------|--------|-------|
|        |                       |            |          |        |       |

### Compliance example

| Regulation | Scope | Applies because… | Key obligation | Linked ADR/RISK |
|------------|-------|------------------|----------------|------------------|
|            |       |                  |                |                  |

## 3. Sources

| Source | Where |
|--------|-------|
| INT-NNN | `input/interviews/INT-NNN.md` |
| Doc    | `input/documentation/...`     |

## 4. Open questions / Follow-ups

- [ ] …
- [ ] …

## 5. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial version | @user |
