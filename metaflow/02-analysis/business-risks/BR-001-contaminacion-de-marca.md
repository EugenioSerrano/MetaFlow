---
id: "BR-001"
title: "Contaminación de marca en el kit de salida"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
category: "adoption"
sources: ["conversación de diseño 2026-08-27"]
tags: [riesgo, marca]
---

# BR-001 — Contaminación de marca en el kit de salida

## 1. Descripción

Un rename incompleto deja menciones de la marca previa (`Avenga`, `AITL`,
`HITL`, `Bolt`, `V-Bounce`, `Raja`, `DORA`) en `distribution-kit/`. Si el kit
se distribuye así, MetaFlow aparece como derivado de Avenga o con restos de su
identidad, dañando la independencia de marca (O1 de la visión).

## 2. Categoría

`adoption`

## 3. Evaluación

| Dimensión | Valor | Razón |
|-----------|-------|-------|
| Probabilidad | `medium` | Los renames automáticos pueden fallar en casos no contemplados (nuevas frases, formatos raros, contenido futuro) |
| Impacto | `high` | Un kit contaminado distribuido es difícil de retractar y daña la identidad |

## 4. Mitigación

- Verificador automático de tokens prohibidos que **falla el pipeline** ante cualquier leftover (S4 del scope MVP).
- Reporte con conteos por regla y lista de remociones para revisión humana.
- Test de aceptación E2E contra el kit real (el verificador debe pasar en cero).

## 5. Contingencia

Si se detecta contaminación en una versión publicada: re-ejecutar el pipeline
corregido, revisar el diff completo, y publicar la versión corregida
registrando el incidente.

## 6. Fuentes

- Conversación de diseño 2026-08-27 (decisión "renombrar todo todo todo")
- `../glossary/metaflow.md` §6 (tokens prohibidos)

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Creado | @eugenioserrano |
