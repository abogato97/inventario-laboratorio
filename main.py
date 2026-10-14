import json
import os

# Ruta al archivo de almacenamiento persistente
RUTA_ARCHIVO_DATOS = os.path.join(os.path.dirname(__file__), "data", "equipos.json")


def cargar_datos():
    """Carga los equipos almacenados desde el archivo JSON al inventario en memoria."""
    if not os.path.exists(RUTA_ARCHIVO_DATOS):
        return []
    try:
        with open(RUTA_ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except (json.JSONDecodeError, OSError):
        return []


def guardar_datos():
    """Guarda el inventario actual en el archivo JSON de forma persistente."""
    os.makedirs(os.path.dirname(RUTA_ARCHIVO_DATOS), exist_ok=True)
    with open(RUTA_ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


# Lista en memoria para almacenar los equipos (inicializada desde el archivo JSON)
inventario = cargar_datos()

# Catálogo de estados válidos permitidos para los equipos
ESTADOS_VALIDOS = ["Disponible", "En mantenimiento", "En uso", "Baja"]


def solicitar_campo_no_vacio(mensaje):
    """Solicita un dato por consola y valida que no se encuentre vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío. Intente nuevamente.")


def solicitar_estado(mensaje="Estado"):
    """Solicita y valida que el estado pertenezca al catálogo permitido."""
    opciones = ", ".join(ESTADOS_VALIDOS)
    while True:
        estado_ingresado = input(f"{mensaje} ({opciones}): ").strip()
        for estado in ESTADOS_VALIDOS:
            if estado_ingresado.lower() == estado.lower():
                return estado
        print(f"Error: Estado no válido. Debe ser uno de los siguientes: {opciones}.")


def registrar_equipo():
    """Registra un nuevo equipo en el inventario solicitando sus datos obligatorios y verificando unicidad."""
    print("\n--- REGISTRAR EQUIPO ---")
    codigo = solicitar_campo_no_vacio("Código: ")

    # Validación de unicidad de código
    for eq in inventario:
        if eq["codigo"].lower() == codigo.lower():
            print(f"Error: Ya existe un equipo registrado con el código '{codigo}'.")
            return

    nombre = solicitar_campo_no_vacio("Nombre: ")
    tipo = solicitar_campo_no_vacio("Tipo (ej. Laptop, Proyector): ")
    estado = solicitar_estado("Estado")
    ubicacion = solicitar_campo_no_vacio("Ubicación (ej. Lab 1, Estante B): ")

    equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion
    }

    inventario.append(equipo)
    guardar_datos()
    print("¡Equipo registrado con éxito!")


def listar_equipos():
    """Muestra en consola la lista completa de equipos registrados en el inventario."""
    print("\n--- LISTA DE EQUIPOS ---")
    if not inventario:
        print("No hay equipos registrados.")
        return

    for eq in inventario:
        print(f"[{eq['codigo']}] {eq['nombre']} | Tipo: {eq['tipo']} | Estado: {eq['estado']} | Ubicación: {eq['ubicacion']}")


def buscar_equipo():
    """Busca un equipo en el inventario por su código y muestra su información detallada."""
    print("\n--- BUSCAR EQUIPO ---")
    codigo = solicitar_campo_no_vacio("Ingrese el código a buscar: ")

    for eq in inventario:
        if eq['codigo'].lower() == codigo.lower():
            print(f"Encontrado: [{eq['codigo']}] {eq['nombre']} | Tipo: {eq['tipo']} | Estado: {eq['estado']} | Ubicación: {eq['ubicacion']}")
            return
    print("Equipo no encontrado.")


def modificar_estado():
    """Permite actualizar el estado de un equipo existente especificando su código."""
    print("\n--- MODIFICAR ESTADO ---")
    codigo = input("Ingrese el código del equipo: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    for eq in inventario:
        if eq['codigo'].lower() == codigo.lower():
            nuevo_estado = solicitar_estado("Ingrese el nuevo estado")
            eq['estado'] = nuevo_estado
            guardar_datos()
            print("Estado actualizado correctamente.")
            return
    print("Equipo no encontrado.")


def eliminar_equipo():
    """Elimina un equipo del inventario a partir de su código."""
    print("\n--- ELIMINAR EQUIPO ---")
    codigo = input("Ingrese el código del equipo a eliminar: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    for eq in inventario:
        if eq['codigo'].lower() == codigo.lower():
            inventario.remove(eq)
            guardar_datos()
            print("Equipo eliminado correctamente.")
            return
    print("Equipo no encontrado.")


def main():
    """Función principal que ejecuta el ciclo interactivo del menú de consola."""
    while True:
        print("\n==================================")
        print("  SISTEMA DE GESTIÓN DE LABORATORIO")
        print("==================================")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo")
        print("4. Modificar estado")
        print("5. Eliminar equipo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            modificar_estado()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()