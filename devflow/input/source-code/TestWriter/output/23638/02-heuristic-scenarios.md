# Escenarios heurísticos — HU 23638

Contexto aplicado: HU materializada en `input/23638.md`, análisis actualizado en `01-analysis.md` y contexto de `context/`. Banca `BI`, plataforma `MB`, módulo `HOME` y funcionalidad `BEC` fueron confirmados por QA. Los resultados no definidos se marcan como gap y no se sustituyen por reglas inventadas.

## Equivalence Partitioning — inicio offline con usuario BEC activo
- AC relacionado: AC1
- Precondición: Usuario BEC activo con datos de la última sesión online disponible; dispositivo en `MB` sin conexión a internet.
- Pasos:
  1. Abrir Bezza sin conectividad y observar el resultado de la validación online.
  2. Iniciar la sesión offline con el usuario BEC activo y verificar la pantalla mostrada.
  3. Tocar el botón de acceso a Pagos QR Offline y observar la navegación.
- Resultado esperado: La validación online falla por falta de conexión, la sesión offline se inicia y se muestra la Pantalla 10.1 - Sin Conexión con el acceso a Pagos QR Offline. No debe redireccionar a la pantalla de usuario sin BEC ni omitir el acceso.

## Equivalence Partitioning — inicio offline con usuario sin BEC activo
- AC relacionado: AC3
- Precondición: Dispositivo sin conexión a internet; usuario no beneficiario BEC activo.
- Pasos:
  1. Abrir Bezza sin conectividad.
  2. Intentar iniciar la sesión offline y observar la pantalla de destino.
- Resultado esperado: El sistema detecta que el usuario no es beneficiario BEC activo y redirecciona a la Pantalla 10.2 - Sin Conexión - usuario sin BEC. No debe mostrar el acceso protegido a Boleto Educativo Cordobés como si el usuario fuera elegible.

## Positive / Negative Testing — validación de conectividad para el flujo offline
- AC relacionado: AC1
- Precondición: Usuario BEC activo y datos de sesión persistidos.
- Pasos:
  1. Abrir Bezza con conectividad disponible y observar si se presenta el flujo de contingencia offline.
  2. Repetir la apertura sin conectividad y comparar la navegación.
- Resultado esperado: El flujo descrito por AC1 se activa en ausencia de conexión; con conectividad disponible, el AC no define que deba mostrarse el flujo offline. El comportamiento exacto de la sesión online exitosa queda como gap y no debe asumirse.

## Decision Table — usuario elegible, datos persistidos, certificado vigente, set biométrico sin mutar y cupo disponible
- AC relacionado: AC2
- Precondición: Usuario BEC activo en Pantalla 10.1; biometría del dispositivo disponible; datos persistidos válidos; certificado vigente dentro de `Vigencia_Certificado_Offline` de 12 horas; set biométrico sin mutar; contador de QRs menor que `Limite_QRs_Offline` de 2.
- Pasos:
  1. Tocar el acceso a Boleto Educativo Cordobés.
  2. Completar exitosamente la autenticación biométrica.
  3. Observar las validaciones y la navegación posterior.
  4. Verificar el QR y el contador regresivo en la Pantalla 10.3 - QR Transporte.
- Resultado esperado: Se construye la trama con datos cacheados, se muestra el QR en la Pantalla 10.3 y comienza una cuenta regresiva de 90 segundos según `Validez_QR_Segundos`. No debe mostrar el QR antes de completar la biometría ni omitir la cuenta regresiva.

## Decision Table — usuario elegible con autenticación biométrica fallida
- AC relacionado: AC4
- Precondición: Usuario BEC activo en Pantalla 10.1; datos persistidos disponibles; certificado vigente y cupo disponible; la autenticación biométrica falla.
- Pasos:
  1. Tocar el acceso a Boleto Educativo Cordobés.
  2. Provocar o informar un error en la validación biométrica del dispositivo.
  3. Observar el estado del acceso y la navegación.
- Resultado esperado: El acceso al flujo protegido permanece bloqueado y no se muestra la Pantalla 10.3 ni un QR. El mensaje, cantidad de reintentos y navegación posterior no están definidos y quedan como gap.

## Decision Table — usuario elegible con certificado fuera de vigencia
- AC relacionado: AC2
- Precondición: Usuario BEC activo; datos persistidos disponibles; certificado con antigüedad mayor a `Vigencia_Certificado_Offline` de 12 horas; set biométrico sin mutar y cupo disponible.
- Pasos:
  1. Acceder a Boleto Educativo Cordobés desde la Pantalla 10.1.
  2. Completar la biometría exitosamente.
  3. Observar el resultado de la validación del certificado y la pantalla resultante.
- Resultado esperado: La HU exige validar la vigencia del certificado, pero no define el mensaje, estado ni navegación cuando está vencido. Registrar el resultado real para completar la regla; no debe considerarse exitoso sin validar el certificado.

## Decision Table — usuario elegible con set biométrico mutado
- AC relacionado: AC2
- Precondición: Usuario BEC activo; datos persistidos y certificado vigente; set biométrico mutado respecto de la última sesión; cupo disponible.
- Pasos:
  1. Acceder a Boleto Educativo Cordobés desde la Pantalla 10.1.
  2. Completar la autenticación biométrica del dispositivo.
  3. Observar el resultado de la validación del set biométrico y la navegación.
- Resultado esperado: La HU exige validar que el set biométrico no haya mutado, pero no define el comportamiento observable cuando mutó. Registrar el resultado real como gap; no debe asumirse que se genera un QR.

