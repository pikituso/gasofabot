def format_station(estacion, distancia, precio, orden, fuel_name):
    direccion = estacion.get("Dirección", "Sin dirección")
    municipio = estacion.get("Municipio", "")
    provincia = estacion.get("Provincia", "")
    nombre = estacion.get("Rótulo", "")
    lat = estacion.get("Latitud", None).replace(",", ".")
    lon = estacion.get("Longitud (WGS84)", None).replace(",", ".")
    precio_str = precio if precio == "N/D" else f"{precio} €"
    maps_url = ""
    if lat and lon:
        maps_url = f"[Ver en Google Maps](https://www.google.com/maps/search/?api=1&query={lat},{lon})"
    return (
        f"*{orden}. {nombre}*\n"
        f"📍 _{direccion}, {municipio}, {provincia}_\n"
        f"🚗 Distancia: {distancia:.2f} km\n"
        f"⛽ {fuel_name}: {precio_str}\n"
        f"{maps_url}"
    )
