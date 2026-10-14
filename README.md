# Sistema de Inventario de Laboratorio

## 1. Descripción

Aplicación en consola para la gestión y control de los equipos tecnológicos pertenecientes al laboratorio. Permite registrar, consultar, actualizar y eliminar la información de los activos de forma organizada.

## 2. Objetivo

Centralizar la administración de los equipos del laboratorio para optimizar el seguimiento de su disponibilidad, estado y ubicación física.

## 3. Usuarios

- Encargados y administradores del laboratorio.
- Personal técnico responsable del mantenimiento de equipos.

## 4. Funcionalidades

- Registrar equipo
- Listar equipos
- Buscar equipo
- Modificar estado
- Eliminar equipo
- Salir del sistema

## 5. Información de los equipos

Cada equipo contiene los siguientes campos (todos obligatorios):

- codigo: Identificador único del equipo (no permite duplicados).
- nombre: Nombre descriptivo del activo.
- tipo: Categoría del equipo (ej. Laptop, Proyector).
- estado: Situación operativa (valores válidos: Disponible, En mantenimiento, En uso, Baja).
- ubicacion: Ubicación física en el laboratorio (ej. Lab 1, Estante B).

## 6. Tecnologías

Lenguaje: Python 3

Almacenamiento: Archivo JSON (`data/equipos.json`) sincronizado en memoria usando la librería nativa `json`.

## 7. Estructura del proyecto

```text
inventario-laboratorio/
├── data/
│   └── equipos.json
├── evidencias/
│   └── validacion.md
├── src/
│   └── inventario.py
├── main.py
├── README.md
└── AGENTS.md
```
## 8. Ejecución

1. Abrir la terminal en la carpeta raíz del proyecto.
2. Ejecutar el siguiente comando:

```bash
python main.py
