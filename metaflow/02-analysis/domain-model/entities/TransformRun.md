---
entity: "TransformRun"
label: "Ejecución de transformación"
module: "metaflow-transform"
status: "stable"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
sources: ["conversación de diseño 2026-08-27", "process/PROC-001.md"]
tags: [domain, transformacion]
---

# TransformRun

## 1. Descripción

Una ejecución completa del pipeline de transformación: toma un `InputKit`,
aplica las reglas de la tabla de mapeo (contenido, rutas y remociones),
escribe el `DistributionKit` y ejecuta la verificación de tokens prohibidos.
El resultado del run es el **reporte** que el humano revisa antes de aceptar
la versión publicada.

## 2. Propiedades

| Propiedad | Tipo | Requerido | Restricciones | Descripción |
|-----------|------|:---------:|---------------|-------------|
| `id` | string | ✅ | formato libre (p. ej. fecha+versión) | Identificador del run |
| `started_at` | dateTime | ✅ | ISO 8601 | Inicio del run |
| `finished_at` | dateTime | ❌ | ISO 8601 | Fin del run |
| `input` | ref | ✅ | → InputKit | Kit de entrada |
| `output` | ref | ❌ | → DistributionKit | Kit de salida (null si falló) |
| `rules_applied` | array | ✅ | — | Conteo de aplicaciones por regla |
| `removals` | array | ✅ | — | Lista de remociones ejecutadas (para revisión humana) |
| `forbidden_hits` | array | ✅ | — | Tokens prohibidos residuales (vacío = verificación OK) |
| `status` | → Enum:`TransformStatus` | ✅ | — | `ok` / `failed` / `dry_run` |

## 3. Relaciones

| Relación | Objetivo | Cardinalidad (este — objetivo) | Descripción |
|----------|----------|:------------------------------:|-------------|
| `consumes` | InputKit | 0..N — 1 | El run lee un kit de entrada |
| `produces` | DistributionKit | 1 — 0..1 | El run escribe un kit de salida (si no falla) |
| `applies` | MappingRule | 0..N — N | El run aplica reglas de la tabla |

## 4. Reglas de negocio

- **RULE-01:** Si `forbidden_hits` no está vacío, el status del run es `failed` aunque la escritura haya terminado: un kit con tokens prohibidos no es publicable.
- **RULE-02:** En modo `dry_run` no se escribe nada en `distribution-kit/`; el reporte muestra el plan completo.
- **RULE-03:** El reporte del run es la evidencia que el humano revisa (equivalente al diff de un V-Bounce/Delivery Loop) antes de aceptar la versión.

## 5. Ejemplo

```yaml
id: "20260827-5.1"
started_at: "2026-08-27T12:00:00Z"
finished_at: "2026-08-27T12:00:42Z"
input: "input-kit (v5.1)"
output: "distribution-kit (v5.1)"
rules_applied: [{ "C1": 87 }, { "B1": 42 }]
removals: [{ "R1": 1 }, { "R2": 2 }]
forbidden_hits: []
status: "ok"
```

## 6. Fuentes

| Fuente | Dónde |
|--------|-------|
| Proceso completo | `../../../process/PROC-001.md` |

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
