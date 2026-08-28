---
id: "MEM-260827-2238-fix-skill-metaflow"
title: "Fix BUG-025: skill MetaFlow reproducible desde el pipeline + front door de la raíz consistente"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
task: "US-001.TASK-030-fix-skill-metaflow"
spec: "SPEC-260827-2229-fix-skill-metaflow"
spec_revision: 1
delivery_loop: 1
execution_outcome: "ready_for_review"
baseline: "273295b"
applied_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
manifest: "metaflow/23-metrics/tasks/US-001.TASK-030-fix-skill-metaflow.json"
diff_ref: ""
review_ready_at: "2026-08-27T22:38:35-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T22:39:55-03:00"
  decided_at: "2026-08-27T22:39:55-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator ejecutor autoasignado) sin hallazgos — diff, tests (RED→GREEN, 107 OK), idempotencia (2 corridas idénticas) y manifest revisados. CP-MEM-Approval 2026-08-27"
---

# MEM-260827-2238 — Fix BUG-025: skill MetaFlow reproducible desde el pipeline + front door consistente

| Field           | Value |
|-----------------|-------|
| **TASK**        | [US-001.TASK-030](../12-functional/tasks/US-001.TASK-030-fix-skill-metaflow.md) |
| **SPEC**        | [SPEC-260827-2229](../21-spec/SPEC-260827-2229-fix-skill-metaflow.md) — rev 1 |
| **Delivery Loop**    | 1 |
| **ADRs**        | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) |

---

## 1. Executive summary

Este Delivery Loop codificó en el pipeline de transformación el rename de la
skill de Codex que hasta ahora solo existía como edición manual: el diccionario
(`mapping.json`) ahora genera `.agents/skills/MetaFlow/SKILL.md` con el
frontmatter `name: MetaFlow`, y el engine (`src/transform.py`) ganó soporte
para reglas de ruta full-path (pattern con `/`), lo que permite distinguir la
carpeta de la skill (`.agents/skills/avenga-devflow` → `MetaFlow`) de la
carpeta de la metodología (`devflow/avenga-devflow` → `metaflow/ai-sdlc/`,
que permanece intacta). Además se restauró la sección de proyecto "Two
partitions" de `AGENTS.md` raíz (contrato de BUG-020/TASK-025 que una edición
manual había vaciado), se actualizaron las referencias stale de `README.md`
raíz y `test_front_door.py`, y se agregó un test de reproducción dedicado.
El resultado: `distribution-kit/` vuelve a ser 100 % reproducible — dos
corridas reales consecutivas producen 149 archivos byte-idénticos (idempotencia
verificada), el kit regenerado contiene la skill `MetaFlow` con cero tokens
prohibidos (exit 0), y la suite completa pasó de 104 tests (1 failure) a
**107 tests, 0 failures**. La evidencia de cada corrida quedó en
`transform-reports/5.1/` (20260827-223709 y 20260827-223732).

## 2. Implemented phases

### Phase A — RED: test de reproducción

Se creó `src/tests/test_reproducibilidad.py` con tres tests que corren el
pipeline real (input-kit → directorio temporal) y verifican: (1) el plan
genera `.agents/skills/MetaFlow/SKILL.md` y no `.agents/skills/ai-sdlc/SKILL.md`;
(2) el archivo generado tiene frontmatter `name: MetaFlow` y no `name: ai-sdlc`;
(3) la carpeta de la metodología `metaflow/ai-sdlc/` sigue existiendo. En el
estado previo al fix, los tests 1 y 2 fallaban (el pipeline producía `ai-sdlc`),
y `test_front_door.test_agents_md_seccion_proyecto` fallaba por la sección de
proyecto vacía — dos evidencias RED del mismo defecto.

### Phase B — Fix del pipeline (mapping + engine)

En `mapping.json` se agregaron dos reglas: `P-M6b` (path_rename full-path
`.agents/skills/avenga-devflow` → `.agents/skills/MetaFlow`, order 1013, scope
path) y `M6d` (rename `name: ai-sdlc` → `name: MetaFlow`, order 87, scope
content, filtrada por ruta de salida `.agents/skills/MetaFlow/SKILL.md`). La
regla `M6d` corre después de `M6b` (order 8, que normaliza `avenga-devflow` →
`ai-sdlc` en todo el contenido) para corregir solo el frontmatter de la skill.
En `src/transform.py`, `build_plan` ahora separa las reglas de ruta cuyo
pattern contiene `/` (full-path) y las aplica sobre la ruta relativa completa
antes del procesamiento por componente; las reglas existentes (ninguna con `/`)
mantienen su comportamiento. Un diff byte a byte confirmó que la skill
generada difiere del kit anterior solo en la línea `name:`.

