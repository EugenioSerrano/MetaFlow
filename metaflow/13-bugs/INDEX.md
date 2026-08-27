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
| [BUG-001](BUG-001-numeracion-plataforma.md) | Carpetas de plataforma numeradas (.github/agents, .opencode/agents) | high | functional | [US-001.TASK-006](../12-functional/tasks/US-001.TASK-006-fix-numeracion-plataforma.md) | approved |

## 🏁 Fixed / Closed

| ID | Document | Status | Fix MEM | Closed date |
|----|----------|--------|---------|-------------|
| [BUG-020](BUG-020-front-door-raiz-stale.md) | Front door raíz stale: README Avenga DevFlow 5.1 + skill avenga-devflow instalado + AGENTS.md sin sección de proyecto | fixed | [MEM-260827-1632-front-door-raiz.md](../22-memory/MEM-260827-1632-front-door-raiz.md) | 2026-08-27 |
| [BUG-002](BUG-002-schema-version-metodologia.md) | Restos v5 en MetaFlow.md §3.12/§5.16 | fixed | [MEM-260827-0406-fix-schema-version-metodologia.md](../22-memory/MEM-260827-0406-fix-schema-version-metodologia.md) | 2026-08-27 |
| [BUG-003](BUG-003-schema-version-agentes.md) | schema_version "5.0" en agent definitions | fixed | [MEM-260827-0406-fix-schema-version-agentes.md](../22-memory/MEM-260827-0406-fix-schema-version-agentes.md) | 2026-08-27 |
| [BUG-004](BUG-004-schema-version-contradicciones.md) | Contradicciones "5.0" vs "1.0" | fixed | [MEM-260827-0406-fix-schema-version-contradicciones.md](../22-memory/MEM-260827-0406-fix-schema-version-contradicciones.md) | 2026-08-27 |
| [BUG-005](BUG-005-naming-familia-v5.md) | Naming "Manifest family v5" → v1 | fixed | [MEM-260827-0407-fix-naming-familia-v1.md](../22-memory/MEM-260827-0407-fix-naming-familia-v1.md) | 2026-08-27 |
| [BUG-006](BUG-006-placeholders-vacios.md) | Placeholders vacíos (G05) | fixed | [MEM-260827-0407-fix-placeholders-g05.md](../22-memory/MEM-260827-0407-fix-placeholders-g05.md) | 2026-08-27 |
| [BUG-007](BUG-007-prefijo-citl-checkpoints.md) | Prefijo CITL-* → CP-* | fixed | [MEM-260827-0408-fix-prefijo-citl.md](../22-memory/MEM-260827-0408-fix-prefijo-citl.md) | 2026-08-27 |
| [BUG-008](BUG-008-rutas-agentes-51.md) | Rutas *51-agents* vs wrappers reales | fixed | [MEM-260827-0408-fix-rutas-agentes.md](../22-memory/MEM-260827-0408-fix-rutas-agentes.md) | 2026-08-27 |
| [BUG-009](BUG-009-template-report-faltante.md) | TEMPLATE-REPORT.html ausente | fixed | [MEM-260827-0408-fix-template-report.md](../22-memory/MEM-260827-0408-fix-template-report.md) | 2026-08-27 |
| [BUG-010](BUG-010-frontmatter-y-cita.md) | Frontmatter "5.1" y cita | fixed | [MEM-260827-0409-fix-frontmatter-cita.md](../22-memory/MEM-260827-0409-fix-frontmatter-cita.md) | 2026-08-27 |
| [BUG-011](BUG-011-mem-campos-manifest.md) | TEMPLATE-MEM 6 vs 8 campos | fixed | [MEM-260827-0410-fix-mem-campos-manifest.md](../22-memory/MEM-260827-0410-fix-mem-campos-manifest.md) | 2026-08-27 |
| [BUG-012](BUG-012-ejemplos-inconsistentes.md) | Ejemplos inconsistentes | fixed | [MEM-260827-0410-fix-ejemplos-inconsistentes.md](../22-memory/MEM-260827-0410-fix-ejemplos-inconsistentes.md) | 2026-08-27 |
| [BUG-013](BUG-013-migracion-agentes-corrupta.md) | Migración condensada corrupta en agent definitions | fixed | [MEM-260827-1034-fix-migracion-agentes.md](../22-memory/MEM-260827-1034-fix-migracion-agentes.md) | 2026-08-27 |
| [BUG-014](BUG-014-g05-wrappers-corrupto.md) | G05 interno de wrappers corrupto | fixed | [MEM-260827-1034-fix-g05-wrappers.md](../22-memory/MEM-260827-1034-fix-g05-wrappers.md) | 2026-08-27 |
| [BUG-015](BUG-015-tautologias-citl.md) | Tautologías CITL en §3.0 | fixed | [MEM-260827-1034-fix-tautologias-citl.md](../22-memory/MEM-260827-1034-fix-tautologias-citl.md) | 2026-08-27 |
| [BUG-016](BUG-016-template-report-anuncios.md) | TEMPLATE-REPORT anunciado en MetaFlow.md/README | fixed | [MEM-260827-1034-fix-template-report-anuncios.md](../22-memory/MEM-260827-1034-fix-template-report-anuncios.md) | 2026-08-27 |
| [BUG-017](BUG-017-citl-asterisco-checkpoint.md) | "CITL-*" como nombre de checkpoint | fixed | [MEM-260827-1034-fix-citl-asterisco.md](../22-memory/MEM-260827-1034-fix-citl-asterisco.md) | 2026-08-27 |
| [BUG-018](BUG-018-g05-pre-v5-citl.md) | G05 "pre-v5 CITL-* names" | fixed | [MEM-260827-1034-fix-g05-pre-v5.md](../22-memory/MEM-260827-1034-fix-g05-pre-v5.md) | 2026-08-27 |
| [BUG-019](BUG-019-seccion-516-linaje-mezclado.md) | §5.16 linaje mezclado | fixed | [MEM-260827-1034-fix-516-linaje.md](../22-memory/MEM-260827-1034-fix-516-linaje.md) | 2026-08-27 |

---

**Last updated:** August 2026
