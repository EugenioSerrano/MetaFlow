---
entity: "MappingRule"
label: "Regla de transformación"
module: "metaflow-transform"
status: "stable"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
sources: ["conversación de diseño 2026-08-27", "glossary/metaflow.md"]
tags: [domain, transformacion]
---

# MappingRule

## 1. Descripción

Una regla individual del diccionario de transformación. Las reglas viven como
**datos** en `mapping.json` (no en código) y el engine las aplica en orden:
**las cadenas más largas primero**, y los patrones regex para los códigos
variables de checkpoint (`AITL-<CODE>-Approval` → `CP-<CODE>-Approval`). Cada
regla puede renombrar contenido, renombrar rutas o remover contenido (con
registro en el reporte).

## 2. Propiedades

| Propiedad | Tipo | Requerido | Restricciones | Descripción |
|-----------|------|:---------:|---------------|-------------|
| `id` | string | ✅ | M1…M11, C1…C6, B1…B16, D1…D6, R1…R4 | Identificador de la regla (por familia del diccionario) |
| `type` | → Enum:`RuleType` | ✅ | — | `rename` / `regex_rename` / `remove` / `path_rename` |
| `pattern` | string | ✅ | — | Texto o expresión regular a buscar |
| `replacement` | string | ❌ | — | Texto de reemplazo (vacío para `remove`; N/A para `path_rename`) |
| `order` | integer | ✅ | 1..N | Orden de aplicación (longest-first por construcción) |
| `scope` | string | ❌ | `content`/`path`/`both` | Dónde aplica la regla |
| `report_on_match` | boolean | ✅ | — | Si la regla se registra en el reporte (siempre true para `remove`) |

## 3. Relaciones

| Relación | Objetivo | Cardinalidad (este — objetivo) | Descripción |
|----------|----------|:------------------------------:|-------------|
| `belongs_to` | MappingTable | N — 1 | Las reglas se agrupan en la tabla de mapeo (`mapping.json`) |
| `applied_in` | TransformRun | N — 0..N | Un run aplica muchas reglas |

## 4. Reglas de negocio

- **RULE-01:** El orden de aplicación debe garantizar que el término más largo se reemplace antes que el más corto (p. ej. `AvengaDevFlow` antes de `Avenga DevFlow` antes de `Avenga`).
- **RULE-02:** Las reglas de tipo `regex_rename` capturan el código variable y lo re-emiten: `AITL-(\w+-?)+-Approval` → `CP-…-Approval`.
- **RULE-03:** Las reglas de tipo `remove` **nunca** son silenciosas: cada remoción se lista en el reporte para revisión humana.
- **RULE-04:** Agregar una regla nueva no requiere tocar el engine — solo se agrega a `mapping.json`.

## 5. Ejemplo

```yaml
id: "C1"
type: "regex_rename"
pattern: "AITL-([A-Z-]+)-Approval"
replacement: "CP-$1-Approval"
order: 10
scope: "content"
report_on_match: true
```

## 6. Fuentes

| Fuente | Dónde |
|--------|-------|
| Diccionario completo | `../../../glossary/metaflow.md` |

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
