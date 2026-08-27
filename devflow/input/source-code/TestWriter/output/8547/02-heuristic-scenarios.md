## Equivalence Partitioning — Pago exitoso con QR Dinámico (clase válida completa)
- AC relacionado: AC1
- Precondición: usuario afiliado activo en Apross; prestador habilitado en BD local; usuario con menos de 3 reintegros usados en el mes; saldo suficiente en cuenta.
- Pasos: 1) Escanear un QR Dinámico desde Home Bezza. 2) Esperar la validación de `AprossService.aprossBenefit`. 3) Verificar pantalla 9.1.1 con mensaje de Reintegro Apross. 4) Presionar "Pagar".
- Resultado esperado: se ejecuta el virtualizador de pago y finaliza en pantalla 9.1.2 - Éxito, con el mensaje "Reintegro en 48hs sujeto a aprobación de apross. Ver Términos y Condiciones."

## Boundary Value Analysis — Primer reintegro del mes (usos = 0)
- AC relacionado: AC1
- Precondición: usuario afiliado activo, prestador habilitado, saldo suficiente, 0 reintegros usados en el mes.
- Pasos: 1) Escanear QR Dinámico. 2) Completar el flujo de pago hasta Éxito.
- Resultado esperado: contador de beneficios se actualiza a `remaining = 3 - 0 - 1 = 2`.

## Boundary Value Analysis — Último reintegro disponible en el mes (usos = 2)
- AC relacionado: AC1
- Precondición: usuario afiliado activo, prestador habilitado, saldo suficiente, 2 reintegros ya usados en el mes (límite de la clase válida "menos de 3").
- Pasos: 1) Escanear QR Dinámico. 2) Completar el flujo de pago hasta Éxito.
- Resultado esperado: contador de beneficios se actualiza a `remaining = 3 - 2 - 1 = 0`.

## State Transition — Secuencia de pantallas del flujo exitoso
- AC relacionado: AC1
- Precondición: todas las precondiciones de AC1 cumplidas.
- Pasos: 1) Desde Home Bezza, escanear QR Dinámico. 2) Verificar transición a pantalla 9.1.1. 3) Presionar "Pagar". 4) Verificar transición a pantalla 9.1.2.
- Resultado esperado: la secuencia de pantallas es Home Bezza → 9.1.1 (Pagar con QR, con mensaje de Reintegro Apross) → 9.1.2 (Éxito), sin pantallas intermedias no documentadas.

## Error Guessing — Doble tap en "Pagar"
- AC relacionado: AC1
- Precondición: todas las precondiciones de AC1 cumplidas, pantalla 9.1.1 visible.
- Pasos: 1) Presionar "Pagar" dos veces consecutivas de forma rápida.
- Resultado esperado: se ejecuta una única transacción y un único decremento del contador de reintegros (no debe duplicarse el reintegro ni el descuento del contador).

## Error Guessing — Pérdida de conectividad durante la virtualización del pago
- AC relacionado: AC1
- Precondición: todas las precondiciones de AC1 cumplidas, virtualizador de pago en ejecución.
- Pasos: 1) Presionar "Pagar". 2) Interrumpir la conexión de red durante la virtualización. 3) Restablecer la conexión.
- Resultado esperado: el sistema no deja el contador de reintegros en un estado inconsistente (ni descontado sin pago confirmado, ni pago confirmado sin descuento); el usuario recibe alguna indicación de que la operación no pudo completarse o debe reintentar.

## Error Guessing — QR Dinámico inválido, corrupto o expirado
- AC relacionado: AC1
- Precondición: usuario afiliado activo, prestador habilitado (si aplica).
- Pasos: 1) Escanear un QR Dinámico inválido, corrupto o expirado desde Home Bezza.
- Resultado esperado: el sistema no debe llegar a mostrar la pantalla 9.1.1 con el mensaje de Reintegro Apross; debe evitar iniciar la validación de `AprossService.aprossBenefit` sobre un QR no procesable.
