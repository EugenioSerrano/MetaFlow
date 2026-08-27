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
| [US-001](user-stories/US-001-toolkit-transformacion.md) | Toolkit de transformación del kit (AvengaDevFlow → MetaFlow) | Pipeline input-kit → distribution-kit con diccionario, verificador y reporte (MVP; 5 SP) — **AITL-US-Approval 2026-08-27** |

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
| [US-001.BOLT-001](bolts/US-001.BOLT-001-engine-transformacion.md) | Engine de transformación + CLI (dry-run y ejecución real) | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-002](bolts/US-001.BOLT-002-verificador-reporte.md) | Verificador de tokens prohibidos + reporte + aceptación E2E | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-003](bolts/US-001.BOLT-003-versionado-y-limpieza.md) | Versionado −4 por contexto + limpieza de citas *Accelerate* + familia de manifests v1 | US-001 | Development Completed (MEM-260827-0217/0225 approved) |
| [US-001.BOLT-004](bolts/US-001.BOLT-004-numeracion-carpetas-kit.md) | Numeración de carpetas internas por ciclo de uso (ADR-002) + test de integridad de links | US-001 | Development Completed (MEM-260827-0244 approved) |
| [US-001.BOLT-005](bolts/US-001.BOLT-005-correccion-numeracion.md) | Corrección del sobre-match de numeración (REV-002) + rename `32-adv-reviews` (ADR-003) | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-006](bolts/US-001.BOLT-006-fix-numeracion-plataforma.md) | Fix BUG-001: no numerar carpetas de plataforma | US-001 | Development Completed (MEM-260827-0308 approved) |

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
