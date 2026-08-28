---
id: "MEM-260828-0125"
title: "Eliminación del track heredado tools/ (legado AvengaDevFlow)"
date: "2026-08-28"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
task: "US-000.TASK-002"
spec: "SPEC-260828-0119"
spec_revision: 1
delivery_loop: 1
execution_outcome: "ready_for_review"
baseline: "2e564b4"
applied_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
manifest: "metaflow/23-metrics/tasks/US-000.TASK-002-eliminacion-track-tools.json"
diff_ref: ""
review_ready_at: "2026-08-28T01:25:28-03:00"
review: # CP-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-28T01:26:00-03:00"
  decided_at: "2026-08-28T01:26:57-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Aprobación del propietario (Dev-validator ejecutor, autoasignado) sin hallazgos — revisó diff, 106 tests OK y las 5 ACs verificadas, 2026-08-28"
---

# MEM-260828-0125 — Eliminación del track heredado `tools/`

| Field           | Value |
|-----------------|-------|
| **TASK**        | US-000.TASK-002 |
| **SPEC**        | [SPEC-260828-0119](../21-spec/SPEC-260828-0119-eliminacion-track-tools.md) rev 1 |
| **Delivery Loop**    | 1 |
| **ADRs**        | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) |

---

## 1. Executive summary

Este Delivery Loop eliminó el track heredado `tools/` del linaje
AvengaDevFlow (10 especificaciones del tooling Go original — clock, identity,
indexer, manifest, next-id, reporter, scaffold, status, validator —, BUILD.md,
README.md y la herramienta Python `agent-wrappers/` con su código y tests),
que el proyecto no iba a usar, y actualizó todo lo que lo referenciaba: el
test de reproducción del BUG-024 (`TestBug024ToolsLinaje` en
`src/tests/test_linaje.py`, que recorría `tools/*.md` y leía `tools/BUILD.md`)
se reemplazó por un guard de ausencia que impide que el track reaparezca sin
un cambio deliberado, y la documentación viva (README de la raíz, mvp-scope
X4 y visión AG4) quedó sin referencias al folder. El borrado se hizo con
`git rm` (24 archivos trackeados) y se completó eliminando físicamente los
`__pycache__` sin trackear que el guard detectó — la suite pasó de 107 a 106
tests (2 eliminados + 1 guard) y quedó en verde. La verificación final
confirmó las 5 ACs: `tools/` ausente del árbol y del índice git, suite
completa OK, sin referencias vivas al folder, artefactos históricos intactos
(G36) y texto del framework + kit intactos (la promesa del tooling track
futuro de la metodología permanece). En paralelo, por instrucción del
propietario, el ADR-002 (superado por ADR-003, vida cerrada) se archivó en
`metaflow/11-adrs/_archive/` con su INDEX actualizado.

## 2. Implemented phases

### Phase A — Borrado del track heredado

Se ejecutó `git rm -r tools/` sobre los 24 archivos trackeados del folder
(registro como borrado, recuperable desde git). El guard de ausencia del
test reveló que quedaban residuos sin trackear — `tools/agent-wrappers/
__pycache__` y `tools/agent-wrappers/tests/__pycache__` (bytecode `.pyc` de
ejecuciones previas, nunca commiteado) — que se eliminaron físicamente con
`Remove-Item -Recurse -Force`. El folder quedó ausente del working tree y del
índice git.

### Phase B — Suite de tests actualizada

`src/tests/test_linaje.py`: se actualizó el docstring (BUG-021..023 +
guard del BUG-024), se eliminó el `import re` (quedaba solo para el test del
BUG-024) y la clase `TestBug024ToolsLinaje` (2 tests que recorría
`tools/*.md` en busca de "devflow" y verificaba el destino `metaflow/bin` en
`tools/BUILD.md`) se reemplazó por `TestToolsAusente` — un guard que afirma
que `(ROOT / "tools")` no existe, impidiendo que el track reaparezca sin un
cambio deliberado. Las clases de reproducción del linaje del kit y front
door (BUG-021..023) quedaron intactas. La suite completa pasó de 107 a 106
tests (2 eliminados + 1 guard) y quedó en verde, incluido el E2E del
pipeline.

### Phase C — Documentación viva

