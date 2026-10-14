from src.inventario import guardar_equipo_bd

def registrar_equipo():
    """Maneja la captura de datos por consola e interactúa con la lógica de negocio."""
    print("\n--- REGISTRAR NUEVO EQUIPO ---")
    codigo = input("Ingrese el código: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    tipo = input("Ingrese el tipo (ej. Laptop, Proyector): ").strip()
    estado = input("Ingrese el estado (ej. Disponible, Mantenimiento): ").strip()
    ubicacion = input("Ingrese la ubicación (ej. Lab 1, Estante A): ").strip()
    
    if not codigo or not nombre:
        print("Error: El código y el nombre son campos obligatorios.")
        return
        
    nuevo_equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion
    }
    
    exito, mensaje = guardar_equipo_bd(nuevo_equipo)
    print(f"\n{mensaje}")