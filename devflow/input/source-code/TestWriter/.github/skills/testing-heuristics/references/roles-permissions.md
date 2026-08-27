# Roles & Permissions

Aplica cuando la HU involucra distintos actores/roles con distinto nivel de acceso.

## Cómo aplicarlo
1. Tomá los roles y permisos explícitos en la HU o en `context/roles-permissions.md`.
2. Generá un escenario por rol relevante ejecutando la acción principal de la HU, verificando que el resultado sea el esperado para ese rol (permitido/denegado/con restricciones).
3. Incluí casos de intento de acceso por un rol sin permiso (negativo) y, si aplica, casos de escalamiento o suplantación si la HU lo menciona.
4. Si los roles/permisos no están documentados en la HU ni en `context/`, no los inventes — generá una pregunta abierta en el análisis de HU.