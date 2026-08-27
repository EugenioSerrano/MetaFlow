---
entity: "DistributionKit"
label: "Kit de salida (MetaFlow)"
module: "metaflow-transform"
status: "stable"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
sources: ["conversación de diseño 2026-08-27"]
tags: [domain, transformacion]
---

# DistributionKit

## 1. Descripción

El kit de **salida** del pipeline: la versión MetaFlow del kit, con el mismo
árbol y funcionalidad que el `InputKit` pero con todos los nombres
transformados según el diccionario (`../glossary/metaflow.md`). Se escribe en
`distribution-kit/` en la raíz del repositorio. Es el **producto** del
proyecto: lo que un adoptante copiaría a su repositorio.

## 2. Propiedades

| Propiedad | Tipo | Requerido | Restricciones | Descripción |
|-----------|------|:---------:|---------------|-------------|
| `path` | string | ✅ | ruta de carpeta | `distribution-kit/` (raíz del repo) |
| `version` | string | ✅ | formato X.Y | Versión del InputKit − 4 (p. ej. 5.1 → 1.1) |
| `source_version` | string | ✅ | formato X.Y | Versión del InputKit que lo originó |
| `generated_at` | dateTime | ✅ | ISO 8601 | Momento del run de transformación |
| `transform_run` | ref | ✅ | → TransformRun | El run que lo produjo |
| `forbidden_tokens` | array | ✅ | vacío = OK | Tokens prohibidos residuales detectados por el verificador (debe ser vacío) |

## 3. Relaciones

| Relación | Objetivo | Cardinalidad (este — objetivo) | Descripción |
|----------|----------|:------------------------------:|-------------|
| `derived_from` | InputKit | 1 — 1 | Cada salida proviene de una entrada |
| `produced_by` | TransformRun | 1 — 1 | El run que la generó |

## 4. Reglas de negocio

- **RULE-01:** El `DistributionKit` debe ser funcionalmente equivalente al `InputKit`: la única diferencia permitida son los cambios de nombres definidos en el diccionario.
- **RULE-02:** Si el verificador encuentra algún token prohibido, el pipeline falla y el kit no se considera publicado (no debe usarse para adoptar).
- **RULE-03:** La versión del kit de salida = versión del kit de entrada − 4 (mayor − 4, menor igual): 5.1 → 1.1 (decisión 2026-08-27).

## 5. Ejemplo

```yaml
path: "distribution-kit"
version: "1.1"
source_version: "5.1"
forbidden_tokens: []
```

## 6. Fuentes

| Fuente | Dónde |
|--------|-------|
| Visión (O1/O2) | `../../../vision/vision.md` |
| Diccionario | `../../../glossary/metaflow.md` |

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
