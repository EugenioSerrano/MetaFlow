---
id: "ADR-001"
title: "Toolkit de transformación: Python, librerías y ubicación del código"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted"
decision_makers: ["Eugenio Serrano — propietario (rol de arquitecto autoasignado: no hay otro titular)"]
sources:
  - "../analysis/scope/mvp-scope.md"
  - "../analysis/glossary/metaflow.md"
  - "../analysis/process/PROC-001-transformacion-kit.md"
  - "conversación de diseño 2026-08-27"
supersedes: []
conflicts_with: []
tags: [python, toolkit, transformacion]
nfrs: ["performance", "portability"]
review_ready_at: "2026-08-27T01:12:34-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "architect"
      model: null
  started_at: "2026-08-27T01:12:34-03:00"
  decided_at: "2026-08-27T01:12:34-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol de arquitecto autoasignado) sin hallazgos — revisión de la propuesta en conversación, 2026-08-27"
---

# ADR-001 — Toolkit de transformación: Python, librerías y ubicación del código

| Field          | Value |
|----------------|-------|
| **Status**     | accepted |
| **Decision-makers** | Eugenio Serrano (propietario) |
| **Sources**    | mvp-scope.md (D1, D4, S1, S6), glossary/metaflow.md, PROC-001, conversación de diseño 2026-08-27 |
| **Supersedes** | None |
| **Conflicts with** | None — primera ADR del registro (§2.8) |

---

## 1. Context

El MVP entrega el toolkit de transformación que convierte el kit de
AvengaDevFlow (`input-kit/`) en el kit de MetaFlow (`distribution-kit/`)
aplicando el diccionario de nombres (`glossary/metaflow.md` → `mapping.json`)
con verificación automática y reporte (scope MVP S1–S7). El análisis ya tomó
decisiones preliminares que deben formalizarse como ADR aprobada para poder
gobernar la SPEC:

- **Lenguaje:** Python — "cero build, stdlib completa" (scope D1, S1).
- **Ubicación:** `src/` — vacía y disponible; `tools/` es la pista del
  repositorio original, que el anti-objetivo AG4 de la visión excluye
  explícitamente (scope D4).

Fuerzas en juego:

- **Cero dependencias y cero build:** el pipeline debe correr en la máquina
  del mantenedor (Windows, PowerShell) sin instalaciones ni pasos de build;
  el journey "publicar nueva versión" invoca `python src/transform.py`
  directamente.
- **Procesamiento de texto:** renames longest-first, regex con captura para
  checkpoints (`AITL-<CODE>-Approval` → `CP-<CODE>-Approval`), renames de
  rutas, remociones con registro — todo sobre archivos md/json/yaml de texto
  (RULE-03 de InputKit).
- **Reglas como datos:** el diccionario vive en `mapping.json`; agregar una
  regla no debe tocar el engine (RULE-04 de MappingRule).
- **Verificabilidad:** tests unitarios (orden, variantes de caso, regex),
  E2E con fixtures y aceptación contra el kit real (scope S6); el pipeline
  debe ser repetible y con evidencia (BR-001 mitigado por el verificador).
- **Tiempo:** O3 de la visión — ejecución < 1 min.

## 2. Alternatives considered

### Alternative A — Python 3 + stdlib únicamente (runtime y tests) (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Cero dependencias y cero build; corre con cualquier Python 3.10+ (probado local con 3.12.10); `pathlib`, `re`, `json`, `argparse`, `dataclasses` y `unittest` cubren engine, CLI, verificador, reporte y tests sin instalar nada; sin riesgo de cadena de dependencias ni problemas de red |
| **Cons** | `unittest` es menos ergonómico que pytest (menos helpers de aserción, sin `parametrize` nativo); sin type-checking estático externo (se mitiga con type hints + tests) |

### Alternative B — Python 3 + pytest (dependencia solo de desarrollo)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Mejor ergonomía de tests: `parametrize`, fixtures, assert con diff legible |
| **Cons** | Rompe "cero build / cero dependencias": requiere `pip install` (fricción en entornos sin red); inconsistente con la razón registrada de la decisión D1 del scope |

### Alternative C — TypeScript / Node

| Aspect   | Detail |
|----------|--------|
| **Pros** | Tipado estático, ecosistema grande |
| **Cons** | Requiere runtime Node + `npm install` + build; peso innecesario para un pipeline de texto puro; contradice la decisión D1 ya tomada en análisis |

### Alternative D — Go (como la pista `tools/` del repo original)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Binario único, rápido |
| **Cons** | Requiere toolchain de build; más código para manipulación de texto; el anti-objetivo AG4 de la visión excluye reimplementar la pista `tools/` |

### Alternative E — Ubicación del código: `src/` vs `tools/` (✅ Selected: `src/`)

| Aspect   | Detail |
|----------|--------|
| **Pros (`src/`)** | Carpeta vacía y disponible en el repo; separación clara del kit de entrada/salida; sin colisión con la pista del repo original |
| **Cons (`src/`)** | Ninguno relevante |
| **Cons (`tools/`)** | Es la pista de herramientas del repositorio original (wrappers, validator, etc.); escribir ahí contradice AG4 y mezcla el proyecto con el legado |