### Phase C — Front door del workshop

Se restauró en `AGENTS.md` raíz la sección "Two partitions — this workshop"
(contenido exacto de HEAD: las tres particiones `metaflow/`, `distribution-kit/`,
`input-kit/` y las tres reglas del workshop). En `README.md` raíz se actualizó
la tabla "What lands" y la nota de plataforma de OpenAI Codex a
`.agents/skills/MetaFlow/SKILL.md` / `name: MetaFlow` / `~/.agents/skills/MetaFlow/`
(las referencias a la carpeta de metodología `metaflow/ai-sdlc/` no cambian).
En `test_front_door.py`, la lista `FRONT_DOOR` ahora apunta a la skill
`MetaFlow`.

### Phase D — GREEN, regeneración real e idempotencia

Se ejecutó `python src/transform.py` dos veces (real): ambas corridas con exit
0, cero tokens prohibidos, 149 archivos / 66 carpetas / 7576 reglas aplicadas,
y snapshots de hash SHA-256 por archivo **idénticos entre corridas** (0
diferencias). La suite completa pasó de 104 tests (1 failure) a 107 tests OK.

## 3. Files created

| File | Purpose |
|------|---------|
| `src/tests/test_reproducibilidad.py` | Test de reproducción del BUG-025: corre el pipeline real a un directorio temporal y verifica que la skill de salida es `.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow`, que no existe `ai-sdlc` y que `metaflow/ai-sdlc/` sigue intacta |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `mapping.json` | Regla `P-M6b` (path_rename full-path `.agents/skills/avenga-devflow` → `.agents/skills/MetaFlow`, order 1013) + regla `M6d` (rename `name: ai-sdlc` → `name: MetaFlow`, order 87, filtrada por ruta de salida de la skill) |
| `src/transform.py` | `build_plan` separa reglas de ruta full-path (pattern con `/`) y las aplica sobre la ruta relativa completa antes de las reglas por componente; sin cambio de comportamiento para las reglas existentes |
| `AGENTS.md` (raíz) | Sección de proyecto "Two partitions — this workshop" restaurada bajo `METAFLOW:PROJECT-SECTION` (contenido de HEAD, 21 líneas) |
| `README.md` (raíz) | Tabla "What lands" y nota de plataforma Codex actualizadas a `.agents/skills/MetaFlow/SKILL.md` / `name: MetaFlow` / `~/.agents/skills/MetaFlow/` |
| `src/tests/test_front_door.py` | `FRONT_DOOR` apunta a `(".agents", "skills", "MetaFlow", "SKILL.md")` |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `distribution-kit/.agents/skills/ai-sdlc/SKILL.md` (generado) | `distribution-kit/.agents/skills/MetaFlow/SKILL.md` | El pipeline ahora genera la skill como `MetaFlow` (regla `P-M6b`); el rename manual previo quedó codificado y reproducible |

## 6. Files deleted

| File | Reason |
|------|--------|
| — (ninguno intencional) | El `ai-sdlc/SKILL.md` del kit dejó de generarse; la purga de retención 2/versión eliminó la corrida 20260827-172449 de `transform-reports/` (comportamiento R6 de US-001, registrado en el log del run) |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Regla full-path (pattern con `/`) en vez de cambiar `P-M6` globalmente | Cambiar `P-M6` rompería `devflow/avenga-devflow` → `metaflow/ai-sdlc/`; una regla más específica aplicada sobre la ruta completa deja la metodología intacta (verificado por el test de la carpeta) |
| Regla content `M6d` corre después de `M6b` (order 87 > 8) con filtro `path` | `M6b` normaliza todo el `avenga-devflow` → `ai-sdlc`; corregir solo el frontmatter de la skill después del normalize evita colisiones de order y no toca el resto del contenido |
| Restaurar `AGENTS.md` raíz con el contenido exacto de HEAD | Opción 1 elegida por el propietario: es el contrato de BUG-020/TASK-025, el README la referencia y el test la exige |
| No tocar `input-kit/` | R1 de US-001: materia prima solo lectura; el diccionario es el lugar de los renames |
| Test de reproducción con pipeline real a temp | Evidencia RED/GREEN autónoma que no depende del estado del kit commiteado |

## 8. Deviations and assumptions

