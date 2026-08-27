# Gaps de cobertura — HU 138124

## Acceptance Criteria sin test cases asociados

- Ninguno de los AC recuperados quedó sin un caso asociado: AC1, AC2 y AC3 tienen cobertura heurística y exploratoria.
- Los Acceptance Criteria posteriores al AC3 no pudieron verificarse porque la respuesta de Azure DevOps llegó truncada. Por lo tanto, no es posible asegurar cobertura sobre esos criterios.

## Combinaciones/condiciones relevantes sin cubrir

- Comportamiento completo con Feature Flag apagada.
- Payload, código de respuesta y resultado del pago cuando el disponible es cero antes de la transacción.
- Reintegro superior al disponible: ajuste al remanente, denegación del beneficio o rechazo de operación.
- Idempotencia exacta ante `tx_id` repetido, timeout y reintentos.
- Concurrencia de dos operaciones del mismo usuario/MCC y política de resolución de la segunda.
- Precedencia entre tope por usuario y tope por MCC.
- Regla de redondeo para cálculos con más de dos decimales.
- Fallos de bloqueo/versionado y rollback de actualización atómica.
- Coordinación entre BFF y Jobs Batch cuando un job se reinicia o reprocesa.
- Zona horaria y semántica del corte mensual del día 1.
- Persistencia del Toast ante cierre, reapertura o navegación de la App.
- Validación y fallback de textos ausentes, vacíos, truncados o con caracteres especiales.
- Roles, permisos, ambientes y datos mínimos para ejecutar las pruebas, no documentados en `context/`.

## Priorización sugerida

- Alta: Feature Flag apagada; disponible cero; reintegro superior al disponible; `tx_id` repetido; timeout/reintento; concurrencia; atomicidad y rollback.
- Media: corte mensual y zona horaria; coordinación con Jobs Batch; precedencia usuario/MCC; redondeo monetario.
- Baja: persistencia visual del Toast; payload con textos alterados; navegación y ciclo de vida móvil.

## Observación de trazabilidad

Los casos generados para condiciones no definidas se conservaron como supuestos o riesgos, no como reglas confirmadas. Deben revisarse contra los Acceptance Criteria completos antes de ejecución formal.
