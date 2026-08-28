---
id: "MEM-260827-1725-fix-tools-linaje"
title: "Delivery Loop 1 — US-001.TASK-029: resto del linaje en tools/ re-expresado a MetaFlow"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
task: "US-001.TASK-029"
spec: "SPEC-260827-1715-fix-tools-linaje"
spec_revision: 1
delivery_loop: 1
execution_outcome: "ready_for_review"
baseline: "5d9b90d (working tree, sin commit)"
applied_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
manifest: "metaflow/23-metrics/tasks/US-001.TASK-029-fix-tools-linaje.json"
diff_ref: "working tree (pendiente instruccion de commit)"
review_ready_at: "2026-08-27T17:25:30-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T21:52:28-03:00"
  decided_at: "2026-08-27T21:52:28-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# MEM-260827-1725-fix-tools-linaje — Delivery Loop 1 — US-001.TASK-029: resto del linaje en tools/ re-expresado a MetaFlow

| Field           | Value |
|-----------------|-------|
| **TASK**        | US-001.TASK-029 |
| **SPEC**        | [SPEC-260827-1715-fix-tools-linaje](../21-spec/SPEC-260827-1715-fix-tools-linaje.md) (rev 1) |
| **Delivery Loop**    | 1 |
| **ADRs**        | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) |

---

## 1. Executive summary

Este Delivery Loop corrigió el BUG-024: las especificaciones del tooling track del workshop (tools/BUILD.md, tools/README.md y los 11 tools/**/DESIGN.md) seguían describiendo el linaje previo — binarios en "distribution-kit/devflow/bin/" (carpeta inexistente en el kit), layout "cmd/devflow", binarios "devflow-windows-amd64.exe" y referencias "DevFlow" al framework. Se re-expresaron los 13 archivos .md de tools/ a la línea MetaFlow (destino distribution-kit/metaflow/bin/, cmd/metaflow, metaflow-windows-amd64.exe, "the metaflow binary", rutas de proyecto adoptante metaflow/). El código de agent-wrappers (.py) quedó fuera del alcance como se definió en la SPEC. El test pasó de RED a GREEN; la suite completa quedó en verde.

## 2. Implemented phases

### Phase A — Test de reproduccion (RED)

Se creo `src/tests/test_linaje.py` (unittest, stdlib) con 8 verificaciones
sobre el output REAL (kit, front door y tools/): ausencia de "v4.2" y
"versions up to 4.1", checkpoints canonicos en las celdas de metricas,
ausencia de "Eugenio Serrano LATAM" (kit + README raiz), presencia de la
entidad real, ausencia de "devflow" en tools/*.md y destino metaflow/bin.
Ejecutado antes de tocar produccion: **7 de 8 fallaron** (RED registrado).

### Phase B — Fix

Re-expresion directa de tools/BUILD.md, tools/README.md y 11 tools/**/DESIGN.md: distribution-kit/devflow/bin/ → distribution-kit/metaflow/bin/, cmd/devflow → cmd/metaflow, devflow-windows-amd64.exe → metaflow-windows-amd64.exe, "the devflow binary" → "the metaflow binary", "the three v4 manifest shapes" → "the three v1 manifest shapes", y el resto de referencias DevFlow → MetaFlow (case-insensitive).

### Phase C — GREEN

Kit regenerado (donde corresponde) y suite completa: `src/tests` **104 OK**
(96 previos + 8 nuevos) y `tools/agent-wrappers/tests` **14 OK**. Verificacion
final de tokens en el kit: cero.

## 3. Files created

| File | Purpose |
|------|---------|
| `src/tests/test_linaje.py` | Suite de reproduccion BUG-021..024: red de seguridad para el linaje, los shorthands, la identidad y tools/ |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| tools/BUILD.md, tools/README.md, tools/**/DESIGN.md (13 archivos) · src/tests/test_linaje.py |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Re-expresión directa (tools/ no es parte del kit y no se regenera) · el código agent-wrappers .py queda fuera (herramienta en uso, revisión aparte) · no se tocó el kit |

## 8. Deviations and assumptions

- Sin desviaciones materiales de la SPEC (fases A-C ejecutadas tal cual).
- Los manifests de TASK-026..029 se crearon con nombre correcto tras corregir
  un error del generador (extension doble .md.md) — corregido y validado.
- git_commit en delivery_loops: null hasta el commit (G34).

## 9. Verification evidence

### Tests — RED (antes del fix)
```
python -m unittest src.tests.test_linaje
Ran 8 tests — FAILED (failures=7)
```

### Tests — GREEN (despues del fix)
```
python -m unittest src.tests.test_linaje
Ran 8 tests in 0.104s — OK

python -m unittest discover -s src/tests -p "test_*.py"
Ran 104 tests in 12.197s — OK

python -m unittest discover -s tools/agent-wrappers/tests -p "test_*.py"
Ran 14 tests in 0.054s — OK
```

### BUG Delivery Loop evidence
- **RED:** 7/8 fallos (patrones de los 4 BUGs presentes en el output real).
- **GREEN:** 8/8 OK + suite completa 104+14; kit con cero tokens prohibidos.

### Gates
| Gate | Resultado |
|------|-----------|
| Unit / integration | pass — 118 tests OK |
| Secret-leak scan | pass — sin secretos |
| Hallucination lint | pass — sin APIs inventadas |
| Test-first evidence | pass — RED registrado antes del fix |
| Behavioral reproducibility | pass — output verificado por test |
| TASK-manifest validation | pass — manifests validos |
| SAST/SBOM, perf, prompt-injection, IP/license, PII, dependency-confusion | n/a — documentacion, sin superficie externa |

## 10. Manual interventions

None — todo el material fue generado por el agente.

## 11. Evidence links

- **Diff / PR:** working tree (sin commit — pendiente instruccion, G34).
- **Commit:** baseline `5d9b90d`.
- **Cumulative TASK manifest:** `metaflow/23-metrics/tasks/US-001.TASK-029-fix-tools-linaje.json`.

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~25 min (bloque TASK-026..029) |
| Delivery Loop number | 1 |
| Tests created | 8 (unit — reproduccion BUG-021..024) |
| AI-generated code | 100% |
| First-pass approval | pending (CP-MEM-Approval) |

## 13. Pending items and stubs

- [x] CP-MEM-Approval (bloque TASK-026..029) — aprobado; pendiente CP-TASK-DONE-Approval.
- [ ] Commit del bloque completo (tras aprobaciones).

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** Este MEM fue creado por el agente sin estado
> mutable y **nunca se auto-aprueba**. Un humano calificado inspecciona el
> diff real, la evidencia RED/GREEN, el MEM y el manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | human:eugenioserrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T17:25:30-03:00` |
| **review.started_at** | `2026-08-27T21:52:28-03:00` |
| **review.decided_at** | `2026-08-27T21:52:28-03:00` |
| **Review evidence** | diff + RED/GREEN + gates + MEM + manifest |
| **Findings** | Ninguno — aprobado sin comentarios |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Aprobación del propietario; diff + RED/GREEN + 118 tests OK revisados |
