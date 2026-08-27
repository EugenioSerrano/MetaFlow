---
entity: "InputKit"
label: "Kit de entrada (AvengaDevFlow)"
module: "metaflow-transform"
status: "stable"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
sources: ["conversación de diseño 2026-08-27"]
tags: [domain, transformacion]
---

# InputKit

## 1. Descripción

El kit de **entrada** del pipeline: una copia íntegra del kit distribuible de
AvengaDevFlow (la carpeta `input-kit/` en la raíz del repositorio). Contiene
`devflow/` completo, `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.github/` y
`.opencode/`. Es el punto de partida de cada transformación: cada nueva
versión de AvengaDevFlow colocada aquí produce una versión de MetaFlow.

## 2. Propiedades

| Propiedad | Tipo | Requerido | Restricciones | Descripción |
|-----------|------|:---------:|---------------|-------------|
| `path` | string | ✅ | ruta de carpeta | Ubicación del kit (raíz del repo) |
| `version` | string | ✅ | formato X.Y | Versión del kit de entrada (fuente de la numeración de salida: versión − 4) |
| `files` | array | ✅ | — | Lista de archivos del kit (≈150) |
| `content_language` | string | ✅ | `en`/`es` | Valor de `devflow/LANGUAGE` del kit |
| `ingested_at` | dateTime | ❌ | ISO 8601 | Momento en que se colocó en `input-kit/` |

## 3. Relaciones

| Relación | Objetivo | Cardinalidad (este — objetivo) | Descripción |
|----------|----------|:------------------------------:|-------------|
| `feeds` | TransformRun | 1 — 0..N | Cada InputKit alimenta uno o más runs de transformación |
| `produces` | DistributionKit | 1 — 1 | Cada versión de entrada produce su versión de salida |

## 4. Reglas de negocio

- **RULE-01:** El contenido de `input-kit/` es **solo lectura** para el pipeline: nunca se modifica, solo se lee.
- **RULE-02:** Cada versión de AvengaDevFlow colocada en `input-kit/` debe producir exactamente un `DistributionKit` (correspondencia 1:1 — O2 de la visión), con versión de salida = versión de entrada − 4 (mayor − 4, menor igual: 5.1 → 1.1).
- **RULE-03:** Los archivos del kit son texto (md/json/yaml); no se esperan binarios.

## 5. Ejemplo

```yaml
path: "input-kit"
version: "5.1"
files: 150
content_language: "en"
```

## 6. Fuentes

| Fuente | Dónde |
|--------|-------|
| Conversación de diseño | `../../../glossary/metaflow.md` §1 |

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
