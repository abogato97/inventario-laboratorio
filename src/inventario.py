import json
import os

RUTA_JSON = os.path.join("data", "equipos.json")

def cargar_equipos():
    """Lee y retorna la lista de equipos desde el archivo JSON."""
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_equipo_bd(nuevo_equipo):
    """Agrega un nuevo equipo al archivo JSON respetando la persistencia."""
    equipos = cargar_equipos()
    
    # Validar que no exista un equipo con el mismo código
    for eq in equipos:
        if eq["codigo"] == nuevo_equipo["codigo"]:
            return False, "El código del equipo ya se encuentra registrado."
            
    equipos.append(nuevo_equipo)
    
    os.makedirs(os.path.dirname(RUTA_JSON), exist_ok=True)
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, indent=4, ensure_ascii=False)
        
    return True, "Equipo registrado con éxito."