---
id: "BR-004"
title: "Decisión de licencia pendiente"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "deprecated"
category: "regulation"
sources: ["conversación de diseño 2026-08-27"]
tags: [riesgo, licencia]
---

# BR-004 — Decisión de licencia pendiente

> **Actualización (2026-08-27):** la decisión fue tomada — licencia
> **propietaria a nombre de Eugenio Serrano** (OQ-002 respondida). Este riesgo
> queda `deprecated`: ya no hay decisión pendiente; lo único residual es cómo
> se materializa el archivo de licencia en el kit (seguimiento en
> `../scope/mvp-scope.md` X1).

## 1. Descripción

La licencia de MetaFlow está sin decidir ("no sería open source del todo,
después veré"). Mientras tanto, el kit de salida no lleva archivo de licencia
ni términos de uso claros, y el repositorio deriva de un contenido
originalmente propietario de Avenga LATAM. Si en el futuro se decide una
licencia open source, habría que verificar que el contenido transformado no
arrastre restricciones del original.

## 2. Categoría

`regulation`

## 3. Evaluación

| Dimensión | Valor | Razón |
|-----------|-------|-------|
| Probabilidad | `medium` | La decisión está explícitamente postergada |
| Impacto | `medium` | Afecta distribución y protección legal de la marca |

## 4. Mitigación

- Atribución reescrita a Eugenio Serrano en el kit de salida (ya decidido).
- OQ-002 abierta para forzar la decisión.
- No prometer "open source" en ningún artefacto hasta decidir.

## 5. Contingencia

Cuando se decida la licencia: agregar el archivo de licencia al kit (regla de
transformación o archivo propio del proyecto) y revisar la procedencia del
contenido.

## 6. Fuentes

- OQ-002
- Conversación de diseño 2026-08-27

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Creado | @eugenioserrano |
