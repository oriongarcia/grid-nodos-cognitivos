# Skill: Red de Nodos Cognitivos

## Propósito
Esta skill expone la **arquitectura viva** que hemos construido en el workspace: contexto sensorial, perfiles humanos, base vectorial y protocolo de comunicación adaptativo. Está diseñada para que Tron (yo) responda rápido, genere acciones y mantenga la memoria compartida.

## Comandos sugeridos
1. `nodo contexto` — Describe las variables sensoriales actuales (`00_CONTEXTO_SENSORIAL`).
2. `nodo perfil <Nombre_Apellido>` — Devuelve el perfil resumido y las relaciones relevantes.
3. `nodo vector <palabra>` — Busca en `vector_index.json` y enlaza archivos con el mismo tag.
4. `nodo protocolo` — Explica la regla del Índice de Confianza y cómo adapto el tono.
5. `nodo tareas` — Muestra el tablero (Notion/Sheets) o los proyectos activos y tareas pendientes.
6. `nodo historial <nombre>` — Rescata el resumen de conversaciones almacenadas.

## Integraciones clave
- Carpeta `grid/` → nodos físicos.
- Documentos `documentation/*` → guía del sistema.
- Google Tasks/Calendar → acciones definidas para cada nodo.
- `vector_index.json` → base de datos semántica.

## Flujo básico
1. El usuario pide información (ej. `nodo perfil Ana_Carolina...`).
2. Tron consulta los archivos correspondientes, evalúa el contexto (sensores, emociones, proyectos).
3. Responde con tono adecuado según el protocolo y puede disparar tareas/recordatorios.

## Mantenimiento
- Cada vez que se crea/actualiza un nodo, actualiza `vector_index.json`.
- Mantener `documentation/` sincronizado con cambios operativos.
