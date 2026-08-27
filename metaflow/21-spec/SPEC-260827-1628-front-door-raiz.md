---
id: "SPEC-260827-1628-front-door-raiz"
title: "SPEC US-001.TASK-025: front door de la raíz — README MetaFlow con dos particiones, AGENTS.md con sección de proyecto, remoción del skill avenga-devflow"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-020"
task: "US-001.TASK-025"
revision: 1
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T16:28:33-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T16:30:08-03:00"
  decided_at: "2026-08-27T16:30:08-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — SPEC US-001.TASK-025 aprobada; autoriza el Delivery Loop con TDD estricto (red→green)"
---

# SPEC-260827-1628 — US-001.TASK-025: front door de la raíz — README MetaFlow con dos particiones, AGENTS.md con sección de proyecto, remoción del skill avenga-devflow

| Field | Value |
|-------|-------|
| **Origin** | BUG-020 (user report) |
| **TASK** | US-001.TASK-025 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Reescribir el front door del workshop: `README.md` de la raíz pasa de ser
el texto íntegro de "Avenga DevFlow 5.1" a describir el repositorio como
workshop **MetaFlow 1.1** con el modelo de **dos particiones** — `metaflow/`
= árbol gobernante instalado (donde se usa MetaFlow, la versión vigente que
gobierna este repositorio) y `distribution-kit/` = el producto, el kit en
construcción (lo que cambia cuando la metodología cambia — la siguiente
versión). La sección de proyecto de `AGENTS.md` (bajo el marcador
`METAFLOW:PROJECT-SECTION`) documenta las dos particiones, y se remueve el
skill `.agents/skills/avenga-devflow/` instalado en la raíz. Si no se
corrige, el front door declara una metodología que este repositorio ya no
usa: confunde a humanos y agentes (un agente puede cargar el skill
`avenga-devflow` — checkpoints `AITL-*`/`BOLT` — en un repo gobernado por
`CP-*`/`TASK`).

## 2. Context

