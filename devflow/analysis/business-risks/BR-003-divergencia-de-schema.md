---
id: "BR-003"
title: "Divergencia de schema del manifest (delivery_loops[] vs v_bounces[])"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
category: "business-model"
sources: ["conversación de diseño 2026-08-27"]
tags: [riesgo, schema, manifest]
---

# BR-003 — Divergencia de schema del manifest

## 1. Descripción

El renombrado total incluye los campos de los manifests y sus schemas
(`v_bounces[]` → `delivery_loops[]`, `bolt{}` → `task{}`, `test_bolts[]` →
`test_tasks[]`, `manifest-v5-bolt.schema.json` → `manifest-v5-task.schema.json`).
Esto hace que el schema de MetaFlow sea **incompatible** con el de
AvengaDevFlow: herramientas, validadores o procesos que esperen el schema
original no entenderán los manifests MetaFlow, y viceversa. Es una
consecuencia buscada del rebrand, pero limita la interoperabilidad con
cualquier tooling del ecosistema Avenga.

## 2. Categoría

`business-model`

## 3. Evaluación

| Dimensión | Valor | Razón |
|-----------|-------|-------|
| Probabilidad | `high` | Es la consecuencia directa de la decisión "renombrar todo" |
| Impacto | `medium` | El ecosistema Avenga no es consumidor de MetaFlow; el costo es no poder reutilizar tooling externo |

## 4. Mitigación

- Documentar el mapeo de campos en el glossary (B11/B12/D3) para poder traducir manifests en ambas direcciones si hiciera falta.
- El toolkit de transformación puede, en el futuro, ofrecer una regla de "mapeo inverso" para interoperar.

## 5. Contingencia

Si surge la necesidad de interoperar con tooling Avenga: crear una pequeña
capa de traducción de manifests (campo a campo) o un modo de exportación.

## 6. Fuentes

- Decisión "renombrar todo todo todo" (2026-08-27)
- `../glossary/metaflow.md` §3 (B11/B12) y §4 (D3)

## 7. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Creado | @eugenioserrano |
