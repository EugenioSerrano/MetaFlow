# Error Guessing

Técnica basada en experiencia de testing para anticipar errores comunes que no surgen de reglas formales explícitas.

## Cómo aplicarlo
1. Pensá en errores típicos del tipo de funcionalidad descrita (ej. doble clic/doble submit, pérdida de conexión a mitad de una operación, reintentos, timeouts, caracteres especiales en campos de texto).
2. Priorizá los que sean plausibles dado el dominio de la HU (pagos, formularios, flujos con estados, etc.), no una lista genérica desconectada del contexto.
3. Diferenciá esto de la exploración generativa de la Skill `exploratory-scenario-generation`: acá se trata de errores comunes y bien conocidos en testing, no de razonamiento creativo abierto sobre el dominio específico.