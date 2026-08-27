---
persona: "MetaFlowMaintainer"
label: "Mantenedor y propietario de MetaFlow"
persona_type: "archetype"
role: "Propietario de la metodología y mantenedor del repositorio"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
sources: ["conversación de diseño 2026-08-27"]
tags: [persona, metaf low]
---

# MetaFlowMaintainer

## 1. Tipo

**Archetype** — Es una composición basada en el rol (en la práctica, la
persona es Eugenio Serrano). La descripción captura el rol de mantenedor sin
inventar detalles personales.

## 2. Snapshot

> El mantenedor es el propietario de la metodología: decide la identidad
> (nombres, atribución, licencia), opera el pipeline de transformación cuando
> llega una nueva versión de AvengaDevFlow a `input-kit/`, y revisa el
> reporte del run antes de aceptar la versión MetaFlow.

| Campo | Valor |
|-------|-------|
| **Tipo** | archetype |
| **Rango etario** | N/A |
| **Rol / contexto** | Propietario y mantenedor único del repositorio |
| **Dispositivo / setup** | Windows, línea de comandos (PowerShell), git |
| **Alfabetización digital** | alta |

## 3. Objetivos

- **Objetivo 1** — Publicar una versión MetaFlow por cada versión de AvengaDevFlow que llegue a `input-kit/` (correspondencia 1:1; numeración de salida = entrada − 4: 5.1 → 1.1).
- **Objetivo 2** — Garantizar cero contaminación de marca: ningún `Avenga`, `AITL`, `HITL`, `Bolt`, `V-Bounce` en el kit de salida.
- **Objetivo 3** — Mantener el mapeo de nombres como datos simples de editar (`mapping.json`), sin tocar código.
- **Objetivo 4** — Revisar cada remoción/transformación antes de aceptar la versión (nada automático y silencioso).

## 4. Puntos de dolor

- **Dolor 1** — Un rename incompleto que deje menciones de Avenga en el kit distribuido (daño de identidad).
- **Dolor 2** — Reglas frágiles que rompan texto (p. ej. un replace ciego que dañe secciones `§4.1` al tocar números).
- **Dolor 3** — No poder verificar fácilmente qué cambió entre el input y el output.

## 5. Contexto de uso

- **Cuándo:** cuando llega una nueva versión de AvengaDevFlow, o cuando hay que ajustar el diccionario.
- **Dónde:** local, en el repositorio MetaFlow.
- **Cómo:** CLI (`python src/transform.py …`), revisa el reporte, commitea los resultados.

## 6. Cita representativa

> *"—" (No hay cita directa disponible — archetype.)*
> — Fuente: N/A (archetype)

## 7. Qué es éxito para él

> El pipeline corre en un comando, el verificador pasa en cero, el reporte
> muestra exactamente los cambios esperados (solo nombres), y la versión
> MetaFlow queda publicada en `distribution-kit/` con la versión correspondiente al input (entrada − 4: 5.1 → 1.1).

## 8. Anti-patrones a evitar

- Que el pipeline escriba sin reporte previo (dry-run siempre disponible).
- Que el mapeo requiera editar código Python para agregar una regla.
- Que el kit de salida mezcle idiomas o deje restos de la marca previa.

## 9. Fuentes

| Fuente | Dónde |
|--------|-------|
| Conversación de diseño 2026-08-27 | `../glossary/metaflow.md` |

## 10. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Borrador inicial | @eugenioserrano |
| 2026-08-27 | Validado por el propietario — status `stable` | @eugenioserrano |
