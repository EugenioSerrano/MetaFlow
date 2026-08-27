---
topic: "business-model"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
sources: ["conversación de diseño 2026-08-27"]
tags: [metaf low, contexto]
---

# Contexto de negocio — MetaFlow (modelo y partes interesadas)

## 1. Resumen

Este documento describe el mundo en el que vive MetaFlow: quiénes son las
partes interesadas, qué modelo de propiedad aplica y qué métricas de éxito
definen al proyecto. MetaFlow es la metodología de Eugenio Serrano, derivada
de AvengaDevFlow con identidad propia; el repositorio que la construye
transforma cada nueva versión del kit de AvengaDevFlow (`input-kit/`) en una
versión de MetaFlow (`distribution-kit/`).

## 2. Contenido

### Partes interesadas

| Parte interesada | Rol (sponsor/usuario/afectado/regulador) | Influencia (H/M/L) | Interés (H/M/L) | Preocupación clave |
|------------------|-------------------------------------------|:------------------:|:----------------:|--------------------|
| Eugenio Serrano | Sponsor y propietario | H | H | Que MetaFlow sea 100 % funcionalmente equivalente a AvengaDevFlow con identidad propia |
| Usuarios/adoptantes de MetaFlow | Usuario | L | M | Que la metodología funcione igual que la original, sin referencias ajenas |
| Avenga LATAM | Afectado (origen del contenido) | L | L | N/A — no participa; el contenido fuente se transforma sin atribución a su marca |
| Agentes de IA (DevFlow Agents) | Usuario | M | H | Que las reglas, guardrails y checkpoints se mantengan legibles y aplicables |

### Modelo de negocio

- **Propiedad:** la metodología y el repositorio son propiedad de **Eugenio
  Serrano**.
- **Licencia:** **propietaria a nombre de Eugenio Serrano** (decidida el
  2026-08-27 — OQ-002). La atribución de autoría se reescribe a
  Eugenio Serrano en el kit de salida.
- **Modelo de evolución:** cada nueva versión de AvengaDevFlow se coloca en
  `input-kit/` y el pipeline de transformación produce la versión
  correspondiente de MetaFlow en `distribution-kit/`. No hay desarrollo de
  contenido de metodología propio en esta etapa: la funcionalidad se hereda
  íntegramente.

### Métricas de éxito

| Métrica | Resultado de visión vinculado | Definición | Línea base | Objetivo | Dueño |
|---------|-------------------------------|------------|------------|----------|-------|
| Cobertura de rename | O1 | Ocurrencias de términos fuente transformadas en el kit de salida | 154 menciones "Avenga" (input) | 100 % (0 en output) | Eugenio Serrano |
| Herencia de versión | O2 | Correspondencia AvengaDevFlow → MetaFlow (salida = entrada − 4) | — | 1:1 (5.1 → 1.1) | Eugenio Serrano |
| Tiempo de transformación | O3 | Duración del pipeline | — | < 1 min | Eugenio Serrano |
| Equivalencia funcional | O1/O2 | Diferencia de contenido entre input y output, excluyendo renames | — | Solo cambios de nombres | Eugenio Serrano |

## 3. Fuentes

| Fuente | Dónde |
|--------|-------|
| Conversación de diseño (2026-08-27) | `../glossary/metaflow.md` (diccionario de rename) |
| Kit de entrada | `../../../input-kit` (raíz del repo) |

## 4. Preguntas abiertas / Seguimientos

- [x] OQ-002 — licencia propietaria a nombre de Eugenio Serrano (2026-08-27).
- [x] OQ-001 — el kit de salida queda en inglés (hereda `en`; 2026-08-27).

## 5. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Versión inicial | @eugenioserrano |
| 2026-08-27 | Validado por el propietario — status `stable` | @eugenioserrano |