### Alternative F — Ubicación de `mapping.json`: raíz del repo vs `src/` (✅ Selected: raíz)

| Aspect   | Detail |
|----------|--------|
| **Pros (raíz)** | Los datos quedan separados del código (la regla RULE-04: agregar reglas sin tocar el engine); visible y editable directamente por el mantenedor; el engine la lee por ruta |
| **Cons (raíz)** | El toolkit no queda 100 % autocontenido en `src/` (aceptable: el repo completo es el producto) |

---

## 3. Decision

Adoptamos la **Alternative A** (Python 3 + stdlib únicamente, runtime y
tests) con la ubicación de la **Alternative E** (`src/`) y la de la
**Alternative F** (`mapping.json` en la raíz del repositorio).

En concreto:

- **Lenguaje/runtime:** Python 3.10+ (probado con 3.12.10 en la máquina del
  mantenedor), usando solo la stdlib: `pathlib`, `re`, `json`, `argparse`,
  `dataclasses`, `unittest`.
- **Estructura de código en `src/`:**
  - `src/transform.py` — CLI principal: `--dry-run` (plan sin escribir) y
    ejecución real (engine: `rename`, `regex_rename`, `remove`,
    `path_rename`, orden longest-first); al finalizar corre el verificador.
  - `src/verify.py` — verificador de tokens prohibidos (falla el run ante
    cualquier leftover).
  - `src/report.py` — generación del reporte (reglas aplicadas, conteos,
    remociones listadas).
  - `src/tests/` — tests unitarios (orden de reglas, variantes de caso,
    regex) + fixtures; E2E contra `input-kit/` real.
- **Datos:** `mapping.json` en la raíz del repositorio, junto a `input-kit/`
  y `distribution-kit/`.
- **Salidas:** `distribution-kit/` (kit transformado) y el reporte de cada
  run en la raíz (`transform-report-<version>.json` + `.md`).
- **Tests:** `unittest` (stdlib) para todo; sin dependencias de terceros en
  ningún entorno.

Esta ADR formaliza las decisiones D1 y D4 del scope y fija el resto de la
plataforma antes de generar la SPEC del MVP.

---

## 4. Consequences

**Positive:**
- El pipeline corre en cualquier máquina con Python 3.10+, sin instalación ni
  build — cumple O3 (verificación 100 % automática) y el journey del
  mantenedor.
- El mantenimiento del diccionario queda en datos (`mapping.json`), no en
  código.
- Sin dependencias de terceros → sin superficie de supply-chain en el MVP.

**Trade-offs:**
- `unittest` ofrece menos ergonomía que pytest; se compensa con la
  simplicidad del toolkit y con tests E2E contra el kit real.
- Sin type-checking estático externo; se mitiga con type hints y tests
  unitarios.

**Technical debt:**
- Si el pipeline crece (diffs entre versiones, merge selectivo — opción B de
  OQ-004), la decisión de adoptar pytest o un runtime con tipado se revisaría
  en una ADR nueva que superseda esta.

---

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| Performance | Tiempo de ejecución del pipeline completo (dry-run y real, incl. verificación) | < 1 min por ejecución (O3 de la visión) | Timing del CLI (p. ej. `Measure-Command` en PowerShell) registrado en el reporte del run |
| Portability | El toolkit corre sin instalación de dependencias y sin build | Cero dependencias de terceros; Python 3.10+ | `python src/transform.py --dry-run` en una instalación limpia de Python |

---

## 6. References

- `../analysis/scope/mvp-scope.md` — decisiones D1 (Python), D4 (`src/`),
  S1 (toolkit), S6 (tests).
- `../analysis/glossary/metaflow.md` — diccionario de transformación
  (fuente de `mapping.json`).
- `../analysis/process/PROC-001-transformacion-kit.md` — proceso que el
  toolkit implementa.
- `../analysis/vision/vision.md` — O3 (tiempo y verificación automática),
  AG4 (no reimplementar `tools/`).
- Related ADRs: none (primera ADR del registro).

---

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). Un ADR no se
> convierte en `accepted` —y por lo tanto en gobernante— sin la aprobación de
> un Arquitecto / Tech Lead. Este ADR es la **fuente de verdad de su propia
> aprobación** (registrada en el bloque `review` del frontmatter); cuando
> gobierne una revisión de SPEC, su ruta aparece en los `sources` de esa
> revisión. Las aprobaciones de ADR nunca se copian al manifest del Bolt.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenioserrano` (rol de arquitecto autoasignado: no hay otro titular) |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T01:12:34-03:00` |
| **review.started_at** | `2026-08-27T01:12:34-03:00` |
| **review.decided_at** | `2026-08-27T01:12:34-03:00` |
| **Findings** | Ninguno — aprobación sin comentarios (registrada en frontmatter `review`) |

---

## 8. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial (propuesta para AITL-ADR-Approval) | @eugenioserrano |
| 2026-08-27 | **AITL-ADR-Approval** — `accepted` por human:eugenioserrano (arquitecto autoasignado), sin hallazgos | @eugenioserrano |
