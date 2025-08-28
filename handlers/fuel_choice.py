from telegram import Update
from telegram.ext import ContextTypes
from services.fuel_api import get_gas_stations
from services.geo import safe_coords, haversine
from utils.format import format_station

FUEL_MAP = {
    "Gasolina 95": "Precio Gasolina 95 E5",
    "Gasolina 98": "Precio Gasolina 98 E5",
    "Diésel": "Precio Gasoleo A"
}

async def fuel_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fuel = update.message.text
    lat, lon = context.user_data.get("lat"), context.user_data.get("lon")

    if not lat or not lon:
        await update.message.reply_text("Por favor, envíame primero tu ubicación 📍")
        return

    if fuel not in FUEL_MAP:
        await update.message.reply_text("Carburante no válido ❌")
        return

    fuel_field = FUEL_MAP[fuel]
    estaciones = get_gas_stations()
    resultados = []

    # Filtrar y calcular distancias
    for e in estaciones:
        try:
            tipo_venta = e.get("Tipo Venta", "").strip().lower()
            if tipo_venta not in ("público", "p"):
                continue

            est_lat, est_lon = safe_coords(e)
            distancia = haversine(lat, lon, est_lat, est_lon)

            precio_str = e.get(fuel_field, "").replace(",", ".")
            if not precio_str:
                continue
            precio = float(precio_str)

            resultados.append({
                "estacion": e,
                "distancia": distancia,
                "precio": precio
            })
        except Exception as ex:
            print(f"Error procesando estación: {ex}")
            continue

    # Ordenar por precio
    resultados = sorted(resultados, key=lambda x: x["precio"])
    top = [r for r in resultados if r["distancia"] <= 25][:3]

    if top:
        mensajes = []
        for i, r in enumerate(top, 1):
            mensajes.append(format_station(r["estacion"], r["distancia"], i, fuel_field, fuel))
        await update.message.reply_text(
            "\n\n".join(mensajes),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(f"No encontré gasolineras cercanas con {fuel} 😢")
