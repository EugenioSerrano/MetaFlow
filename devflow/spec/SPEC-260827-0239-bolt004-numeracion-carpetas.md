---
id: "SPEC-260827-0239"
title: "BOLT-004 — Numeración de carpetas internas del kit (ADR-002) + test de integridad de links"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "US-001"
bolt: "US-001.BOLT-004"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-002-numeracion-carpetas-kit.md"
prerequisites:
  - "devflow/spec/SPEC-260827-0124-bolt001-engine-transformacion.md"
  - "devflow/spec/SPEC-260827-0142-bolt002-verificador-reporte.md"
  - "devflow/spec/SPEC-260827-0211-bolt003-versionado-limpieza.md"
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T02:39:49-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:41:57-03:00"
  decided_at: "2026-08-27T02:41:57-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión de la SPEC de BOLT-004 en conversación, 2026-08-27. Autoriza el V-Bounce 4"
---

# SPEC-260827-0239 — BOLT-004: Numeración de carpetas + test de links

| Field | Value |
|-------|-------|
| **Origin** | US-001 |
| **Bolt** | US-001.BOLT-004 |
| **ADRs** | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-002](../adrs/ADR-002-numeracion-carpetas-kit.md) (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Implementar el esquema de numeración de carpetas internas del kit definido en
la **ADR-002** (aprobada): las 20 carpetas de `metaflow/` pasan a
`01-input` … `53-actors` (orden por ciclo de uso, gaps de 10, sin espacios),
con la **reescritura completa de las referencias** en el contenido (las
~1524 medidas en REV-001) y un **test de integridad de links** que garantiza
cero links rotos en el kit adoptado (F-02 del REV-001). `ai-sdlc/` y las
carpetas de plataforma de la raíz (`.agents/`, `.github/`, `.opencode/`) no
se numeran.

**Si no se implementa:** el kit mantiene el orden actual (decisión ADR-002
incumplida) y el link roto detectado en el baseline
(`reports/README.md → TEMPLATE-REPORT.html`, efecto de la exclusión X6)
queda sin cobertura automática.

## 2. Context

REV-001 (aprobado, Plan B) midió el ruido: 1524 referencias de ruta, 91 de
144 archivos. La ADR-002 fijó el esquema. La verificación del baseline
(2026-08-27) encontró 5 links "rotos" en el kit actual: 4 son placeholders de
templates (`url`, `Customer.md`, `PersonaName.md`, `vision.md` en
TEMPLATE-*) y **1 es real**: `reports/README.md` referencia
`./TEMPLATE-REPORT.html`, excluido por el pipeline (X6) — este Bolt lo
neutraliza con una regla de datos. El engine necesita un ajuste menor:
**regex en reglas de ruta** (anclas) para renombrar componentes exactos sin
corromper subcarpetas (`business-risks` no debe convertirse en
`business-51-risks`).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-001.BOLT-004-numeracion-carpetas-kit.md` | AITL-BOLT-READY-Approval ✓ |
| Feature US | `devflow/functional/user-stories/US-001-toolkit-transformacion.md` | AITL-US-Approval ✓ |
| ADRs | ADR-001, **ADR-002** (esquema de numeración) | AITL-ADR-Approval ✓ |
| REV | `devflow/reviews/REV-001-renombrado-carpetas-metaflow.md` | AITL-REV-Approval ✓ (Plan B) |
| Prior SPECs | BOLT-001 rev 2, BOLT-002 rev 2, BOLT-003 rev 2 (Done) | ✓ |
| Repository baseline | `58ac5eb` (+ trabajo previo sin commitear, G34) | — |

## 4. Scope

### In scope

- `src/transform.py`: soporte de **`regex_rename` en reglas de ruta**
  (compilar patrón + sub con backrefs) para anclas de componente exacto.
- `mapping.json`: 20 reglas de contenido (`(?<![\w-])input\b` →
  `01-input`, etc.) + 20 reglas de ruta (`^input$` → `01-input`, etc.) con
  orden longest-first (protección de substrings) + regla que neutraliza la
  referencia al template excluido en `reports/README.md`.
- `src/tests/`: `test_links.py` (integridad de links — clasifica placeholders
  de templates, exige 0 links reales rotos), `test_numbering.py` (reglas de
  numeración y protecciones de substrings) + fixture `refs.md` + E2E real
  (0 referencias viejas, 0 links rotos, verificador en cero).

### Out of scope

- `ai-sdlc/` y raíz del kit (`.agents/`, `.github/`, `.opencode/`).
- Subcarpetas internas de `input/` (business, databases, …).
- Template HTML de MetaFlow (X6 — solo se neutraliza la referencia rota).
- Traducciones, migración de la raíz.

## 5. Prerequisites and baseline

- BOLT-001..003 Done (suite 64/64). ADR-002 accepted.
- Baseline de links del kit actual: 285 links, 4 placeholders + 1 roto real.
- `input-kit/` v5.1; evidencia previa en `transform-reports/5.1/`.

## 6. Phases

### Phase A — Engine: regex en reglas de ruta

**Duration:** 0.5h — **Complexity:** Low

#### A.1 `apply_path` con `regex_rename`

`apply_path` actualmente hace `str.replace` para todas las reglas de ruta.
Se agrega soporte: si `rule.type == "regex_rename"`, se compila el patrón y
se aplica `pattern.sub(_to_python_repl(replacement), component)` — con
anclas (`^…$`) los componentes se renombran solo cuando coinciden completos.
Las reglas `path_rename` y `rename` mantienen el comportamiento actual.

**Files modified:**
- `src/transform.py` — `apply_path` con soporte regex.

### Phase B — Diccionario: numeración + protección de substrings + fix de link

**Duration:** 1.5h — **Complexity:** Medium

#### B.1 Reglas de contenido (regex_rename, orden 90–109)

Para cada carpeta del esquema ADR-002: `(?<![\w-])<nombre>\b` →
`<NN>-<nombre>` (el lookbehind negativo protege substrings: `business-risks`
no se toca; `adversarial-reviews` no se corrompe por la regla de `reviews`;
`agents-data` no se corrompe por la de `agents`). Orden longest-first
(`adversarial-reviews` y `agents-data` antes que sus substrings).

| order | id | pattern | replacement |
|-------|----|---------|-------------|
| 90 | N01 | `(?<![\w-])input\b` | `01-input` |
| 91 | N02 | `(?<![\w-])analysis\b` | `02-analysis` |
| 92 | N03 | `(?<![\w-])discovery\b` | `03-discovery` |
| 93 | N11 | `(?<![\w-])adrs\b` | `11-adrs` |
| 94 | N12 | `(?<![\w-])functional\b` | `12-functional` |
| 95 | N13 | `(?<![\w-])bugs\b` | `13-bugs` |
| 96 | N21 | `(?<![\w-])spec\b` | `21-spec` |
| 97 | N22 | `(?<![\w-])memory\b` | `22-memory` |
| 98 | N23 | `(?<![\w-])metrics\b` | `23-metrics` |
| 99 | N24 | `(?<![\w-])tests\b` | `24-tests` |
| 100 | N31 | `(?<![\w-])reviews\b` | `31-reviews` |
| 101 | N32 | `(?<![\w-])adversarial-reviews\b` | `32-adversarial-reviews` |
| 102 | N33 | `(?<![\w-])risks\b` | `33-risks` |
| 103 | N34 | `(?<![\w-])incidents\b` | `34-incidents` |
| 104 | N35 | `(?<![\w-])retros\b` | `35-retros` |
| 105 | N41 | `(?<![\w-])prompts\b` | `41-prompts` |
| 106 | N42 | `(?<![\w-])reports\b` | `42-reports` |
| 107 | N51 | `(?<![\w-])agents\b` | `51-agents` |
| 108 | N52 | `(?<![\w-])agents-data\b` | `52-agents-data` |
| 109 | N53 | `(?<![\w-])actors\b` | `53-actors` |

> Orden real ajustado por longest-first: `adversarial-reviews` y `agents-data`
> antes de `reviews` y `agents`. El `\b` final evita "inputs", "reviewsX", etc.

#### B.2 Reglas de ruta (regex_rename, orden 1020–1039)

Para cada carpeta: `^<nombre>$` → `<NN>-<nombre>` (componente exacto; solo
se renombra la carpeta top-level, nunca subcarpetas como `business-risks` o
`tests/test-cases`).

#### B.3 Fix del link roto (regla de datos)

`reports/README.md` referencia `./TEMPLATE-REPORT.html` (excluido). Regla de
contenido que neutraliza la referencia (reemplaza el enlace por texto plano
con nota "template pendiente — X6"). El test de links exige 0 links reales
rotos.

### Phase C — Tests

**Duration:** 1.5h — **Complexity:** Medium

#### C.1 `test_links.py` — integridad de links

Recorre un árbol MD, resuelve cada link relativo y clasifica: **placeholders
de templates** (archivos `TEMPLATE-*.md` o targets de ejemplo como `url`,
`*Name.md`, `example-*`) se ignoran; el resto debe **resolver** (0 links
reales rotos). Corre sobre el output del fixture y sobre el kit real.

#### C.2 `test_numbering.py` — reglas y protecciones

Contenido: `input/` → `01-input/`; `analysis/` → `02-analysis/`;
`business-risks/` **intacto**; `adversarial-reviews/` →
`32-adversarial-reviews/` (y nunca `adversarial-31-reviews/`);
`agents-data/` → `52-agents-data/` (y nunca `51-…`); "the input folder" →
"the 01-input folder". Rutas: componente `input` → `01-input`;
`business-risks` intacto; `tests` → `24-tests`.

#### C.3 E2E real + fixture

- Fixture `refs.md` (input/expected) con referencias numeradas y substrings
  protegidos.
- E2E real: 0 ocurrencias de referencias viejas
  (`(?<![\w-])(input|…|actors)/`); las 20 carpetas renombradas existen; 0
  links reales rotos; verificador en cero.

**Files created:**
- `src/tests/test_links.py`, `src/tests/test_numbering.py`,
  `src/tests/fixtures/kit-mini/refs.md` + expected.

---

## 7. Acceptance criteria

### AC (BOLT-004): Numeración ADR-002 aplicada

**Given** el kit real transformado,
**When** se inspeccionan las carpetas de `metaflow/`,
**Then** las 20 carpetas tienen el prefijo del esquema (`01-input`…`53-actors`),
`ai-sdlc/` no tiene prefijo, y **no queda ninguna referencia a los nombres
viejos** como ruta.

### AC (BOLT-004): Integridad de links

**Given** el kit real transformado,
**When** se resuelven todos los links relativos,
**Then** 0 links reales rotos (los placeholders de templates se clasifican y
excluyen).

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US AC-1 (equivalencia) | Numeración mecánica 1:1 + links verificados | `test_links.py`, `test_numbering.py`, E2E real |
| ADR-002 (esquema) | Phase B: 20×2 reglas + protecciones | `test_numbering.py` |
| REV-001 F-02 (links) | Phase C.1: test de integridad de links | `test_links.py` |
| REV-001 baseline (link roto real) | Phase B.3: neutralización de la referencia a TEMPLATE-REPORT.html | `test_links.py` (0 rotos) |

---

## 8. Testing strategy

- **Unit tests (~10 casos):** numeración de contenido (4), protecciones de
  substrings (3), rutas con anclas (3).
- **Links (2):** fixture y kit real — 0 links reales rotos, placeholders
  clasificados.
- **E2E (1):** kit real — carpetas renombradas, 0 referencias viejas, 0
  links rotos, verificador en cero.
- **Edge cases:** `business-risks/` dentro de `analysis/`; `reviews` dentro
  de `adversarial-reviews`; `agents` dentro de `agents-data`; "inputs"
  (plural, no se toca); links a `TEMPLATE-REPORT.html` (excluido).
- **BUG evidence:** N/A (no es BUG Bolt).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (64 + nuevas) | pass (objetivo) |
| SAST / SBOM | Sin dependencias ni red | n/a |
| Perf-smoke (p95/p99) | Pipeline < 1 min | pass (objetivo) |
| Prompt-injection scan | Sin inputs no confiables | n/a |
| Secret-leak scan | Sin credenciales | pass |
| Hallucination lint | stdlib verificada | pass |
| IP / license provenance | Cero dependencias | n/a |
| PII / DLP | Sin datos personales | n/a |
| Dependency-confusion | Cero dependencias | n/a |
| Test-first evidence | Tests antes del código | pass (objetivo) |
| Behavioral reproducibility | Mismo input → mismo output | pass (objetivo) |
| Bolt-manifest validation | Manifest válido | pass |
| **Link integrity** | 0 links reales rotos en el kit | pass (objetivo) |

---

## 10. Security and data

- Sin cambios de superficie: reglas de texto y rutas; `data_classification:
  internal`.
- El test de links recorre rutas relativas dentro del árbol del kit (sin
  salir del árbol — los targets absolutos/http se ignoran).

## 11. Monitoring and observability

- El reporte del run lista las reglas N01–N53 aplicadas; la evidencia queda
  en `transform-reports/` (retención 2).

## 12. Migration, compatibility and rollback

- **Migration:** N/A — el kit se regenera completo (una pasada mecánica 1:1).
- **Compatibility:** el soporte regex en rutas es aditivo (reglas viejas sin
  regex siguen funcionando); regresión cubierta por la suite previa.
- **Rollback:** git + re-ejecución (evidencia previa conservada).

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Reescritura incompleta de referencias | 2 | 4 | E2E con conteo de referencias viejas = 0 |
| Substrings corrompidos (business-risks, adversarial-reviews, agents-data) | 3 | 4 | Lookbehind negativo + anclas + tests dedicados |
| Links rotos residuales | 2 | 4 | `test_links.py` (0 reales) |
| Churn de diff enorme | 5 | 1 | Aceptado (REV-001) — cambio 1:1 mecánico de una sola pasada |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Regex con lookbehind `(?<![\w-])` en contenido | Protege substrings (`business-risks`, `adversarial-reviews`, `agents-data`) sin listas de excepciones |
| Regex anclada `^…$` en rutas | Solo renombra la carpeta top-level, nunca subcarpetas |
| `\b` final en contenido | Evita falsos positivos ("inputs") |
| Neutralizar (no borrar) la referencia a TEMPLATE-REPORT.html | El template vuelve con X6; la referencia queda como nota |
| Soporte regex en `apply_path` | Cambio mínimo y aditivo del engine (BOLT-004) |

## 15. Stop conditions

- Si el conteo de referencias viejas no llega a 0 en el E2E real: detener y
  clasificar los contextos restantes (nunca forzar).
- Si un link real no puede resolverse tras la numeración: detener e
  investigar (no ignorar).

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B, C)
- [ ] ACs de BOLT-004 cumplidas (numeración + 0 links rotos)
- [ ] Tests GREEN (suite completa, 0 failures)
- [ ] Code follows ADR-001/ADR-002 (Python stdlib; esquema de numeración)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in
      `devflow/metrics/bolts/US-001.BOLT-004-numeracion-carpetas-kit.json`
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-001 (AC-1, Rev 7), BOLT-004 (aprobado), ADR-001/ADR-002 (accepted)
- REV-001 (aprobado — Plan B, F-02)
- Baseline de links: informe 2026-08-27 (285 links, 1 roto real)

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de BOLT-004 |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator registra `AITL-SPEC-Approval` (bloque `review` del
> frontmatter). La aprobación autoriza el code-run / V-Bounce.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:39:49-03:00` |
| **review.started_at** | `2026-08-27T02:41:57-03:00` |
| **review.decided_at** | `2026-08-27T02:41:57-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
