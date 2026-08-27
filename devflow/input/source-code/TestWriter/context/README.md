# Contexto de proyecto

Esta carpeta contiene el conocimiento específico del proyecto/equipo que usa este Test Design Agent. Separarlo del agente y las skills permite reutilizar el mismo pipeline en distintos proyectos sin tocar `.github/`.

Completá estos archivos por proyecto (podés dejarlos vacíos si todavía no aplican, pero no borrarlos):

- `business-rules.md`: reglas de negocio estables del proyecto (ej. topes, fórmulas, condiciones de elegibilidad) que no deberían repetirse en cada HU.
- `glossary.md`: términos y siglas propias del dominio del proyecto.
- `roles-permissions.md`: actores/roles del sistema y qué puede hacer cada uno.

El agente y las skills leen estos archivos antes de analizar una HU o aplicar heurísticas, y **nunca inventan** información que debería estar acá pero no está — en ese caso generan una pregunta abierta para el QA.
