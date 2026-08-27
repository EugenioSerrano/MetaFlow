---
id: "MEM-260827-1632-front-door-raiz"
title: "Delivery Loop 1 — US-001.TASK-025: front door de la raíz reescrito a MetaFlow 1.1 (dos particiones), AGENTS.md con sección de proyecto, skill avenga-devflow removido"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
task: "US-001.TASK-025"
spec: "SPEC-260827-1628-front-door-raiz"
spec_revision: 1
delivery_loop: 1
execution_outcome: "ready_for_review"
baseline: "5d9b90d"
applied_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
manifest: "metaflow/23-metrics/tasks/US-001.TASK-025-front-door-raiz.json"
diff_ref: "working tree (sin commit — pendiente instrucción del usuario)"
review_ready_at: "2026-08-27T16:32:12-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T16:49:05-03:00"
  decided_at: "2026-08-27T16:49:05-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — diff + evidencia RED/GREEN + gates + MEM + manifest revisados; 110 tests OK. CP-MEM-Approval 2026-08-27"
---

# MEM-260827-1632 — US-001.TASK-025: front door de la raíz a MetaFlow 1.1

| Field           | Value |
|-----------------|-------|
| **TASK**        | US-001.TASK-025 |
| **SPEC**        | [SPEC-260827-1628-front-door-raiz](../21-spec/SPEC-260827-1628-front-door-raiz.md) (rev 1) |
| **Delivery Loop**    | 1 |
| **ADRs**        | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) |

---

## 1. Executive summary

Este Delivery Loop corrigió el BUG-020 reescribiendo el front door de la
raíz del workshop, que tras la migración §5.16 seguía siendo el texto
íntegro de "Avenga DevFlow 5.1". El README.md raíz ahora describe el
repositorio como workshop de MetaFlow 1.1 con el modelo de dos particiones
(`metaflow/` = árbol gobernante instalado, donde se usa MetaFlow hoy;
`distribution-kit/` = el producto en construcción, la siguiente versión
del kit), con instrucciones de adopción, orden de lectura y notas de
plataforma re-expresadas en el linaje MetaFlow y cero referencias a la
marca o estructura del linaje previo. La sección de proyecto del AGENTS.md
raíz (bajo el marcador `METAFLOW:PROJECT-SECTION`, con el bloque framework
intacto) ahora documenta las dos particiones y sus reglas, y el skill
`.agents/skills/avenga-devflow/` dejó de existir en la raíz (queda solo
`ai-sdlc`). El cambio se condujo con TDD estricto: el test de reproducción
`src/tests/test_front_door.py` falló primero (RED: 4/5 fallos — README con
Avenga, rutas `devflow/`, skill presente, AGENTS.md sin sección) y pasó
después del fix (GREEN: 5/5). La suite completa quedó en verde: 96 tests en
`src/tests` (91 previos + 5 nuevos) y 14 en `tools/agent-wrappers`, sin
regresiones en el kit.

## 2. Implemented phases

### Phase A — Test de reproducción (RED)

Se creó `src/tests/test_front_door.py` (unittest, stdlib — mismo patrón
que `test_restos_v5.py`), que verifica el front door del REPOSITORIO (no
del kit): (1) cero tokens prohibidos (`Avenga|DevFlow|devflow|BOLT|AITL|HITL`)
en README.md, AGENTS.md, CLAUDE.md y los tres agent definitions instalados;
(2) README.md sin rutas `devflow/`; (3) ausencia de `.agents/skills/avenga-devflow`;
(4) README.md con MetaFlow, `metaflow/`, `distribution-kit/` y versión 1.1;
(5) AGENTS.md con sección de proyecto bajo el marcador que menciona ambas
particiones. Ejecutado antes de tocar producción: **4 de 5 tests fallaron**
(RED registrado).

### Phase B — README.md de la raíz (MetaFlow 1.1, dos particiones)

