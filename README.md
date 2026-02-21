# Skill Red de Nodos Cognitivos

Este paquete empaqueta la arquitectura completa (sensores, perfiles, vector db, protocolo de tono) como una skill reutilizable dentro de OpenClaw.

## Estructura
- `documents/` → resúmenes clave (estado, tablero, vectores, protocolo).
- `scripts/` → helpers: listar nodos, generar vista rápida y añadir embeddings.
- `SKILL.md` → descripción principal (ya creada). No olvides mantenerla sincronizada.

## Instalación recomendada
1. Copia esta carpeta bajo `skills/` del otro agente. Mantén ruta `skills/nodos-cognitivos`.
2. Ajusta los paths `nodos-cognitivos/` si el workspace tiene otra raíz.
3. Ejecuta `npm`/`python` según los scripts para generar reportes.

## Uso
- Fija el `SKILL.md` como guía de comando.
- Usa los documentos para refrescar y exportar.
- Para alimentar un vector, añade la entrada al `vector_index.json` con `embedding` desde tu modelo favorito.

## Créditos
Diseñado y construido por **Orión García Sequera** (Ingeniero en Sistemas, responsable técnico) y **Ana Carolina Guerra Rodríguez** (Psicóloga, arquitecta del protocolo humano). Ana aportó el conocimiento emocional y de relación humana; Orión estructuró la arquitectura técnica y las integraciones. Mantén los archivos `documentation/credits.md` y `nodos-cognitivos/00-README.md` actualizados con estos nombres para que la autoría viaje con la Skill.
