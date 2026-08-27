# Configuracion QA para diseno de pruebas

Este archivo contiene valores de respaldo para el diseño de pruebas. El pipeline debe tomar primero los valores explícitos de la HU y detenerse con una pregunta crítica solo si no encuentra un valor requerido ni en la HU ni en este archivo.

## Area Path

- Area Path de respaldo: 

El valor debe ser el nombre completo y exacto que espera Azure DevOps, por ejemplo `Soluciones\TRB-CashManagement\PRD-VALORES`.

La fuente principal es el campo `area_path` del front matter de `input/<id>.md`. También puede reconocerse el campo `Área` o `Area` cuando la HU materializada use ese formato. Este valor solo se utiliza como fallback si la HU no contiene un Area Path.

## Contexto de ejecucion

Cada HU debe declarar las combinaciones aplicables. No se deben generar combinaciones automaticamente ni asumir valores.

- Tipo de Banca permitido: `BE` (Banca Empresa) o `BI` (Banca Individuo)
- Plataforma de Prueba permitida: `MB` (mobile) o `WB` (web/desktop)
- Modulo fijo de la nomenclatura: `HOME`

## Metadata requerida por HU

La HU o una respuesta explicita de QA debe indicar:

- Tipo de Banca: `BE` o `BI`
- Plataforma de Prueba: `MB` o `WB`
- Funcionalidad para el titulo

Si una HU aplica a mas de una combinacion de banca y plataforma, QA debe enumerarlas expresamente. El caso se genera solo para las combinaciones declaradas.
