# Escenarios exploratorios — HU 138124

> Se revisó `02-heuristic-scenarios.md` antes de proponer estos casos. No se repiten las combinaciones básicas de flag/disponibilidad ni la concurrencia genérica ya cubierta allí.

## Exploratory — Navegación atrás desde el comprobante de límite
- Justificación: La App recibe un Toast condicionado por la respuesta del BFF; la navegación puede provocar duplicación o pérdida visual del mensaje.
- AC relacionado: AC1
- Precondición: Pago exitoso que agotó el disponible y mostró el Toast azul.
- Pasos: Volver desde Resultado Exitoso, regresar al comprobante y observar la pantalla nuevamente.
- Resultado esperado: No se vuelve a acreditar ni actualizar consumo; la presentación del mensaje debe ser consistente con la política de reingreso, que no está explicitada.

## Exploratory — Cierre y reapertura de la App entre respuesta BFF y renderizado
- Justificación: La respuesta puede llegar correctamente pero perderse durante el ciclo de vida móvil.
- AC relacionado: AC1, AC2
- Precondición: Pago completado; cerrar la App inmediatamente antes o durante la presentación del resultado.
- Pasos: Reabrir la App y consultar el comprobante de la operación.
- Resultado esperado: El estado de la operación y el consumo no se duplican ni se pierden; la persistencia esperada del Toast debe confirmarse.

## Exploratory — Cambio de MCC entre configuración y confirmación
- Justificación: El tope se controla por rubro y una inconsistencia de datos podría aplicar el límite al MCC equivocado.
- AC relacionado: AC1, AC2, AC3
- Precondición: Preparar una operación donde el MCC informado en el QR difiera del MCC asociado al comercio/configuración.
- Pasos: Procesar el Pago QR y comparar MCC usado, consumo actualizado y payload.
- Resultado esperado: El BFF utiliza una única fuente consistente para evaluar el MCC y no mezcla consumos entre rubros; la fuente de verdad debe confirmarse.

## Exploratory — Reinicio del Job Batch durante una operación BFF
- Justificación: La HU identifica una vulnerabilidad entre procesamiento en tiempo real y procesos diferidos.
- AC relacionado: AC1, AC2
- Precondición: Pago en ejecución mientras se reinicia o pausa el Job Batch relacionado.
- Pasos: Completar la operación y luego verificar tablas de consumo, deduplicación y respuesta al usuario.
- Resultado esperado: El procesamiento BFF conserva atomicidad e idempotencia y el Job Batch no duplica la acreditación; la coordinación exacta entre ambos procesos debe confirmarse.

## Exploratory — Reintento después de timeout con respuesta desconocida
- Justificación: En pagos, un timeout puede ocultar una operación ya confirmada y provocar un segundo intento.
- AC relacionado: AC1, AC2, AC3
- Precondición: Enviar un pago y provocar timeout después de que el backend pueda haber persistido el resultado.
- Pasos: Consultar el estado y reintentar con el mismo `tx_id`.
- Resultado esperado: El reintento se resuelve idempotentemente y no produce doble acreditación ni doble consumo; se conserva el resultado original cuando corresponda.

## Exploratory — Cambio de mes durante una solicitud en vuelo
- Justificación: El mensaje define renovación el día 1, y una solicitud que cruza el corte puede consumir el período incorrecto.
- AC relacionado: AC1, AC2, AC3
- Precondición: Iniciar una operación inmediatamente antes del cambio mensual y completar el procesamiento después del corte.
- Pasos: Comparar período, disponible, consumo registrado y texto mostrado.
- Resultado esperado: La operación se asigna a un único período de manera determinista; la zona horaria y política de corte requieren confirmación.

## Exploratory — Payload con textos de límite incompletos o alterados
- Justificación: La App muestra textos recibidos del BFF; un campo vacío, truncado o inesperado puede romper el comprobante o mostrar información incorrecta.
- AC relacionado: AC1, AC2
- Precondición: Simular respuesta con `show_limit_reached_message` verdadero y uno de los textos ausente, vacío o con caracteres especiales.
- Pasos: Renderizar la Pantalla de Resultado Exitoso con cada variante.
- Resultado esperado: La App no muestra un mensaje engañoso ni falla; el comportamiento de validación/fallback no está definido y debe confirmarse.
