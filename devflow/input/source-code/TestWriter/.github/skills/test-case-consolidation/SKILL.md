---
name: test-case-consolidation
description: 'Use como último paso del pipeline para fusionar los escenarios deterministas (heurísticas) y exploratorios (LLM), eliminar duplicados/equivalentes, mapearlos a Acceptance Criteria, indicar la técnica y origen de cada uno, detectar gaps de cobertura, priorizar y producir el CSV final de test cases.'
---

# Test Case Consolidation

## Cuándo usar
- Siempre al final del pipeline, después de `testing-heuristics` y `exploratory-scenario-generation`.

## Input
- `output/<id>/02-heuristic-scenarios.md`
- `output/<id>/03-exploratory-scenarios.md`
- Acceptance Criteria de la HU (desde `output/<id>/01-analysis.md` o `input/<id>.md`)

## Procedimiento
1. **Deduplicar**: comparar escenarios de 02 y 03 (y dentro de cada archivo) para detectar duplicados exactos o equivalentes funcionalmente. Ante un duplicado, conservá la versión más específica y descartá la otra, dejando registro de qué técnica quedó asociada.
2. **Mapear a Acceptance Criteria**: cada test case final debe indicar a qué AC corresponde (`Coverage Tag`). Si un escenario no mapea a ningún AC explícito, indicalo igual (ej. riesgo derivado del dominio) pero no lo descartes solo por eso.
3. **Marcar técnica y origen**: cada test case lleva `Technique/Heuristic` (la técnica que lo originó, ej. "Boundary Value Analysis", "Error Guessing", "Exploratory/LLM") y `Origin` (`Heuristic` o `Exploratory`).
4. **Objetivo/Descripción**: para cada test case, redactá `Objective` como el propósito de la validación y `Description` como el alcance funcional del caso. Ambos campos se completan solo en la primera fila del caso.
5. **Detectar gaps de cobertura**: listá qué Acceptance Criteria no tienen ningún test case asociado, y qué combinaciones relevantes de condiciones quedaron sin cubrir.
6. **Priorizar** (cuando sea posible con la información disponible): marcá los test cases críticos para el flujo principal vs. los de menor impacto, sin inventar criterios de negocio que no estén documentados.
7. **Normalizar**: asigná un número correlativo de tres dígitos desde `001` por HU y construí el título con el patrón exacto `NNN - BE|BI - MB|WB - HOME - Funcionalidad - Descripción`. Usá únicamente valores de banca y plataforma declarados por QA o por la HU.
8. **Detallar pasos**: desglosá cada interacción en una fila independiente. La primera fila de cada caso es exclusivamente la cabecera del caso: debe contener la metadata del test case y dejar vacíos `Test Step`, `Step Action` y `Step Expected`. El paso `1` debe comenzar siempre en la fila inmediatamente siguiente, y cada paso posterior debe ocupar su propia fila. Cada `Step Action` debe indicar qué se toca o ingresa, qué se observa y qué validación visual, funcional o de navegación se realiza. Cada `Step Expected` debe indicar el resultado esperado y qué no debe ocurrir.
9. **Calcular complejidad** según la cantidad total de pasos: `3 - Baja` para 1 a 4 pasos, `2 - Media` para 5 a 9 pasos y `1 - Alta` para 10 o más pasos.
10. **Asignar prioridad**: `1` para flujo principal, humo, regresión, automatización o riesgo crítico/alto; `2` para escenarios alternativos relevantes o riesgo medio; `3` para situaciones de bajo riesgo, baja frecuencia o defectos bajos.

## Output

### `output/<id>/<id>_testcases.csv`
Usá el esquema de [testcases-template.csv](./assets/testcases-template.csv). El orden exacto es `ID`, `Work Item Type`, `Title`, `Objective`, `Description`, `Test Step`, `Step Action`, `Step Expected`, `Area Path`, `Assigned To`, `State`, `QA Status`, `QA Comment`, `Source HU ID`, `Coverage Tag`, `Technique/Heuristic`, `Origin`, `BComplejidad`, `BPrioridadTC`.
- La fila de cabecera de cada test case es la única fila que lleva `Work Item Type`, `Title`, `Objective`, `Description`, `Area Path`, `State`, `QA Status`, `Source HU ID`, `Coverage Tag`, `Technique/Heuristic`, `Origin`, `BComplejidad` y `BPrioridadTC`; también debe dejar vacíos `Test Step`, `Step Action` y `Step Expected`. Las filas siguientes contienen únicamente el número de paso, la acción y el resultado esperado, con toda la metadata vacía.
- `ID` y `Assigned To` quedan vacíos salvo que QA indique lo contrario. `State` es `Design`, `Work Item Type` es `Test Case` y `Test Step` es un entero secuencial desde `1`.
- `Coverage Tag` usa el mismo identificador de AC que la HU (ej. `AC1`).
- `Area Path` debe provenir primero de la metadata de la HU (`area_path`, `Área` o `Area`). Si la HU no lo contiene, usá el valor de respaldo de `context/test-design-config.md`; nunca lo inventes. Si ambas fuentes están vacías, detené la generación y preguntá a QA.

### `output/<id>/04-coverage-gaps.md`
```markdown
# Gaps de cobertura — HU <id>

## Acceptance Criteria sin test cases asociados
- <AC id> — <por qué quedó sin cobertura o qué falta para cubrirlo>

## Combinaciones/condiciones relevantes sin cubrir
- <descripción>

## Priorización sugerida
- Alta: <lista>
- Media: <lista>
- Baja: <lista>
```
