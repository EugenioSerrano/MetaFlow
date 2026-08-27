# Bugs — Index

**Methodology version:** 5.1

Confirmed defects (`BUG-NNN`) with evidence, reproduction conditions,
expected/actual result, impact and severity. Each approved BUG has
**exactly one dedicated Bolt** and is fixed via strict TDD inside ONE
V-Bounce (red evidence → fix → green). No Bolt may be created before
`AITL-BUG-Approval`.

---

## 🟡 Draft (pending AITL-BUG-Approval)

| ID | Document | Severity | Nature | Detected in |
|----|----------|----------|--------|-------------|
| —  | —        | —        | —      | —           |

## ✅ Approved / 🔄 In-fix (Bolt created or executing)

| ID | Document | Severity | Nature | Dedicated Bolt | Status |
|----|----------|----------|--------|----------------|--------|
| [BUG-001](BUG-001-numeracion-plataforma.md) | Las reglas PN numeran `.github/agents` y `.opencode/agents` | high | functional | US-001.BOLT-006 | approved |

## 🏁 Fixed / Closed

| ID | Document | Status | Fix MEM | Closed date |
|----|----------|--------|---------|-------------|
| [BUG-002](BUG-002-schema-version-metodologia.md) | MetaFlow.md §3.12/§5.16 declaran schema_version "5.0" y migración corrupta | fixed | MEM-260827-0406 (BOLT-007) | 2026-08-27 |
| [BUG-003](BUG-003-schema-version-agentes.md) | Los 4 agent definitions instruyen schema_version "5.0" | fixed | MEM-260827-0406 (BOLT-008) | 2026-08-27 |
| [BUG-004](BUG-004-schema-version-contradicciones.md) | Contradicciones "5.0" vs "1.0" dentro del mismo documento | fixed | MEM-260827-0406 (BOLT-009) | 2026-08-27 |
| [BUG-005](BUG-005-naming-familia-v5.md) | Restos de naming "Manifest family v5" / "Schema family v5" | fixed | MEM-260827-0407 (BOLT-010) | 2026-08-27 |
| [BUG-006](BUG-006-placeholders-vacios.md) | Placeholders vacíos "The  is invalid" — incluida la regla G05 | fixed | MEM-260827-0407 (BOLT-011) | 2026-08-27 |
| [BUG-007](BUG-007-prefijo-citl-checkpoints.md) | Prefijo no canónico CITL-* como nombre de checkpoint | fixed | MEM-260827-0408 (BOLT-012) | 2026-08-27 |
| [BUG-008](BUG-008-rutas-agentes-51.md) | Rutas *51-agents* documentadas vs wrappers reales (.agents/, .github/agents/, .opencode/agents/) | fixed | MEM-260827-0408 (BOLT-013) | 2026-08-27 |
| [BUG-009](BUG-009-template-report-faltante.md) | TEMPLATE-REPORT.html anunciado pero ausente | fixed | MEM-260827-0408 (BOLT-014) | 2026-08-27 |
| [BUG-010](BUG-010-frontmatter-y-cita.md) | Frontmatter version "5.1" y autor vacío en la cita | fixed | MEM-260827-0409 (BOLT-015) | 2026-08-27 |
| [BUG-011](BUG-011-mem-campos-manifest.md) | TEMPLATE-MEM describe delivery_loops[] con 6 campos (schema exige 8) | fixed | MEM-260827-0410 (BOLT-016) | 2026-08-27 |
| [BUG-012](BUG-012-ejemplos-inconsistentes.md) | Ejemplos inconsistentes: español en §3.12 y write_paths del repo de distribución | fixed | MEM-260827-0410 (BOLT-017) | 2026-08-27 |
| [BUG-013](BUG-013-migracion-agentes-corrupta.md) | Sección de migración condensada corrupta en los 4 agent definitions | fixed | MEM-260827-1034 (BOLT-018) | 2026-08-27 |
| [BUG-014](BUG-014-g05-wrappers-corrupto.md) | G05 interno de los 4 agent definitions corrupto (placeholder + canónico mal declarado) | fixed | MEM-260827-1034 (BOLT-019) | 2026-08-27 |
| [BUG-015](BUG-015-tautologias-citl.md) | Tautologías CITL en MetaFlow.md §3.0 ("CITL is the default case of CITL") | fixed | MEM-260827-1034 (BOLT-020) | 2026-08-27 |
| [BUG-016](BUG-016-template-report-anuncios.md) | TEMPLATE-REPORT.html sigue anunciado en MetaFlow.md §5.12 y README.md | fixed | MEM-260827-1034 (BOLT-021) | 2026-08-27 |
| [BUG-017](BUG-017-citl-asterisco-checkpoint.md) | "CITL-*" usado como nombre de checkpoint (test-cases README, GUARDRAILS T12) | fixed | MEM-260827-1034 (BOLT-022) | 2026-08-27 |
| [BUG-018](BUG-018-g05-pre-v5-citl.md) | G05 declara "pre-v5 `CITL-*` names" como legacy (CITL es el concepto vigente) | fixed | MEM-260827-1034 (BOLT-023) | 2026-08-27 |
| [BUG-019](BUG-019-seccion-516-linaje-mezclado.md) | §5.16: narrativa del linaje previo mezclada con el presente del kit | fixed | MEM-260827-1034 (BOLT-024) | 2026-08-27 |

---

**Last updated:** August 2026
