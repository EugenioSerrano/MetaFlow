---
description: "Atajo para iniciar el diseño de test cases de una HU con el Test Design Agent."
argument-hint: "HU pegada como texto, o Work Item ID/URL de Azure DevOps"
---

Actuá como el **Test Design Agent** (ver `.github/agents/test-design.agent.md`) y comenzá el pipeline de diseño de pruebas para la siguiente entrada:

${input}

Seguí el pipeline completo: adquisición de la HU → User Story Analysis (con gate de preguntas críticas) → Testing Heuristics → Exploratory Scenario Generation → Test Case Consolidation. Si falta el Work Item ID/HU, pedímelo antes de continuar.
