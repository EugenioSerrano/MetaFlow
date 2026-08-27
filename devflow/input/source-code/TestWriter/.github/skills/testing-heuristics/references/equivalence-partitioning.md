# Equivalence Partitioning

Dividí cada campo/entrada relevante en clases de equivalencia: valores válidos e inválidos que el sistema debería tratar de la misma manera.

## Cómo aplicarlo
1. Identificá cada campo/parámetro con reglas de validación explícitas o inferidas (tipo de dato, formato, rango, valores permitidos).
2. Para cada campo, definí al menos:
   - una clase válida representativa;
   - una o más clases inválidas representativas (formato incorrecto, tipo incorrecto, valor fuera de dominio, vacío/nulo si aplica).
3. Generá un escenario por clase representativa, no por cada valor posible dentro de la clase.
4. Si el campo no tiene reglas documentadas ni inferibles, no inventes rangos — marcalo como pregunta abierta en el análisis de HU en lugar de asumir límites aquí.