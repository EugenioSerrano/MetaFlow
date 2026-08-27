---
enum: "EnumName"
label: "Human-readable name"
module: ""           # bounded context / module — or "general"
date: "YYYY-MM-DD"
author: ""           # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""              # LLM used (e.g. "Claude Sonnet")
status: "draft"      # draft | stable | deprecated
sources: []          # INT-NNN, documentation references
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — descriptions,
  value definitions — goes in the project's content_language. See
  devflow/README.md -> Language policy.
  `AITL-*-Approval` codes are never translated.
-->

# EnumName

## 1. Description

> What this enumeration represents in the business domain and when it is
> used.

## 2. Values

| Value      | Description                |
|------------|----------------------------|
| `VALUE_1`  | Description of value 1     |
| `VALUE_2`  | Description of value 2     |

## 3. Used by

| Entity | Property |
|--------|----------|
| `EntityName` | `propertyName` |

## 4. Notes

- *(Optional: legacy code mapping, sort order, extensibility rules,
  terminal vs. transitional states, etc.)*

## 5. Sources

| Source  | Where |
|---------|-------|
| INT-NNN | `../../../input/interviews/INT-NNN.md` |

## 6. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial draft | @user |
