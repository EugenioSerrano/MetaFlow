---
name: azure-devops-retrieval
description: 'Use cuando el QA da un Work Item ID o URL de Azure DevOps en lugar de pegar la HU manualmente, y el servidor MCP ado-remote-mcp está configurado y autenticado. Recupera Title, Description, Acceptance Criteria y Work Items relacionados, y los materializa en un archivo local para que el resto del pipeline nunca tenga que volver a consultar Azure DevOps.'
---

# Azure DevOps Retrieval

## Cuándo usar
- Solo cuando el QA identifica la HU por Work Item ID/URL (no cuando pega el texto directamente).
- Requiere que `.vscode/mcp.json` tenga configurado el servidor `ado-remote-mcp` y que la sesión esté autenticada contra la organización correspondiente. Si no está disponible, informá al QA que debe pegar la HU manualmente en su lugar; no falles el pipeline completo por esto.

## Input
- Work Item ID o URL provisto por el QA.

## Procedimiento
1. Verificá si ya existe `input/<id>.md`. Si existe y el QA no pidió explícitamente un refresh, usá ese archivo y no llames al MCP.
2. Si no existe (o se pidió refresh), consultá vía `ado-remote-mcp` el Work Item: Title, Description, Acceptance Criteria, tipo de Work Item, y relaciones con otros Work Items (parent/children/related) cuando estén disponibles y sean relevantes para el análisis.
3. Materializá el resultado en `input/<id>.md` (ver formato abajo). Esta es la **única** llamada al MCP para esta HU dentro del pipeline.
4. A partir de acá, todas las demás Skills (`user-story-analysis`, `testing-heuristics`, `exploratory-scenario-generation`, `test-case-consolidation`) leen únicamente este archivo local — nunca vuelven a invocar el MCP.

## Output
`input/<id>.md`:

```markdown
---
source: azure-devops
work_item_id: <id>
url: <url del work item>
fetched_at: <fecha ISO>
---

# <Title>

## Description
<descripción del work item>

## Acceptance Criteria
<AC tal como están en el work item, preservando su identificación original si la tienen>

## Related Work Items
- <tipo> <id> — <título> — <tipo de relación: parent/child/related>
```

Si algún campo no está disponible en el Work Item, dejalo indicado como "No disponible en Azure DevOps" en vez de completarlo con contenido inventado.
