---
id: "ADR-002"
title: "Numeración de carpetas internas del kit por ciclo de uso"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "superseded"
decision_makers: ["Eugenio Serrano — propietario (rol de arquitecto autoasignado: no hay otro titular)"]
sources:
  - "devflow/reviews/REV-001-renombrado-carpetas-metaflow.md"
  - "devflow/analysis/glossary/metaflow.md"
supersedes: []
conflicts_with: []
tags: [kit, numeracion, carpetas]
nfrs: ["path_hygiene"]
review_ready_at: "2026-08-27T02:37:29-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "architect"
      model: null
  started_at: "2026-08-27T02:39:49-03:00"
  decided_at: "2026-08-27T02:39:49-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol de arquitecto autoasignado) sin hallazgos — esquema de numeración por ciclo de uso confirmado (incl. ai-sdlc sin número y raíz sin número), 2026-08-27"
---

# ADR-002 — Numeración de carpetas internas del kit por ciclo de uso

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | Eugenio Serrano (propietario) |
| **Sources**    | REV-001 (aprobado — Plan B), glossary/metaflow.md |
| **Supersedes** | None |
| **Conflicts with** | None |

---

## 1. Context

La revisión REV-001 (aprobada) midió el ruido de renombrar las carpetas
internas del kit: 1524 referencias de ruta, 1700 menciones y 91 de 144
archivos (63 %) afectados. El propietario decidió **Plan B**: renombrar con
prefijos numéricos para ordenar las carpetas. El criterio de orden elegido
por el propietario es **el ciclo de uso** (no la taxonomía de gobernanza):
las carpetas se ordenan como se usan en el trabajo diario — el ciclo de
desarrollo con `spec` y `memory` juntos (SPEC → V-Bounce → MEM), los `bugs`
pegados a `functional` (donde se procesan vía su Bolt dedicado), y el resto
por bloques de uso (entrada → definición → ejecución → calidad/aprendizaje →
soporte → operación).

Restricciones:
- **Sin espacios** en los nombres (tooling: rutas limpias en shell/grep/
  scripts — F-03 del REV).
- **Gaps numéricos** para crecer sin renumerar (estilo "dejar espacios").
- La reescritura de referencias es **completa** y verificada con un **test de
  integridad de links** (F-02 del REV).
- El núcleo (`ai-sdlc/`, la metodología) y las carpetas de plataforma de la
  raíz (`.agents/`, `.github/`, `.opencode/`) **no se numeran**.

## 2. Alternatives considered

### Alternative A — Prefijos numéricos sin espacios, gaps de 10, orden por ciclo de uso (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Orden visual por uso (el ciclo real); gaps de 10 por bloque (01-09, 11-19, 21-29…) permiten insertar carpetas nuevas sin renumerar; sin espacios → tooling limpio; `spec`/`memory` juntos y `bugs` junto a `functional` reflejan el flujo de trabajo |
| **Cons** | Churn alto en el diff (1524 referencias — aceptado, REV-001); requiere test de integridad de links nuevo |

### Alternative B — Prefijos con espacios ("1 - input")

| Aspect   | Detail |
|----------|--------|
| **Pros** | Legibilidad "humana" |
| **Cons** | Rompe rutas sin comillas, greps y scripts (F-03) — descartada |

### Alternative C — Sin renombrar (Plan A del REV)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Cero churn; el orden ya está en la semántica e índices |
| **Cons** | El propietario prioriza el orden visual por uso — descartada |

### Alternative D — Secuencial sin gaps (01…20)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Simple |
| **Cons** | Insertar una carpeta nueva renumeraría todo — descartada |

## 3. Decision

Se adoptan **prefijos numéricos de 2 dígitos sin espacios, con gaps de 10 por
bloque, ordenados por ciclo de uso**, según el siguiente esquema:

| Bloque | Carpeta | Función / uso |
|--------|---------|---------------|
| Entrada | `01-input` | Evidencia cruda |
| | `02-analysis` | Análisis de negocio |
| | `03-discovery` | Hallazgos técnicos/legado |
| Definición | `11-adrs` | Decisiones de arquitectura |
| | `12-functional` | US + TASKs/Bolts (definición de trabajo) |
| | `13-bugs` | Defectos — entran al ciclo vía su Bolt dedicado (junto a functional) |
| Ejecución | `21-spec` | Planes de implementación |
| | `22-memory` | MEMs — junto a spec (SPEC → V-Bounce → MEM) |
| | `23-metrics` | Manifests/métricas — el V-Bounce produce MEM + manifest |
| | `24-tests` | Casos de prueba (verificación del delivery) |
| Calidad y aprendizaje | `31-reviews` | Revisiones (REV) |
| | `32-adversarial-reviews` | Revisiones adversariales (AREV) |
| | `33-risks` | Registro de riesgos del proyecto |
| | `34-incidents` | Incidentes |
| | `35-retros` | Retrospectivas |
| Soporte | `41-prompts` | Prompts del proyecto |
| | `42-reports` | Reportes generados |
| Operación | `51-agents` | Sistema de agentes |
| | `52-agents-data` | Datos de agentes |
| | `53-actors` | Registro de actores |

**No se numeran:** `ai-sdlc/` (núcleo de la metodología — ordena al final) y
las carpetas de plataforma de la raíz del kit (`.agents/`, `.github/`,
`.opencode/`).

**Orden de aplicación en el diccionario:** las reglas de contenido respetan
longest-first — `adversarial-reviews/` antes que `reviews/`, `agents-data/`
antes que `agents/` — para no corromper substrings.

## 4. Consequences

**Positive:**
- Orden visual que refleja el ciclo de uso (spec↔memory juntos, bugs junto a
  functional).
- Crecimiento sin renumerar (gaps de 10).
- Rutas limpias sin espacios (tooling amigable).
- La reescritura completa + test de integridad de links mantienen el kit
  consistente.

**Trade-offs:**
- Churn de diff alto (63 % de los archivos) — aceptado por el propietario
  (REV-001 aprobado); la revisión de diffs seguirá siendo viable porque el
  cambio es 1:1 y mecánico (una sola pasada).

**Technical debt:**
- El diccionario gana ~40 reglas (path + contenido) para el renombrado y su
  orden; se mantiene como datos.

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| path_hygiene | Rutas del kit sin espacios ni caracteres especiales problemáticos | Nombres de carpeta: `NN-nombre` (dígitos + guion + kebab-case) | Test de integridad de links + E2E (todos los links relativos resuelven) |

## 6. References

- `devflow/reviews/REV-001-renombrado-carpetas-metaflow.md` (aprobado — Plan B)
- `devflow/analysis/glossary/metaflow.md` (diccionario — las reglas de renombrado se agregan como datos)
- Related ADRs: ADR-001 (plataforma del toolkit)

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). Este ADR no se
> convierte en `accepted` sin la aprobación de un Arquitecto / Tech Lead.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenioserrano` (rol de arquitecto autoasignado: no hay otro titular) |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:37:29-03:00` |
| **review.started_at** | `2026-08-27T02:39:49-03:00` |
| **review.decided_at** | `2026-08-27T02:39:49-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 8. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial (propuesta para AITL-ADR-Approval) | @eugenioserrano |
| 2026-08-27 | **AITL-ADR-Approval** — `accepted` por human:eugenioserrano (arquitecto autoasignado), sin hallazgos | @eugenioserrano |
