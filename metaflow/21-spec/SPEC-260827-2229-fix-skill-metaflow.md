---
id: "SPEC-260827-2229-fix-skill-metaflow"
title: "Fix BUG-025: codificar el rename de la skill ai-sdlc → MetaFlow en el pipeline y restaurar el front door de la raíz"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-025"
task: "US-001.TASK-030-fix-skill-metaflow"
revision: 1
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T22:29:00-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T22:32:42-03:00"
  decided_at: "2026-08-27T22:32:42-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — SPEC-260827-2229 revisada: fases RED→GREEN, ACs testables, gates, idempotencia (AC-6) y rollback definidos. CP-SPEC-Approval 2026-08-27"
---

# SPEC-260827-2229 — Fix BUG-025: skill MetaFlow reproducible desde el pipeline + front door de la raíz consistente

| Field | Value |
|-------|-------|
| **Origin** | [BUG-025](../13-bugs/BUG-025-skill-metaflow-no-reproducible.md) (aprobado — CP-BUG-Approval 2026-08-27) |
| **TASK** | [US-001.TASK-030](../12-functional/tasks/US-001.TASK-030-fix-skill-metaflow.md) (aprobado — CP-TASK-READY-Approval 2026-08-27) |
| **ADRs** | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) (reglas longest-first, path_rename, verificador) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Codificar en el pipeline de transformación el rename de la skill de Codex
`.agents/skills/ai-sdlc/SKILL.md` → `.agents/skills/MetaFlow/SKILL.md` (ruta y
frontmatter `name: MetaFlow`), que hoy existe solo como edición manual
untracked: una regeneración real de `distribution-kit/` la revierte a
`ai-sdlc` (regla `P-M6`) y pierde el trabajo. Simultáneamente, restaurar la
sección de proyecto "Two partitions" de `AGENTS.md` raíz (contrato de
BUG-020/TASK-025) y actualizar las referencias stale de `README.md` raíz y
`test_front_door.py`. Al terminar, el kit vuelve a ser 100 % reproducible
desde el pipeline con la skill `MetaFlow`, el front door del workshop es
consistente y la suite de tests queda 100 % verde. Si no se implementa, cada
regeneración destruye el rename manual y la suite permanece en rojo.

## 2. Context

El BUG-025 (aprobado) documenta dos ediciones manuales fuera del pipeline:

1. **Rename de la skill a mano:** `.agents/skills/ai-sdlc/` → `.agents/skills/MetaFlow/`
   (y `name: ai-sdlc` → `name: MetaFlow`) en la raíz y en `distribution-kit/`.
   El pipeline sigue generando `ai-sdlc` (regla `P-M6`, path_rename
   `avenga-devflow → ai-sdlc`, order 1009) y el engine (`apply_path`) aplica
   renames **por componente de ruta**, sin poder distinguir
   `.agents/skills/avenga-devflow` (debe → `MetaFlow`) de `devflow/avenga-devflow`
   (debe → `metaflow/ai-sdlc/`). Un diff byte a byte demostró que el contenido
   de la skill manual es idéntico al del kit actual salvo la línea
   `name: ai-sdlc` → `name: MetaFlow`.
2. **AGENTS.md raíz vaciado:** la sección de proyecto quedó vacía, rompiendo
   `test_front_door.test_agents_md_seccion_proyecto` y la referencia de
   `README.md` raíz ("it carries the two-partition model in its project section").

Restricciones vigentes: ADR-001 (engine en `src/`, diccionario en
`mapping.json` como datos, reglas aplicadas en orden longest-first, verificador
de tokens prohibidos al final del run real); regla del workshop (nada edita
`distribution-kit/` a mano — se regenera); `input-kit/` es solo lectura (R1 de
US-001); la carpeta de la metodología `metaflow/ai-sdlc/` conserva su nombre.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | [US-001.TASK-030](../12-functional/tasks/US-001.TASK-030-fix-skill-metaflow.md) | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | [US-001](../12-functional/user-stories/US-001-toolkit-transformacion.md) | CP-US-Approval ✓ (2026-08-27) |
| BUG | [BUG-025](../13-bugs/BUG-025-skill-metaflow-no-reproducible.md) | CP-BUG-Approval ✓ (2026-08-27) |
| ADRs | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) | CP-ADR-Approval ✓ |
| OQs | OQ-001..004 | answered ✓ (sin bloqueo G35) |
| Repository baseline | HEAD `273295b` (+ working tree con ediciones manuales del BUG-025) | — |

## 4. Scope

### In scope

