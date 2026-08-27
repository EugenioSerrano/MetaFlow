---
id: "MEM-260827-0257"
title: "BOLT-005 — Corrección del sobre-match de numeración + 32-adv-reviews (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-005"
spec: "SPEC-260827-0251"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-005-correccion-numeracion.json"
diff_ref: ""
review_ready_at: "2026-08-27T02:57:47-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:58:54-03:00"
  decided_at: "2026-08-27T02:58:54-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 73/73, corrida de producción (0 sobre-match, enum OK, 32-adv-reviews) y manifest en conversación, 2026-08-27"
---

# MEM-260827-0257 — BOLT-005: Corrección del sobre-match + 32-adv-reviews

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-005 |
| **SPEC**        | [SPEC-260827-0251](../spec/SPEC-260827-0251-bolt005-correccion-numeracion.md) — revisión 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-003](../adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce corrige los hallazgos de la REV-002 (aprobada): el sobre-match
de las reglas de numeración que corrompió **1224 referencias de prosa**
("12-functional analyst", "run the 24-tests") y rompió el enum del schema de
manifests. Según la ADR-003, las 20 reglas de contenido (N-rules) pasaron a
exigir la **barra** como delimitador (`(?<![\w-])<nombre>/` → `NN-<nombre>/`):
ahora **solo las referencias de ruta se numeran** y el vocabulario suelto
queda intacto (los enums de schemas incluidos). Además la carpeta 32 pasó a
**`32-adv-reviews`** (N32/PN32). Resultado de la corrida de producción:
**EXIT=0**, **0 sobre-match en prosa** (verificado por el medidor y la E2E),
enum del schema **`["functional","non-functional","test"]`** restaurado,
`32-adv-reviews` presente y `32-adversarial-reviews` ausente, 0 referencias
viejas y 0 links reales rotos. La suite completa quedó en verde:
**73/73 tests** (72 previos + ajustes + 1 nuevo de prosa), con RED registrado
(6 fallas de expectativa) y GREEN. Con esto la REV-002 queda cerrada y el kit
**MetaFlow v1.1 es consistente y publicable**: identidad propia, versionado
1.1/familia v1, carpetas numeradas por uso, vocabulario intacto, JSONs y
links sanos.

## 2. Implemented phases

### Phase A — Diccionario: N-rules con barra + rename 32

Se reescribieron las **20 reglas de contenido** de numeración: el patrón
pasó de `(?<![\w-])<nombre>(?![\w-])` (palabra suelta) a
`(?<![\w-])<nombre>/` (referencia de ruta) con reemplazo `NN-<nombre>/` que
conserva la barra. El lookbehind negativo mantiene las protecciones de
substrings (`business-risks/`, `reviews/` dentro de `adversarial-reviews/`,
`agents/` dentro de `agents-data/`). La **N32** ahora mapea
`adversarial-reviews/` → `32-adv-reviews/` y la **PN32** (ruta anclada)
`^adversarial-reviews$` → `32-adv-reviews`. El resto del esquema ADR-002 se
mantiene (ADR-003 no cambió bloques ni gaps).

### Phase C — Tests

`test_numbering.py` reescrito: las 20 carpetas como rutas, **prosa intacta**
(la palabra suelta no se numera), protecciones de substrings, plurales y
campos (`inputs`, `spec_revisions`, `test_bolts`→`test_tasks` por B12),
componentes de ruta con anclas (incl. `adversarial-reviews` →
`32-adv-reviews`), y la **E2E real** que verifica: 20 carpetas + `ai-sdlc`,
`32-adversarial-reviews` ausente, **0 sobre-match** (ningún `NN-nombre` sin
`/`), 0 referencias viejas y el **enum del schema**
`["functional","non-functional","test"]`. El fixture `refs.md` esperado usa
`32-adv-reviews/`. Se corrigió la expectativa de `test_remove` (DORA
"metrics" ya no se numera sin barra).

## 3. Files created

| File | Purpose |
|------|---------|
| — | Ninguno (cambios sobre archivos existentes) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `mapping.json` | N-rules de contenido con barra obligatoria (`(?<![\w-])<nombre>/` → `NN-<nombre>/`); N32/PN32 → `32-adv-reviews` |
| `src/tests/test_numbering.py` | Reescrito: prosa intacta, rutas con barra, 32-adv-reviews, enum del schema, E2E con 0 sobre-match |
| `src/tests/fixtures/kit-mini-expected/refs.md` | `32-adv-reviews/` |
| `src/tests/test_remove.py` | Expectativa DORA: "metrics" sin numerar (barra) |
| `devflow/analysis/glossary/metaflow.md` | Nota de la familia N: reglas con barra (ADR-003) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno en el repo (el rename es del pipeline: `32-adv-reviews` en el kit) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| **Barra obligatoria en N-rules** | La referencia de ruta es `nombre/`; la palabra suelta es vocabulario (ADR-003, REV-002 F-04/F-05) |
| **Reemplazo conserva la barra** (`NN-<nombre>/`) | Mantiene la ruta válida tras el reemplazo |
| **Lookbehind `(?<![\w-])` se mantiene** | Protege substrings (`business-risks/`, `adversarial-reviews/`, `agents-data/`) |
| **Rename 32 solo en N32/PN32** | Cambio mínimo según ADR-003 |
| **Test de sobre-match en la E2E** | Garantiza que el vocabulario nunca vuelva a corromperse |

## 8. Deviations and assumptions

- **Test del enum:** la clave del schema transformado es `task` (B-rules),
  no `bolt` — el test accede a `properties.task.properties.type.enum`.
- **El fixture de test usaba el nombre de salida como entrada** (bug del
  test, no del pipeline): se corrigió usando el nombre original
  (`adversarial-reviews/`).
- **Sin commits** (G34): `git_commit: null`.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 73 tests in 11.064s
OK        (72 previos + ajustes + 1 nuevo)
```

### RED → GREEN evidence (test-first)
- **RED:** 6 fallas (expectativas de barra/adv) antes de la implementación.
- **GREEN:** misma suite tras la implementación → `Ran 73 tests ... OK`.

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos
total: 149 archivos, 66 carpetas, 0 binarios, 1 excluido, 5810 reglas, 27 remociones
evidencia: transform-reports/5.1/20260827-025738/ (retención: purgada 022508)
sobre-match en prosa: 0 ✓ (medidor + E2E)
enum del schema: ['functional','non-functional','test'] ✓
carpeta 32: 32-adv-reviews ✓ (32-adversarial-reviews ausente)
referencias viejas: 0 ✓ · links reales rotos: 0 ✓
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 73/73 |
| **Prose integrity** | pass — 0 sobre-match |
| Link integrity | pass — 0 links reales rotos |
| Perf-smoke (p95/p99) | pass |
| SAST / SBOM | n/a |
| Prompt-injection scan | n/a |
| Secret-leak scan | pass |
| Hallucination lint | pass |
| IP / license provenance | n/a |
| PII / DLP | n/a |
| Dependency-confusion | n/a |
| Test-first evidence | pass — RED registrado |
| Behavioral reproducibility | pass |
| Bolt-manifest validation | pass |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente.

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34).
- **Commit:** baseline `58ac5eb` (trabajo sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-005-correccion-numeracion.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-025738/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15 min |
| V-Bounce number | 1 (BOLT-005) |
| Tests created/ajustados | 1 nuevo + suite reescrita; total 73 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **AITL-BOLT-DONE-Approval** de BOLT-005 (la última de la US-001).
- [ ] **X6** — template HTML de reportes de MetaFlow.
- [ ] Migración de gobernanza (OQ-003) y absorción de la próxima versión
  (OQ-004 — reglas genéricas: v6 → v2 automático).
- [ ] Mejora futura: mover la lista de tokens prohibidos del verificador a
  `mapping.json` (datos) para que agregar un token nuevo no toque código.

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Este MEM no tiene status mutable y **nunca
> se auto-aprueba**. El Dev-validator que ejecutó el Bolt inspecciona el diff
> real, la evidencia de tests/gates, el MEM y el manifest, y registra
> `AITL-MEM-Approval` aquí y en el `checkpoint_approvals[]` del manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenioserrano` (Dev-validator — rol autoasignado: no hay otro titular) |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:57:47-03:00` |
| **review.started_at** | `2026-08-27T02:58:54-03:00` |
| **review.decided_at** | `2026-08-27T02:58:54-03:00` |
| **Review evidence** | diff de código + fixture + tests 73/73 + corrida de producción (exit 0, 0 sobre-match, enum OK, 32-adv-reviews) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 73/73 en verde, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
