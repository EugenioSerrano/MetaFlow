---
id: "MEM-260827-0244"
title: "BOLT-004 — Numeración de carpetas internas del kit + test de integridad de links (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-004"
spec: "SPEC-260827-0239"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-002-numeracion-carpetas-kit.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-004-numeracion-carpetas-kit.json"
diff_ref: ""
review_ready_at: "2026-08-27T02:44:50-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:46:11-03:00"
  decided_at: "2026-08-27T02:46:11-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 72/72, corrida de producción (20 carpetas, 0 refs viejas, 0 links rotos) y manifest en conversación, 2026-08-27"
---

# MEM-260827-0244 — BOLT-004: Numeración de carpetas + test de links

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-004 |
| **SPEC**        | [SPEC-260827-0239](../spec/SPEC-260827-0239-bolt004-numeracion-carpetas.md) — revisión 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-002](../adrs/ADR-002-numeracion-carpetas-kit.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce ejecutó la **transformación más grande del proyecto** — el
renombrado de las 20 carpetas internas del kit según la ADR-002 (orden por
ciclo de uso, gaps de 10, sin espacios) con la reescritura completa de las
referencias (~1524 medidas en REV-001) — y salió **limpia**: EXIT=0, las 20
carpetas renombradas (`01-input` … `53-actors`) con `ai-sdlc/` intacto, **0
referencias viejas** como ruta en todo el kit (verificado por la E2E real) y
**0 links reales rotos** (nuevo `test_links.py`, REV-001 F-02). El link roto
real detectado en el baseline (`reports/README.md → TEMPLATE-REPORT.html`,
efecto de la exclusión X6) quedó **neutralizado** con una regla de datos
(L01). Para lograrlo se agregó soporte de **regex en reglas de ruta**
(anclas `^…$`) en el engine y 41 reglas al diccionario (20 de contenido con
lookbehind/lookahead `(?<![\w-])…(?![\w-])` — protegen substrings como
`business-risks`, `adversarial-reviews` y `agents-data` —, 20 de ruta
ancladas y la L01). La suite completa pasó **72/72 tests** (64 previos + 8
nuevos: 3 de links + 5 de numeración incl. E2E real), con RED registrado (7
fallas de expectativa) y GREEN. El diff del kit es grande (una sola pasada
mecánica 1:1) pero la evidencia con diffs en `transform-reports/` permite
verificar que el cambio es exactamente el esperado: numeración + renames, sin
alterar contenido funcional.

## 2. Implemented phases

### Phase A — Engine: regex en reglas de ruta

`apply_path` ahora distingue `regex_rename` (compila el patrón y aplica
`sub` con backrefs) del `path_rename`/`rename` (substring replace). Esto
permite anclas `^…$` por componente: solo la carpeta top-level se renombra,
nunca subcarpetas (`business-risks`, `tests/test-cases`, `agents-data`).

### Phase B — Diccionario: numeración + protecciones + fix de link

Se agregaron **20 reglas de contenido** (N01–N53, órdenes 90–109) con
patrones `(?<![\w-])<nombre>(?![\w-])`: el lookbehind negativo protege el
frente (`business-risks` no se toca por la regla de `risks`;
`adversarial-reviews` no se corrompe por la de `reviews`) y el lookahead
negativo protege el final (`agents-data` no se corrompe por la de `agents`;
`inputs`, `spec_revisions`, `test_bolts` quedan intactos). **20 reglas de
ruta** (PN01–PN53, órdenes 1020–1039) con anclas `^…$`. La **L01** neutraliza
el enlace roto `[`TEMPLATE-REPORT.html`](./TEMPLATE-REPORT.html)` en
`reports/README.md` (lo deja como texto plano — el template vuelve con X6).
Orden longest-first: `adversarial-reviews` y `agents-data` antes que sus
substrings.

### Phase C — Tests

`test_links.py` (3 casos): clasificación de placeholders (archivos
`TEMPLATE-*` y targets de ejemplo como `url`, `Customer.md`, `PersonaName.md`,
`TEMPLATE-REPORT.html`), fixture con 0 rotos y **kit real con 0 links reales
rotos**. `test_numbering.py` (5 casos): las 20 carpetas numeradas, protecciones
de substrings, plurales/campos protegidos, componentes de ruta con anclas y la
**E2E real** (carpetas renombradas + conteo de referencias viejas = 0). El
fixture `refs.md` ejercita las referencias y protecciones. Se ajustaron dos
expectativas previas: `test_bolts` → `test_tasks` (B12) y `metrics` →
`23-metrics` (N23) en `test_remove`.

## 3. Files created

| File | Purpose |
|------|---------|
| `src/tests/test_links.py` | Test de integridad de links relativos del kit: clasifica placeholders de templates y exige 0 links reales rotos (REV-001 F-02) |
| `src/tests/test_numbering.py` | Suite de numeración: 20 carpetas, protecciones de substrings, anclas de ruta y E2E real con conteo de referencias viejas |
| `src/tests/fixtures/kit-mini/refs.md` | Fixture de entrada: referencias a las 20 carpetas + substrings protegidos |
| `src/tests/fixtures/kit-mini-expected/refs.md` | Fixture esperado: referencias numeradas + protecciones |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | `apply_path` con soporte de `regex_rename` (compila + sub con backrefs) para anclas de componente |
| `mapping.json` | 41 reglas nuevas: N01–N53 (contenido, con lookbehind/lookahead), PN01–PN53 (rutas ancladas), L01 (fix del link a TEMPLATE-REPORT.html) |
| `devflow/analysis/glossary/metaflow.md` | Sección nueva de numeración (familia N) documentando el esquema ADR-002 y las protecciones |
| `src/tests/test_remove.py`, `test_rename.py`, `test_report.py` | Expectativas ajustadas por la numeración (`test_tasks`, `23-metrics`, `21-spec`, conteos 9/10) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno en el repo (los renames son del pipeline: ver `distribution-kit/metaflow/01-input…53-actors`) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| **Lookbehind + lookahead `(?<![\w-])…(?![\w-])` en contenido** | Protege substrings por ambos lados: `business-risks` (frente), `agents-data` (final), `inputs`/`spec_revisions` (final) — más robusto que `\b` solo (refinamiento sobre la SPEC, misma intención) |
| **Anclas `^…$` en rutas** | Solo la carpeta top-level se renombra; las subcarpetas (`business-risks`, `test-cases`) nunca se tocan |
| **Regex en `apply_path`** | Cambio mínimo y aditivo del engine (reglas viejas sin regex intactas) |
| **L01 neutraliza (no borra) la referencia** | El template de reporte vuelve con X6; la referencia queda como nota de texto |
| **Orden longest-first en N-rules** | `adversarial-reviews` y `agents-data` antes de sus substrings (defensa en profundidad, aunque los lookarounds ya protegen) |
| **E2E con conteo de referencias viejas = 0** | Garantiza que la reescritura fue completa (REV-001: 1524 referencias) |

## 8. Deviations and assumptions

- **Refinamiento de patrón:** la SPEC proponía `\b` final; se implementó
  `(?![\w-])` porque `\b` solo no protege `agents-data` (el guion es boundary).
  Misma intención aprobada (protección de substrings) — registrado aquí.
- **El diff del kit es grande (una pasada):** aceptado por REV-001; la
  evidencia con diffs permite verificar que el cambio es solo numeración +
  renames.
- **Sin commits** (G34): `git_commit: null`.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 72 tests in 10.804s
OK        (64 previos + 8 nuevos: 3 links + 5 numeración)
```

### RED → GREEN evidence (test-first)
- **RED:** 7 fallas (expectativas de numeración y fixture) antes de la
  implementación.
- **GREEN:** misma suite tras la implementación → `Ran 72 tests ... OK`.

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos
total: 149 archivos, 66 carpetas, 0 binarios, 1 excluido, 6555 reglas, 27 remociones
evidencia: transform-reports/5.1/20260827-024439/ (retención: purgada 021702)
carpetas: 01-input … 53-actors (20) + ai-sdlc sin número ✓
referencias viejas como ruta: 0 ✓ (E2E)
links reales rotos: 0 ✓ (test_links; el roto de reports/README neutralizado)
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 72/72 |
| **Link integrity** | pass — 0 links reales rotos en el kit real |
| Perf-smoke (p95/p99) | pass — pipeline < 1 min |
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
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-004-numeracion-carpetas-kit.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-024439/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~20 min |
| V-Bounce number | 1 (BOLT-004) |
| Tests created | 8 nuevos; suite total 72 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **AITL-BOLT-DONE-Approval** de BOLT-004 (aceptación final — la última de la US-001).
- [ ] **X6** — template HTML de reportes de MetaFlow (la referencia neutralizada volverá a ser link cuando exista).
- [ ] Migración de gobernanza (OQ-003) y absorción de la próxima versión (OQ-004).

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
| **review_ready_at** | `2026-08-27T02:44:50-03:00` |
| **review.started_at** | `2026-08-27T02:46:11-03:00` |
| **review.decided_at** | `2026-08-27T02:46:11-03:00` |
| **Review evidence** | diff de código + fixture + tests 72/72 + corrida de producción (exit 0, 20 carpetas, 0 refs viejas, 0 links rotos) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 72/72 en verde, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
