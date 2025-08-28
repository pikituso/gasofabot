import math

def parse_coord(value: str) -> float:
    """
    Convierte coordenadas del ministerio a float.
    Limpia espacios y cambia coma por punto.
    """
    try:
        return float(value.strip().replace(",", "."))
    except:
        raise ValueError(f"Coordenada inválida: {value}")

def haversine(lat1, lon1, lat2, lon2) -> float:
    """
    Calcula distancia en km entre dos coordenadas (lat/lon) usando la fórmula Haversine.
    """
    R = 6371  # radio de la Tierra en km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def safe_coords(estacion: dict):
    try:
        lat = float(estacion.get("Latitud", "0").strip().replace(",", "."))
        lon = float(estacion.get("Longitud (WGS84)", "0").strip().replace(",", "."))
        if lat == 0 or lon == 0:
            raise ValueError("Coordenadas no válidas")
        return lat, lon
    except:
        raise ValueError(f"Coordenadas inválidas: {estacion.get('Rótulo','')}")