Tres documentos vivos se actualizaron para eliminar las referencias al
folder: (1) `README.md` de la raíz — el párrafo de la sección "Working on the
methodology" que describía "[`tools/`](tools/) holds the source code of the
tools..." (un enlace muerto tras el borrado) se reemplazó por una nota sin la
ruta literal: el tooling track heredado fue eliminado (2026-08-28,
US-000.TASK-002) y la metodología no requiere toolchain; (2)
`metaflow/02-analysis/scope/mvp-scope.md` X4 — el pendiente "Cuando se decida
el futuro de la pista" quedó decidido: "Decidido 2026-08-28: eliminación del
track (US-000.TASK-002) | Cerrado"; D4 se conservó como registro de la
decisión histórica (`src/` sobre `tools/`); (3) `metaflow/02-analysis/
vision/vision.md` AG4 — nota de resolución: la pista heredada fue eliminada;
el anti-objetivo (no reimplementarla) permanece.

## 3. Files created

| File | Purpose |
|------|---------|
| `metaflow/12-functional/tasks/US-000.TASK-002-eliminacion-track-tools.md` | TASK no-funcional aprobado que definió el WHAT (borrado del track + actualización de referencias) |
| `metaflow/21-spec/SPEC-260828-0119-eliminacion-track-tools.md` | SPEC aprobada (revisión 1) que planificó el borrado en tres fases |
| `metaflow/23-metrics/tasks/US-000.TASK-002-eliminacion-track-tools.json` | Manifest del TASK (validado contra `manifest-v1-task.schema.json`) con checkpoints y la entrada de este Delivery Loop |
| `metaflow/11-adrs/_archive/ADR-002-numeracion-carpetas-kit.md` | ADR-002 archivado (vida cerrada, superseded por ADR-003) — instrucción del propietario, §5.4 |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/tests/test_linaje.py` | Clase `TestBug024ToolsLinaje` reemplazada por el guard `TestToolsAusente` (ausencia de `tools/`); docstring actualizado; `import re` eliminado |
| `README.md` (raíz) | Párrafo muerto sobre `tools/` reemplazado por la nota de eliminación del track (sin ruta literal) |
| `metaflow/02-analysis/scope/mvp-scope.md` | X4: pendiente resuelto (eliminación del track, 2026-08-28); D4 conservado como registro histórico |
| `metaflow/02-analysis/vision/vision.md` | AG4: nota de resolución (pista eliminada; anti-objetivo permanece) |
| `metaflow/11-adrs/INDEX.md` | ADR-002 movido a `_archive/` (link actualizado, nota de archivado) |
| `metaflow/12-functional/INDEX.md` | TASK-002 agregado (candidate → In Development → Development Completed en el ciclo) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `metaflow/11-adrs/ADR-002-numeracion-carpetas-kit.md` | `metaflow/11-adrs/_archive/ADR-002-numeracion-carpetas-kit.md` | Archivado de documento con vida cerrada (superseded por ADR-003) — §5.4, G38 |

## 6. Files deleted

| File | Reason |
|------|--------|
| `tools/**` (24 archivos trackeados: 10 DESIGN.md, BUILD.md, README.md, agent-wrappers/DESIGN.md + generate.py + parity.py + agentmodel.py + tests) | Track heredado de AvengaDevFlow sin uso en el proyecto — decisión del propietario 2026-08-28 (US-000.TASK-002) |
| `tools/**/__pycache__/*.pyc` (residuos sin trackear) | Bytecode de ejecuciones previas; el guard detectó que el folder seguía existiendo y se completó el borrado físico |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Reemplazar `TestBug024ToolsLinaje` por el guard `TestToolsAusente` en vez de borrar los tests sin más | La reproducción del BUG-024 pierde su sujeto, pero el guard impide que el track reaparezca sin un cambio deliberado — y de hecho detectó los residuos `__pycache__` en el primer run |
| Completar el borrado físico de los `__pycache__` sin trackear | `git rm` solo elimina archivos trackeados; el folder debe desaparecer del working tree (AC-1) |
| Nota de eliminación en README sin la ruta literal `tools/` | Evita un enlace muerto y mantiene limpio el grep de restos (AC-3); el mensaje ("no tooling required") se conserva |
| X4 marcado resuelto; D4 conservado | X4 era el pendiente ("cuando se decida el futuro de la pista") — este cambio ES la decisión; D4 es el registro histórico de la decisión `src/` sobre `tools/` |
| No tocar el texto del framework ni el kit (AC-5) | La promesa del tooling track futuro en `MetaFlow.md` §42-reports es genérica de la metodología, no este folder heredado; cambiarla sería un cambio de metodología aparte |
| ADR-002 archivado en paralelo | Vida cerrada (superseded por ADR-003) — instrucción explícita del propietario; ADR-001 (parcialmente superado pero activo) NO se archiva (G38) |

## 8. Deviations and assumptions

Sin desviaciones respecto de la SPEC aprobada (revisión 1), con dos
hallazgos de ejecución resueltos dentro del alcance: (1) los residuos
`__pycache__` sin trackear que impedían la AC-1 (detectados por el guard,
eliminados físicamente); (2) una referencia viva adicional en `README.md`
(sección "Working on the methodology", línea 132) que la revisión previa no
había capturado por truncamiento del grep — corregida en la Fase C dentro del
mismo loop (el criterio AC-3 cumplió su función). Se asumió que las notas de
resolución (X4, AG4, README) son documentación de la decisión y no
"referencias vivas" al folder — coherente con la SPEC.

## 9. Verification evidence

### Build
```
Sin build — Python 3.12 + stdlib únicamente (ADR-001); sin dependencias.
```

### Tests
```
python -m unittest discover -s src/tests -p "test_*.py"
Ran 106 tests in 16.057s
OK
(107 → 106: 2 tests del BUG-024 eliminados + 1 guard de ausencia)
```

### ACs verificadas
- AC-1: `tools/` ausente del working tree (Test-Path False) y del índice git
  (`git ls-files tools` vacío) ✓
- AC-2: suite completa verde (106 tests, 0 fallos) ✓
- AC-3: grep de `tools/` en `src/` y docs vivas — solo restos intencionales
  (guard, aserción de strings de test_restos_v5, notas de resolución
  X4/D4/AG4) ✓
- AC-4: históricos intactos — `git status` sin cambios en MEMs/SPECs/ADRs/
  US/BUGs/REVs (solo INDEXes y ADR-002 archivado) ✓
- AC-5: `metaflow/ai-sdlc/MetaFlow.md` y `distribution-kit/` sin cambios ✓

### Gates
| Gate | Status |
|------|--------|
| Unit / integration (suite completa) | pass |
| Secret-leak scan (diff sin secretos) | pass |
| Hallucination lint (docs vivas coherentes con el árbol) | pass |
| Behavioral reproducibility (E2E del pipeline) | pass |
| TASK-manifest validation | pass |
| SAST/DAST, perf-smoke, prompt-injection, IP/license, PII/DLP, dependency-confusion, test-first-evidence | n/a (razones en SPEC §9: borrado + tests, sin superficie externa) |

## 10. Manual interventions

None — todo el cambio fue generado y verificado por el agente dentro del
Delivery Loop (el hallazgo de los `__pycache__` y de la referencia de README
se resolvió dentro del loop, sin intervención humana).

## 11. Evidence links

- **Diff / PR:** working tree (sin commit todavía — pendiente de `CP-MEM-Approval`)
- **Commit baseline:** `2e564b4`
- **Cumulative TASK manifest:** `metaflow/23-metrics/tasks/US-000.TASK-002-eliminacion-track-tools.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~30 min ciclo total (sesión 01:17–01:25) |
| Delivery Loop number | 1 |
| Tests created | 1 guard (`TestToolsAusente`); 2 eliminados; 106 total en verde |
| AI-generated code | 100% |
| First-pass approval | pendiente de revisión humana |

## 13. Pending items and stubs

- [ ] Commit del paquete tras `CP-MEM-Approval` (G34: solo con orden explícita)
- [ ] `CP-TASK-DONE-Approval` (aceptación, Tech Lead — routing `debt`)
- [ ] Fuera de alcance: el tooling track futuro de la metodología
  (`MetaFlow.md` §42-reports) — cambio de metodología aparte si se decide

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the TASK; QA/Sec/domain reviewers optional, any risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `CP-MEM-Approval` here and in the manifest's
> `checkpoint_approvals[]`. `approved` completes the Delivery Loop (and, if latest,
> marks the TASK `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW Delivery Loop with a
> NEW MEM. `CP-TASK-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | `human:eugenioserrano` |
| **Roles** | dev_validator |
| **Decision** | approved |
| **review_ready_at** | `2026-08-28T01:25:28-03:00` |
| **review.started_at** | `2026-08-28T01:26:00-03:00` |
| **review.decided_at** | `2026-08-28T01:26:57-03:00` |
| **Review evidence** | diff completo, 106 tests OK, AC-1..AC-5 verificadas |
| **Comments** | None |
| **Findings** | None |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected: diff + tests + ACs (2026-08-28) |
