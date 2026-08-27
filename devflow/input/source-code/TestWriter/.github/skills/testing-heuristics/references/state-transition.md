# State Transition Testing

Aplica cuando la entidad de la HU tiene estados definidos (ej. una operación que pasa de Pendiente a Éxito o Rechazada).

## Cómo aplicarlo
1. Listá los estados explícitos o inferidos de la entidad y las transiciones válidas entre ellos.
2. Generá un escenario por cada transición válida documentada.
3. Generá también escenarios de transición inválida (ej. intentar pasar de un estado terminal a otro estado) si la HU o `context/` dan indicios de que eso debería estar bloqueado.
4. Si el diagrama de estados completo no está documentado, no lo inventes — documentá los estados que sí aparecen y generá una pregunta abierta sobre los que falten.