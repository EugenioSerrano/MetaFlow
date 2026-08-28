---
id: "ADR-004"
title: "Ubicación de mapping.json: traslado a src/ (toolkit autocontenido)"
date: "2026-08-28"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["Eugenio Serrano — propietario (rol de arquitecto autoasignado: no hay otro titular)"]
sources:
  - "ADR-001-toolkit-transformacion.md (Alternative F)"
  - "../analysis/process/PROC-001-transformacion-kit.md"
  - "../analysis/glossary/metaflow.md"
  - "conversación de diseño 2026-08-28"
supersedes: ["ADR-001"] # parcial: solo la decisión de ubicación del diccionario (Alternative F)
conflicts_with: [] # la decisión que contradice (ubicación de mapping.json) queda resuelta por este supersede
tags: [python, toolkit, transformacion, mapping]
nfrs: [] # sin NFRs nuevos — portability/performance del ADR-001 permanecen
review_ready_at: "2026-08-28T01:00:19-03:00"
review: # CP-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "architect"
      model: null
  started_at: "2026-08-28T01:01:00-03:00"
  decided_at: "2026-08-28T01:01:26-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Aprobación del propietario (rol de arquitecto autoasignado) sin hallazgos — revisión de la propuesta en conversación, 2026-08-28. Supercede parcialmente al ADR-001 (Alternative F)"
---

# ADR-004 — Ubicación de `mapping.json`: traslado a `src/`

| Field          | Value |
|----------------|-------|
| **Status**     | accepted (`CP-ADR-Approval` 2026-08-28) |
| **Decision-makers** | Eugenio Serrano (propietario) |
| **Sources**    | ADR-001 (Alternative F), PROC-001, glossary/metaflow.md, conversación de diseño 2026-08-28 |
| **Supersedes** | ADR-001 — **parcial**: únicamente la decisión de ubicación del diccionario (Alternative F); el resto del ADR-001 (Python 3 + stdlib, código en `src/`, salidas, tests) permanece vigente |
| **Conflicts with** | None — la decisión que contradice queda resuelta por este supersede (§2.8) |

---

## 1. Context

El ADR-001 (aprobado) fijó `mapping.json` en la **raíz del repositorio** con
la Alternative F: los datos quedan separados del código (RULE-04: agregar
reglas sin tocar el engine), visibles y editables directamente por el
mantenedor. El propio ADR registró el costo de esa elección: *"el toolkit no
queda 100 % autocontenido en `src/` (aceptable: el repo completo es el
producto)"*.

Con el toolkit en uso, el propietario revisó la estructura y concluyó que ese
costo ya no es aceptable: `mapping.json` en la raíz no tiene relación con los
otros elementos del nivel superior — que son los dos kits (`input-kit/`,
`distribution-kit/`) y los metadatos del repositorio. El diccionario es parte
del **toolkit** (junto a `src/transform.py`, `src/verify.py`, `src/report.py`
y `src/tests/`), no del repo: el pipeline debe ser un todo autocontenido
dentro de `src/`.

Fuerzas en juego:

- **Toolkit autocontenido:** `src/` debe contener todo lo que el pipeline
  necesita para correr: engine, verificador, reporte, diccionario y tests.
- **Raíz limpia:** el nivel superior del repo queda para los kits y los
  metadatos; la raíz no es un directorio de trabajo del pipeline.
- **Reglas como datos (RULE-04):** se preserva — el diccionario sigue siendo
  un archivo de datos JSON (tipo `MappingTable` del domain model), solo
  cambia su ubicación. Agregar una regla sigue sin tocar el engine.
- **CLI ya preparado:** `src/transform.py` acepta `--mapping <ruta>`; el
  default pasa de la raíz a `src/mapping.json`.

## 2. Alternatives considered

