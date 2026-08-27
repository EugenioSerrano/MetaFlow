# Análisis de HU 23638 — [Pago de Transporte] - Boleto Educativo Cordobés - BEC Offline

## Información explícita
- Work Item: `23638`.
- Tipo: `User Story`.
- Proyecto: `Soluciones`.
- Area Path: `Soluciones\Canales\PRD-Billetera\SCT-Billetera`.
- Actor declarado: `Team Analyst Billetera Bezza`.
- La aplicación móvil Bezza debe permitir un flujo de Pagos QR Offline cuando no haya conectividad.
- El acceso al flujo requiere autenticación biométrica.
- El flujo usa datos persistidos, certificados y configuraciones de cuenta guardados durante la última sesión online.
- El alcance funcional declarado incluye generación y regeneración limitada de códigos QR con expiración.
- `AC1`: con usuario BEC activo y validación online fallida en ausencia de conectividad, se inicia sesión offline, se muestra la Pantalla 10.1 - Sin Conexión y el acceso a Pagos QR Offline.
- `AC2`: con biometría exitosa, datos persistidos, certificado vigente, set biométrico sin mutar y cupos disponibles, se genera el QR en la Pantalla 10.3 - QR Transporte con cuenta regresiva.
- `AC3`: si el usuario no es beneficiario BEC activo, se muestra la Pantalla 10.2 - Sin Conexión - usuario sin BEC.
- `AC4`: si falla la autenticación biométrica, el acceso al flujo protegido debe permanecer bloqueado.
- Variables declaradas: `Vigencia_Certificado_Offline` de 12 horas, `Limite_QRs_Offline` por defecto de 2 QRs y `Validez_QR_Segundos` de 90 segundos.
- Confirmaciones de QA: tipo de banca `BI`, plataforma `MB` y funcionalidad para títulos `BEC`.
- QA indicó continuar con la información disponible y aceptar como supuestos los gaps pendientes; estas confirmaciones resuelven las preguntas críticas del gate.

## Información inferida
- La plataforma involucrada parece ser mobile porque la HU menciona una aplicación móvil; esto no alcanza para asignar formalmente el código requerido `MB`.
- La funcionalidad podría describirse como generación de QR de transporte BEC Offline; debe ser confirmada por QA para usarla en títulos.
- La banca no puede inferirse con seguridad a partir de BEC, Bezza o Beneficios Sociales.
- La existencia de Work Items hijos y casos relacionados indica dependencias o cobertura previa, pero sus reglas no fueron consultadas ni deben asumirse.

## Información faltante
- Reglas y mensajes observables para los casos de certificado vencido, set biométrico mutado, ausencia de datos persistidos, cupos agotados, expiración y regeneración, salvo lo que se detalle en los criterios disponibles.
- Criterios completos de aceptación y comportamiento esperado de cada flujo alternativo no visible en la materialización local.
- Actor operativo o rol de usuario final que ejecuta el flujo.

## Supuestos (no confirmados)
- La banca declarada para los casos es `BI`.
- La plataforma declarada para los casos es `MB`.
- La funcionalidad declarada por QA para los títulos es `BEC`.
- Los valores de 12 horas, 2 QRs y 90 segundos son los únicos parámetros de negocio confirmados para el análisis.
- Los comportamientos no definidos explícitamente se mantienen como supuestos aceptados por QA y deben registrarse como gaps, sin inventar reglas ni mensajes.

## Preguntas abiertas
### Críticas resueltas como supuestos aceptados
- QA confirmó banca `BI`, plataforma `MB` y funcionalidad `BEC`.
- QA indicó continuar con la información disponible y aceptar los supuestos/gaps pendientes; no se bloquea el pipeline por los comportamientos no definidos.

### No críticas
- ¿Cuál es el mensaje exacto que debe visualizarse cuando el usuario no es BEC o falla la biometría?
- ¿Qué datos específicos componen la trama del QR y cómo se valida su contenido?
- ¿Qué ocurre al finalizar los 90 segundos de validez y al intentar regenerar un QR?

## Evaluación de Acceptance Criteria
- Los criterios disponibles identifican flujo principal y algunos flujos alternativos, y contienen precondiciones, navegación y varios parámetros verificables.
- AC1, AC2 y AC3 son verificables en términos de conectividad, elegibilidad, pantallas y navegación.
- AC2 combina varias validaciones técnicas y de negocio, pero no define el comportamiento observable cuando cada validación falla.
- AC4 define el bloqueo ante error biométrico, pero no especifica mensaje, cantidad de reintentos, estado de sesión ni navegación resultante.
- No se puede evaluar la cobertura completa porque la materialización local conserva solo los criterios disponibles en la respuesta de sesión y deja explícitamente indicado que existe contenido adicional no visible.

## Estado del gate

**DESBLOQUEADO CON SUPUESTOS ACEPTADOS.** El `Area Path` está resuelto desde la metadata de la HU. QA confirmó banca `BI`, plataforma `MB` y funcionalidad `BEC`, y autorizó continuar con la información disponible. Las preguntas críticas quedan resueltas como supuestos aceptados; los comportamientos no definidos se documentan como gaps y no se convierten en reglas inventadas.