Se reescribió el README.md completo: encabezado MetaFlow 1.1; bloque
"Two partitions, and that is deliberate" con la tabla
`metaflow/` (gobernante instalado) vs `distribution-kit/` (producto — la
siguiente versión), el release loop §5.16 y la regla que las separa;
sección de adopción (copia del kit con `cp -a`/`robocopy`, tabla de qué
aterriza dónde, notas de plataforma Claude/Codex/Copilot/OpenCode con los
nombres nuevos `ai-sdlc`/`MetaFlow.agent.md`/`MetaFlow.md`); orden de
lectura de los documentos 1.1; "Working on the methodology" (camino
gobernado, `tools/` no distribuido, CHANGELOG raíz); y la declaración de
propiedad adaptada (MetaFlow / Eugenio Serrano LATAM) conservando la cita
al artículo base (AWS DevOps Blog). Cero menciones al linaje Avenga.

### Phase C — AGENTS.md: sección de proyecto + remoción del skill

Se agregó a `AGENTS.md` la sección de proyecto bajo el marcador
`METAFLOW:PROJECT-SECTION` (el bloque framework queda byte a byte intacto):
nombra las dos particiones (`metaflow/` gobernante, `distribution-kit/`
producto, `input-kit/` materia prima del pipeline) y las tres reglas del
workshop (nada edita `distribution-kit/` a mano — se regenera; nada edita
el `metaflow/` raíz salvo la migración; todo cambio de metodología sigue el
camino gobernado). Se eliminó `.agents/skills/avenga-devflow/`; la
verificación posterior confirma que `.agents/skills/` contiene únicamente
`ai-sdlc` y que no quedan nombres `avenga|devflow` fuera de lo excluido por
diseño (fixtures de tests, artefactos de análisis, input-kit, CHANGELOG).

### Phase D — GREEN + suite completa

`src/tests/test_front_door.py` → 5/5 OK. Suite completa:
`python -m unittest discover -s src/tests -p "test_*.py"` → **96 tests OK**
(el E2E ejecutó un transform real en temp: 149 archivos, 7554 reglas,
26 remociones, verificación sin tokens); `tools/agent-wrappers/tests` →
**14 tests OK**. Total: 110 tests verdes, 0 regresiones.

## 3. Files created

| File | Purpose |
|------|---------|
| `src/tests/test_front_door.py` | Suite de verificación del front door de la raíz: detecta cualquier retorno del linaje Avenga en README/AGENTS/CLAUDE/wrappers, exige el modelo de dos particiones en README.md y AGENTS.md, y verifica la ausencia del skill `avenga-devflow` — la red de seguridad del BUG-020 |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `README.md` (raíz) | Reescritura completa: de "Avenga DevFlow 5.1" a front door MetaFlow 1.1 con el modelo de dos particiones, adopción, lectura y notas de plataforma |
| `AGENTS.md` (raíz) | Sección de proyecto poblada bajo `METAFLOW:PROJECT-SECTION` (dos particiones + reglas del workshop); bloque framework intacto |
| `metaflow/13-bugs/BUG-020-front-door-raiz-stale.md` | CP-BUG-Approval registrado; status → in-fix |
| `metaflow/21-spec/SPEC-260827-1628-front-door-raiz.md` | CP-SPEC-Approval registrado |
| `metaflow/12-functional/tasks/US-001.TASK-025-front-door-raiz.md` | CP-TASK-READY-Approval registrado |
| `metaflow/23-metrics/tasks/US-001.TASK-025-front-door-raiz.json` | Manifest: spec_revisions[1] + CP-TASK-READY/SPEC + delivery_loops[1] |
| `metaflow/23-metrics/user-stories/US-001-toolkit-transformacion.json` | `tasks[]` += TASK-025 |
| `metaflow/12-functional/INDEX.md` / `metaflow/13-bugs/INDEX.md` | TASK-025 en la tabla funcional; BUG-020 en Approved/In-fix |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| `.agents/skills/avenga-devflow/SKILL.md` | Skill del linaje Avenga instalado en la raíz — la definición vigente es `.agents/skills/ai-sdlc/SKILL.md` (BUG-020) |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Test contra el front door REAL de la raíz (no un fixture) | El objeto del defecto es el propio repositorio — verificarlo directamente es la evidencia honesta y protege contra regresión |
| `unittest` stdlib (sin pytest) | ADR-001 (stdlib) y consistencia con el resto de la suite; funciona sin dependencias |
| README re-expresa las secciones válidas del README viejo (adopción, plataforma) | No se pierde contenido útil: la adopción del kit es el mismo procedimiento en el linaje MetaFlow, con los nombres nuevos |
| AGENTS.md: solo sección de proyecto | El bloque framework es del framework (se reemplaza en la próxima migración §5.16) — la información del workshop pertenece bajo el marcador |
| Fix directo en archivos del front door, sin tocar el toolkit ni regenerar el kit | BUG-020: los archivos viven fuera de `distribution-kit/`; el kit ya estaba limpio |

