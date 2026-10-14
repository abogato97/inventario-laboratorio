# Reglas para agentes de IA

## 1. Lenguaje

- El proyecto está desarrollado en Python 3.
- Todo el código, comentarios, mensajes de la consola e interfaz deben estar redactados estrictamente en español.

## 2. Convenciones de nombres

- Utilizar `snake_case` para nombres de variables, parámetros y funciones (ej. `registrar_equipo`, `codigo_equipo`).
- El modelo base se estructura con diccionarios. Se reservará `PascalCase` para clases únicamente si se solicita explícitamente programar con POO (ej. `EquipoLaboratorio`).
- Usar nombres claros y descriptivos en español para todas las entidades.

## 3. Organización del código

- El punto de entrada principal debe ser el archivo `main.py`.
- Mantener una estructura modular simple y legible.
- Las funciones obligatorias gestionan el menú de interactividad en consola y pueden apoyarse en funciones dedicadas para lógica de validación y persistencia.

## 4. Funciones

- El sistema debe implementar exactamente las siguientes funciones obligatorias:
  1. `registrar_equipo()`
  2. `listar_equipos()`
  3. `buscar_equipo()`
  4. `modificar_estado()`
  5. `eliminar_equipo()`
- Cada función debe realizar únicamente una tarea específica de manera limpia y modular, conservando su firma sin parámetros para compatibilidad con el menú.

## 5. Datos

- Almacenamiento: Archivo JSON (`data/equipos.json`) sincronizado en memoria mediante listas y diccionarios con la biblioteca nativa `json`.
- Cada objeto de equipo debe incluir obligatoriamente los campos:
  - `codigo`
  - `nombre`
  - `tipo`
  - `estado`
  - `ubicacion`

## 6. Restricciones

- No utilizar librerías o dependencias externas no autorizadas; priorizar las librerías nativas de Python.
- No duplicar funciones ni alterar la firma de funciones existentes.
- Evitar cambios innecesarios o reescrituras globales en archivos que ya funcionan correctamente.

## 7. Modificación del código

- Toda modificación sugerida por la IA debe ser incremental y preservar las funciones de trabajo previas.
- Respetar siempre las convenciones de nombres e idioma fijados por el equipo.

## 8. Procedimiento antes de realizar cambios

- Analizar y leer previamente la estructura de archivos (`README.md` y `AGENTS.md`).
- Explicar brevemente los cambios antes de proponer o aplicar modificaciones en el código fuente.

## 9. Documentación

- Todas las funciones deben incluir docstring.
- El docstring debe describir brevemente el propósito de la función.
