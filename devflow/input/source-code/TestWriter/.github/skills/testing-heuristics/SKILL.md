---
name: testing-heuristics
description: 'Use después de User Story Analysis para aplicar sistemáticamente técnicas deterministas de diseño de pruebas (equivalence partitioning, boundary value analysis, decision tables, state transition, positive/negative testing, error guessing, CRUD, roles/permisos) y generar el set base de test cases con trazabilidad a la técnica que los originó.'
---

# Testing Heuristics

## Cuándo usar
- Siempre después de `user-story-analysis` y solo cuando no quedan preguntas críticas sin responder.
- Es la base de cobertura **determinista**: nunca se salta ni se reemplaza por la exploración generativa (Skill `exploratory-scenario-generation`).

## Input
- `output/<id>/01-analysis.md` (HU ya clarificada: explícito + inferido + supuestos aceptados).
- Acceptance Criteria de la HU.
- `context/` del proyecto (reglas de negocio, glosario, roles/permisos) si existe.

## Técnicas a aplicar
Revisá cada técnica y aplicá las que correspondan según la naturaleza de la HU (no todas aplican siempre). El detalle de cada una está en su propio archivo de referencia — cargalo solo cuando necesites el detalle:

- [Equivalence Partitioning](./references/equivalence-partitioning.md)
- [Boundary Value Analysis](./references/boundary-value-analysis.md)
- [Decision Tables](./references/decision-tables.md)
- [State Transition Testing](./references/state-transition.md)
- [CRUD Scenarios](./references/crud-scenarios.md)
- [Error Guessing](./references/error-guessing.md)
- [Roles & Permissions](./references/roles-permissions.md)
- Positive / Negative Testing: para cada regla o AC, generá al menos un caso positivo y uno negativo explícito (no requiere archivo de referencia aparte, es transversal a las demás técnicas).

Para agregar una heurística nueva en el futuro: creá un archivo nuevo en `references/` y sumale una línea a esta lista. No hace falta tocar el agente ni otras skills.

## Procedimiento
1. Por cada técnica aplicable, generá los escenarios correspondientes.
2. Cada escenario debe indicar explícitamente qué técnica lo originó (no dejes escenarios sin técnica asociada).
3. Relacioná cada escenario con el/los Acceptance Criteria que cubre (usá el mismo identificador de AC que use la HU, ej. `AC1`).
4. No dupliques escenarios entre técnicas; si dos técnicas producen el mismo caso, quedate con la técnica más específica y anotalo.
5. Incorporá, cuando la HU o el contexto lo respalden, escenarios de múltiples cuentas, seguridad, validaciones de UI, errores/negativos, flujo EndToEnd y HUs dependientes. Si falta la regla o la dependencia, registrá una pregunta o gap en lugar de inventarla.

## Output
Escribí el resultado en `output/<id>/02-heuristic-scenarios.md`, una entrada por escenario:

```markdown
## <Técnica> — <título del escenario>
- AC relacionado: <AC1, AC2, ...>
- Precondición: ...
- Pasos: cada paso debe describir qué toca o ingresa el usuario, sobre qué elemento, qué observa y qué validación de navegación, UI o funcionalidad realiza.
- Resultado esperado: resultado visible/funcional y comportamiento que no debe ocurrir para cada paso.
```

Este archivo es el input obligatorio de `exploratory-scenario-generation` (para evitar duplicados) y de `test-case-consolidation`.
