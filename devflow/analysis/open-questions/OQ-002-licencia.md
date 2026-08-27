---
id: "OQ-002"
title: "¿Cuál es la licencia final de MetaFlow?"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "answered"
priority: "P2"
owner: "eugenioserrano"
validator: "eugenioserrano"
targets:
  - "../scope/mvp-scope.md"
  - "../business-risks/BR-004-licencia-pendiente.md"
sources:
  - "conversación de diseño 2026-08-27"
related: ["OQ-003"]
tags: [licencia]
revisit_on: ""
closed_on: "2026-08-27"
closed_by: "human:eugenioserrano"
---

# OQ-002 — ¿Cuál es la licencia final de MetaFlow?

## 1. Pregunta

> ¿Qué licencia o términos de uso rigen a MetaFlow y su repositorio?

## 2. Contexto

- **¿Qué artefactos bloquea?** La inclusión de un archivo de licencia en el kit de salida y en el repositorio; cualquier promesa de "open source".
- **¿Qué supuesto usamos mientras tanto?** Propiedad de Eugenio Serrano, sin licencia declarada, sin promesas de open source.
- **¿Impacto si nos equivocamos?** Distribuir sin licencia o con licencia equivocada expone legalmente al propietario.

## 3. Hipótesis (supuesto de trabajo)

> *Asumimos licencia propietaria de Eugenio Serrano (no open source total);
> el propietario dijo "no sería open source del todo, después veré".*

## 4. Opciones en consideración

| # | Opción | Implicación | Fuente |
|---|--------|-------------|--------|
| A | Propietaria (todos los derechos reservados) | Máxima protección; sin archivo de licencia estándar | conversación 2026-08-27 |
| B | Open source con licencia permisiva (MIT/Apache) | Distribución libre; requiere verificar procedencia del contenido transformado | — |
| C | Open source con copyleft (GPL/AGPL) | Requiere que derivados compartan; inusual para una metodología | — |
| D | Licencia dual | Máxima flexibilidad; más complejidad | — |

## 5. Registro de investigación (append-only)

| Fecha | Autor | Nota |
|-------|-------|------|
| 2026-08-27 | @eugenioserrano | Abierta; el propietario la resolverá "después" |
| 2026-08-27 | @eugenioserrano | Respondida: licencia propietaria a nombre de Eugenio Serrano |

## 6. Resolución

**Respondida (2026-08-27, eugenioserrano): opción A** — licencia **propietaria a nombre de Eugenio Serrano** (todos los derechos reservados). Sin promesas de open source; el archivo de licencia se materializa en el kit cuando se defina cómo (seguimiento en scope X1).

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Abierta | @eugenioserrano |
