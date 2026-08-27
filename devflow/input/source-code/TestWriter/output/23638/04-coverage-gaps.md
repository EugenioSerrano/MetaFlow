# Gaps de cobertura — HU 23638

## Acceptance Criteria sin test cases asociados
- No hay Acceptance Criteria sin casos asociados. AC1, AC2, AC3 y AC4 tienen cobertura en el CSV final.

## Combinaciones/condiciones relevantes sin cubrir
- El comportamiento observable con conectividad disponible y validacion online exitosa no esta definido en la HU.
- No estan definidos el mensaje, estado, navegacion ni politica de reintentos ante error biometrico.
- No esta definido el tratamiento de certificado vencido ni si el limite exacto de 12 horas es inclusivo.
- No esta definido el resultado ante set biometrico mutado.
- No esta definido el resultado ante ausencia o inconsistencia de datos persistidos.
- No estan definidos el mensaje, bloqueo, renovacion o reutilizacion al alcanzar o superar los 2 QRs offline.
- No esta definida la regeneracion de QR ni su relacion con el limite de QRs.
- No esta definido el estado, mensaje o accion del QR al llegar a cero segundos de validez.
- No estan definidos los efectos de cancelar biometria, volver, enviar la app a segundo plano, cerrar forzadamente o cambiar de orientacion.
- No esta definida la fuente de tiempo ni la respuesta a cambios del reloj del dispositivo.
- No esta definido el comportamiento ante perdida de conectividad durante la generacion.
- No estan definidos los controles de vinculacion entre usuario autenticado y datos cacheados de la ultima sesion.
- La trama del QR no especifica campos ni una regla observable de validacion de contenido.
- No hay reglas de roles/permisos ni operaciones CRUD documentadas en `context/`; no se agregaron casos por esas tecnicas.

## Priorizacion sugerida
- Alta: 001, 004, 005, 010, 012, 013, 020.
- Media: 002, 003, 006, 007, 009, 011, 014, 015, 016, 017, 018, 019.
- Baja: 021, 022.

QA autorizo continuar con estos supuestos. Los gaps no deben interpretarse como reglas esperadas ni como defectos hasta que producto defina el comportamiento.
