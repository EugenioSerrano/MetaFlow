---
id: "SPEC-260827-0355-bolt009-fix-schema-version-contradicciones"
title: "SPEC BOLT-009: contradicciones \"5.0\" vs \"1.0\" de schema_version en documentos del kit"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-004"
bolt: "US-001.BOLT-009"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T03:55:34-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T03:58:00-03:00"
  decided_at: "2026-08-27T03:58:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobacion del propietario (Dev-validator autoasignado) sin hallazgos - SPEC US-001.BOLT-009 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red->green)"
---

# SPEC-260827-0355 — BOLT-009: fix contradicciones "5.0" vs "1.0"

| Field | Value |
|-------|-------|
| **Origin** | BUG-004 (REV-003 F-04) |
| **Bolt** | US-001.BOLT-009 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir las reglas/diccionario del transform para que ningún documento
del kit regenere con `schema_version "5.0"`: las ocurrencias residuales en
`23-metrics/README.md:183`, `TEMPLATE-US.md:47` y `TEMPLATE-TC.md:42`
deben quedar en `"1.0"`, consistentes con las demás secciones de esos
mismos documentos. Si no se corrige, quien copie el template puede crear
un manifest que no valida (G23).

## 2. Context

El BUG-004 (aprobado) documenta tres contradicciones dentro del mismo
documento (resto del linaje v5 que el diccionario no cubrió). La familia
v1 está fijada por los schemas y REV-002/BOLT-003.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-001.BOLT-009 | AITL-BOLT-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | AITL-US-Approval ✓ |
| BUG | BUG-004 | AITL-BUG-Approval ✓ |
| REV evidence | REV-003 | AITL-REV-Approval ✓ |
| ADRs | ADR-001 | AITL-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

## 4. Scope

### In scope

- Reglas/diccionario que unifican `"5.0"` → `"1.0"` en los 3 archivos.
- Test de reproducción (RED) + E2E + regeneración.

### Out of scope

- BUG-002/003/005 (Bolts dedicados).

## 5. Prerequisites and baseline

- BOLT-005/BOLT-006 Done; Python 3 + stdlib (ADR-001).

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproducción

Test que verifica cero `schema_version "5.0"` / `exactly "5.0"` en
`23-metrics/README.md`, `TEMPLATE-US.md` y `TEMPLATE-TC.md` del kit
regenerado. Ejecutar y registrar el **RED**.

**Files created:**
- `tools/tests/test_bolt009_schema_version_docs.py`.

### Phase B — Fix del diccionario/reglas

**Duration:** 1h — **Complexity:** Low

#### B.1 Reglas de contenido

Ampliar `mapping.json` para unificar las tres ocurrencias a `"1.0"`.

**Files modified:**
- `mapping.json`.

### Phase C — Regeneración y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Regenerar el kit

Ejecutar `python src/transform.py`, regenerar `distribution-kit/`, correr
la suite y registrar el **GREEN** + evidencia en `transform-reports/`.

## 7. Acceptance criteria

### AC-1: Documentos sin "5.0"

**Given** un kit transformado, **When** se inspeccionan 23-metrics/README,
TEMPLATE-US y TEMPLATE-TC, **Then** no contienen `schema_version "5.0"` /
`exactly "5.0"` y declaran `"1.0"`.

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-004 (expected result) | Reglas unifican a `"1.0"` | test_bolt009 (RED→GREEN) + grep |

## 8. Testing strategy

- **Unit tests:** reglas del diccionario.
- **Integration tests:** transform completo.
- **E2E tests:** grep de los 3 archivos.
- **BUG evidence:** RED → GREEN registrados.

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a (stdlib) |
| Perf-smoke | — | n/a |
| Prompt-injection scan | — | n/a |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a |
| PII / DLP | — | n/a |
| Dependency-confusion | — | n/a |
| Test-first evidence | RED antes del fix | pass (a verificar) |
| Behavioral reproducibility | kit reproducible | pass (a verificar) |
| Bolt-manifest validation | manifest v5 válido | pass (a verificar) |

## 10. Security and data

- Sin superficie externa; `data_classification: internal`.

## 11. Monitoring and observability

- n/a — evidencia en `transform-reports/`.

## 12. Migration, compatibility and rollback

- **Migration:** regeneración (idempotente).
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert + regeneración.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresión de otros textos | 2 | 3 | E2E de tokens + suite |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform | El kit es output regenerado |

## 15. Stop conditions

- Tokens no reproducibles con las reglas (bloqueo → MEM con evidencia).

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; cero `"5.0"` en los 3 archivos
- [ ] Tests GREEN; AC-1 satisfecha
- [ ] MEM + manifest `v_bounces[]` + AITL-MEM-Approval

## 17. References

- BUG-004, REV-003, ADR-001, US-001.

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (draft) |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que
> el Dev-validator registra `AITL-SPEC-Approval`.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator autoasignado) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T03:55:34-03:00` |
| **review.started_at** | `2026-08-27T03:58:00-03:00` |
| **review.decided_at** | `2026-08-27T03:58:00-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
