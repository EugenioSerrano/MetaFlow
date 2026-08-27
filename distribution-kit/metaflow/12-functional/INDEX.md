# Functional — Index

**Methodology version:** 1.1

Work definition: feature User Stories (approved at `CP-US-Approval`),
the permanent `US-000-non-functional.md` container (no approval lifecycle),
and the three canonical TASK types (functional / non-functional / test).
Mandatory structure: User Stories in `user-stories/`, TASKs in `tasks/`.
Integration with external SDLC tools (Azure DevOps, Jira, etc.) is team
configuration — the methodology prescribes no mechanism (see README).

---

## 🟡 Draft feature USs (pending CP-US-Approval)

| ID | Document | Description |
|----|----------|-------------|
| —  | —        | —           |

## ✅ Approved feature USs

| ID | Document | Description |
|----|----------|-------------|
| —  | —        | —           |

## Permanent container (US-000)

| ID | Document | Description |
|----|----------|-------------|
| US-000 | [US-000-non-functional.md](user-stories/US-000-non-functional.md) | Non-functional container — always active, no approval lifecycle |

---

## TASKs

> **Source of the next `NNN`.** Sequential TASK numbers are scoped to their
> parent and come from these tables (N02–N04). Check the highest `TASK-NNN`
> under the same parent before creating a new one; archived IDs are never
> reused.

### Functional TASKs (`US-NNN.TASK-NNN`)

| ID | Document | Parent US | State |
|----|----------|-----------|-------|
| —  | —        | —         | —     |

### Non-functional TASKs (`US-000.TASK-NNN`)

| ID | Document | State |
|----|----------|-------|
| —  | —        | —     |

### Test TASKs (`TC-NNN.TASK-NNN`)

| ID | Document | Parent TC | State |
|----|----------|-----------|-------|
| —  | —        | —         | —     |

> State is derived, never stored in the manifest: `In Development` ·
> `Development Completed` (latest MEM approved) · `Done`
> (`CP-TASK-DONE-Approval`). Candidate TASKs awaiting
> `CP-TASK-READY-Approval` are listed with state `candidate`.

---

## ⛔ Deprecated

| ID | Document | Status |
|----|----------|--------|
| —  | —        | —      |

---

**Last updated:** August 2026
