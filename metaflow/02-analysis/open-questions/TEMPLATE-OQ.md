---
id: "OQ-NNN"
title: ""                 # short, imperative — "Can a customer have multiple active subscriptions?"
date: "YYYY-MM-DD"        # date opened
author: ""                # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0) — who spotted the gap
llm: ""                   # LLM used when the AI agent surfaced it (if applicable)
status: "open"            # open | in-validation | answered | deferred | dropped
priority: "P1"            # P0 (blocks analysis closure) | P1 (blocks a specific artifact) | P2 (nice-to-have)
owner: ""                 # person responsible for chasing the answer
validator: ""             # stakeholder who must validate the answer (filled when known)
targets:                  # canonical artifacts this OQ will update once answered
  - "../domain-model/entities/Customer.md"
sources:                  # where the gap surfaced
  - "../../01-input/interviews/INT-007.md"
related: []               # other OQ-NNN / RISK-NNN / ADR-NNN / DISC-NNN
tags: []
revisit_on: ""            # only if status=deferred — date or trigger
closed_on: ""             # YYYY-MM-DD (when status moves to answered/dropped)
closed_by: ""             # who closed it
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — question text,
  context, hypothesis, resolution — goes in the project's content_language.
  See metaflow/README.md -> Language policy.
  `CP-*-Approval` codes are never translated.
-->

# OQ-NNN — [Title]

## 1. Question

> State the question in **one sentence**. Atomic. If you wrote "and" or "or",
> split it into two OQs.

## 2. Context

Why this question matters and how it blocks downstream work.

- **What artifact(s) are blocked?** (link to `targets`)
- **What assumption are we running on until this is answered?**
- **What's the impact if we get it wrong?**

## 3. Hypothesis (working assumption)

Best guess today, used to keep work flowing until the answer arrives.

> Example: *"Assuming a customer can have only one active subscription; if
> wrong, `Customer ↔ Subscription` becomes 1..N and billing logic changes."*

## 4. Options under consideration

| # | Option | Implication | Source |
|---|--------|-------------|--------|
| A |        |             |        |
| B |        |             |        |

## 5. Investigation log (append-only)

| Date       | Author | Note |
|------------|--------|------|
| YYYY-MM-DD | @user  | Opened from interview INT-007, minute 14:32 |
|            |        |      |

## 6. Resolution

Filled in only when status becomes `answered` / `deferred` / `dropped`.

- **Decision:** …
- **Validated by:** @stakeholder on YYYY-MM-DD (source: link)
- **Propagated to:** link to the exact section / commit in each `targets`
  artifact that absorbed the answer.
- **If deferred:** revisit trigger / date and why it does not block now.
- **If dropped:** reason (scope cut, duplicate of OQ-MMM, promoted to
  RISK-NNN / ADR-NNN, …).

## 7. History

| Date       | Change                                         | Author |
|------------|------------------------------------------------|--------|
| YYYY-MM-DD | Opened                                         | @user  |
| YYYY-MM-DD | Status → in-validation (answer drafted)        | @user  |
| YYYY-MM-DD | Status → answered, propagated to `Customer.md` | @user  |