- Sin desviaciones de la SPEC-260827-2229 rev 1: las cinco fases se
  implementaron según lo prescrito y las 7 ACs quedaron verificadas.
- El defecto preexistente `tasks[28] = "...TASK-029-fix-tools-linaje.md.md"`
  en el manifest de US-001 quedó **fuera de alcance** (G36 — valor registrado;
  decisión del propietario pendiente).
- La purga automática de la corrida 20260827-172449 en `transform-reports/`
  es el comportamiento esperado de retención (2 por versión, R6).

## 9. Verification evidence

### Build
```
python src/transform.py   # corrida real 1 → exit 0, 149 archivos, 7576 reglas, 0 tokens prohibidos
python src/transform.py   # corrida real 2 → exit 0, idéntica; evidencia 20260827-223732
```

### Tests
```
python -m unittest discover -s src/tests
Ran 107 tests in 16.197s
OK
```

### BUG Delivery Loop evidence
- **RED:** `python -m unittest src.tests.test_reproducibilidad` → 2 failures
  (el plan generaba `.agents/skills/ai-sdlc/SKILL.md`; la skill MetaFlow no
  existía en la salida) + `test_front_door.test_agents_md_seccion_proyecto`
  FAIL (sección de proyecto vacía) — suite previa 104 tests, 1 failure.
- **GREEN:** `python -m unittest src.tests.test_reproducibilidad` → 3/3 OK;
  `python -m unittest src.tests.test_front_door` → 5/5 OK; suite completa
  → 107 tests OK; kit regenerado con `name: MetaFlow` y diff vs HEAD anterior
  de una sola línea (`name: ai-sdlc` → `name: MetaFlow`).

### Gates
- Unit/integration: **pass** (107 tests OK)
- Perf-smoke: **pass** (corridas reales < 1 min, ADR-001)
- Secret-leak: **pass** (sin secretos)
- Hallucination-lint: **pass** (documentación verificable contra el árbol real)
- IP/license: **pass** (sin dependencias nuevas)
- Test-first evidence: **pass** (RED registrado antes del fix)
- Behavioral reproducibility: **pass** (2 corridas → 149 archivos idénticos)
- TASK-manifest validation: **pass** (manifest TASK-030 válido contra schema v1)
- SAST/DAST, prompt-injection, PII/DLP, dependency-confusion: **n/a** (sin
  superficie externa, sin secretos, sin PII, stdlib únicamente — razones en
  SPEC §9)

## 10. Manual interventions

Ninguna — todo el código, reglas y documentación fueron generados por el agente
en el Delivery Loop (el trabajo manual previo del usuario quedó codificado y
sustituido por el producto del pipeline).

## 11. Evidence links

- **Diff / PR:** working tree (sin commit — G34: requiere pedido explícito)
- **Commit:** baseline `273295b` (working tree con los cambios del fix)
- **Cumulative TASK manifest:** `metaflow/23-metrics/tasks/US-001.TASK-030-fix-skill-metaflow.json`
- **Evidencia de corridas:** `transform-reports/5.1/20260827-223709/` y `20260827-223732/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1h (ciclo completo con gobernanza) |
| Delivery Loop number | 1 |
| Tests created | 3 (E2E de reproducción del pipeline) |
| AI-generated code | 100 % |
| First-pass approval | pendiente (CP-MEM-Approval) |

## 13. Pending items and stubs

- [ ] Decisión del propietario sobre el defecto preexistente
  `.md.md` en el manifest de US-001 (G36 — fuera de este TASK)
- [ ] Commit de los cambios (requiere pedido explícito — G34)
- [ ] `CP-TASK-DONE-Approval` tras la aprobación del MEM

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** Este MEM no tiene estado mutable y nunca se
> auto-aprueba. El Dev-validator que ejecutó el TASK inspecciona el diff real,
> la evidencia de tests/gates, el MEM y el manifest, y registra
> `CP-MEM-Approval` aquí y en el `checkpoint_approvals[]` del manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenioserrano` |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T22:38:35-03:00` — paquete completo presentado |
| **review.started_at** | `2026-08-27T22:39:55-03:00` |
| **review.decided_at** | `2026-08-27T22:39:55-03:00` |
| **Review evidence** | diff (mapping + engine + front door + tests), 107 tests OK, RED→GREEN, idempotencia (2 corridas idénticas), manifest válido |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Aprobación del propietario (Dev-validator ejecutor autoasignado) sin hallazgos — diff, tests (RED→GREEN, 107 OK), idempotencia y manifest revisados |
