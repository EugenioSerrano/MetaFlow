# Análisis de HU 8547 — [APROSS] Pagar con QR - 1.0

## Información explícita
- **Actores**: usuario afiliado a Apross (paga con QR). El rol "Team Analyst" en la narrativa es el autor de la historia, no un actor del sistema.
- **Precondiciones (AC1)**: afiliado activo en Apross; prestador habilitado en BD local; menos de 3 reintegros usados en el mes (RULE_APROSS); QR escaneado es Dinámico; saldo suficiente en cuenta.
- **Postcondición (AC1)**: pantalla 9.1.2 - Éxito; mensaje "Reintegro en 48hs sujeto a aprobación de apross. Ver Términos y Condiciones."; contador actualizado con `remaining = 3 - usos - 1`.
- **Reglas de negocio**: monto fijo de reintegro $4000; tope de 3 reintegros/mes (RULE_APROSS); validación de afiliado activo; validación de prestador habilitado; validación de saldo suficiente; decremento de contador tras éxito; acreditación diferida en 48hs sujeta a aprobación de Apross.
- **Servicio/pantallas**: `AprossService.aprossBenefit`; pantalla 9.1.1 (Pagar con QR) y 9.1.2 (Éxito).
- **Alcance incluido**: QR dinámico, QR estático (monto manual), actualización de contador, mensajes de confirmación, manejo de estados éxito/error según "configuración de cashback".
- **Alcance excluido**: cambios de arquitectura de pagos no relacionados a Apross, reglas de negocio de otros beneficios, permisos de dispositivo.

## Información inferida
- El QR Estático (AC2) requeriría ingreso manual del monto por el usuario (inferido del título "Monto manual"), pero no hay Given/When/Then que lo confirme.
- Existiría una configuración de "cashback" que determina si se aplica o no el beneficio Apross (inferido de la mención en Alcance), pero no está descripta en ningún AC ni regla de negocio.

## Información faltante
- **AC2 completo**: no tiene Given/When/Then; está marcado en la propia HU como "parcialmente documentado... requiere revisión de detalle".
- **Comportamiento cuando NO se cumple alguna precondición de AC1**: afiliado inactivo, prestador no habilitado, límite de 3 reintegros ya alcanzado, saldo insuficiente. La HU no define pantalla, mensaje ni si el pago continúa sin el beneficio o se bloquea.
- **Definición de "configuración de cashback"**: no se documentan sus valores posibles ni qué pantalla/mensaje corresponde a cada estado de éxito/error.
- **Diferencias Android vs. iOS**: el checklist de validación de aceptación pide validar ambas plataformas, pero no hay ningún AC que describa diferencias de comportamiento entre ellas.
- **Flujo posterior al rechazo del reintegro por Apross** (pasadas las 48hs): no se describe si hay notificación, reversión de contador, o algún estado visible para el usuario.
- **Validación/formato del monto manual** en QR estático (depende de que se complete AC2).

## Supuestos (no confirmados)
- Se podría asumir que si no se cumple alguna precondición de AC1, el pago sigue su curso normal sin el beneficio Apross (sin bloquear la transacción), pero esto **no está confirmado** por ningún AC ni regla de negocio — no debe darse por sentado al diseñar pruebas.

## Preguntas abiertas

### Críticas (bloquean el diseño de pruebas)
1. ¿Cuál es el Given/When/Then completo de AC2 (Pago con QR Estático / monto manual)? Sin esto no se puede diseñar cobertura para ese criterio.
2. ¿Qué debe mostrar el sistema cuando falla alguna precondición de AC1 (afiliado inactivo, prestador no habilitado, tope de 3 reintegros alcanzado, saldo insuficiente)? ¿Se bloquea el pago o continúa sin el beneficio?
3. ¿Qué es la "configuración de cashback" mencionada en el alcance, qué valores toma, y qué pantallas/mensajes corresponden a cada estado de éxito/error derivado de ella?

### No críticas
1. ¿Existen diferencias de comportamiento o UI entre Android e iOS para este flujo?
2. ¿Qué ocurre si Apross rechaza el reintegro luego de las 48hs (notificación, reversión de contador, etc.)?

## Evaluación de Acceptance Criteria
- **AC1**: bien formado (Given/When/Then), verificable, pero cubre únicamente el camino feliz. No define contrapartes negativas pese a listar precondiciones que podrían no cumplirse (afiliado inactivo, prestador no habilitado, límite alcanzado, saldo insuficiente).
- **AC2**: incompleto, no verificable en su estado actual — requiere completarse antes de poder diseñar test cases para QR estático.
- No existe ningún AC dedicado al manejo de errores, pese a que tanto el alcance como el checklist de validación lo mencionan explícitamente como parte del trabajo.

---
**Gate**: hay 3 preguntas críticas sin responder (AC2 incompleto, comportamiento ante precondiciones no cumplidas, y definición de "configuración de cashback"). Por diseño del pipeline, el proceso se detiene acá para consultarlas con el QA antes de avanzar a `testing-heuristics`.
