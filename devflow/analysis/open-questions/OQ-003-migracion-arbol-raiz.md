---
id: "OQ-003"
title: "¿El árbol devflow/ raíz de este repositorio se migra a MetaFlow en algún momento?"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "answered"
priority: "P1"
owner: "eugenioserrano"
validator: "eugenioserrano"
targets:
  - "../../AGENTS.md"
  - "../../README.md"
sources:
  - "conversación de diseño 2026-08-27"
related: ["OQ-002"]
tags: [gobernanza, migracion]
revisit_on: ""
closed_on: "2026-08-27"
closed_by: "human:eugenioserrano"
---

# OQ-003 — ¿El árbol `devflow/` raíz se migra a MetaFlow?

## 1. Pregunta

> ¿El `devflow/` de la raíz de este repositorio (la metodología instalada que
> gobierna el proyecto) se migra a MetaFlow, o permanece como AvengaDevFlow
> instalado?

## 2. Contexto

- **¿Qué artefactos bloquea?** La gobernanza de este repositorio: hoy opera bajo AvengaDevFlow v5.0 instalado (checkpoints `AITL-*`). Si se migra, los checkpoints pasarían a `CP-*` y el contenido a MetaFlow.
- **¿Qué supuesto usamos mientras tanto?** El árbol raíz permanece como está (AvengaDevFlow instalado, `AITL-*`), y solo `distribution-kit/` es el producto MetaFlow.
- **¿Impacto si nos equivocamos?** Migrar la gobernanza antes de tener el kit estable obligaría a gobernar con una metodología aún no publicada; no migrar nunca deja el repo gobernado por la marca previa.

## 3. Hipótesis (supuesto de trabajo)

> *Asumimos que la gobernanza raíz permanece en AvengaDevFlow hasta que el
> kit MetaFlow esté estable y se decida la migración (la §5.16 de la propia
> metodología describe ese procedimiento: renombrar, instalar, migrar,
> reconciliar).*

## 4. Opciones en consideración

| # | Opción | Implicación | Fuente |
|---|--------|-------------|--------|
| A | Permanecer con AvengaDevFlow instalado (default) | Gobernanza estable; el repo habla de AITL-* mientras el producto dice CP-* | default actual |
| B | Migrar la raíz al kit MetaFlow cuando esté estable | Coherente con la identidad; requiere procedimiento §5.16 | — |

## 5. Registro de investigación (append-only)

| Fecha | Autor | Nota |
|-------|-------|------|
| 2026-08-27 | @eugenioserrano | Abierta; no bloquea el MVP (X3 del scope) |
| 2026-08-27 | @eugenioserrano | Respondida: opción B (migrar cuando el kit esté estable) + numeración de salida = entrada − 4 (5.1 → 1.1) |

## 6. Resolución

**Respondida (2026-08-27, eugenioserrano): opción B** — el `devflow/` raíz se migra a MetaFlow **cuando el kit esté estable**, siguiendo el procedimiento §5.16 de la propia metodología (renombrar → instalar → migrar → reconciliar), para probar que todo siga fluyendo correctamente. El proceso de transformación se corre **en cada versión nueva** de AvengaDevFlow.

**Decisión adicional (registrada aquí por surgir en esta pregunta):** la numeración de MetaFlow va 4 números atrasada respecto de AvengaDevFlow — versión de salida = versión de entrada − 4 (mayor − 4, menor igual): **5.1 → 1.1**.

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Abierta | @eugenioserrano |
