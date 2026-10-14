# Evidencias de Validación del Sistema de Inventario de Laboratorio

Este documento recopila las pruebas de validación funcional y el cumplimiento de las directrices de contexto definidas en [README.md](../README.md) y [AGENTS.md](../AGENTS.md).

---

## 1. Verificación de Reglas y Convenciones (AGENTS.md)

| Criterio evaluado | Estado | Evidencia en el código |
| :--- | :---: | :--- |
| **Uso estricto de `snake_case`** | **Cumple** | Nombres de funciones (`registrar_equipo`, `buscar_equipo`, etc.) y variables (`nuevo_estado`, `codigo`, `ubicacion`) en minúsculas separadas por guiones bajos. |
| **Idioma acordado (Español)** | **Cumple** | Todos los mensajes de interfaz, comentarios, variables y docstrings redactados 100% en español. |
| **Sin dependencias externas** | **Cumple** | Uso exclusivo de librerías nativas de Python (`json`, `os`). |
| **Estructura y responsabilidades** | **Cumple** | Punto de entrada en `main.py`, separación de responsabilidades y firmas sin parámetros preservadas. |
| **Modelo de datos obligatorio** | **Cumple** | Cada activo cuenta obligatoriamente con: `codigo`, `nombre`, `tipo`, `estado`, `ubicacion`. |
| **Documentación (Docstrings)** | **Cumple** | Todas las funciones contienen docstring explicativo describiendo su propósito. |
| **Almacenamiento persistente** | **Cumple** | Datos sincronizados y persistidos en archivo JSON (`data/equipos.json`). |

---

## 2. Matriz de Pruebas Funcionales

### Caso 1: Registrar equipo y validación de unicidad de código
- **Objetivo**: Verificar que se registre un activo correctamente y que no se permitan códigos duplicados ni campos en blanco.
- **Entradas**:
  - Código: `EQ-01`
  - Nombre: `Laptop Dell Latitude`
  - Tipo: `Laptop`
  - Estado: `Disponible`
  - Ubicación: `Lab 1 - Mesa 3`
- **Resultado esperado**: Equipo registrado exitosamente en memoria y persistido en `data/equipos.json`.
- **Prueba de duplicado**: Al intentar registrar nuevamente un equipo con código `EQ-01`, el sistema muestra:  
  `Error: Ya existe un equipo registrado con el código 'EQ-01'.`
- **Estado**: **Aprobado**.

---

### Caso 2: Listar equipos registrados
- **Objetivo**: Visualizar todos los equipos presentes en el inventario.
- **Salida obtenida en consola**:
  ```text
  --- LISTA DE EQUIPOS ---
  [EQ-01] Laptop Dell Latitude | Tipo: Laptop | Estado: Disponible | Ubicación: Lab 1 - Mesa 3
  ```
- **Estado**: **Aprobado**.

---

### Caso 3: Buscar equipo por código
- **Objetivo**: Localizar activos existentes y controlar búsquedas de códigos inexistentes o vacíos.
- **Búsqueda exitosa (`EQ-01`)**:
  ```text
  --- BUSCAR EQUIPO ---
  Ingrese el código a buscar: EQ-01
  Encontrado: [EQ-01] Laptop Dell Latitude | Tipo: Laptop | Estado: Disponible | Ubicación: Lab 1 - Mesa 3
  ```
- **Búsqueda inexistente (`EQ-99`)**:
  ```text
  Equipo no encontrado.
  ```
- **Estado**: **Aprobado**.

---

### Caso 4: Modificar estado de un equipo
- **Objetivo**: Actualizar el estado físico/operativo utilizando únicamente el catálogo de estados válidos (`Disponible`, `En mantenimiento`, `En uso`, `Baja`).
- **Entradas**:
  - Código: `EQ-01`
  - Nuevo estado: `En mantenimiento`
- **Resultado obtenido**:
  ```text
  --- MODIFICAR ESTADO ---
  Ingrese el código del equipo: EQ-01
  Ingrese el nuevo estado (Disponible, En mantenimiento, En uso, Baja): En mantenimiento
  Estado actualizado correctamente.
  ```
- **Estado**: **Aprobado**.

---

### Caso 5: Eliminar equipo
- **Objetivo**: Dar de baja un equipo del inventario y actualizar el almacenamiento.
- **Entradas**: Código `EQ-01`.
- **Resultado obtenido**:
  ```text
  --- ELIMINAR EQUIPO ---
  Ingrese el código del equipo a eliminar: EQ-01
  Equipo eliminado correctamente.
  ```
- **Verificación posterior**: Al listar o buscar `EQ-01`, el sistema confirma que ya no existe en el inventario ni en el archivo JSON.
- **Estado**: **Aprobado**.

---

### Caso 6: Validación de persistencia en `data/equipos.json`
- **Objetivo**: Asegurar que los datos sobrevivan al cierre del programa.
- **Procedimiento**:
  1. Se registró el equipo `EQ-01`.
  2. Se cerró la aplicación seleccionando la opción `0. Salir`.
  3. Se inspeccionó el archivo `data/equipos.json`, verificando la estructura JSON válida:
     ```json
     [
         {
             "codigo": "EQ-01",
             "nombre": "Laptop Dell Latitude",
             "tipo": "Laptop",
             "estado": "En mantenimiento",
             "ubicacion": "Lab 1 - Mesa 3"
         }
     ]
     ```
  4. Se reanudó la ejecución de `main.py` y se listaron los equipos, confirmando la carga automática en memoria.
- **Estado**: **Aprobado**.

---

## 3. Conclusión de la Validación
El sistema cumple al 100% con los requerimientos funcionales descritos en `README.md` y con todas las restricciones de ingeniería de contexto definidas en `AGENTS.md`.
