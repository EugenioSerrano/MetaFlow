---
id: "SPEC-260827-0355-bolt007-fix-schema-version-metodologia"
title: "SPEC BOLT-007: restos del linaje v5 en MetaFlow.md §3.12/§5.16 (familia v1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-002"
bolt: "US-001.BOLT-007"
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
  acknowledgment_reason: "Aprobacion del propietario (Dev-validator autoasignado) sin hallazgos - SPEC US-001.BOLT-007 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red->green)"
---

# SPEC-260827-0355 — BOLT-007: fix restos v5 en MetaFlow.md §3.12/§5.16

| Field | Value |
|-------|-------|
| **Origin** | BUG-002 (REV-003 F-01/F-02) |
| **Bolt** | US-001.BOLT-007 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir en el toolkit de transformación las reglas/diccionario que
producen el `MetaFlow.md` del kit con restos del linaje v5: la §3.12 debe
declarar la familia de manifests **v1** (`schema_version` exactly
`"1.0"`, sin la historia 4.x/5.0 ni el rename corrupto
`checkpoint_approvals[]` → `checkpoint_approvals[]`) y la §5.16 debe
describir la conversión real de la familia v1 con checkpoints `CP-*` (sin
`CITL ⊇ CITL`, sin "v5 checkpoint enum accepts only CITL-*", sin
`schema_version becomes "5.0"`). Si no se corrige, la fuente normativa del
kit instruye manifests que no validan contra los schemas v1 del propio kit
(G23).

## 2. Context

El BUG-002 (aprobado) documenta los pasajes corruptos en
`distribution-kit/metaflow/ai-sdlc/MetaFlow.md` (líneas 3268, 3272-3278,
4769-4783), heredados del input-kit Avenga v5 con reemplazos mecánicos
incompletos. La decisión de la familia v1 está fijada por REV-002/BOLT-003
y los schemas `manifest-v1*.schema.json` (`const: "1.0"`). El fix vive en
el pipeline (`src/transform.py` + `mapping.json`) y el kit se regenera.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-001.BOLT-007 | AITL-BOLT-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | AITL-US-Approval ✓ |
| BUG | BUG-002 | AITL-BUG-Approval ✓ |
| REV evidence | REV-003 | AITL-REV-Approval ✓ |
| ADRs | ADR-001 | AITL-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

## 4. Scope

### In scope

- Reglas/diccionario del transform que reescriben §3.12 y §5.16 del
  MetaFlow.md (familia v1, conversión `CP-*`).
- Test de reproducción (RED) + tests de reglas + E2E.
- Regeneración del kit y verificación de cero tokens v5.

### Out of scope

- BUG-003..BUG-012 (Bolts dedicados BOLT-008..017).
- Contenido sustantivo de la metodología (solo texto de versión/migración).

## 5. Prerequisites and baseline

- BOLT-005/BOLT-006 Done (baseline del diccionario corregido y
  regeneración estable).
- Python 3 + stdlib (ADR-001); `src/transform.py` funcional.

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproducción

Crear un test del toolkit que ejecute el transform sobre el input-kit y
verifique que el `MetaFlow.md` regenerado **no** contiene: `schema_version
is exactly 5.0`, `a schema change means 5.0`, `becomes "5.0"`, `CITL ⊇
CITL`, `accepts only CITL-*`. Ejecutar y registrar el **RED** (el kit
actual produce esas coincidencias).

**Files created:**
- `tools/tests/test_bolt007_schema_version.py` (o el patrón de tests del
  repo) — verifica cero tokens v5 en §3.12/§5.16 del kit regenerado.

### Phase B — Fix del diccionario/reglas

**Duration:** 1h — **Complexity:** Low

#### B.1 Reglas de contenido

Ampliar `mapping.json` (y el diccionario del transform) para reescribir
los pasajes: `schema_version is exactly 5.0` → `schema_version is exactly
"1.0"` (familia v1), eliminar la narrativa `4.x keeps 4.0 / a schema
change means 5.0`, corregir el rename corrupto y reescribir la §5.16 para
la conversión v1 con `CP-*` (sin `CITL-*`).

**Files modified:**
- `mapping.json` — reglas de contenido para §3.12/§5.16.

### Phase C — Regeneración y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Regenerar el kit

Ejecutar `python src/transform.py` (dry-run + real), regenerar
`distribution-kit/`, correr la suite completa y registrar el **GREEN** +
evidencia en `transform-reports/`.

## 7. Acceptance criteria

### AC-1: §3.12 declara la familia v1

**Given** un kit transformado, **When** se inspecciona `MetaFlow.md`
§3.12, **Then** `schema_version` es exactly `"1.0"` y no hay narrativa
4.x/5.0 ni rename corrupto.

### AC-2: §5.16 describe la conversión real

**Given** un kit transformado, **When** se inspecciona `MetaFlow.md`
§5.16, **Then** no hay `CITL ⊇ CITL`, `accepts only CITL-*`, `becomes
"5.0"` ni `CP-* → CP-*` y la conversión es consistente con la familia v1.

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-002 (expected result) | Reglas del diccionario corrigen los pasajes | test_bolt007 (RED→GREEN) + grep del kit regenerado |

## 8. Testing strategy

- **Unit tests:** reglas del diccionario (los reemplazos exactos
  aplican); test de reproducción RED→GREEN.
- **Integration tests:** transform completo sobre el input-kit.
- **E2E tests:** kit regenerado sin los tokens v5 listados (grep).
- **Edge cases:** variantes de espaciado/comillas de los tokens.
- **BUG evidence:** RED (kit actual con coincidencias) → GREEN (kit
  regenerado sin coincidencias).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a (sin dependencias nuevas; Python stdlib) |
| Perf-smoke (p95/p99) | — | n/a (sin superficie de servicio) |
| Prompt-injection scan | — | n/a (sin prompts de entrada) |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a (sin código de terceros nuevo) |
| PII / DLP | — | n/a (sin PII) |
| Dependency-confusion | — | n/a (stdlib) |
| Test-first evidence | RED registrado antes del fix | pass (a verificar) |
| Behavioral reproducibility | kit reproducible | pass (a verificar) |
| Bolt-manifest validation | manifest v5 válido | pass (a verificar) |

## 10. Security and data

- Sin superficie externa; el toolkit procesa documentos del repo
  (`data_classification: internal`).
- Sin secretos, sin PII.

## 11. Monitoring and observability

- n/a — herramienta de transformación local; la evidencia se registra en
  `transform-reports/`.

## 12. Migration, compatibility and rollback

- **Migration:** regeneración del kit (idempotente).
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert del cambio de reglas + regeneración previa.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresión de otros textos al ampliar el diccionario | 2 | 3 | E2E completa de tokens + suite |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform, no edición manual del kit | El kit es output regenerado; la edición manual se pierde en la próxima corrida |
| Reescritura completa de los pasajes corruptos | Evita reglas parciales que dejen restos |

## 15. Stop conditions

- Los tokens v5 no son reproducibles con las reglas (bloqueo → MEM con
  evidencia).
- Aparece una fuente gobernada draft/inconsistente (G15).

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; kit regenerado sin tokens v5
- [ ] Tests GREEN; AC-1/AC-2 satisfechas
- [ ] MEM + manifest `v_bounces[]` + AITL-MEM-Approval

## 17. References

- BUG-002, REV-003, ADR-001, US-001.

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
