---
id: "BR-002"
title: "Divergencia con AvengaDevFlow en futuras versiones"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
category: "business-model"
sources: ["conversación de diseño 2026-08-27"]
tags: [riesgo, versiones]
---

# BR-002 — Divergencia con AvengaDevFlow en futuras versiones

## 1. Descripción

MetaFlow hereda funcionalidad 1:1 de AvengaDevFlow. Si una futura versión de
AvengaDevFlow introduce conceptos nuevos (nombres, artefactos, carpetas) que
el diccionario de `mapping.json` no cubre, el pipeline los deja sin
transformar (leftovers) o los transforma mal, y MetaFlow se queda atrás en
funcionalidad o produce un kit inconsistente.

## 2. Categoría

`business-model`

## 3. Evaluación

| Dimensión | Valor | Razón |
|-----------|-------|-------|
| Probabilidad | `high` | Es el modelo de herencia mismo: cada versión nueva es un input distinto |
| Impacto | `medium` | El verificador detecta leftovers; el costo es trabajo manual por versión, no daño permanente |

## 4. Mitigación

- El verificador de tokens prohibidos y el reporte de diffs hacen visible lo no cubierto.
- Proceso definido para absorber versiones nuevas (PROC-001, excepción 2).
- El diccionario vive como datos y se extiende sin tocar código.

## 5. Contingencia

Ante una versión con contenido nuevo: extender el diccionario con las reglas
nuevas (creando o actualizando artefactos de análisis/glossary), re-ejecutar,
y revisar el diff manualmente antes de publicar.

## 6. Fuentes

- OQ-004 (absorción de futuras versiones)
- `../process/PROC-001.md` §7

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Creado | @eugenioserrano |
