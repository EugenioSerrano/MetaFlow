# TestWriter — Guía global

Este repo distribuye un **Test Design Agent** para QA manual. El agente orquesta skills; no dupliques su lógica aquí.

## Puntos de entrada y fuentes de verdad
- Para ejecutar el flujo completo, usar [`test-design.agent.md`](agents/test-design.agent.md) o el atajo [`design-tests.prompt.md`](prompts/design-tests.prompt.md).
- La HU local es la fuente operativa después de la adquisición: [`input/<id>.md`](../input/). Azure DevOps se consulta únicamente durante `azure-devops-retrieval` cuando el QA entrega un ID o URL.
- Las reglas estables del proyecto están en [`context/`](../context/); leer `business-rules.md`, `glossary.md`, `roles-permissions.md` y `test-design-config.md` antes de diseñar o consolidar pruebas.
- Las instrucciones detalladas de cada etapa viven en [`skills/`](skills/). Mantener este archivo como índice y reglas de coordinación, no como copia de esas skills.

## Pipeline (siempre en este orden)
1. (opcional) Azure DevOps Retrieval → materializa la HU en `input/<id>.md`
2. User Story Analysis → `output/<id>/01-analysis.md` (gate: si hay preguntas críticas, detenerse y preguntar al QA)
3. Testing Heuristics → `output/<id>/02-heuristic-scenarios.md`
4. Exploratory Scenario Generation → `output/<id>/03-exploratory-scenarios.md` (debe leer 02 para no duplicar)
5. Test Case Consolidation → `output/<id>/<id>_testcases.csv` + `output/<id>/04-coverage-gaps.md`

## Reglas no negociables
- **Nunca inventar** reglas de negocio, roles, estados o datos que no estén en la HU, en sus Acceptance Criteria o en `context/`. Si falta información, generar una pregunta abierta en vez de asumir.
- El conocimiento específico de cada proyecto vive en `context/` (business-rules, glossary, roles-permissions). Leerlo antes de aplicar heurísticas o analizar la HU.
- La cobertura determinista (heurísticas) nunca se salta ni se reemplaza por exploración generativa; ambas son complementarias y deben quedar etiquetadas por separado (`Origin`: Heuristic | Exploratory).
- Persistir artefactos intermedios como archivos en `output/<id>/`, no solo en el chat, para mantener auditabilidad.
- Leer `context/test-design-config.md` antes de consolidar. Resolver `Area Path` primero desde la metadata de la HU (`area_path`, `Área` o `Area`) y usar el contexto solo como fallback. Si falta en ambas fuentes, o faltan banca, plataforma o funcionalidad, generar una pregunta crítica y detener el pipeline.
- El CSV final debe respetar el esquema de `.github/skills/test-case-consolidation/assets/testcases-template.csv`, incluyendo `Objective`, `Description`, `Technique/Heuristic`, `Origin`, `BComplejidad` y `BPrioridadTC`.
- Cada título debe seguir exactamente `NNN - BE|BI - MB|WB - HOME - Funcionalidad - Descripción`, con numeración correlativa de tres dígitos desde `001`.
- Los campos de configuración y trazabilidad solo se completan en la primera fila de cada caso. Esa fila es exclusivamente la cabecera y debe dejar vacíos `Test Step`, `Step Action` y `Step Expected`; el paso `1` comienza obligatoriamente en la fila siguiente. Las filas adicionales contienen únicamente el número de paso, acción y resultado esperado.
- Azure DevOps solo se consulta una vez por HU (vía la skill de retrieval); el resto del pipeline lee siempre el archivo local materializado, nunca llama al MCP directamente.

## Validación antes de cerrar
- Confirmar que existan `01-analysis.md`, `02-heuristic-scenarios.md`, `03-exploratory-scenarios.md`, `04-coverage-gaps.md` y `<id>_testcases.csv` dentro de `output/<id>/`.
- Revisar que las preguntas críticas sigan resueltas o estén documentadas como bloqueo en `04-coverage-gaps.md`; no presentar una HU bloqueada como cobertura completa.
- Verificar que el encabezado del CSV coincida con [`testcases-template.csv`](skills/test-case-consolidation/assets/testcases-template.csv), que cada caso empiece con una cabecera sin datos de paso y que sus pasos sean secuenciales desde `1`.
- Usar siempre la plantilla vigente y la skill de consolidación como autoridad del esquema; los CSV existentes en `output/` pueden ser ejemplos o borradores históricos y no sustituyen esa especificación.
- Este repositorio no define un build o suite automatizada; la validación principal es la consistencia entre la HU, los artefactos intermedios y el CSV. Si se necesita una comprobación rápida del CSV en PowerShell, usar `Import-Csv output/<id>/<id>_testcases.csv`.