### Alternative A — `mapping.json` en `src/` (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | `src/` queda autocontenido (engine + diccionario + tests — el toolkit completo); la raíz queda limpia (solo `input-kit/`, `distribution-kit/` y metadatos del repo); RULE-04 intacta (reglas como datos, ubicación aparte); el CLI ya soporta `--mapping` para rutas alternativas (tests, fixtures); sin cambios de runtime: `python src/transform.py` sigue igual |
| **Cons** | Editar reglas requiere entrar a `src/` (menor: es el toolkit, el mantenedor lo conoce); el toolkit sigue dependiendo del resto del repo para correr (los kits) — el "repo completo es el producto" se mantiene |

### Alternative B — Mantener `mapping.json` en la raíz (status quo)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Visible y editable directamente desde la raíz; no toca código ni tests |
| **Cons** | El toolkit no es autocontenido; la raíz mezcla diccionario del pipeline con los kits y metadatos — el punto que el propietario quiere corregir |

## 3. Decision

Se traslada `mapping.json` de la raíz del repositorio a **`src/mapping.json`**.
`src/` pasa a contener el toolkit completo: engine (`transform.py`),
verificador (`verify.py`), reporte (`report.py`), diccionario
(`mapping.json`) y tests (`tests/`). El default de carga en
`src/transform.py` (`DEFAULT_MAPPING`) se actualiza a `src/mapping.json`; el
flag `--mapping` se conserva para rutas alternativas.

Esta ADR **supercede parcialmente al ADR-001**: reemplaza únicamente la
decisión de la Alternative F (ubicación del diccionario en la raíz). El resto
del ADR-001 permanece vigente: Python 3.10+ con stdlib únicamente, código en
`src/`, salidas (`distribution-kit/` y reportes), tests con `unittest`, NFRs
de performance y portability.

## 4. Consequences

**Positive:**
- `src/` es el toolkit completo y portable: copiar `src/` + los kits permite
  regenerar el kit en cualquier máquina con Python 3.10+.
- La raíz queda con una sola responsabilidad: los kits y los metadatos del
  repositorio.
- El diccionario sigue siendo datos puros (RULE-04) — sin cambios en cómo se
  agregan reglas.

**Trade-offs:**
- El mantenedor edita las reglas en `src/mapping.json` (ruta explícita y
  documentada en README/PROC-001).
- El toolkit por sí solo no es ejecutable sin los kits — igual que hoy
  ("el repo completo es el producto" se mantiene).

**Technical debt:**
- Ninguno nuevo. La ubicación queda registrada en esta ADR; un cambio futuro
  de estructura seguiría el mismo camino (nueva ADR que superceda).

## 5. Applicable NFRs

Sin NFRs nuevos. Los NFRs del ADR-001 (performance < 1 min por ejecución,
portability cero dependencias / Python 3.10+) no cambian con la ubicación del
diccionario.

## 6. References

- ADR-001-toolkit-transformacion.md — decisión original (Alternative F) que
  esta ADR supercede parcialmente.
- `../analysis/process/PROC-001-transformacion-kit.md` — proceso que el
  toolkit implementa (se actualiza la ruta del diccionario en la entrega).
- `../analysis/glossary/metaflow.md` — diccionario canónico, fuente de las
  reglas de `mapping.json`.
- `../analysis/domain-model/relationships/metaflow-transform.md` — la
  entidad `MappingTable` materializa `mapping.json`.

---

## 7. CP-ADR-Approval

> **CP-ADR-Approval** (MetaFlow §2.8, §3.0, §3.5). Un ADR no se convierte en
> `accepted` — y por lo tanto en gobernante — sin la aprobación de un
> Arquitecto / Tech Lead. Esta ADR es la **fuente de verdad de su propia
> aprobación** (registrada en el bloque `review` del frontmatter con la
> evidencia de revisión); cuando gobierne una revisión de SPEC, su ruta
> aparece en los `sources` de esa revisión. Las aprobaciones de ADR nunca se
> copian al manifest del TASK.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenioserrano` |
| **Role** | architect (autoasignado: no hay otro titular) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-28T01:00:19-03:00` |
| **review.started_at** | `2026-08-28T01:01:00-03:00` |
| **review.decided_at** | `2026-08-28T01:01:26-03:00` |
| **Findings** | None — acknowledged_without_comment (razón en el frontmatter) |
