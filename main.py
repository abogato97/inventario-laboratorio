# Lista en memoria para almacenar los equipos (se pueden guardar como diccionarios)
inventario = []

def registrar_equipo():
    print("\n--- REGISTRAR EQUIPO ---")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    tipo = input("Tipo (ej. Laptop, Proyector): ")
    estado = input("Estado (ej. Disponible, En mantenimiento): ")
    ubicacion = input("Ubicación (ej. Lab 1, Estante B): ")
    
    equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion
    }
    
    inventario.append(equipo)
    print("¡Equipo registrado con éxito!")

def listar_equipos():
    print("\n--- LISTA DE EQUIPOS ---")
    if not inventario:
        print("No hay equipos registrados.")
        return
    
    for eq in inventario:
        print(f"[{eq['codigo']}] {eq['nombre']} | Tipo: {eq['tipo']} | Estado: {eq['estado']} | Ubicación: {eq['ubicacion']}")

def buscar_equipo():
    print("\n--- BUSCAR EQUIPO ---")
    codigo = input("Ingrese el código a buscar: ")
    for eq in inventario:
        if eq['codigo'] == codigo:
            print(f"Encontrado: {eq['nombre']} - Estado: {eq['estado']} - Ubicación: {eq['ubicacion']}")
            return
    print("Equipo no encontrado.")

def modificar_estado():
    print("\n--- MODIFICAR ESTADO ---")
    codigo = input("Ingrese el código del equipo: ")
    for eq in inventario:
        if eq['codigo'] == codigo:
            nuevo_estado = input("Ingrese el nuevo estado: ")
            eq['estado'] = nuevo_estado
            print("Estado actualizado correctamente.")
            return
    print("Equipo no encontrado.")

def eliminar_equipo():
    print("\n--- ELIMINAR EQUIPO ---")
    codigo = input("Ingrese el código del equipo a eliminar: ")
    for eq in inventario:
        if eq['codigo'] == codigo:
            inventario.remove(eq)
            print("Equipo eliminado correctamente.")
            return
    print("Equipo no encontrado.")

def main():
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