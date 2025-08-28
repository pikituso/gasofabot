from telegram import Update
from telegram.ext import ContextTypes
from handlers.distance_choice import ask_distance
from handlers.bot_states import DISTANCIA

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    lat, lon = user_location.latitude, user_location.longitude

    # Solo actualizar la ubicación, mantener el resto de datos
    context.user_data["lat"] = lat
    context.user_data["lon"] = lon
    # No resetear la distancia, mantener la que haya
    if "distancia" not in context.user_data:
        context.user_data["distancia"] = 15  # Solo por defecto si no existe

    await ask_distance(update, context)
    return DISTANCIA