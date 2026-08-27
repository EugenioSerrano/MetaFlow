# Análisis de HU 138124 — Topes por usuario y por período

## Información explícita

- La solución aplica a pagos con QR y al flujo de cashback de Billetera Bezza.
- Existe una Feature Flag de topes con estados encendida/apagada.
- El control se realiza por usuario y rubro/categoría MCC.
- El procesamiento debe ser atómico e idempotente mediante `tx_id`.
- Se requiere precisión monetaria con `BigDecimal` de escala 2.
- Se mencionan las tablas `cashback_mcc_tope_config`, `cashback_entitlement_usage_mcc` y `cashback_entitlement_tx_dedup`.
- Con Feature Flag encendida y disponible agotado por la compra, la API debe devolver `show_limit_reached_message = true` y los textos definidos.
- El mensaje de título esperado es "¡Le sacaste provecho a Bezza!".
- El mensaje de cuerpo esperado es "Llegaste al límite de reintegros de este rubro. Se renuevan el 1 del mes que viene.".
- La App debe mostrar el Toast informativo en la Pantalla de Resultado Exitoso.
- Si queda disponible mayor a cero, `show_limit_reached_message` debe ser falso y no deben enviarse los textos.
- Si el disponible es cero antes de la transacción, el BFF debe registrar la denegación por tope y derivar al flujo de pago tradicional.

## Información inferida

- El límite se evalúa por período mensual, porque el mensaje indica renovación el día 1 del mes siguiente.
- El mensaje de límite alcanzado corresponde únicamente al caso en que la transacción consume la totalidad del beneficio, no al caso en que el usuario ya tenía disponible cero.
- La respuesta del BFF es el contrato que consume la App Mobile para decidir si muestra el Toast.

## Información faltante

- El resto de la Description y de los Acceptance Criteria no pudo recuperarse de forma verificable porque la respuesta extensa de Azure DevOps fue truncada por la interfaz.
- Comportamiento completo de la Feature Flag apagada.
- Resultado funcional exacto cuando el disponible del MCC es cero antes de pagar: campos de API, estado del pago y mensajes al usuario.
- Comportamiento esperado ante `tx_id` repetido y definición de la respuesta idempotente.
- Regla de precedencia si el tope por usuario y el tope por MCC se alcanzan simultáneamente.
- Regla exacta de cálculo, redondeo y escala para montos con más de dos decimales.
- Comportamiento ante errores de actualización atómica, bloqueo por versión o caída de Jobs Batch.
- Contrato completo de la API: campos obligatorios, campos omitidos versus nulos y códigos de error.
- Momento exacto de actualización del consumo respecto de la acreditación del reintegro.
- Criterios de renovación mensual y zona horaria aplicable.
- Roles, permisos, ambientes y datos de prueba específicos. Los archivos de `context/` no documentan estos aspectos.

## Supuestos (no confirmados)

- Se probará el flujo de pago QR existente con un usuario autenticado y un comercio válido.
- Los valores de tope y consumo estarán configurados en las tablas mencionadas.
- El `tx_id` será único para una transacción nueva.

## Preguntas abiertas

### Críticas (bloquean el diseño de pruebas)

- ¿Cuál es el comportamiento verificable de la Feature Flag apagada: se omite el control de topes, se mantiene el flujo legacy y qué campos devuelve la API?
- Cuando el disponible del MCC es cero antes de la transacción, ¿se rechaza solo el reintegro o también el pago, qué respuesta/código devuelve el BFF y qué debe mostrar la App?
- ¿Cuáles son los Acceptance Criteria completos posteriores al criterio 3, incluyendo reglas de usuario, MCC, idempotencia, concurrencia y errores transaccionales?
- Ante un `tx_id` duplicado, ¿debe devolverse la respuesta original sin volver a acreditar ni incrementar consumo, y qué estado deben mostrar BFF y App?
- Si el reintegro excede el disponible, ¿se ajusta al remanente, se deniega el beneficio completo o se rechaza la operación?

### No críticas

- ¿Qué zona horaria y fecha de corte se usan para renovar el período mensual?
- ¿Los textos deben enviarse omitidos o como `null` cuando `show_limit_reached_message` es falso?
- ¿Cuál es el código MCC y configuración mínima requerida para los datos de prueba?
- ¿La App debe mostrar el Toast solo después de una confirmación exitosa de pago y acreditación del beneficio?

## Evaluación de Acceptance Criteria

- Los criterios 1 y 2 son parcialmente verificables y contienen valores esperados concretos para la API y la UI.
- El criterio 3 está incompleto en la información recuperada; no permite determinar el resultado esperado completo.
- No se puede confirmar cobertura suficiente de los estados de Feature Flag, límites por usuario/MCC, transacciones repetidas, concurrencia, precisión monetaria, fallos transaccionales ni renovación mensual porque el contenido restante no está disponible.
- El pipeline queda detenido en este gate. No se generan escenarios heurísticos, exploratorios ni CSV final hasta que QA confirme las respuestas críticas o autorice explícitamente continuar con supuestos documentados.
