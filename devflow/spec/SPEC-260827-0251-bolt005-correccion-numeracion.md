---
id: "SPEC-260827-0251"
title: "BOLT-005 — Corrección del sobre-match de numeración + rename 32-adv-reviews"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "US-001"
bolt: "US-001.BOLT-005"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
prerequisites:
  - "devflow/spec/SPEC-260827-0239-bolt004-numeracion-carpetas.md"
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T02:51:33-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:53:28-03:00"
  decided_at: "2026-08-27T02:53:28-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión de la SPEC de BOLT-005 en conversación, 2026-08-27. Autoriza el V-Bounce 5"
---

# SPEC-260827-0251 — BOLT-005: Corrección del sobre-match + 32-adv-reviews

| Field | Value |
|-------|-------|
| **Origin** | US-001 |
| **Bolt** | US-001.BOLT-005 |
| **ADRs** | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-003](../adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md) (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir los hallazgos de la REV-002 (aprobada): las reglas de contenido de
numeración (N-rules) sobre-numeraron **palabras de vocabulario** en prosa
(1224 corrupciones: "12-functional analyst", "run the 24-tests") y rompieron
el enum del schema de manifests (`"functional"` → `"12-functional"` — un
manifest con `type: functional` ya no valida). Según la ADR-003 (accepted),
las reglas de contenido pasan a exigir la **barra** (`<nombre>/`) — solo se
numeran **referencias de ruta** — y la carpeta 32 pasa a **`32-adv-reviews`**.
Se regenera el kit y se agregan tests que fijan: prosa intacta, enum del
schema restaurado, rename 32, substrings protegidos, 0 referencias viejas y
0 links rotos.

**Si no se implementa:** el kit queda con vocabulario corrompido y el schema
de manifests invalidando `type: functional` — no publicable (REV-002).

## 2. Context

REV-002 midió el sobre-match: 1224 corrupciones de prosa (p. ej.
`12-functional analyst` ×254, `run existing 24-tests` ×222,
`02-analysis artifacts` ×176, `role 51-agents` ×115) y el enum del schema
`["12-functional","non-functional","test"]`. La causa: los patrones
`(?<![\w-])<nombre>(?![\w-])` numeran la palabra suelta. La ADR-003 fija la
corrección: la barra es el delimitador de referencia de ruta; además
`adversarial-reviews` → `adv-reviews` (decisión del propietario).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-001.BOLT-005-correccion-numeracion.md` | AITL-BOLT-READY-Approval ✓ |
| Feature US | `devflow/functional/user-stories/US-001-toolkit-transformacion.md` | AITL-US-Approval ✓ |
| ADRs | ADR-001, **ADR-003** (supersede ADR-002) | AITL-ADR-Approval ✓ |
| REV | `devflow/reviews/REV-002-consistencia-kit.md` (F-04/F-05/F-06) | AITL-REV-Approval ✓ |
| Prior SPECs | BOLT-004 rev 1 (Done) | ✓ |
| Repository baseline | `58ac5eb` (+ trabajo previo sin commitear, G34) | — |

## 4. Scope

### In scope

- `mapping.json`: reescribir las 20 reglas de contenido N-rules con **barra
  obligatoria** (`(?<![\w-])<nombre>/` → `NN-<nombre>/`), N32/PN32 →
  `32-adv-reviews`; las reglas de ruta ancladas no cambian salvo PN32.
- `src/tests/`: `test_numbering.py` actualizado (prosa intacta, enum del
  schema, 32-adv-reviews, substrings), fixture `refs.md` actualizado, E2E
  real con conteo de sobre-match = 0 y enum verificado.
- Regeneración del kit de producción.

### Out of scope

- `ai-sdlc/` y raíz; subcarpetas de `input/`; X6; otros cambios de esquema
  (ADR-003 no cambia el resto).

## 5. Prerequisites and baseline

- BOLT-001..004 Done (suite 72/72). ADR-003 accepted. REV-002 approved.
- Kit actual con las 1224 corrupciones (a regenerar).
- `input-kit/` v5.1; evidencia en `transform-reports/5.1/`.

## 6. Phases

### Phase A — Diccionario: N-rules con barra + rename 32

**Duration:** 1h — **Complexity:** Medium

#### A.1 Reglas de contenido (regex_rename, órdenes 90–109)

Cada regla pasa a: `(?<![\w-])<nombre>/` → `NN-<nombre>/` — la **barra** es el
delimitador de referencia de ruta; la palabra suelta ("functional analyst",
"run the tests", enums de schemas) queda intacta. El lookbehind negativo
sigue protegiendo substrings (`business-risks/`, `reviews/` dentro de
`adversarial-reviews/`, `agents/` dentro de `agents-data/`). N32:
`(?<![\w-])adversarial-reviews/` → `32-adv-reviews/`. Orden longest-first
(`adversarial-reviews/` y `agents-data/` antes que sus substrings).

#### A.2 Reglas de ruta

PN32: `^adversarial-reviews$` → `32-adv-reviews` (única regla de ruta que
cambia; el resto PN01–PN53 quedan igual).

### Phase B — Tests

**Duration:** 1.5h — **Complexity:** Medium

#### B.1 `test_numbering.py` actualizado

- **Prosa intacta:** "functional analyst stays", "run the tests", "the
  memory", "risks of X", "inputs" → sin números.
- **Refs de ruta:** `input/` → `01-input/`; `functional/` → `12-functional/`;
  `adversarial-reviews/` → `32-adv-reviews/`; `reviews/` → `31-reviews/`;
  `agents-data/` → `52-agents-data/`; `agents/` → `51-agents/`.
- **Substrings:** `analysis/business-risks/` → `02-analysis/business-risks/`
  (risks intacto).
- **Rutas (anclas):** `adversarial-reviews` → `32-adv-reviews`; `reviews` →
  `31-reviews`; `business-risks` intacto.
- **Enum del schema (E2E real):** `manifest-v1-task.schema.json` →
  `bolt.type.enum == ["functional","non-functional","test"]`.
- **E2E real:** 0 sobre-match en prosa (ningún `NN-nombre` sin `/` después),
  0 referencias viejas, `32-adv-reviews` presente y `32-adversarial-reviews`
  ausente, 0 links rotos, verificador en cero.

**Files modified:**
- `src/tests/test_numbering.py` — expectativas con barra y rename 32.
- `src/tests/fixtures/kit-mini/refs.md` + expected — `adversarial-reviews/`
  → `32-adv-reviews/`.

---

## 7. Acceptance criteria

### AC (BOLT-005): Vocabulario intacto + esquema ADR-003

**Given** el kit real transformado,
**When** se inspecciona el contenido,
**Then** **0 sobre-match** (ningún `NN-nombre` como palabra suelta), el enum
del schema es `["functional","non-functional","test"]`, la carpeta
`32-adv-reviews` existe (y no `32-adversarial-reviews`), 0 referencias
viejas y 0 links reales rotos.

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| REV-002 F-04 (sobre-match) | Phase A.1: reglas con barra | `test_numbering.py` + E2E (0 sobre-match) |
| REV-002 F-05 (enum schema) | Phase A.1 (la barra no toca enums) | E2E: enum verificado |
| REV-002 F-06 / ADR-003 (32-adv-reviews) | Phase A.1/A.2: N32/PN32 | `test_numbering.py` + E2E |
| US AC-1 (equivalencia) | Regeneración mecánica | Suite completa + links |

---

## 8. Testing strategy

- **Unit (~10 casos):** prosa intacta (5), refs de ruta (3), substrings (2).
- **E2E (1):** kit real — 0 sobre-match, enum, 32-adv-reviews, 0 refs viejas,
  0 links rotos, verificador en cero.
- **Edge cases:** "functional" en enum y prosa; "reviews" dentro de
  "adversarial-reviews"; "agents" dentro de "agents-data"; "inputs";
  `spec_revisions`; "01-input/" ya numerado.
- **BUG evidence:** N/A (no es BUG Bolt).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (72 + ajustes) | pass (objetivo) |
| Link integrity | 0 links reales rotos | pass (objetivo) |
| Prose integrity | 0 sobre-match de numeración | pass (objetivo) |
| SAST / SBOM | Sin dependencias ni red | n/a |
| Prompt-injection scan | Sin inputs no confiables | n/a |
| Secret-leak scan | Sin credenciales | pass |
| Hallucination lint | stdlib verificada | pass |
| IP / license provenance | Cero dependencias | n/a |
| PII / DLP | Sin datos personales | n/a |
| Dependency-confusion | Cero dependencias | n/a |
| Test-first evidence | Tests antes del código | pass (objetivo) |
| Behavioral reproducibility | Determinista | pass (objetivo) |
| Bolt-manifest validation | Manifest válido | pass |

---

## 10. Security and data

- Sin cambios de superficie; `data_classification: internal`.

## 11. Monitoring and observability

- El reporte del run lista las reglas N aplicadas; evidencia en
  `transform-reports/` (retención 2).

## 12. Migration, compatibility and rollback

- **Migration:** N/A — el kit se regenera completo.
- **Compatibility:** el cambio es de patrones en datos (misma estructura de
  reglas); el engine no cambia en este Bolt.
- **Rollback:** git + re-ejecución.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Re-corrupción de prosa | 1 | 4 | Test de sobre-match = 0 en E2E |
| Enum del schema vuelve a romperse | 1 | 4 | Test de enum en E2E |
| Refs de ruta sin numerar (falso negativo) | 2 | 3 | E2E con conteo de refs viejas = 0 |
| Rename 32 incompleto | 1 | 3 | E2E: 32-adv-reviews presente, 32-adversarial-reviews ausente |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Barra obligatoria en N-rules de contenido | La referencia de ruta es `nombre/`; la palabra suelta es vocabulario (ADR-003) |
| Reemplazo conserva la barra (`NN-<nombre>/`) | Mantiene la ruta válida tras el reemplazo |
| Lookbehind `(?<![\w-])` se mantiene | Protege substrings (`business-risks/`, `adversarial-reviews/`, `agents-data/`) |
| Rename 32 en N32/PN32 (no tocar el resto) | Cambio mínimo según ADR-003 |

## 15. Stop conditions

- Si tras el fix quedan sobre-matches o refs sin numerar: detener y
  clasificar (nunca forzar).
- Si el enum del schema no vuelve a `["functional","non-functional","test"]`:
  detener e investigar.

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B)
- [ ] ACs de BOLT-005 cumplidas (0 sobre-match, enum OK, 32-adv-reviews)
- [ ] Tests GREEN (suite completa, 0 failures)
- [ ] Code follows ADR-001/ADR-003
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in
      `devflow/metrics/bolts/US-001.BOLT-005-correccion-numeracion.json`
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-001 (AC-1, Rev 8), BOLT-005 (aprobado), ADR-001/ADR-003 (accepted)
- REV-002 (aprobado — F-04/F-05/F-06)

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de BOLT-005 |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator registra `AITL-SPEC-Approval` (bloque `review` del
> frontmatter). La aprobación autoriza el code-run / V-Bounce.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:51:33-03:00` |
| **review.started_at** | `2026-08-27T02:53:28-03:00` |
| **review.decided_at** | `2026-08-27T02:53:28-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
