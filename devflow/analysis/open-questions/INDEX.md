# Open Questions — Index

**Methodology version:** 5.0

Centralized backlog of analysis-phase open questions. See
[README.md](README.md) for lifecycle, rules and templates.

> **Sunset rule (G35):** before `AITL-BOLT-READY-Approval` (readiness), every
> OQ whose `targets` include that Bolt's parent US or one of its governing
> artifacts must be `answered`, `deferred` or `dropped`. No `open` /
> `in-validation` OQ may survive into delivery.

---

## 🔴 Open (not yet investigated)

| ID     | Title | Priority | Status | Owner | Targets | Opened |
|--------|-------|----------|--------|-------|---------|--------|
| *(empty — all questions answered 2026-08-27)* | | | | | | |

## 🔄 In validation / Deferred

| ID | Title | Revisit on | Owner | Reason |
|----|-------|------------|-------|--------|
|    |       |            |       |        |

## 🏁 Answered

| ID     | Title | Status   | Closed on  | Closed by | Resolution / target |
|----|-------|----------|------------|-----------|---------------------|
| [OQ-001](OQ-001-idioma-del-kit.md) | ¿En qué idioma se genera el kit de salida? | answered | 2026-08-27 | eugenioserrano | Heredar `en` — el kit queda en inglés |
| [OQ-002](OQ-002-licencia.md) | ¿Cuál es la licencia final de MetaFlow? | answered | 2026-08-27 | eugenioserrano | Propietaria a nombre de Eugenio Serrano |
| [OQ-003](OQ-003-migracion-arbol-raiz.md) | ¿El devflow/ raíz se migra a MetaFlow? | answered | 2026-08-27 | eugenioserrano | Migrar cuando el kit esté estable (§5.16); versión de salida = entrada − 4 (5.1 → 1.1) |
| [OQ-004](OQ-004-futuras-versiones.md) | ¿Cómo se absorben futuras versiones con contenido nuevo? | answered | 2026-08-27 | eugenioserrano | Re-transformación completa por versión |

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
