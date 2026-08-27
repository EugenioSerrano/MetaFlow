# Decision Tables

Útil cuando la HU combina varias condiciones independientes que determinan un resultado distinto (reglas de negocio con múltiples condicionales).

## Cómo aplicarlo
1. Identificá las condiciones relevantes explícitas en la HU/AC (ej. "usuario afiliado activo", "prestador habilitado", "menos de 3 reintegros en el mes").
2. Armá una tabla con las combinaciones relevantes de esas condiciones (no necesariamente todas las combinaciones posibles si son muchas; priorizá las combinaciones con valor de negocio real y las que la HU menciona explícitamente).
3. Cada fila/combinación de la tabla es un escenario de prueba con su resultado esperado según la regla de negocio.
4. Si el resultado de alguna combinación no está definido en la HU/AC/`context/`, no lo completes por lógica propia — es una pregunta abierta para el análisis de HU.