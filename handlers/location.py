from telegram import Update
from telegram.ext import ContextTypes
from handlers.distance_choice import ask_distance
from handlers.bot_states import DISTANCIA

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    lat, lon = user_location.latitude, user_location.longitude

    context.user_data["lat"] = lat
    context.user_data["lon"] = lon
    context.user_data["distancia"] = 15  # Por defecto

    await ask_distance(update, context)
    return DISTANCIA