El BUG-020 (aprobado) documenta los restos de la migración §5.16 en la
raíz: el pipeline de transformación cubre `distribution-kit/` y la
migración instaló `metaflow/`, pero los archivos del taller fuera de ambos
(README.md, AGENTS.md, `.agents/skills/`) no fueron reescritos. El README
viejo sí documentaba su equivalente ("two devflow/ trees, and that is
deliberate"); el linaje MetaFlow no tiene ese equivalente. El fix vive en
los archivos del front door (no en el toolkit): no se regenera el kit.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-025 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-020 | CP-BUG-Approval ✓ (2026-08-27) |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

## 4. Scope

### In scope

- `README.md` (raíz): reescritura completa a MetaFlow 1.1 — dos
  particiones, adopción, lectura, notas de plataforma, sin referencias al
  linaje Avenga.
- `AGENTS.md` (raíz): sección de proyecto bajo el marcador
  `METAFLOW:PROJECT-SECTION` con las dos particiones (el bloque framework
  no se toca).
- Remoción de `.agents/skills/avenga-devflow/`.
- Nuevos tests de verificación del front door en `src/tests/`.

### Out of scope

- `CHANGELOG.md` (historia — G36), `input-kit/` (materia prima), `mapping.json`,
  fixtures de tests, `tools/`, `distribution-kit/` (ya limpio), artefactos
  de `metaflow/02-analysis/` y gobernanza (referencias contextuales).

## 5. Prerequisites and baseline

- TASK-005/006/024 Done (baseline); Python 3 + stdlib (ADR-001); tests en
  `unittest` (sin dependencias externas).

## 6. Phases

### Phase A — Test de reproducción (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Crear `src/tests/test_front_door.py`

Test `unittest` que verifica el front door de la RAÍZ (no el kit) y que
hoy falla (RED):

- **A.1.1** Cero tokens prohibidos (`Avenga`, `DevFlow`, `devflow`,
  `BOLT`, `AITL`, `HITL` — case-insensitive) en: `README.md`, `AGENTS.md`,
  `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`,
  `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md`.
- **A.1.2** `README.md` documenta las dos particiones: contiene
  `distribution-kit/` y `metaflow/` como particiones del workshop +
  "MetaFlow" y versión 1.1.
- **A.1.3** `AGENTS.md` tiene sección de proyecto: contiene el marcador
  `METAFLOW:PROJECT-SECTION` y, después de él, las dos particiones.
- **A.1.4** `.agents/skills/avenga-devflow` no existe.
- **A.1.5** `README.md` no referencia rutas `devflow/`.

Ejecutar y registrar el **RED** (README actual = texto Avenga 5.1 →
A.1.1/A.1.2/A.1.5 fallan; avenga-devflow existe → A.1.4 falla; AGENTS.md
sin sección → A.1.3 falla).

**Files created:**
- `src/tests/test_front_door.py` — Tests de verificación del front door de
  la raíz (ausencia de tokens del linaje Avenga + modelo de dos
  particiones + ausencia del skill viejo).

### Phase B — README.md de la raíz (MetaFlow 1.1, dos particiones)

**Duration:** 1h — **Complexity:** Low

#### B.1 Reescritura del README

Reemplazar el texto Avenga por un README MetaFlow con:

- **Encabezado:** "MetaFlow — AI-native SDLC", versión 1.1, una línea de
  qué es (agente genera el código/tests/diseño final; el humano gobierna
  por checkpoints CITL).
- **Bloque de dos particiones** (lo que pide BUG-020):
  | Partición | Qué es |
  |-----------|--------|
  | `metaflow/` (raíz) | El árbol gobernante INSTALADO — donde se usa MetaFlow hoy; la versión vigente que gobierna este repositorio |
  | `distribution-kit/` | El PRODUCTO — el kit que un proyecto copia; lo que cambia cuando la metodología cambia; la siguiente versión |
  Regla que las separa: nada edita el árbol `metaflow/` de la raíz excepto
  la migración §5.16; el trabajo de metodología vive en
  `distribution-kit/` vía el pipeline de transformación (`input-kit/` →
  `distribution-kit/`).
- **Adopción:** copiar el contenido de `distribution-kit/` (robocopy / cp
  -a — con la advertencia de las carpetas con punto), tabla de qué aterriza
  dónde, notas de plataforma (Claude/Codex/Copilot/OpenCode), luego
  `metaflow/LANGUAGE`, `metaflow/README.md`.
- **Orden de lectura** (MetaFlow.md, GUARDRAILS, ONBOARDING), **trabajar en
  la metodología** (todo cambio al kit pasa por el camino gobernado:
  origen aprobado → TASK → SPEC → Delivery Loop → MEM), nota de `tools/`
  (no distribuido; opcional por contrato), limitaciones conocidas.
- Cero referencias a Avenga/DevFlow/BOLT/AITL/HITL.

**Files modified:**
- `README.md` — Reescritura completa (front door del workshop).

### Phase C — AGENTS.md: sección de proyecto + remoción del skill

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Sección de proyecto de AGENTS.md

Agregar bajo el marcador `METAFLOW:PROJECT-SECTION` (nunca tocar el bloque
framework de arriba) un bloque corto que nombre las dos particiones
(`metaflow/` gobernante instalado; `distribution-kit/` producto en
construcción; `input-kit/` materia prima) y que todo cambio de metodología
sigue el camino gobernado.

**Files modified:**
- `AGENTS.md` — Sección de proyecto poblada (merge en el marcador).

#### C.2 Remoción del skill viejo

Eliminar `.agents/skills/avenga-devflow/` (queda solo `ai-sdlc`).

**Files deleted:**
- `.agents/skills/avenga-devflow/SKILL.md` — Skill del linaje Avenga
  (la definición de plataforma vigente es `.agents/skills/ai-sdlc/SKILL.md`).

### Phase D — GREEN + suite completa

**Duration:** 0.5h — **Complexity:** Low

#### D.1 Verificación

Correr `src/tests/test_front_door.py` (GREEN) y la suite completa
(`python -m unittest discover -s src/tests -p "test_*.py"` — o pytest si
está disponible). Registrar el **GREEN**.

---

## 7. Acceptance criteria

### AC-1: Front door sin tokens del linaje Avenga

**Given** los archivos del front door de la raíz (README.md, AGENTS.md,
CLAUDE.md, `.agents/`, `.github/`, `.opencode/`),
**When** se escanean por tokens prohibidos,
**Then** cero coincidencias de `Avenga|DevFlow|devflow|BOLT|AITL|HITL`.

### AC-2: README documenta las dos particiones

**Given** el README.md de la raíz,
**When** se lee,
**Then** describe `metaflow/` (donde se usa MetaFlow) y `distribution-kit/`
(el producto — la siguiente versión) como las dos particiones del workshop,
con la regla que las separa.

### AC-3: AGENTS.md con sección de proyecto

**Given** el AGENTS.md de la raíz,
**When** se inspecciona,
**Then** el bloque framework queda intacto y la sección bajo
`METAFLOW:PROJECT-SECTION` documenta las dos particiones.

### AC-4: Skill avenga-devflow ausente

**Given** `.agents/skills/`,
**When** se lista,
**Then** solo existe `ai-sdlc`.

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-020 (expected result) | Fases B/C reescriben README/AGENTS.md y remueven el skill | test_front_door.py (RED→GREEN) + suite completa |

---

## 8. Testing strategy

- **Unit tests:** `src/tests/test_front_door.py` — 5 verificaciones sobre
  el front door real de la raíz (tokens prohibidos, dos particiones en
  README, sección de proyecto en AGENTS.md, ausencia del skill, sin rutas
  `devflow/`).
- **Integration tests:** n/a (sin componentes nuevos).
- **E2E tests:** suite completa (regresión — los tests existentes de
  `distribution-kit/` deben seguir verdes).
- **Edge cases:** tokens en cualquier caso (case-insensitive); contenido de
  AGENTS.md antes y después del marcador (el bloque framework no debe
  contener las dos particiones).
- **BUG evidence:** RED (front door actual con Avenga + skill presente) →
  GREEN (front door reescrito + skill ausente).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a (documentación + stdlib) |
| Perf-smoke | — | n/a |
| Prompt-injection scan | — | n/a |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a (sin dependencias nuevas) |
| PII / DLP | — | n/a |
| Dependency-confusion | — | n/a |
| Test-first evidence | RED antes del fix | pass (a verificar) |
| Behavioral reproducibility | front door verificable por test | pass (a verificar) |
| TASK-manifest validation | manifest v1 válido | pass (a verificar) |

---

## 10. Security and data

- Sin superficie externa; `data_classification: internal`. El README no
  expone secretos ni credenciales.

---

## 11. Monitoring and observability

- n/a — evidencia en tests + git diff del front door.

---

## 12. Migration, compatibility and rollback

- **Migration:** edición directa de archivos del front door (fuera del
  kit); no requiere regeneración.
- **Compatibility:** sin cambios de API ni del kit.
- **Rollback:** git revert + re-ejecución de la suite.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Tocar el bloque framework de AGENTS.md al editar la sección de proyecto | 2 | 4 | Editar solo bajo el marcador; test A.1.3 verifica la presencia del marcador |
| Perder contenido útil del README viejo (notas de adopción) | 2 | 2 | Re-expresar en MetaFlow las secciones válidas (adopción, plataforma, lectura) |
| Regresión del kit | 1 | 3 | Suite completa verde |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en los archivos del front door, no en el toolkit | BUG-020: los archivos tocados viven fuera de distribution-kit/ (no se regenera el kit) |
| Tests contra la raíz real (no un fixture) | El front door es el propio repo — verificarlo directamente es la evidencia honesta |
| `unittest` stdlib | ADR-001 (stdlib); los tests del repo ya son unittest — sin pytest obligatorio |

---

## 15. Stop conditions

- El test de reproducción no puede expresar el expected result del BUG
  (bloqueo → MEM con evidencia).
- Un cambio material en las fuentes gobernadas invalida esta SPEC (G15):
  detener, revisar, re-aprobar.

---

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; front door reescrito + skill ausente
- [ ] Tests GREEN (test_front_door + suite completa); AC-1..4 satisfechas
- [ ] MEM + manifest `delivery_loops[]` + CP-MEM-Approval

---

## 17. References

- BUG-020, US-001, ADR-001, TEMPLATE-SPEC.md, test_restos_v5.py (patrón de tests).

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (US-001.TASK-025, BUG-020) |
| 2026-08-27 | eugenioserrano | **CP-SPEC-Approval** — aprobada; autoriza el Delivery Loop (TDD red→green) |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que
> el Dev-validator registra `CP-SPEC-Approval`.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator autoasignado) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T16:28:33-03:00` |
| **review.started_at** | `2026-08-27T16:30:08-03:00` |
| **review.decided_at** | `2026-08-27T16:30:08-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
