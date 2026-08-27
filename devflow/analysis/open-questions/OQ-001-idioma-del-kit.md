---
id: "OQ-001"
title: "¿En qué idioma se genera el kit de salida (devflow/LANGUAGE del DistributionKit)?"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "answered"
priority: "P2"
owner: "eugenioserrano"
validator: "eugenioserrano"
targets:
  - "../scope/mvp-scope.md"
  - "../glossary/metaflow.md"
sources:
  - "conversación de diseño 2026-08-27"
related: []
tags: [idioma, kit]
revisit_on: ""
closed_on: "2026-08-27"
closed_by: "human:eugenioserrano"
---

# OQ-001 — ¿En qué idioma se genera el kit de salida?

## 1. Pregunta

> ¿El `devflow/LANGUAGE` del kit de salida (`distribution-kit/`) se hereda tal
> cual del input (inglés) o se transforma a `es`?

## 2. Contexto

- **¿Qué artefactos bloquea?** El contenido del kit de salida; la regla de transformación para `devflow/LANGUAGE` en `mapping.json`.
- **¿Qué supuesto usamos mientras tanto?** El kit hereda el idioma del input (`en`): la transformación solo cambia nombres, no traduce contenido.
- **¿Impacto si nos equivocamos?** Si el kit se traduce/transforma a `es`, es un cambio de contenido masivo (no un rename); si se deja en `en` y el propietario quería `es`, el kit no cumple su expectativa.

## 3. Hipótesis (supuesto de trabajo)

> *Asumimos que el kit de salida mantiene el idioma del input (`en`): la
> transformación es de nombres, no de traducción. Si se decidiera `es`, sería
> un proyecto de traducción aparte (fuera del scope MVP, X2).*

## 4. Opciones en consideración

| # | Opción | Implicación | Fuente |
|---|--------|-------------|--------|
| A | Heredar `en` (sin regla sobre LANGUAGE) | Coherente con "solo nombres cambian"; el proyecto MetaFlow habla castellano pero el kit hereda contenido inglés | default actual |
| B | Transformar `LANGUAGE` a `es` | El kit declara castellano pero su contenido sigue en inglés → inconsistencia interna del kit | — |
| C | Proyecto de traducción completo a `es` | Fuera de scope MVP; es traducción, no transformación | X2 del scope |

## 5. Registro de investigación (append-only)

| Fecha | Autor | Nota |
|-------|-------|------|
| 2026-08-27 | @eugenioserrano | Abierta desde la conversación de diseño; default = opción A |
| 2026-08-27 | @eugenioserrano | Respondida: opción A — el kit queda en inglés (hereda `en`); todos los documentos del kit quedan en inglés |

## 6. Resolución

**Respondida (2026-08-27, eugenioserrano): opción A** — el kit de salida hereda el idioma del input (`en`): todos los documentos del kit quedan en inglés. La transformación es solo de nombres; la traducción completa (opción C) queda descartada.

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Abierta | @eugenioserrano |
