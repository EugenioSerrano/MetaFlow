---
enum: "RuleType"
label: "Tipo de regla de transformación"
module: "metaflow-transform"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
sources: ["conversación de diseño 2026-08-27"]
tags: [domain, transformacion]
---

# RuleType

## 1. Descripción

Clasificación de las reglas de `mapping.json`. Determina cómo el engine
interpreta la regla: reemplazo de texto exacto, reemplazo por patrón,
remoción de contenido, o renombrado de ruta (archivos/carpetas).

## 2. Valores

| Valor | Descripción |
|-------|-------------|
| `rename` | Reemplazo de texto **exacto** (cadena literal, longest-first) — p. ej. `AvengaDevFlow` → `MetaFlow` |
| `regex_rename` | Reemplazo por **expresión regular** con captura y re-emisión — p. ej. `AITL-([A-Z-]+)-Approval` → `CP-$1-Approval` |
| `remove` | **Remoción** de contenido (frases completas) con registro obligatorio en el reporte — p. ej. citas a Raja SP / DORA |
| `path_rename` | Renombrado de **ruta** (archivo o carpeta) — p. ej. `avenga-metaflow/` → `ai-sdlc/` |

## 3. Usado por

| Entidad | Propiedad |
|---------|-----------|
| `MappingRule` | `type` |

## 4. Notas

- Las reglas `path_rename` se aplican sobre el árbol de rutas ANTES de
  transformar el contenido (las rutas en prosa las cubren reglas `rename`
  de contenido, p. ej. M11).
- Las reglas `remove` nunca son silenciosas (RULE-03 de `MappingRule`).

## 5. Fuentes

| Fuente | Dónde |
|--------|-------|
| Diccionario de transformación | `../../../glossary/metaflow.md` |

## 6. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
