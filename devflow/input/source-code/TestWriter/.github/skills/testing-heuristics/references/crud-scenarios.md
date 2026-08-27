# CRUD Scenarios

Aplica cuando la HU describe la gestión de una entidad (crear, leer, actualizar, eliminar/dar de baja).

## Cómo aplicarlo
1. Identificá qué operaciones CRUD están explícitamente en el alcance de la HU (no asumas que las cuatro aplican si solo se describe una).
2. Para cada operación en alcance, generá casos de creación/lectura/actualización/baja válidos y sus contrapartes inválidas (datos duplicados, entidad inexistente, permisos insuficientes).
3. Considerá efectos colaterales entre operaciones (ej. ¿qué pasa con datos relacionados al eliminar/dar de baja una entidad?) solo si la HU o `context/` los mencionan.