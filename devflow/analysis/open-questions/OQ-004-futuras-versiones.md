---
id: "OQ-004"
title: "¿Cómo se absorben las futuras versiones de AvengaDevFlow con contenido nuevo?"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "answered"
priority: "P1"
owner: "eugenioserrano"
validator: "eugenioserrano"
targets:
  - "../process/PROC-001.md"
  - "../business-risks/BR-002-divergencia-con-avenga.md"
sources:
  - "conversación de diseño 2026-08-27"
related: ["BR-002"]
tags: [versiones, transformacion]
revisit_on: ""
closed_on: "2026-08-27"
closed_by: "human:eugenioserrano"
---

# OQ-004 — ¿Cómo se absorben futuras versiones con contenido nuevo?

## 1. Pregunta

> ¿El pipeline re-transforma la versión completa de AvengaDevFlow en cada
> ciclo, o se necesita un mecanismo de diff/merge para absorber solo el
> contenido nuevo?

## 2. Contexto

- **¿Qué artefactos bloquea?** PROC-001 (excepción 2) y el diseño del pipeline para la segunda versión heredada.
- **¿Qué supuesto usamos mientras tanto?** Re-transformación completa: cada nueva versión de AvengaDevFlow reemplaza `input-kit/` y el pipeline genera `distribution-kit/` desde cero (con el diccionario extendido si hace falta).
- **¿Impacto si nos equivocamos?** Si una versión introduce conceptos nuevos, el diccionario debe extenderse manualmente; un mecanismo de diff lo haría más automático pero agrega complejidad al MVP.

## 3. Hipótesis (supuesto de trabajo)

> *Asumimos re-transformación completa por versión: el MVP no hace diffs
> entre versiones (X5 del scope). El diccionario se extiende por versión y el
> verificador + diff manual cubren el contenido nuevo.*

## 4. Opciones en consideración

| # | Opción | Implicación | Fuente |
|---|--------|-------------|--------|
| A | Re-transformación completa (default MVP) | Simple y repetible; el trabajo de contenido nuevo cae en extender el diccionario | X5 del scope |
| B | Diff entre versiones de AvengaDevFlow + merge selectivo | Automatiza la absorción; requiere pipeline de diff, revisión por feature | futuro |
| C | Mantener el árbol Avenga como referencia versionada y aplicar solo deltas | Complejo; alto costo de mantenimiento | — |

## 5. Registro de investigación (append-only)

| Fecha | Autor | Nota |
|-------|-------|------|
| 2026-08-27 | @eugenioserrano | Abierta; el MVP asume opción A |
| 2026-08-27 | @eugenioserrano | Respondida: opción A — re-transformación completa por versión |

## 6. Resolución

**Respondida (2026-08-27, eugenioserrano): opción A** — **re-transformación completa por versión**: cada versión nueva de AvengaDevFlow reemplaza `input-kit/` y el pipeline regenera `distribution-kit/` desde cero; el contenido nuevo se absorbe extendiendo el diccionario (`mapping.json`). El diff entre versiones + merge selectivo (opción B) queda como posible futuro.

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Abierta | @eugenioserrano |
