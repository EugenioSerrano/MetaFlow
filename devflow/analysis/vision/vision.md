---
title: "MetaFlow — Visión de producto"
version: "1.0"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
horizon: "12-18 meses"
sponsor: "Eugenio Serrano"
sources: ["conversación de diseño 2026-08-27"]
tags: [metaf low, transformacion, metodologia]
---

# Visión de producto — MetaFlow

## 1. Declaración de visión

> Para **Eugenio Serrano**, propietario de la metodología, que necesita una
> identidad propia e independiente para el framework que usa, **MetaFlow** es
> una **metodología de desarrollo de software asistida por IA** que **hereda
> íntegramente la funcionalidad de AvengaDevFlow** con nombres y atribución
> propios.
> A diferencia de **AvengaDevFlow** (cuya marca y autoría pertenecen a Avenga
> LATAM), **MetaFlow** es propiedad de Eugenio Serrano: misma funcionalidad,
> identidad nueva, y un pipeline de transformación que permite absorber cada
> nueva versión de AvengaDevFlow convirtiéndola en una versión de MetaFlow.

## 2. Resultados deseados

| # | Resultado | Señal que observamos | Línea base | Objetivo |
|---|-----------|----------------------|------------|----------|
| O1 | **Independencia de identidad** — MetaFlow no menciona Avenga ni sus marcas en el kit distribuido | Barrido de verificación sin tokens prohibidos (`Avenga`, `AITL`, `HITL`, `Bolt`, `V-Bounce`, `Raja`, `DORA`) | 154 menciones de "Avenga" en 144 archivos | **0** menciones |
| O2 | **Herencia de versiones 1:1** — cada versión de AvengaDevFlow en `input-kit/` produce una versión de MetaFlow en `distribution-kit/` | Versión del kit de salida = versión del kit de entrada **− 4** (mayor − 4, menor igual: 5.1 → 1.1) | — | 1:1 (una entrada → una salida), sin reescrituras manuales |
| O3 | **Transformación repetible** — el pipeline se ejecuta con un comando y su verificación es automática | Tiempo de ejecución; exit code del verificador | — | < 1 min; verificación 100 % automática |
| O4 | **Gobernanza propia** — el proyecto se desarrolla con la metodología, con artefactos en `devflow/` | Artefactos de análisis, US, TASKs, SPECs y MEMs del proyecto | — | Cobertura AITL completa |

## 3. Anti-objetivos

- AG1 — **No es una traducción** de la metodología: el contenido se hereda tal cual; solo cambian los nombres.
- AG2 — **No es una reescritura** de los conceptos: la funcionalidad (guardrails G01–G39, checkpoints, manifests, vocabulario US/TC/ADR…) se conserva íntegra.
- AG3 — **No es una filiación con Avenga**: no se presenta como versión oficial ni derivada de Avenga LATAM.
- AG4 — **No busca** reimplementar la pista de herramientas (`tools/`) del repositorio original.

## 4. Métricas de éxito tentativas

| Métrica | Definición | Objetivo tentativo |
|---------|------------|--------------------|
| Cobertura de rename | % de ocurrencias de los términos fuente que quedan transformados en el kit de salida | 100 % (verificador en cero) |
| Herencia de versión | Correspondencia versión AvengaDevFlow → versión MetaFlow | 1:1 |
| Tiempo de transformación | Duración del pipeline completo (transform + verificación) | < 1 min |
| Revisión humana | Casos que requieren intervención manual tras el transform | Tendencia a 0 |

## 5. Alcance de un vistazo

- **Dentro (v1):** toolkit de transformación en `src/` (Python), mapeo de nombres completo, verificación automática, reporte de transformación, `distribution-kit/` como salida.
- **Fuera (v1):** archivo de licencia en el kit (decidido: propietaria a nombre de Eugenio Serrano; falta definir cómo se materializa), traducción del contenido (decidido: el kit queda en inglés), migración del árbol `devflow/` raíz de este repositorio (decidido: cuando el kit esté estable).
- **Posiblemente después:** integración CI, diffs entre versiones heredadas, wrapper MCP, template HTML de reportes con branding propio de MetaFlow (el de Avenga no se migra — ver scope X6).

## 6. Preguntas abiertas

Cerradas el 2026-08-27 (propietario):

- [x] OQ-001 — el kit de salida queda en inglés (hereda `en`; sin traducción).
- [x] OQ-002 — licencia propietaria a nombre de Eugenio Serrano.
- [x] OQ-003 — la raíz se migra a MetaFlow cuando el kit esté estable (§5.16); el proceso se corre en cada versión nueva. Además: numeración de salida = entrada − 4 (5.1 → 1.1).
- [x] OQ-004 — re-transformación completa por versión (diff/merge como futuro).

## 7. Fuentes

| Fuente | Dónde |
|--------|-------|
| Conversación de diseño (2026-08-27) | Mapeo de nombres completo — ver `../glossary/metaflow.md` |

## 8. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Versión inicial | @eugenioserrano |
| 2026-08-27 | Validado por el propietario — status `stable` | @eugenioserrano |
