# Escenarios heurísticos — HU 138124

> Se continúa con los AC recuperados (AC1-AC3). Los resultados no definidos por la HU se marcan como "a confirmar" y también quedan registrados en los gaps.

## Equivalence Partitioning — Feature Flag encendida y transacción agota el tope
- AC relacionado: AC1
- Precondición: Feature Flag de topes encendida; usuario y operación con datos válidos; el reintegro consume exactamente el disponible mensual del MCC.
- Pasos: Ejecutar un Pago con QR y consultar la respuesta del BFF y las tablas de consumo/deduplicación.
- Resultado esperado: El cálculo se realiza con BigDecimal escala 2; se actualiza el consumo de forma atómica y la deduplicación por `tx_id`; `show_limit_reached_message` es `true`; se devuelven exactamente el título y cuerpo definidos; la App muestra el Toast azul en Resultado Exitoso.

## Equivalence Partitioning — Feature Flag encendida y queda disponible positivo
- AC relacionado: AC2
- Precondición: Feature Flag encendida; el reintegro deja disponible mensual mayor a cero.
- Pasos: Ejecutar un Pago con QR y revisar BFF y App.
- Resultado esperado: El consumo se actualiza atómicamente; `show_limit_reached_message` es `false`; no se envían los textos de límite; la App muestra la confirmación sin banner/Toast de límite.

## Equivalence Partitioning — Disponible cero antes de la transacción
- AC relacionado: AC3
- Precondición: Feature Flag encendida; disponible del MCC igual a cero antes del pago.
- Pasos: Ejecutar un Pago con QR y consultar estado de operación, consumo y respuesta.
- Resultado esperado: El BFF registra la denegación por tope y deriva al flujo de pago tradicional. Código, payload y mensaje final quedan sujetos al criterio incompleto de la HU.

## Equivalence Partitioning — Feature Flag apagada
- AC relacionado: AC1, AC2, AC3
- Precondición: Feature Flag de topes apagada; repetir una operación con disponible agotado y otra con disponible positivo.
- Pasos: Ejecutar ambos Pagos con QR y revisar BFF, consumo y App.
- Resultado esperado: A confirmar: la HU menciona el estado apagado pero no define si se omite el control, se conserva el flujo legacy ni qué payload debe devolver.

## Boundary Value Analysis — Disponible mensual exacto agotado
- AC relacionado: AC1
- Precondición: Disponible igual al reintegro calculado, con precisión de dos decimales.
- Pasos: Ejecutar el pago que consume el importe exacto restante.
- Resultado esperado: El disponible queda en cero sin desvío de precisión; se comporta como AC1 y muestra el mensaje de límite alcanzado.

## Boundary Value Analysis — Disponible mayor que cero por el menor margen representable
- AC relacionado: AC2
- Precondición: Disponible posterior al cálculo mayor que cero por el menor margen representable a escala 2.
- Pasos: Ejecutar el pago y consultar respuesta y consumo.
- Resultado esperado: Se clasifica como disponible restante positivo; `show_limit_reached_message` es `false` y no se envían textos de límite.

## Boundary Value Analysis — Disponible cero antes del pago
- AC relacionado: AC3
- Precondición: Disponible exactamente igual a cero antes de iniciar la operación.
- Pasos: Ejecutar el Pago con QR.
- Resultado esperado: Se registra la denegación por tope y se deriva al flujo tradicional; no se debe acreditar un reintegro ni incrementar el consumo. El resultado del pago debe confirmarse con el PO porque el AC está incompleto.

## Boundary Value Analysis — Reintegro con más de dos decimales
- AC relacionado: AC1, AC2
- Precondición: Configurar una operación cuyo cálculo intermedio requiera redondeo.
- Pasos: Ejecutar el pago y comparar cálculo, consumo persistido y respuesta del BFF.
- Resultado esperado: A confirmar: el sistema debe usar BigDecimal escala 2 y no introducir desvíos, pero la regla exacta de redondeo no está documentada.

## Decision Table — Combinaciones principales de flag y disponibilidad
- AC relacionado: AC1, AC2, AC3
- Precondición: Preparar operaciones con flag encendida/apagada y disponibilidad: positiva, exacta agotada y cero previa.
- Pasos: Ejecutar una prueba por cada combinación definida en la matriz: ON+positivo; ON+agotado; ON+cero previo; OFF+positivo; OFF+agotado; OFF+cero previo.
- Resultado esperado: ON+positivo sigue AC2; ON+agotado sigue AC1; ON+cero previo sigue AC3; los resultados de las tres combinaciones OFF deben confirmarse porque no están descritos.

## State Transition Testing — Pago exitoso con agotamiento del tope
- AC relacionado: AC1
- Precondición: Operación nueva, flag encendida y reintegro que agota el disponible.
- Pasos: Iniciar Pago QR, completar procesamiento BFF y observar Resultado Exitoso.
- Resultado esperado: La operación transiciona al resultado exitoso; el consumo queda actualizado una sola vez y el Toast se muestra en la pantalla final.

## State Transition Testing — Pago con disponible cero deriva al flujo tradicional
- AC relacionado: AC3
- Precondición: Operación nueva, flag encendida y disponible cero previo.
- Pasos: Iniciar Pago QR y seguir la derivación informada por el BFF.
- Resultado esperado: Se registra la denegación por tope y la operación transiciona al flujo tradicional; no se muestra el Toast de consumo total salvo que el AC completo lo indique.

## Positive/Negative Testing — Consumo atómico y deduplicación
- AC relacionado: AC1, AC2
- Precondición: Operación nueva con `tx_id` único y configuración válida.
- Pasos: Ejecutar el pago y revisar las tres tablas involucradas.
- Resultado esperado: Caso positivo: se registra consumo y deduplicación coherentes. Caso negativo: ante una repetición del mismo `tx_id`, no debe generarse doble acreditación ni doble consumo; el contrato de respuesta idempotente queda a confirmar.

## Error Guessing — Doble envío de la operación
- AC relacionado: AC1, AC2, AC3
- Precondición: Pantalla de pago lista con una operación válida.
- Pasos: Enviar la acción de pago dos veces rápidamente o reintentar la misma petición.
- Resultado esperado: No se duplica la acreditación, el consumo ni el registro lógico de la operación; el comportamiento exacto de la segunda respuesta queda a confirmar.

## Error Guessing — Fallo de red durante la actualización
- AC relacionado: AC1, AC2, AC3
- Precondición: Pago en ejecución con flag encendida.
- Pasos: Interrumpir la conectividad durante el procesamiento atómico y restaurarla antes de reintentar.
- Resultado esperado: No queda una combinación inconsistente de acreditación y consumo; la operación debe ser recuperable o informarse como fallida según el contrato aún no documentado.

## Error Guessing — Lectura concurrente del mismo disponible
- AC relacionado: AC1, AC2, AC3
- Precondición: Dos solicitudes válidas del mismo usuario/MCC con disponibilidad cercana al límite.
- Pasos: Ejecutar ambas solicitudes en paralelo con `tx_id` distintos.
- Resultado esperado: El bloqueo/versionado impide sobreconsumo; cada operación recibe un resultado coherente con el disponible real. La política exacta para la segunda solicitud debe confirmarse.