- `mapping.json`: regla **path full-path** `.agents/skills/avenga-devflow` →
  `.agents/skills/MetaFlow` (pattern con `/`, aplicada sobre la ruta relativa
  completa antes del procesamiento por componente) + regla **content** para el
  frontmatter `name: avenga-devflow` → `name: MetaFlow` (filtrada por ruta de
  salida `.agents/skills/MetaFlow/SKILL.md`, order anterior a `M6b`).
- `src/transform.py`: soporte en `build_plan` para reglas de ruta cuyo pattern
  contenga `/` (full-path), aplicadas sobre `rel_posix` antes de `apply_path`
  por componente; las reglas existentes sin `/` mantienen su comportamiento.
- Regeneración real de `distribution-kit/` (`python src/transform.py`).
- `AGENTS.md` (raíz): restauración de la sección de proyecto "Two partitions
  — this workshop" (contenido exacto de HEAD, 21 líneas).
- `README.md` (raíz): tabla "What lands" y nota de plataforma Codex —
  `.agents/skills/ai-sdlc/SKILL.md` → `.agents/skills/MetaFlow/SKILL.md` y
  `(ai-sdlc)` → `(MetaFlow)` (solo las referencias a la **skill**; las citas a
  la carpeta de metodología `metaflow/ai-sdlc/` no cambian).
- `src/tests/`: test de reproducción (pipeline → temp → verifica
  `.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow`), ajuste de
  `test_front_door.py` (`FRONT_DOOR` → `MetaFlow`) y verificación de que
  `test_path_rename.py` / `test_numbering.py` (que enumeran reglas) no se
  rompen (ajustarlos si enumeran ids de forma cerrada).

### Out of scope

- `input-kit/` (materia prima Avenga — no se toca, R1).
- La carpeta `metaflow/ai-sdlc/` del kit (la metodología conserva su nombre).
- `CHANGELOG.md` (historia — G36).
- `tools/` (track de tooling, fuera del transform).
- Commit/push (G34: requiere pedido explícito del humano).
- El defecto preexistente `tasks[28] = "...TASK-029-fix-tools-linaje.md.md"`
  en el manifest de US-001 (G36 — decisión del propietario, reportado).

## 5. Prerequisites and baseline

- BUG-025 aprobado y TASK-030 aprobado (checkpoints registrados).
- Baseline: HEAD `273295b`; working tree con la skill manual
  `.agents/skills/MetaFlow/SKILL.md` (untracked) y `AGENTS.md` raíz sin
  sección de proyecto.
- Suite actual: 104 tests, 1 failure (`test_agents_md_seccion_proyecto`).

## 6. Phases

### Phase A — RED: test de reproducción (sin tocar código de producción)

**Duration:** 1h total cycle — **Complexity:** Low

#### A.1 Test de reproducción del pipeline (nuevo)

Nuevo test en `src/tests/test_reproducibilidad.py` (o extensión de
`test_e2e.py`): ejecuta `run_transform(input-kit → temp, mapping.json real)`
y verifica que el plan/output contiene `.agents/skills/MetaFlow/SKILL.md`
con frontmatter `name: MetaFlow` y que NO existe `.agents/skills/ai-sdlc/`.

**Hoy (RED esperado):** el pipeline produce `.agents/skills/ai-sdlc/SKILL.md`
con `name: ai-sdlc` → el test falla. Registrar la salida como evidencia RED.

**Files created:**
- `src/tests/test_reproducibilidad.py` — test que corre el pipeline real a
  un directorio temporal y valida la skill de salida (ruta + frontmatter).

#### A.2 RED existente (front door)

Ejecutar y registrar: `python -m unittest src.tests.test_front_door` →
`test_agents_md_seccion_proyecto` FAIL (sección de proyecto vacía). Es la
segunda evidencia RED del mismo Delivery Loop.

---

### Phase B — Fix del pipeline: reglas full-path + content

**Duration:** 3h total cycle — **Complexity:** Medium

#### B.1 `mapping.json` — regla path full-path

**Files modified:**
- `mapping.json` — nueva regla `path_rename` con pattern `.agents/skills/avenga-devflow`
  → replacement `.agents/skills/MetaFlow`, `scope: "path"`, order libre en el
  rango de paths (verificar con `load_mapping` que no colisiona; p. ej. 1013).

La regla contiene `/` en el pattern, lo que la distingue de las reglas
por-componente existentes (P-M6, P-M7, PN*...). Se aplicará sobre la ruta
relativa completa en la Phase B.2, ANTES del procesamiento por componente, de
modo que `P-M6` ya no encuentre `avenga-devflow` en esa ruta y `devflow/
avenga-devflow/` siga → `metaflow/ai-sdlc/`.

