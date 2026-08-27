---
name: user-story-analysis
description: 'Use when recibís una User Story/HU nueva (texto pegado o archivo en input/) y necesitás evaluar su calidad y testabilidad antes de diseñar pruebas. Analiza claridad, completitud, ambigüedades, contradicciones, reglas de negocio faltantes, precondiciones, postcondiciones, actores, roles/permisos, estados, dependencias, datos, manejo de errores y calidad de los Acceptance Criteria.'
---

# User Story Analysis

## Cuándo usar
- Es siempre el primer paso del pipeline de diseño de pruebas, antes de aplicar cualquier heurística.
- También se puede reinvocar si el QA actualiza la HU o responde preguntas abiertas previas.

## Input
- Texto de la HU (pegado en el chat) o el archivo materializado `input/<id>.md`.
- Acceptance Criteria de la HU (si vienen separados, incluilos).
- Contenido de `context/business-rules.md`, `context/glossary.md` y `context/roles-permissions.md`, si existen, para no marcar como "faltante" algo que ya está documentado a nivel proyecto.

## Procedimiento
1. Leé la HU completa y el contexto de proyecto disponible.
2. Clasificá cada aspecto relevante (actores, roles/permisos, precondiciones, postcondiciones, estados, dependencias, datos necesarios, manejo de errores, reglas de negocio) en una de estas categorías, sin mezclarlas:
   - **Explícito**: está escrito literalmente en la HU o sus AC.
   - **Inferido**: se puede deducir con razonable seguridad de la HU + `context/`, pero no está dicho literalmente. Indicá de dónde se infiere.
   - **Faltante**: no está ni explícito ni inferible con seguridad.
   - **Supuesto**: algo que asumirías para poder avanzar, pero que debería confirmarse (nunca lo tomes como definitivo).
   - **Pregunta abierta**: duda concreta que el QA debería llevarle al Analista Funcional/PO/stakeholder.
3. Para cada pregunta abierta, marcá si es **crítica** (bloquea el diseño de pruebas, ej. falta una regla de negocio central o un AC contradice a otro) o **no crítica** (detalle menor, se puede diseñar con un supuesto documentado).
4. Evaluá la calidad de los Acceptance Criteria: ¿son verificables? ¿cubren casos negativos? ¿son ambiguos o se contradicen entre sí?
5. NUNCA completes huecos inventando reglas, roles, estados o datos. Si falta información, generá una pregunta abierta.

## Output
Escribí el resultado en `output/<id>/01-analysis.md` con esta estructura:

```markdown
# Análisis de HU <id> — <título>

## Información explícita
...

## Información inferida
- <dato> — inferido de: <origen>

## Información faltante
- <aspecto no cubierto>

## Supuestos (no confirmados)
- <supuesto>

## Preguntas abiertas
### Críticas (bloquean el diseño de pruebas)
- <pregunta>

### No críticas
- <pregunta>

## Evaluación de Acceptance Criteria
- <observaciones sobre claridad, verificabilidad, cobertura negativa, contradicciones>
```

Si hay preguntas críticas, el agente orquestador debe detenerse y presentarlas al QA antes de continuar con la Skill `testing-heuristics`.