## Equivalence Partitioning — datos persistidos disponibles versus ausentes
- AC relacionado: AC2
- Precondición: Usuario BEC activo; dispositivo offline; preparar una ejecución con datos cacheados y otra sin datos cacheados.
- Pasos:
  1. En la ejecución con datos cacheados, abrir BEC Offline y completar la biometría.
  2. Verificar si la trama se construye con los datos persistidos.
  3. Repetir la ejecución sin datos persistidos y completar la biometría.
  4. Observar la pantalla resultante y el estado del flujo.
- Resultado esperado: Con datos cacheados, la trama usa esos datos conforme a AC2. Para datos ausentes, la HU no define mensaje ni navegación; registrar el gap y no generar QR basándose en datos inventados.

## Boundary Value Analysis — vigencia del certificado offline
- AC relacionado: AC2
- Precondición: Usuario BEC activo, datos persistidos, set biométrico sin mutar y cupo disponible; disponer de certificados con antigüedad inmediatamente menor, igual y mayor a 12 horas.
- Pasos:
  1. Ejecutar el acceso con certificado dentro de 12 horas y completar biometría.
  2. Repetir con certificado en el límite de 12 horas.
  3. Repetir con certificado fuera del límite de 12 horas.
  4. Observar validación, navegación y disponibilidad del QR en cada ejecución.
- Resultado esperado: La vigencia se evalúa contra `Vigencia_Certificado_Offline = 12 horas`. El tratamiento observable exacto del límite y del certificado vencido no está documentado; registrar esos resultados como gap y no asumir inclusión o exclusión del límite.

## Boundary Value Analysis — límite de QRs offline
- AC relacionado: AC2
- Precondición: Usuario BEC activo; certificado vigente, datos persistidos y set biométrico sin mutar; contador de usos disponible en 0, 1 y 2 QRs generados.
- Pasos:
  1. Generar un QR con contador 0 y verificar el resultado.
  2. Generar un QR adicional con contador 1 y verificar el resultado.
  3. Intentar generar o regenerar otro QR con contador 2.
  4. Observar contador, acceso al QR y comportamiento de la acción posterior al límite.
- Resultado esperado: El parámetro `Limite_QRs_Offline` tiene valor por defecto 2 y los dos primeros usos deben evaluarse como disponibles según AC2. El comportamiento al alcanzar o superar el límite, incluido mensaje y regeneración, no está definido; registrar el gap y no asumir si se bloquea, se reutiliza o se renueva el cupo.

## Boundary Value Analysis — validez temporal del QR
- AC relacionado: AC2
- Precondición: QR generado correctamente en Pantalla 10.3.
- Pasos:
  1. Observar la cuenta regresiva al generarse el QR.
  2. Verificar el valor inicial esperado de `Validez_QR_Segundos = 90`.
  3. Observar el estado en el instante previo, en el límite y después de 90 segundos.
- Resultado esperado: Se muestra una cuenta regresiva asociada a una validez de 90 segundos. La pantalla, validez efectiva y acción sobre el QR después de cero segundos no están definidas; registrar el gap y no asumir una transición o mensaje.

## State Transition Testing — sesión offline hacia pantalla de sin conexión
- AC relacionado: AC1, AC3
- Precondición: Aplicación abierta sin conexión; preparar usuario BEC activo y usuario sin BEC activo.
- Pasos:
  1. Iniciar la sesión offline con el usuario BEC activo.
  2. Verificar la transición a Pantalla 10.1 - Sin Conexión y la disponibilidad del acceso QR Offline.
  3. Repetir con el usuario sin BEC activo.
  4. Verificar la transición a Pantalla 10.2 - Sin Conexión - usuario sin BEC.
- Resultado esperado: La transición depende de la elegibilidad declarada: usuario BEC a Pantalla 10.1 y usuario sin BEC a Pantalla 10.2. No debe intercambiarse el destino.

## State Transition Testing — acceso protegido hacia QR Transporte
- AC relacionado: AC2, AC4
- Precondición: Usuario BEC activo en Pantalla 10.1.
- Pasos:
  1. Seleccionar Boleto Educativo Cordobés.
  2. En una ejecución, completar biometría exitosamente con las condiciones de AC2.
  3. En otra ejecución, producir un error biométrico.
  4. Observar la transición en ambos resultados.
- Resultado esperado: Con validaciones exitosas se transiciona a Pantalla 10.3 - QR Transporte; con error biométrico el acceso permanece bloqueado. No debe mostrarse un QR en la ejecución fallida.

## Error Guessing — doble toque en generación o regeneración
- AC relacionado: AC2
- Precondición: Usuario BEC activo, validaciones exitosas y un cupo disponible.
- Pasos:
  1. Tocar dos veces rápidamente el control de generación o regeneración de QR.
  2. Observar la cantidad de QRs generados, el contador de cupo, la navegación y la cuenta regresiva.
- Resultado esperado: Registrar si se genera una sola operación o más de una. La HU no define la política de doble toque; no asumir consumo adicional ni duplicación como comportamiento esperado.

## Error Guessing — pérdida de conectividad durante la generación
- AC relacionado: AC1, AC2
- Precondición: Usuario BEC activo en Pantalla 10.1, datos offline válidos y flujo de autenticación iniciado.
- Pasos:
  1. Iniciar el acceso a Boleto Educativo Cordobés.
  2. Completar biometría mientras se interrumpe o se mantiene la ausencia de conexión.
  3. Observar si la generación usa datos locales, muestra un error o cambia de pantalla.
- Resultado esperado: La HU contempla el flujo sin conexión y datos cacheados, pero no define una interrupción adicional durante la generación. Registrar el comportamiento y el gap; no debe asumirse una consulta online ni datos nuevos.
