# Gaps de cobertura — HU 8547

## Acceptance Criteria sin test cases asociados
- **AC2 (Pago con QR Estático / monto manual)**: sin Given/When/Then completo en la HU (marcado como "requiere revisión de detalle"). No se pudo diseñar ningún test case. Pregunta crítica pendiente (ver `01-analysis.md`).

## Combinaciones/condiciones relevantes sin cubrir
- **Negative testing de AC1**: comportamiento ante afiliado inactivo, prestador no habilitado, tope de 3 reintegros ya alcanzado, o saldo insuficiente. Bloqueado por pregunta crítica sobre qué debe mostrar el sistema en cada caso (¿bloquea el pago o continúa sin el beneficio?).
- **"Configuración de cashback"**: su interacción con el beneficio Apross no se pudo diseñar como test case ejecutable; quedó documentada como escenario exploratorio bloqueado hasta resolver la pregunta crítica sobre su definición.
- **Diferencias Android vs. iOS**: no crítico, pero el checklist de validación de aceptación de la HU pide probar ambas plataformas sin que haya AC que distinga comportamiento entre ellas.
- **Flujo posterior a un rechazo del reintegro por Apross tras las 48hs**: no crítico, sin documentación sobre notificación o reversión de contador.

## Priorización sugerida
- **Alta**: pago exitoso camino feliz (TC1), doble tap en Pagar (TC5), pérdida de conectividad durante la virtualización (TC6), reutilización del mismo QR (TC9) — impactan directamente la integridad del contador y la no-duplicación de reintegros.
- **Media**: primer/último reintegro del mes (TC2, TC3), secuencia de pantallas (TC4), abandono del flujo antes de pagar (TC10).
- **Baja**: QR inválido/corrupto (TC7), renovación de contador en cambio de mes (TC8), pérdida de sesión durante espera de aprobación (TC11) — riesgos exploratorios, no bloqueantes para un release inmediato.

## Pendiente para completar cobertura total
Antes de considerar esta HU con cobertura completa, se necesita del QA/Analista Funcional/PO:
1. Given/When/Then completo de AC2.
2. Definición del comportamiento del sistema ante cada precondición de AC1 no cumplida.
3. Definición de la "configuración de cashback" y sus estados de éxito/error asociados.
