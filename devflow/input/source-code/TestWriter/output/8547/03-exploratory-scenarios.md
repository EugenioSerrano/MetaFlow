## Exploratory — Renovación del contador de reintegros en el cambio de mes
- Justificación: la fórmula `remaining = 3 - usos - 1` depende del "mes" del usuario; un tester experimentado probaría el comportamiento justo en el límite entre un mes y el siguiente, donde suelen aparecer defectos de reseteo de contadores.
- AC relacionado: ninguno explícito, riesgo derivado de la regla de negocio RULE_APROSS (tope mensual).
- Precondición: usuario con 3 reintegros usados en el mes anterior (contador en 0), llega el cambio de mes.
- Pasos: 1) Verificar el contador justo antes del cambio de mes. 2) Verificar el contador justo después del cambio de mes. 3) Intentar un pago con QR Dinámico en el nuevo mes.
- Resultado esperado a validar: el contador debería renovarse a 3 disponibles en el nuevo mes; verificar que no persiste el conteo del mes anterior.

## Exploratory — Reutilización del mismo QR Dinámico tras un pago exitoso
- Justificación: los QRs dinámicos suelen tener una única validez; un tester probaría escanear nuevamente el mismo QR inmediatamente después de completar el pago para detectar reintegros duplicados.
- AC relacionado: AC1 (interacción no cubierta por el escenario base de pago exitoso)
- Precondición: pago exitoso ya realizado con un QR Dinámico específico.
- Pasos: 1) Volver a escanear el mismo QR Dinámico usado en el pago anterior. 2) Intentar procesar la validación nuevamente.
- Resultado esperado a validar: el sistema no debería aplicar un segundo reintegro sobre el mismo QR/transacción ya procesada.

## Exploratory — Abandono del flujo entre la pantalla 9.1.1 y la acción "Pagar"
- Justificación: es una secuencia de uso poco frecuente pero real (usuario ve el mensaje de reintegro y decide no pagar), distinta del camino feliz documentado en 02-heuristic-scenarios.md que sí llega a presionar "Pagar".
- AC relacionado: AC1 (variante no cubierta)
- Precondición: pantalla 9.1.1 visible con mensaje de Reintegro Apross.
- Pasos: 1) Salir de la pantalla 9.1.1 sin presionar "Pagar" (botón atrás o cierre de la app). 2) Verificar el estado del contador de reintegros.
- Resultado esperado a validar: el contador no debe decrementarse si el pago no se confirma.

## Exploratory — Interacción entre el beneficio Apross y otra configuración de cashback en la misma transacción
- Justificación: la HU menciona "estados de éxito o error según configuración de cashback" sin detallarla; un tester experimentado exploraría si puede coexistir con el beneficio Apross en el mismo pago, más allá de que el detalle exacto ya quedó marcado como pregunta crítica en el análisis.
- AC relacionado: ninguno explícito, riesgo derivado del alcance documentado.
- Precondición: transacción elegible para Apross que también sea elegible para algún cashback general del comercio/QR.
- Pasos: 1) Procesar un pago con QR Dinámico elegible para Apross en un contexto donde también aplicaría cashback general.
- Resultado esperado a validar: comportamiento no documentado — este escenario queda como riesgo a confirmar, no como caso ejecutable hasta que se resuelva la pregunta crítica sobre "configuración de cashback".

## Exploratory — Pérdida de sesión/cierre de la app durante la espera de aprobación de Apross (48hs)
- Justificación: la confirmación es diferida (48hs); un tester probaría si el usuario recibe la notificación/estado correcto si cierra sesión, desinstala y reinstala la app, o cambia de dispositivo antes de que se resuelva la aprobación.
- AC relacionado: AC1 (etapa posterior al pago exitoso, no cubierta por el escenario base)
- Precondición: pago exitoso con reintegro pendiente de aprobación Apross.
- Pasos: 1) Cerrar sesión o desinstalar la app antes de las 48hs. 2) Volver a ingresar con el mismo usuario luego de que se resuelva la aprobación.
- Resultado esperado a validar: el estado final del reintegro (aprobado/rechazado) debe reflejarse correctamente para el usuario independientemente de estos eventos intermedios.