## 8. Deviations and assumptions

- Sin desviaciones materiales de la SPEC (fases A–D ejecutadas tal cual).
- Asunción: la remoción del skill se verificó por estado final (`.agents/skills/`
  contiene solo `ai-sdlc` y el escaneo de nombres no encuentra restos fuera de
  lo excluido por diseño) — el fix no regenera el kit.
- Fuera de alcance (confirmado): CHANGELOG.md, input-kit/, mapping.json,
  fixtures, tools/, artefactos de análisis/gobernanza.

## 9. Verification evidence

### Tests — RED (antes del fix)
```
python -m unittest src.tests.test_front_door -v
Ran 5 tests in 0.003s
FAILED (failures=4)   # Avenga en README.md:1 · devflow/ en README ·
                      # skill avenga-devflow presente · AGENTS.md sin sección
```

### Tests — GREEN (después del fix)
```
python -m unittest src.tests.test_front_door -v
Ran 5 tests in 0.005s
OK

python -m unittest discover -s src/tests -p "test_*.py"
Ran 96 tests in 11.742s
OK

python -m unittest discover -s tools/agent-wrappers/tests -p "test_*.py"
Ran 14 tests in 0.043s
OK
```

### BUG Delivery Loop evidence
- **RED:** 4/5 fallos en `test_front_door.py` sobre el front door previo
  (README Avenga 5.1, rutas `devflow/`, skill presente, AGENTS.md sin sección).
- **GREEN:** 5/5 OK tras el fix; suite completa 96 + 14 = 110 tests OK; E2E
  con transform real (149 archivos, verificación sin tokens prohibidos).

### Gates
| Gate | Resultado |
|------|-----------|
| Unit / integration | pass — 110 tests OK |
| Secret-leak scan | pass — sin secretos en el diff |
| Hallucination lint | pass — sin APIs/servicios inventados (documentación) |
| Test-first evidence | pass — RED registrado antes del fix |
| Behavioral reproducibility | pass — el front door queda verificado por test |
| TASK-manifest validation | pass — manifest válido contra manifest-v1-task.schema.json |
| SAST/SBOM, perf-smoke, prompt-injection, IP/license, PII/DLP, dependency-confusion | n/a — documentación, sin superficie externa ni dependencias nuevas |

## 10. Manual interventions

None — todo el material del Delivery Loop (tests, README, AGENTS.md,
artefactos de gobernanza) fue generado por el agente.

## 11. Evidence links

- **Diff / PR:** working tree (sin commit — pendiente instrucción explícita del usuario, G34).
- **Commit:** baseline `5d9b90d` (HEAD previo al loop; cambios sin commitear).
- **Cumulative TASK manifest:** `metaflow/23-metrics/tasks/US-001.TASK-025-front-door-raiz.json`.

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~35 min |
| Delivery Loop number | 1 |
| Tests created | 5 (unit — verificación del front door) |
| AI-generated code | 100% |
| First-pass approval | pending (CP-MEM-Approval) |

## 13. Pending items and stubs

- [ ] CP-MEM-Approval (este paquete) y luego CP-TASK-DONE-Approval (aceptación).
- [ ] Fuera de alcance: release formal del kit (tag), aprobaciones pendientes de TASK-003/004/006, cierre de BUG-001.

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** Este MEM fue creado por el agente sin estado
> mutable y **nunca se auto-aprueba**. Un humano calificado (el Dev-validator
> que ejecutó el TASK) inspecciona el diff real, la evidencia de
> tests/gates, el MEM y el manifest, y registra `CP-MEM-Approval` aquí y en
> `checkpoint_approvals[]` del manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | human:eugenioserrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T16:32:12-03:00` |
| **review.started_at** | `2026-08-27T16:49:05-03:00` |
| **review.decided_at** | `2026-08-27T16:49:05-03:00` |
| **Review evidence** | diff completo + RED/GREEN + gates + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno — aprobado sin comentarios |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Aprobación del propietario (Dev-validator autoasignado); diff + RED/GREEN + 110 tests OK revisados |
