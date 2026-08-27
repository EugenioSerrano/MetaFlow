---
name: exploratory-scenario-generation
description: 'Use después de Testing Heuristics para explorar generativamente edge cases, corner cases, interacciones inesperadas, secuencias poco frecuentes y riesgos que las técnicas deterministas no cubrieron. Recibe siempre los escenarios ya generados para evitar duplicados.'
---

# Exploratory Scenario Generation

## Cuándo usar
- Siempre después de `testing-heuristics`, nunca antes ni en su reemplazo.
- Es la fase **generativa** del pipeline: complementa la cobertura determinista, no la sustituye.

## Input
- `output/<id>/01-analysis.md` (contexto de la HU: explícito, inferido, supuestos aceptados).
- `output/<id>/02-heuristic-scenarios.md` (obligatorio leerlo antes de generar nada, para no duplicar).
- `context/` del proyecto, si existe, para detectar riesgos conocidos del dominio (ej. integraciones frágiles, reglas históricamente propensas a errores).

## Qué buscar
- Edge cases y corner cases no cubiertos por las clases de equivalencia o límites ya definidos.
- Interacciones inesperadas entre distintas partes de la HU o con otras funcionalidades relacionadas.
- Secuencias de uso poco frecuentes (ej. navegación hacia atrás, cancelar a mitad de flujo, repetir una acción rápidamente).
- Combinaciones de condiciones que las decision tables de la fase determinista no priorizaron.
- Escenarios de error e inconsistencias funcionales que un tester experimentado probaría aunque no estén documentados explícitamente.
- Riesgos derivados del contexto del proyecto (dominio de negocio, integraciones conocidas).

## Procedimiento
1. Leé completo `02-heuristic-scenarios.md` antes de proponer nada nuevo.
2. Por cada escenario nuevo que propongas, verificá explícitamente que no sea equivalente a uno ya listado en 02; si es una variante cercana, indicá en qué se diferencia.
3. Para cada escenario, incluí una breve justificación de por qué un tester experimentado lo probaría (no solo "por las dudas").
4. No reetiquetes escenarios heurísticos como exploratorios ni viceversa.
5. Priorizá riesgos adicionales de múltiples cuentas, seguridad, UI, errores/negativos, flujo EndToEnd y HUs dependientes cuando estén respaldados por la HU o `context/`. Si no están definidos, documentá el gap sin asumir el comportamiento.

## Output
Escribí el resultado en `output/<id>/03-exploratory-scenarios.md`:

```markdown
## Exploratory — <título del escenario>
- Justificación: <por qué vale la pena probarlo>
- AC relacionado: <AC1, AC2, ... o "ninguno explícito, riesgo derivado del dominio">
- Precondición: ...
- Pasos: detallá cada toque, dato ingresado, elemento observado, validación visual/funcional/navegación y condición que no debe ocurrir.
- Resultado esperado: resultado observable y comportamiento prohibido.
```
