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
| [US-001.BOLT-007](bolts/US-001.BOLT-007-fix-schema-version-metodologia.md) | Fix BUG-002: restos v5 en MetaFlow.md §3.12/§5.16 | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-008](bolts/US-001.BOLT-008-fix-schema-version-agentes.md) | Fix BUG-003: schema_version "5.0" en agent definitions | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-009](bolts/US-001.BOLT-009-fix-schema-version-contradicciones.md) | Fix BUG-004: contradicciones "5.0" vs "1.0" | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-010](bolts/US-001.BOLT-010-fix-naming-familia-v1.md) | Fix BUG-005: naming "Manifest family v5" → v1 | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-011](bolts/US-001.BOLT-011-fix-placeholders-g05.md) | Fix BUG-006: placeholders vacíos (G05) | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-012](bolts/US-001.BOLT-012-fix-prefijo-citl.md) | Fix BUG-007: prefijo CITL-* → CP-* | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-013](bolts/US-001.BOLT-013-fix-rutas-agentes.md) | Fix BUG-008: rutas *51-agents* vs wrappers reales | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-014](bolts/US-001.BOLT-014-fix-template-report.md) | Fix BUG-009: TEMPLATE-REPORT.html ausente | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-015](bolts/US-001.BOLT-015-fix-frontmatter-cita.md) | Fix BUG-010: frontmatter "5.1" y cita | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-016](bolts/US-001.BOLT-016-fix-mem-campos-manifest.md) | Fix BUG-011: TEMPLATE-MEM 6 vs 8 campos | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-017](bolts/US-001.BOLT-017-fix-ejemplos-inconsistentes.md) | Fix BUG-012: ejemplos inconsistentes | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-018](bolts/US-001.BOLT-018-fix-migracion-agentes.md) | Fix BUG-013: migración condensada corrupta en agent definitions | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-019](bolts/US-001.BOLT-019-fix-g05-wrappers.md) | Fix BUG-014: G05 interno de wrappers corrupto | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-020](bolts/US-001.BOLT-020-fix-tautologias-citl.md) | Fix BUG-015: tautologías CITL en §3.0 | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-021](bolts/US-001.BOLT-021-fix-template-report-anuncios.md) | Fix BUG-016: TEMPLATE-REPORT anunciado en MetaFlow.md/README | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-022](bolts/US-001.BOLT-022-fix-citl-asterisco.md) | Fix BUG-017: "CITL-*" como nombre de checkpoint | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-023](bolts/US-001.BOLT-023-fix-g05-pre-v5.md) | Fix BUG-018: G05 "pre-v5 CITL-* names" | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |
| [US-001.BOLT-024](bolts/US-001.BOLT-024-fix-516-linaje.md) | Fix BUG-019: §5.16 linaje mezclado | US-001 | **Done** (AITL-BOLT-DONE-Approval 2026-08-27) |

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
