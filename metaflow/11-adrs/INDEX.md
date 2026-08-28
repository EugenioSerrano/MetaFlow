# ADRs — Index

**Methodology version:** 1.1

Architecture Decision Records: brief, immutable documents that capture
significant architectural decisions, their context, alternatives considered
and consequences. An ADR becomes governing only after `CP-ADR-Approval`
(Architect / Tech Lead). Source code is the definitive reference for the
current implementation state; the approved ADR is the governing reference
for the decisions it records.

---

## 🟡 Draft (pending `CP-ADR-Approval`)

| ID | Document | Description |
|----|----------|-------------|
| —  | —        | —           |

## ✅ Accepted

| ID | Document | Description |
|----|----------|-------------|
| [ADR-001](ADR-001-toolkit-transformacion.md) | Toolkit de transformación: Python, librerías y ubicación del código | Python 3 + stdlib únicamente, `src/` como ubicación, `mapping.json` en la raíz — **CP-ADR-Approval 2026-08-27** — parcialmente superado por [ADR-004](ADR-004-ubicacion-mapping-json.md) (ubicación de `mapping.json`; el resto vigente) |
| [ADR-003](ADR-003-ajuste-numeracion-32-adv-reviews.md) | Ajuste del esquema de numeración: `32-adv-reviews` + reglas de contenido con barra | Supersede ADR-002; corrige el sobre-match (REV-002 F-04/F-05) — **CP-ADR-Approval 2026-08-27** |
| [ADR-004](ADR-004-ubicacion-mapping-json.md) | Ubicación de `mapping.json`: traslado a `src/` (toolkit autocontenido) | Supercede parcialmente al ADR-001 (solo la Alternative F); el resto del ADR-001 permanece vigente — **CP-ADR-Approval 2026-08-28** |

## ❌ Rejected

| ID | Document | Reason |
|----|----------|--------|
| —  | —        | —      |

## ⛔ Superseded

| ID | Document | Superseded by |
|----|----------|---------------|
| [ADR-002](_archive/ADR-002-numeracion-carpetas-kit.md) | Numeración de carpetas internas del kit por ciclo de uso — archivado 2026-08-28 (vida cerrada) | [ADR-003](ADR-003-ajuste-numeracion-32-adv-reviews.md) (2026-08-27) |

## ⛔ Deprecated

| ID | Document | Status |
|----|----------|--------|
| —  | —        | —      |

---

**Last updated:** August 2026
