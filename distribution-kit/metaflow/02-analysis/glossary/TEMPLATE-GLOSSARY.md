---
module: ""           # bounded context / module — or "general"
date: "YYYY-MM-DD"
author: ""           # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""              # LLM used (e.g. "Claude Sonnet")
status: "draft"      # draft | stable | deprecated
tags: []
sources: []          # interview IDs, document refs
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. Term definitions and
  descriptions go in the project's content_language. See
  metaflow/README.md -> Language policy.
  `CP-*-Approval` codes are never translated.
-->

# Glossary — [Module / Bounded Context]

> One entry per business term. Keep entries short and concrete.

---

## 1. [Term 1]

| Field | Value |
|-------|-------|
| **Definition**          | [What it means exactly in this project]                |
| **Synonyms**            | [Other words for the same concept]                     |
| **Do not confuse with** | [Similar terms with different meaning]                 |
| **Entity**              | [Link to `../domain-model/entities/<Entity>.md` if any] |
| **Example**             | [Concrete case]                                        |
| **Source**              | [INT-NNN or document]                                  |

---

## 2. [Term 2]

| Field | Value |
|-------|-------|
| **Definition**          |  |
| **Synonyms**            |  |
| **Do not confuse with** |  |
| **Entity**              |  |
| **Example**             |  |
| **Source**              |  |

---

## 3. Banned terms (optional section)

| Banned term | Reason | Use instead |
|-------------|--------|-------------|
|             |        |             |

## 4. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Created | ... |
