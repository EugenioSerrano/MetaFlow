# Functional — Index

**Methodology version:** 5.1

Work definition: feature User Stories (approved at `AITL-US-Approval`),
the permanent `US-000-non-functional.md` container (no approval lifecycle),
and the three canonical Bolt types (functional / non-functional / test).
Mandatory structure: User Stories in `user-stories/`, Bolts in `bolts/`.
Integration with external SDLC tools (Azure DevOps, Jira, etc.) is team
configuration — the methodology prescribes no mechanism (see README).

---

## 🟡 Draft feature USs (pending AITL-US-Approval)

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

## Bolts

> **Source of the next `NNN`.** Sequential Bolt numbers are scoped to their
> parent and come from these tables (N02–N04). Check the highest `BOLT-NNN`
> under the same parent before creating a new one; archived IDs are never
> reused.

### Functional Bolts (`US-NNN.BOLT-NNN`)

| ID | Document | Parent US | State |
|----|----------|-----------|-------|
| —  | —        | —         | —     |

### Non-functional Bolts (`US-000.BOLT-NNN`)

| ID | Document | State |
|----|----------|-------|
| —  | —        | —     |

### Test Bolts (`TC-NNN.BOLT-NNN`)

| ID | Document | Parent TC | State |
|----|----------|-----------|-------|
| —  | —        | —         | —     |

> State is derived, never stored in the manifest: `In Development` ·
> `Development Completed` (latest MEM approved) · `Done`
> (`AITL-BOLT-DONE-Approval`). Candidate Bolts awaiting
> `AITL-BOLT-READY-Approval` are listed with state `candidate`.

---

## ⛔ Deprecated

| ID | Document | Status |
|----|----------|--------|
| —  | —        | —      |

---

**Last updated:** August 2026