#### B.2 `src/transform.py` — soporte full-path en `build_plan`

**Files modified:**
- `src/transform.py` — en `build_plan`, separar `rules_for_path` en dos
  conjuntos: reglas cuyo pattern contenga `/` (full-path) y el resto
  (componentes). Aplicar las full-path sobre `rel_posix` (substring replace,
  mismo orden que hoy) y luego el loop por componente con las restantes.
  Respetar el filtro existente de carpetas ocultas (excluir `PN*` para rutas
  cuyo primer componente empiece con `.`). No cambia el comportamiento de las
  reglas existentes (ninguna tiene `/` en el pattern).

**Verificación unitaria:** `test_path_rename.py` y `test_numbering.py` deben
seguir en verde (ajustarlos solo si enumeran ids de reglas de forma cerrada,
documentando el cambio en el MEM).

#### B.3 `mapping.json` — regla content del frontmatter

**Files modified:**
- `mapping.json` — nueva regla `rename` con pattern `name: avenga-devflow` →
  `name: MetaFlow`, `scope: "content"`, `path: ".agents/skills/MetaFlow/SKILL.md"`
  (ruta de salida post-path_rename), order libre **anterior a `M6b`** (order 8;
  p. ej. 5, verificando que no colisione).

La regla se aplica solo al archivo de la skill (filtro `path` del engine) y
antes de `M6b`, que convierte el resto de `avenga-devflow` → `ai-sdlc`. El
resultado: frontmatter `name: MetaFlow` y cuerpo idéntico al actual
(verificado por diff: solo cambia la línea `name:`).

#### B.4 Regeneración real del kit

Ejecutar `python src/transform.py` (real). Verificar:
- exit 0, cero tokens prohibidos (verificador), reporte en
  `transform-reports/5.1/<run>/`.
- `.agents/skills/MetaFlow/SKILL.md` presente con `name: MetaFlow`; sin
  `.agents/skills/ai-sdlc/`; `metaflow/ai-sdlc/` intacta (la metodología).

---

### Phase C — Front door del workshop (raíz)

**Duration:** 1h total cycle — **Complexity:** Low

#### C.1 `AGENTS.md` raíz — restaurar la sección de proyecto

**Files modified:**
- `AGENTS.md` — restaurar bajo `METAFLOW:PROJECT-SECTION` la sección
  "Two partitions — this workshop" (contenido exacto de HEAD: las tres
  particiones `metaflow/`, `distribution-kit/`, `input-kit/` + las tres
  reglas del workshop). Solo bajo el marcador; el bloque framework intacto.

#### C.2 `README.md` raíz — citas de la skill

**Files modified:**
- `README.md` — tabla "What lands": `.agents/skills/ai-sdlc/SKILL.md` →
  `.agents/skills/MetaFlow/SKILL.md`; nota de plataforma Codex: `(`ai-sdlc`)`
  → `(`MetaFlow`)`. No se tocan las referencias a `metaflow/ai-sdlc/`.

#### C.3 `src/tests/test_front_door.py`

**Files modified:**
- `src/tests/test_front_door.py` — `FRONT_DOOR`:
  `(".agents", "skills", "ai-sdlc", "SKILL.md")` →
  `(".agents", "skills", "MetaFlow", "SKILL.md")`.

---

### Phase D — GREEN, idempotencia y cierre

**Duration:** 1h total cycle — **Complexity:** Low

#### D.1 Suite completa en verde

Ejecutar `python -m unittest discover -s src/tests` → 0 failures
(incluye el nuevo test de reproducción y `test_front_door`).

#### D.2 Idempotencia (opción A del usuario)

Segunda corrida real `python src/transform.py` → comparar el árbol de
`distribution-kit/` resultante contra la corrida anterior (hash por archivo o
`git diff --no-index` sobre dos snapshots): sin diferencias = kit idempotente.
Evidencia registrada en el MEM.

#### D.3 Estado final verificado

`git status` confirma: `.agents/skills/MetaFlow/SKILL.md` generado por el
pipeline (ya no untracked), `ai-sdlc` ausente en el kit; `AGENTS.md` y
`README.md` de la raíz con los cambios del fix.

---

## 7. Acceptance criteria

### AC-1: Pipeline genera la skill en la ruta y con el nombre correctos

**Given** el mapping y el engine con el fix,
**When** se ejecuta el pipeline (dry-run y real),
**Then** el plan/output contiene `.agents/skills/MetaFlow/SKILL.md` con
frontmatter `name: MetaFlow` y no contiene `.agents/skills/ai-sdlc/`.

