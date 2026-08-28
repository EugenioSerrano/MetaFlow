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
| [US-001](user-stories/US-001-toolkit-transformacion.md) | Toolkit de transformación del kit (AvengaDevFlow → MetaFlow) | Pipeline input-kit → distribution-kit con diccionario, verificador y reporte (MVP; 5 SP) — **CP-US-Approval 2026-08-27** |

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
| [US-001.TASK-001](tasks/US-001.TASK-001-engine-transformacion.md) | Engine de transformación + CLI (dry-run y ejecución real) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-002](tasks/US-001.TASK-002-verificador-reporte.md) | Verificador de tokens prohibidos + reporte + aceptación E2E | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-003](tasks/US-001.TASK-003-versionado-y-limpieza.md) | Versionado −4 y limpieza de referencias (VERSION, Methodology version, v5.1, Accelerate) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-004](tasks/US-001.TASK-004-numeracion-carpetas-kit.md) | Numeración de carpetas internas del kit por ciclo de uso (ADR-002) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-005](tasks/US-001.TASK-005-correccion-numeracion.md) | Corrección del sobre-match de numeración + rename 32-adv-reviews (REV-002, ADR-003) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-006](tasks/US-001.TASK-006-fix-numeracion-plataforma.md) | Fix BUG-001: no numerar las carpetas de plataforma (.github, .opencode) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-007](tasks/US-001.TASK-007-fix-schema-version-metodologia.md) | Fix BUG-002: restos del linaje v5 en MetaFlow.md §3.12/§5.16 (schema_version "5.0", migración corrupta) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-008](tasks/US-001.TASK-008-fix-schema-version-agentes.md) | Fix BUG-003: schema_version "5.0" en los 4 agent definitions | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-009](tasks/US-001.TASK-009-fix-schema-version-contradicciones.md) | Fix BUG-004: contradicciones "5.0" vs "1.0" de schema_version en 23-metrics/README, TEMPLATE-US, TEMPLATE-TC | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-010](tasks/US-001.TASK-010-fix-naming-familia-v1.md) | Fix BUG-005: restos de naming "Manifest family v5" / "Schema family v5" | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-011](tasks/US-001.TASK-011-fix-placeholders-g05.md) | Fix BUG-006: placeholders vacíos "The  is invalid" — incluida la regla G05 | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-012](tasks/US-001.TASK-012-fix-prefijo-citl.md) | Fix BUG-007: prefijo no canónico CITL-* en checkpoints (README, TEMPLATE-SPEC) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-013](tasks/US-001.TASK-013-fix-rutas-agentes.md) | Fix BUG-008: rutas *51-agents* documentadas vs wrappers reales | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-014](tasks/US-001.TASK-014-fix-template-report.md) | Fix BUG-009: TEMPLATE-REPORT.html anunciado pero ausente en 42-reports/ | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-015](tasks/US-001.TASK-015-fix-frontmatter-cita.md) | Fix BUG-010: frontmatter version "5.1" y autor vacío en la cita del MetaFlow.md | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-016](tasks/US-001.TASK-016-fix-mem-campos-manifest.md) | Fix BUG-011: TEMPLATE-MEM con 6 de 8 campos de delivery_loops[] | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-017](tasks/US-001.TASK-017-fix-ejemplos-inconsistentes.md) | Fix BUG-012: ejemplos inconsistentes (español en §3.12 y write_paths del repo de distribución) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-018](tasks/US-001.TASK-018-fix-migracion-agentes.md) | Fix BUG-013: sección de migración condensada corrupta en los 4 agent definitions | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-019](tasks/US-001.TASK-019-fix-g05-wrappers.md) | Fix BUG-014: G05 interno de los 4 agent definitions corrupto | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-020](tasks/US-001.TASK-020-fix-tautologias-citl.md) | Fix BUG-015: tautologías CITL en MetaFlow.md §3.0 | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-021](tasks/US-001.TASK-021-fix-template-report-anuncios.md) | Fix BUG-016: TEMPLATE-REPORT.html sigue anunciado en MetaFlow.md §5.12 y README.md | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-022](tasks/US-001.TASK-022-fix-citl-asterisco.md) | Fix BUG-017: "CITL-*" usado como nombre de checkpoint | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-023](tasks/US-001.TASK-023-fix-g05-pre-v5.md) | Fix BUG-018: G05 declara "pre-v5 `CITL-*` names" como legacy | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-024](tasks/US-001.TASK-024-fix-516-linaje.md) | Fix BUG-019: §5.16 narrativa del linaje mezclada con el presente | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-025](tasks/US-001.TASK-025-front-door-raiz.md) | Fix BUG-020: front door de la raíz — README MetaFlow con dos particiones, AGENTS.md con sección de proyecto, remoción del skill avenga-devflow | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-026](tasks/US-001.TASK-026-fix-historia-linaje.md) | Fix BUG-021: historia del linaje previo declarada como tal (v4.2/4.1) en el kit | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-027](tasks/US-001.TASK-027-fix-shorthands-metricas.md) | Fix BUG-022: shorthands de checkpoints no canónicos en tablas de métricas | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-028](tasks/US-001.TASK-028-fix-propiedad-identidad.md) | Fix BUG-023: declaración de propiedad con la entidad real (Eugenio Serrano) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-029](tasks/US-001.TASK-029-fix-tools-linaje.md) | Fix BUG-024: resto del linaje en tools/ (BUILD.md/README -> metaflow/bin) | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |
| [US-001.TASK-030](tasks/US-001.TASK-030-fix-skill-metaflow.md) | Fix BUG-025: codificar el rename de la skill ai-sdlc → MetaFlow en el pipeline (kit reproducible) + restaurar la sección de proyecto de AGENTS.md raíz | US-001 | **Done** (CP-TASK-DONE-Approval 2026-08-27) |

### Non-functional TASKs (`US-000.TASK-NNN`)

| ID | Document | State |
|----|----------|-------|
| [US-000.TASK-001](tasks/US-000.TASK-001-ubicacion-mapping-json.md) | Traslado de `mapping.json` a `src/` — toolkit autocontenido (ADR-004) | Development Completed (CP-MEM-Approval 2026-08-28) |

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
