# TestWriter

TestWriter es un agente para diseñar casos de prueba manuales a partir de una User Story (HU). Analiza la historia, aplica heurísticas de testing, explora escenarios adicionales y consolida un CSV trazable para Azure DevOps.

## Guía rápida

### 1. Preparar el contexto del proyecto

Antes de analizar una HU, completar los archivos de [`context/`](context/):

- [`business-rules.md`](context/business-rules.md): reglas de negocio estables.
- [`glossary.md`](context/glossary.md): términos y siglas del dominio.
- [`roles-permissions.md`](context/roles-permissions.md): roles, actores y permisos.
- [`test-design-config.md`](context/test-design-config.md): valores de respaldo y convenciones de banca, plataforma y funcionalidad.

El agente usa este contexto para diseñar pruebas y no inventa reglas, estados, roles ni datos. Cuando falta información relevante, genera una pregunta abierta. El `Area Path` se toma primero de la metadata de la HU (`area_path`, `Área` o `Area`) y el archivo de contexto funciona como respaldo. Cada HU debe declarar la banca (`BE` o `BI`), plataforma (`MB` o `WB`) y funcionalidad aplicables.

### 2. Incorporar la HU

Guardar la historia como `input/<id>.md`, por ejemplo [`input/8547.md`](input/8547.md).

La HU puede:

- Copiarse manualmente en ese archivo.
- Materializarse desde Azure DevOps mediante la skill `azure-devops-retrieval`, usando un Work Item ID o URL.

Después de materializarla, el resto del pipeline trabaja únicamente con el archivo local.

### 3. Ejecutar el agente desde VS Code

Abrir este repositorio en VS Code y pedir al **Test Design Agent** que procese la HU. Por ejemplo:

> Analiza y genera los casos de prueba para `input/8547.md`.

También se puede proporcionar directamente el texto de una HU o un Work Item ID/URL de Azure DevOps.

Si el análisis detecta preguntas críticas, el pipeline se detiene para que QA las responda antes de continuar.

### 4. Revisar los resultados

Para una HU con ID `8547`, los artefactos se guardan en `output/8547/`:

1. `01-analysis.md`: calidad, testabilidad, ambigüedades y preguntas pendientes.
2. `02-heuristic-scenarios.md`: escenarios deterministas derivados de técnicas de testing.
3. `03-exploratory-scenarios.md`: escenarios exploratorios adicionales, sin duplicar los heurísticos.
4. `04-coverage-gaps.md`: cobertura faltante, bloqueos y prioridades.
5. `8547_testcases.csv`: casos consolidados listos para revisar o importar.

El ejemplo [`output/8547/`](output/8547/) muestra el resultado completo para la HU 8547. La plantilla de CSV está disponible en [`output/8547_example_testcases_draft.csv`](output/8547_example_testcases_draft.csv).

## Orden del pipeline

El flujo debe ejecutarse siempre en este orden:

1. Azure DevOps Retrieval (opcional): materializa la HU en `input/<id>.md`.
2. User Story Analysis: analiza la calidad de la HU y funciona como puerta de entrada.
3. Testing Heuristics: genera cobertura determinista.
4. Exploratory Scenario Generation: agrega casos exploratorios.
5. Test Case Consolidation: elimina duplicados, prioriza y genera el CSV final.

La cobertura heurística y la exploratoria son complementarias y deben conservar su origen (`Heuristic` o `Exploratory`). Los títulos siguen `NNN - BE|BI - MB|WB - HOME - Funcionalidad - Descripción`.

## Reglas importantes

- No inventar reglas de negocio, roles, estados ni datos.
- Leer el contenido de `context/` antes de diseñar pruebas.
- Persistir los artefactos intermedios en `output/<id>/`, no solo en el chat.
- Mantener trazabilidad de cada caso hacia su Acceptance Criteria.
- Consultar Azure DevOps una sola vez por HU; luego usar siempre la copia local.
- Resolver las preguntas críticas del análisis antes de considerar completa la cobertura.
- El CSV final incluye `Objective`, `Description`, `Technique/Heuristic`, `Origin`, `BComplejidad` y `BPrioridadTC`; la configuración de cada caso solo aparece en su primera fila.

## Estructura del repositorio

```text
.github/
  agents/                 Definición del Test Design Agent
  prompts/                Prompts reutilizables
  skills/                 Skills que implementan cada etapa del pipeline
  copilot-instructions.md Reglas globales del agente
context/                  Conocimiento específico del proyecto
input/                    User Stories materializadas o ingresadas manualmente
output/                   Artefactos y CSV de casos de prueba
```

## Requisitos

- VS Code con GitHub Copilot habilitado.
- Acceso al agente y las skills incluidas en `.github/`.
- Para recuperar HUs desde Azure DevOps: MCP de Azure DevOps configurado y autenticado.
- Para trabajar sin Azure DevOps: basta con guardar la HU en `input/<id>.md`.

## Resultado esperado

El entregable principal es `output/<id>/<id>_testcases.csv`. Debe conservar el esquema de la plantilla y añadir las columnas `Objective/Description`, `Technique/Heuristic` y `Origin`, junto con la trazabilidad al Work Item y a cada Acceptance Criterion.