### AC-2: La carpeta de la metodología no cambia

**Given** el input `devflow/avenga-devflow/`,
**When** se transforma,
**Then** la ruta de salida es `metaflow/ai-sdlc/` (intacta).

### AC-3: Kit real regenerado y verificado

**Given** una ejecución real del pipeline,
**When** termina,
**Then** `distribution-kit/.agents/skills/MetaFlow/SKILL.md` existe con
`name: MetaFlow`, no existe `.agents/skills/ai-sdlc/` y el verificador reporta
cero tokens prohibidos (exit 0).

### AC-4: AGENTS.md raíz con sección de proyecto

**Given** el `AGENTS.md` de la raíz,
**When** se inspecciona bajo `METAFLOW:PROJECT-SECTION`,
**Then** documenta el modelo de dos particiones (`metaflow/`,
`distribution-kit/`, `input-kit/`).

### AC-5: README y test referencian la skill MetaFlow

**Given** el `README.md` raíz y `test_front_door.py`,
**When** se inspeccionan,
**Then** citan `.agents/skills/MetaFlow/SKILL.md` y `name: MetaFlow`, sin
referencias a la skill `ai-sdlc`.

### AC-6: Idempotencia

**Given** dos ejecuciones reales consecutivas del pipeline,
**When** se comparan los árboles de `distribution-kit/` resultantes,
**Then** son idénticos (sin diff).

### AC-7: Suite completa en verde

**Given** la suite de tests,
**When** se ejecuta `python -m unittest discover -s src/tests`,
**Then** 0 failures (con RED registrado antes del fix).

### AC mapping to source (functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-025 expected_result | Reglas full-path + content en mapping; engine; regeneración real; restauración AGENTS.md; README/test | AC-1..AC-7 + test de reproducción + suite verde |
| US-001 AC-2 (diccionario extensible) | Los cambios son reglas en `mapping.json` (datos) + un cambio acotado del engine | Tests unitarios + E2E |
| US-001 AC-10/R5 (borrado previo) | La regeneración real borra y reconstruye `distribution-kit/` | AC-3, AC-6 |

---

## 8. Testing strategy

- **Unit tests:** comportamiento full-path de `build_plan` (regla con `/`
  aplica sobre la ruta completa; reglas sin `/` intactas) — en
  `test_path_rename.py` o nuevo caso en `test_reproducibilidad.py`.
- **Integration/E2E:** `test_reproducibilidad.py` corre el pipeline real a
  temp y valida la skill de salida; suite completa en verde.
- **Kit real:** AC-3 (verificador + rutas) tras la regeneración.
- **Edge cases:** ruta `.agents/skills/avenga-devflow` (→ MetaFlow) vs
  `devflow/avenga-devflow` (→ ai-sdlc) — no sobre-match; regla content solo
  en el archivo de la skill (filtro `path`); colisión de orders rechazada por
  `load_mapping`.
- **BUG evidence:** RED = test de reproducción fallando (produce `ai-sdlc`) +
  `test_agents_md_seccion_proyecto` FAIL → GREEN = suite completa + kit real
  con `MetaFlow` + idempotencia (AC-6).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (104+ tests) | pass |
| SAST / DAST | Sin superficie externa (pipeline local, stdlib) | n/a (razón: sin código desplegado) |
| Perf-smoke (p95/p99) | Transform < 1 min (ADR-001) | pass (evidencia: corridas reales) |
| Prompt-injection scan | Sin entradas externas no confiables | n/a (razón: diccionario versionado, input controlado) |
| Secret-leak scan | Sin secretos en el diff | pass |
| Hallucination lint | Documentación verificable contra el árbol real | pass |
| IP / license provenance | Sin dependencias nuevas (stdlib) | pass |
| PII / DLP | Sin datos personales (data_classification: internal) | n/a (razón: sin PII) |
| Dependency-confusion | Sin dependencias externas | n/a (razón: stdlib únicamente) |
| Test-first evidence | RED registrado antes del fix (Phase A) | pass |
| Behavioral reproducibility | Idempotencia: 2 corridas → mismo árbol (AC-6) | pass |
| TASK-manifest validation | Manifest TASK-030 válido contra schema v1 | pass |

---

## 10. Security and data

- Sin autenticación, red, secretos ni datos personales: pipeline local que
  procesa documentación de un repositorio versionado.
- `data_classification: internal` — sin cambios de clasificación.
- Riesgo de contaminación de marca (BR-001) controlado por el verificador de
  tokens prohibidos en cada corrida real.

---

