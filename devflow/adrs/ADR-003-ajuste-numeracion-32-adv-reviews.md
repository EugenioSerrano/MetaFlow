---
id: "ADR-003"
title: "Ajuste del esquema de numeración: 32-adv-reviews y reglas de contenido con barra"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted"
decision_makers: ["Eugenio Serrano — propietario (rol de arquitecto autoasignado: no hay otro titular)"]
sources:
  - "devflow/adrs/ADR-002-numeracion-carpetas-kit.md"
  - "devflow/reviews/REV-002-consistencia-kit.md"
supersedes:
  - "devflow/adrs/ADR-002-numeracion-carpetas-kit.md"
conflicts_with: []
tags: [kit, numeracion, carpetas]
nfrs: ["path_hygiene"]
review_ready_at: "2026-08-27T02:49:14-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "architect"
      model: null
  started_at: "2026-08-27T02:51:33-03:00"
  decided_at: "2026-08-27T02:51:33-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol de arquitecto autoasignado) sin hallazgos — 32-adv-reviews y reglas de contenido con barra confirmados (supersede ADR-002), 2026-08-27"
---

# ADR-003 — Ajuste del esquema de numeración: 32-adv-reviews y reglas con barra

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | Eugenio Serrano (propietario) |
| **Sources**    | ADR-002 (supersede), REV-002 (F-04/F-05/F-06) |
| **Supersedes** | ADR-002 |
| **Conflicts with** | None |

---

## 1. Context

La ADR-002 (accepted) definió el esquema de numeración de carpetas del kit.
Dos ajustes surgen tras la REV-002: (a) el propietario decidió acortar el
nombre de la carpeta 32 de `adversarial-reviews` a `adv-reviews`; (b) la
implementación de las reglas de contenido (N-rules) sobre-numeró **palabras
de vocabulario** en prosa (1224 corrupciones: "12-functional analyst", "run
the 24-tests") y rompió el enum del schema de manifests (`"functional"` →
`"12-functional"`) — el alcance correcto de las reglas de contenido es
**solo referencias de ruta** (nombre seguido de `/`), no la palabra suelta.

## 2. Alternatives considered

### Alternative A — Nombre 32: `adv-reviews` + reglas de contenido con barra obligatoria (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Nombre corto y legible (`32-adv-reviews`); las reglas de contenido solo numeran rutas (`functional/` → `12-functional/`), dejando intacto el vocabulario ("functional analyst", enums de schemas) |
| **Cons** | Las menciones en prosa sin barra ("the functional folder") no se numeran — cosmético, aceptable |

### Alternative B — Mantener `adversarial-reviews` y reglas con barra

| Aspect   | Detail |
|----------|--------|
| **Pros** | Sin cambio de nombre |
| **Cons** | El propietario prefiere el nombre corto — descartada |

### Alternative C — Mantener reglas por palabra suelta

| Aspect   | Detail |
|----------|--------|
| **Pros** | Numeraría también menciones en prosa |
| **Cons** | Corrompe vocabulario (F-04/F-05 de REV-002) — descartada |

## 3. Decision

Se adopta la **Alternative A**:

1. **La carpeta 32** del esquema pasa de `adversarial-reviews` a
   **`adv-reviews`**: `32-adv-reviews`. El resto del esquema de la ADR-002 se
   mantiene sin cambios (bloques, gaps de 10, sin espacios, `ai-sdlc/` y raíz
   sin número).
2. **Las reglas de contenido** de numeración aplican **solo a referencias de
   ruta**: patrón `(?<![\w-])<nombre>/` → `NN-<nombre>` (la barra es el
   delimitador). Las palabras de vocabulario ("functional", "tests",
   "memory", "risks", enums de schemas, etc.) quedan intactas. Las reglas de
   ruta (`^<nombre>$` → `NN-<nombre>`) no cambian.
3. Las protecciones de substrings se mantienen por el lookbehind:
   `business-risks/`, `adversarial-reviews/` (hoy `32-adv-reviews/` — el
   lookbehind protege `reviews/` dentro), `agents-data/`.

## 4. Consequences

**Positive:**
- Kit con vocabulario intacto (se corrige F-04/F-05 de REV-002).
- Nombre corto y legible para la carpeta de revisiones adversariales.
- Los enums de los schemas de manifests vuelven a validar
  `["functional", "non-functional", "test"]`.

**Trade-offs:**
- Las menciones en prosa sin barra no se numeran (cosmético).

**Technical debt:**
- Ninguno nuevo; se corrige el defecto de implementación de la ADR-002.

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| path_hygiene | Rutas del kit sin espacios; solo referencias de ruta se numeran | Nombres `NN-nombre`; vocabulario intacto | E2E + test de prosa (0 sobre-match) + test de enum del schema |

## 6. References

- ADR-002 (superseded por esta)
- REV-002 (F-04/F-05/F-06)
- Related ADRs: ADR-001

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5).

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenioserrano` (rol de arquitecto autoasignado: no hay otro titular) |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:49:14-03:00` |
| **review.started_at** | `2026-08-27T02:51:33-03:00` |
| **review.decided_at** | `2026-08-27T02:51:33-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 8. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial (supersede ADR-002: 32-adv-reviews + reglas de contenido con barra) | @eugenioserrano |
| 2026-08-27 | **AITL-ADR-Approval** — `accepted` por human:eugenioserrano (arquitecto autoasignado), sin hallazgos | @eugenioserrano |
