# Boundary Value Analysis

Complementa Equivalence Partitioning enfocándose en los límites de cada clase de equivalencia, donde los defectos son más probables.

## Cómo aplicarlo
1. Para cada campo con límites explícitos o inferidos (mínimo, máximo, longitud, cantidad de intentos, montos, fechas), generá casos en:
   - el valor límite exacto (mínimo y máximo);
   - un valor justo por debajo del límite;
   - un valor justo por encima del límite.
2. Si la HU menciona contadores o topes (ej. "máximo 3 reintegros al mes"), aplicá BVA sobre ese contador: 2, 3 y 4 usos.
3. No inventes límites numéricos que no estén en la HU, AC o `context/`; si el límite no está definido, generá una pregunta abierta en el análisis en vez de asumir un valor.