## 11. Monitoring and observability

- Evidencia de cada corrida real en `transform-reports/5.1/<run>/`
  (reporte JSON+MD, diffs por archivo, lista de sin-cambios, log) — retención
  2 por versión (R6 de US-001).
- El reporte del run documenta la regla full-path aplicada (conteo por regla).

---

## 12. Migration, compatibility and rollback

- **Migration:** N/A (sin schema ni datos persistentes; el kit es generado).
- **Compatibility:** las reglas existentes sin `/` en el pattern mantienen
  comportamiento idéntico (verificado por la suite previa en verde).
- **Rollback:** revertir `mapping.json` + `src/transform.py` y regenerar —
  el pipeline es idempotente (AC-6); el kit vuelve a `ai-sdlc` si se revierte.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresión del engine al separar full-path | 2 | 4 | Suite completa (104+ tests) + unitarios del nuevo camino |
| Sobre-match del rename (tocar `metaflow/ai-sdlc/`) | 2 | 4 | Pattern full-path específico `.agents/skills/avenga-devflow` + AC-2 |
| Colisión de orders en mapping | 1 | 3 | `load_mapping` la rechaza; verificación al agregar reglas |
| Tests que enumeran reglas de forma cerrada se rompen | 3 | 2 | Verificar `test_path_rename.py`/`test_numbering.py` y ajustarlos documentando |
| Encoding del archivo generado difiere del manual | 2 | 2 | Diff byte a byte en la verificación de la regeneración |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Regla **full-path** (pattern con `/`) en vez de cambiar `P-M6` globalmente | Cambiar `P-M6` rompería `devflow/avenga-devflow` → `metaflow/ai-sdlc/`; una regla más específica (longest-first) deja la metodología intacta |
| Regla **content** filtrada por `path` en vez de editar el input | `input-kit/` es solo lectura (R1); el diccionario es el lugar de los renames |
| No tocar el defecto `.md.md` del manifest de US-001 | G36 (valor registrado) — decisión del propietario, reportado fuera del TASK |
| Restaurar AGENTS.md raíz (opción 1 del usuario) | Contrato de BUG-020/TASK-025: la sección documenta las dos particiones; el test y el README la referencian |

---

## 15. Stop conditions

- El engine no puede distinguir `.agents/skills/avenga-devflow` de
  `devflow/avenga-devflow` sin romper reglas existentes → parar y consultar
  (posible ADR para un mecanismo distinto).
- La regeneración real produce tokens prohibidos → parar, registrar en MEM y
  revisar reglas (el verificador bloquea el run).
- Un test existente de reglas cerradas exige rediseño del enfoque → parar y
  consultar al propietario antes de cambiarlo.

---

## 16. Definition of Done (DoD)

- [ ] Phase A RED registrada (test de reproducción + test_front_door)
- [ ] Phases B–D implementadas; AC-1..AC-7 pasan
- [ ] Suite completa GREEN (unit + E2E)
- [ ] Regeneración real con cero tokens prohibidos + idempotencia verificada
- [ ] Código/reglas siguen ADR-001
- [ ] Gates pass / waived / n/a (razón) según tabla
- [ ] MEM creado en `metaflow/22-memory/` (red y green por separado)
- [ ] Manifest `delivery_loops[]` entry en `23-metrics/tasks/US-001.TASK-030-fix-skill-metaflow.json`
- [ ] CP-MEM-Approval registrado

---

## 17. References

- [BUG-025](../13-bugs/BUG-025-skill-metaflow-no-reproducible.md)
- [US-001](../12-functional/user-stories/US-001-toolkit-transformacion.md)
- [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md)
- [US-001.TASK-030](../12-functional/tasks/US-001.TASK-030-fix-skill-metaflow.md)
- [MEM-260827-1632-front-door-raiz](../22-memory/MEM-260827-1632-front-door-raiz.md) (contrato de AGENTS.md)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Revisión 1 — borrador inicial (derivada de BUG-025 + TASK-030) |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator (+ domain owners aplicables) registra `CP-SPEC-Approval`
> (en el bloque `review` del frontmatter). La aprobación del TASK
> (`CP-TASK-READY-Approval`) autoriza preparar la SPEC; **la aprobación de la
> SPEC** autoriza el code-run / Delivery Loop. Un cambio material de una
> fuente gobernada invalida esta aprobación — parar, revisar y re-aprobar
> (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator (eugenioserrano) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T22:29:00-03:00` |
| **review.started_at** | `2026-08-27T22:32:42-03:00` |
| **review.decided_at** | `2026-08-27T22:32:42-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
