# Open Questions — Index

**Methodology version:** 1.1

Centralized backlog of analysis-phase open questions. See
[README.md](README.md) for lifecycle, rules and templates.

> **Sunset rule (G35):** before `CP-TASK-READY-Approval` (readiness), every
> OQ whose `targets` include that TASK's parent US or one of its governing
> artifacts must be `answered`, `deferred` or `dropped`. No `open` /
> `in-validation` OQ may survive into delivery.

---

## 🔴 Open (not yet investigated)

| ID     | Title | Priority | Status | Owner | Targets | Opened |
|--------|-------|----------|--------|-------|---------|--------|
| —      | —     | —        | —      | —     | —       | —      |

## 🔄 In validation / Deferred

| ID | Title | Revisit on | Owner | Reason |
|----|-------|------------|-------|--------|
|    |       |            |       |        |

## 🏁 Answered

| ID | Title | Status   | Closed on  | Closed by | Resolution / target |
|----|-------|----------|------------|-----------|---------------------|
| [OQ-001](OQ-001-idioma-del-kit.md) | ¿En qué idioma se genera el kit de salida? | answered | 2026-08-27 | @eugenioserrano | Opción A — el kit hereda el idioma del input (`en`); la transformación es solo de nombres |
| [OQ-002](OQ-002-licencia.md) | ¿Cuál es la licencia final de MetaFlow? | answered | 2026-08-27 | @eugenioserrano | Opción A — licencia propietaria a nombre de Eugenio Serrano (todos los derechos reservados); materialización en scope X1 |
| [OQ-003](OQ-003-migracion-arbol-raiz.md) | ¿El árbol metaflow/ raíz se migra a MetaFlow? | answered | 2026-08-27 | @eugenioserrano | Opción B — migrar cuando el kit esté estable, vía §5.16; numeración de salida = entrada − 4 (5.1 → 1.1) |
| [OQ-004](OQ-004-futuras-versiones.md) | ¿Cómo se absorben futuras versiones de AvengaDevFlow con contenido nuevo? | answered | 2026-08-27 | @eugenioserrano | Opción A — re-transformación completa por versión; contenido nuevo vía diccionario extendido (`mapping.json`) |

## ⛔ Dropped (no longer relevant — not an answer)

| ID | Title | Status  | Closed on  | Closed by | Reason |
|----|-------|---------|------------|-----------|--------|
|    |       | dropped | YYYY-MM-DD | @user     |        |

---

## Counters

| Status        | Count |
|---------------|-------|
| open          | 0     |
| in-validation | 0     |
| answered      | 4     |
| deferred      | 0     |
| dropped       | 0     |
| **total**     | **4** |

> Update counters whenever an OQ changes state.

---

**Last updated:** August 2026
