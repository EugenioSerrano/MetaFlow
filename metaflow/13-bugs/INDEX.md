# Bugs — Index

**Methodology version:** 1.1

Confirmed defects (`BUG-NNN`) with evidence, reproduction conditions,
expected/actual result, impact and severity. Each approved BUG has
**exactly one dedicated TASK** and is fixed via strict TDD inside ONE
Delivery Loop (red evidence → fix → green). No TASK may be created before
`CP-BUG-Approval`.

---

## 🟡 Draft (pending CP-BUG-Approval)

| ID | Document | Severity | Nature | Detected in |
|----|----------|----------|--------|-------------|
| —  | —        | —        | —      | —           |

## ✅ Approved / 🔄 In-fix (TASK created or executing)

| ID | Document | Severity | Nature | Dedicated TASK | Status |
|----|----------|----------|--------|----------------|--------|
| —  | —        | —        | —      | —              | —      |

## 🏁 Fixed / Closed

| ID | Document | Status | Fix MEM | Closed date |
|----|----------|--------|---------|-------------|
| [BUG-001](BUG-001-numeracion-plataforma.md) | Las reglas PN numeran las carpetas de plataforma .github/agents y .opencode/agents | fixed | [MEM-260827-0308-bolt006-fix-numeracion-plataforma](../22-memory/MEM-260827-0308-bolt006-fix-numeracion-plataforma.md) | 2026-08-27 |
| [BUG-002](BUG-002-schema-version-metodologia.md) | MetaFlow.md §3.12/§5.16 declaran schema_version "5.0" y la sección de migración 4.0→5.0 quedó corrupta | fixed | [MEM-260827-0406-fix-schema-version-metodologia](../22-memory/MEM-260827-0406-fix-schema-version-metodologia.md) | 2026-08-27 |
| [BUG-003](BUG-003-schema-version-agentes.md) | Los 4 agent definitions del kit instruyen schema_version "5.0" | fixed | [MEM-260827-0406-fix-schema-version-agentes](../22-memory/MEM-260827-0406-fix-schema-version-agentes.md) | 2026-08-27 |
| [BUG-004](BUG-004-schema-version-contradicciones.md) | Contradicciones "5.0" vs "1.0" de schema_version dentro de un mismo documento del kit | fixed | [MEM-260827-0406-fix-schema-version-contradicciones](../22-memory/MEM-260827-0406-fix-schema-version-contradicciones.md) | 2026-08-27 |
| [BUG-005](BUG-005-naming-familia-v5.md) | Restos de naming "Manifest family v5" / "Schema family v5" / "manifest v5" en 8+ archivos del kit | fixed | [MEM-260827-0407-fix-naming-familia-v1](../22-memory/MEM-260827-0407-fix-naming-familia-v1.md) | 2026-08-27 |
| [BUG-006](BUG-006-placeholders-vacios.md) | Placeholders vacíos "The  is invalid" en 7 lugares del kit — incluida la regla G05 | fixed | [MEM-260827-0407-fix-placeholders-g05](../22-memory/MEM-260827-0407-fix-placeholders-g05.md) | 2026-08-27 |
| [BUG-007](BUG-007-prefijo-citl-checkpoints.md) | Prefijo no canónico CITL-* usado como nombre de checkpoint en README y TEMPLATE-SPEC | fixed | [MEM-260827-0408-fix-prefijo-citl](../22-memory/MEM-260827-0408-fix-prefijo-citl.md) | 2026-08-27 |
| [BUG-008](BUG-008-rutas-agentes-51.md) | Rutas documentadas *51-agents* no coinciden con los wrappers reales (.agents/, .github/agents/, .opencode/agents/) | fixed | [MEM-260827-0408-fix-rutas-agentes](../22-memory/MEM-260827-0408-fix-rutas-agentes.md) | 2026-08-27 |
| [BUG-009](BUG-009-template-report-faltante.md) | TEMPLATE-REPORT.html anunciado en 42-reports/README pero ausente del kit | fixed | [MEM-260827-0408-fix-template-report](../22-memory/MEM-260827-0408-fix-template-report.md) | 2026-08-27 |
| [BUG-010](BUG-010-frontmatter-y-cita.md) | MetaFlow.md con frontmatter version "5.1" y autor vacío en la cita del paper | fixed | [MEM-260827-0409-fix-frontmatter-cita](../22-memory/MEM-260827-0409-fix-frontmatter-cita.md) | 2026-08-27 |
| [BUG-011](BUG-011-mem-campos-manifest.md) | TEMPLATE-MEM describe delivery_loops[] con 6 campos; el schema exige 8 | fixed | [MEM-260827-0410-fix-mem-campos-manifest](../22-memory/MEM-260827-0410-fix-mem-campos-manifest.md) | 2026-08-27 |
| [BUG-012](BUG-012-ejemplos-inconsistentes.md) | Ejemplos inconsistentes: comentario en español en §3.12 y write_paths con paths del repo de distribución | fixed | [MEM-260827-0410-fix-ejemplos-inconsistentes](../22-memory/MEM-260827-0410-fix-ejemplos-inconsistentes.md) | 2026-08-27 |
| [BUG-013](BUG-013-migracion-agentes-corrupta.md) | Sección de migración condensada corrupta en los 4 agent definitions | fixed | [MEM-260827-1034-fix-migracion-agentes](../22-memory/MEM-260827-1034-fix-migracion-agentes.md) | 2026-08-27 |
| [BUG-014](BUG-014-g05-wrappers-corrupto.md) | G05 interno de los 4 agent definitions corrupto (placeholder y canónico mal declarado) | fixed | [MEM-260827-1034-fix-g05-wrappers](../22-memory/MEM-260827-1034-fix-g05-wrappers.md) | 2026-08-27 |
| [BUG-015](BUG-015-tautologias-citl.md) | Tautologías del fundamento CITL en MetaFlow.md §3.0 ("CITL is the default case of CITL") | fixed | [MEM-260827-1034-fix-tautologias-citl](../22-memory/MEM-260827-1034-fix-tautologias-citl.md) | 2026-08-27 |
| [BUG-016](BUG-016-template-report-anuncios.md) | TEMPLATE-REPORT.html sigue anunciado en MetaFlow.md §5.12 y README.md (Known Limitations) | fixed | [MEM-260827-1034-fix-template-report-anuncios](../22-memory/MEM-260827-1034-fix-template-report-anuncios.md) | 2026-08-27 |
| [BUG-017](BUG-017-citl-asterisco-checkpoint.md) | "CITL-*" usado como nombre de checkpoint en 24-tests/test-cases/README.md y GUARDRAILS T12 | fixed | [MEM-260827-1034-fix-citl-asterisco](../22-memory/MEM-260827-1034-fix-citl-asterisco.md) | 2026-08-27 |
| [BUG-018](BUG-018-g05-pre-v5-citl.md) | G05 del GUARDRAILS declara "the pre-v5 `CITL-*` names" como legacy (CITL es el concepto vigente) | fixed | [MEM-260827-1034-fix-g05-pre-v5](../22-memory/MEM-260827-1034-fix-g05-pre-v5.md) | 2026-08-27 |
| [BUG-019](BUG-019-seccion-516-linaje-mezclado.md) | §5.16: narrativa del linaje previo (3.0→4.0→5.0) mezclada con el presente del kit | fixed | [MEM-260827-1034-fix-516-linaje](../22-memory/MEM-260827-1034-fix-516-linaje.md) | 2026-08-27 |
| [BUG-020](BUG-020-front-door-raiz-stale.md) | Front door de la raíz stale tras la migración: README.md aún describe Avenga DevFlow 5.1, sin modelo de dos particiones, y el skill .agents/skills/avenga-devflow quedó instalado | fixed | [MEM-260827-1632-front-door-raiz](../22-memory/MEM-260827-1632-front-door-raiz.md) | 2026-08-27 |
| [BUG-021](BUG-021-historia-linaje-previo.md) | Historia del linaje previo presentada como historia propia del kit: "removed in v4.2" (17 ubicaciones) y "versions up to 4.1 shipped one inside metaflow/" (4 agent definitions) | fixed | [MEM-260827-1725-fix-historia-linaje](../22-memory/MEM-260827-1725-fix-historia-linaje.md) | 2026-08-27 |
| [BUG-022](BUG-022-shorthands-checkpoints-metricas.md) | Shorthands de checkpoints no canónicos en tablas de métricas: "TASK TASK-DONE" y "TASK-DONE - TASK-READY" sin CP-* ni backticks | fixed | [MEM-260827-1725-fix-shorthands-metricas](../22-memory/MEM-260827-1725-fix-shorthands-metricas.md) | 2026-08-27 |
| [BUG-023](BUG-023-propiedad-identidad.md) | Declaración de propiedad con entidad inexistente: "of Eugenio Serrano LATAM" — la entidad es Eugenio Serrano (decisión del propietario 2026-08-27) | fixed | [MEM-260827-1725-fix-propiedad-identidad](../22-memory/MEM-260827-1725-fix-propiedad-identidad.md) | 2026-08-27 |
| [BUG-024](BUG-024-tools-linaje-devflow.md) | Restos del linaje en el tooling del workshop: tools/BUILD.md y tools/README.md referencian "devflow" y "distribution-kit/devflow/bin/" (carpeta inexistente en el kit) | fixed | [MEM-260827-1725-fix-tools-linaje](../22-memory/MEM-260827-1725-fix-tools-linaje.md) | 2026-08-27 |
| [BUG-025](BUG-025-skill-metaflow-no-reproducible.md) | Skill renombrada ai-sdlc → MetaFlow solo a mano (el pipeline sigue generando ai-sdlc — el kit no es reproducible) y sección de proyecto de AGENTS.md raíz vaciada (suite en rojo) | closed | [MEM-260827-2238-fix-skill-metaflow](../22-memory/MEM-260827-2238-fix-skill-metaflow.md) | 2026-08-27 |

---

**Last updated:** August 2026
