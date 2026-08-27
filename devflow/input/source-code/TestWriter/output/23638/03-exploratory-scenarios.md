# Escenarios exploratorios — HU 23638

Estos escenarios fueron comparados contra `02-heuristic-scenarios.md`. No repiten las particiones, límites, transiciones ni el doble toque ya cubiertos allí; exploran secuencias y estados de aplicación adicionales. Los resultados no definidos por la HU se conservan como gaps.

## Exploratory — abandonar el flujo protegido antes de completar la biometría
- Justificación: La navegación hacia atrás o el abandono durante una autenticación puede dejar una sesión protegida parcialmente iniciada o exponer el acceso sin una validación completa.
- AC relacionado: AC2, AC4
- Precondición: Usuario BEC activo en Pantalla 10.1 y acceso a Boleto Educativo Cordobés visible.
- Pasos:
  1. Tocar el acceso a Boleto Educativo Cordobés.
  2. Mientras se muestra la solicitud biométrica, usar el control de cancelar o volver del dispositivo.
  3. Observar la pantalla, el estado del acceso y si queda un QR disponible.
- Resultado esperado: Registrar si el flujo vuelve a una pantalla permitida o queda bloqueado. No debe mostrarse la Pantalla 10.3 ni un QR sin autenticación biométrica exitosa; la navegación exacta posterior no está definida.

## Exploratory — aplicación enviada a segundo plano durante la cuenta regresiva
- Justificación: El cambio de ciclo de vida puede pausar, reiniciar o desincronizar una cuenta regresiva de 90 segundos, afectando la validez del QR mostrado.
- AC relacionado: AC2
- Precondición: QR generado correctamente en Pantalla 10.3 con cuenta regresiva activa.
- Pasos:
  1. Registrar el valor visible de la cuenta regresiva.
  2. Enviar Bezza a segundo plano durante un intervalo observable y volver a abrirla.
  3. Comparar el valor de la cuenta regresiva, el QR y la pantalla mostrada.
- Resultado esperado: Registrar si la cuenta continúa respecto del tiempo transcurrido y si el QR permanece disponible. La HU no define el comportamiento ante segundo plano; no asumir que el contador se reinicia ni que el QR sigue siendo válido.

## Exploratory — cierre forzado y reapertura durante una sesión offline
- Justificación: Un cierre inesperado puede provocar reutilización de datos temporales, pérdida del estado de cupos o acceso al QR sin repetir controles.
- AC relacionado: AC1, AC2, AC4
- Precondición: Usuario BEC activo; ejecutar una vez con la aplicación en Pantalla 10.1 y otra con un QR visible en Pantalla 10.3.
- Pasos:
  1. Cerrar forzadamente Bezza desde cada estado preparado.
  2. Reabrir la aplicación aún sin conexión.
  3. Observar la pantalla inicial, el acceso a BEC Offline, la biometría solicitada y el QR.
- Resultado esperado: Registrar la recuperación de cada estado. No debe darse por válido un acceso protegido ni un QR solo por haber existido antes del cierre; la política de persistencia del estado offline no está definida.

## Exploratory — cambiar la biometría del dispositivo entre sesiones online y offline
- Justificación: La HU exige que el set biométrico no mute; cambiar la configuración del dispositivo entre la sesión online y el uso offline puede revelar si esa condición se valida realmente.
- AC relacionado: AC2
- Precondición: Usuario BEC con datos persistidos y certificado vigente; set biométrico registrado durante la última sesión online.
- Pasos:
  1. Modificar el set biométrico del dispositivo antes de abrir Bezza sin conexión.
  2. Iniciar la sesión offline y acceder a Boleto Educativo Cordobés.
  3. Completar la biometría disponible y observar el resultado.
- Resultado esperado: Registrar la decisión de la validación de mutación. La HU no define mensaje ni navegación para esta condición; no debe generarse QR sin que la validación del set biométrico sea compatible con AC2.

## Exploratory — datos cacheados de una cuenta y usuario autenticado diferente
- Justificación: La dependencia de datos de la última sesión online puede producir exposición de datos o generación con una cuenta distinta si cambia el usuario localmente.
- AC relacionado: AC1, AC2
- Precondición: Dispositivo con datos cacheados de un usuario BEC y posibilidad de iniciar la aplicación con un usuario diferente sin conexión.
- Pasos:
  1. Iniciar la aplicación offline con el usuario diferente.
  2. Observar la elegibilidad mostrada y los datos asociados a la sesión.
  3. Intentar acceder a BEC Offline y completar biometría si el acceso aparece disponible.
- Resultado esperado: Registrar si el sistema vincula los datos cacheados con el usuario autenticado. No debe mostrarse ni generarse un QR con datos de otra cuenta; la política exacta ante la discrepancia no está definida y queda como gap.

## Exploratory — rotación o cambio de hora del dispositivo durante la vigencia
- Justificación: El certificado y la validez del QR dependen del tiempo; una modificación del reloj local puede exponer validaciones basadas solo en hora del dispositivo.
- AC relacionado: AC2
- Precondición: Usuario BEC elegible, certificado vigente y QR generado con cuenta regresiva activa.
- Pasos:
  1. Registrar la hora y el valor visible de la cuenta regresiva.
  2. Cambiar la hora del dispositivo hacia adelante o hacia atrás dentro de un entorno controlado.
  3. Volver a observar el certificado, el QR, el contador y la posibilidad de regeneración.
- Resultado esperado: Registrar cualquier cambio de estado, contador o acceso. La fuente de tiempo y el comportamiento ante alteración del reloj no están definidos; no asumir que la hora local es confiable ni que el QR debe continuar válido.

## Exploratory — orientación y tamaño de pantalla durante la visualización del QR
- Justificación: En mobile, un cambio de orientación o tamaño puede ocultar el QR, truncar la cuenta regresiva o alterar la lectura visual necesaria para transporte.
- AC relacionado: AC2
- Precondición: QR visible en Pantalla 10.3 con cuenta regresiva activa.
- Pasos:
  1. Rotar el dispositivo o cambiar el tamaño disponible si el entorno lo permite.
  2. Observar que el QR, la cuenta regresiva y los controles sigan visibles.
  3. Verificar que la rotación no genere un QR adicional ni reinicie el contador sin indicación.
- Resultado esperado: Registrar la adaptación visual y la conservación del estado. La HU no define soporte de orientación ni respuesta de layout; no asumir un reinicio o una nueva generación.
