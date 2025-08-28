def format_station(estacion, distancia, idx, fuel_field, fuel_name):
    nombre = estacion.get("Rótulo", "Desconocido").title()
    direccion = estacion.get("Dirección", "")
    poblacion = estacion.get("Municipio", "")
    est_lat = estacion.get("Latitud", "").replace(",", ".")
    est_lon = estacion.get("Longitud (WGS84)", "").replace(",", ".")

    precio_raw = estacion.get(fuel_field, "")
    precio = precio_raw.replace(",", ".") if precio_raw else "N/D"

    return (
        f"*{idx}. {nombre}*\n"
        f"📍 {direccion}, {poblacion}\n"
        f"🚗 {distancia:.1f} km\n"
        f"⛽ {fuel_name}: {precio} €\n"
        f"[Ver en Google Maps](https://www.google.com/maps/search/?api=1&query={est_lat},{est_lon})"
    )
