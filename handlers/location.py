from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    lat, lon = user_location.latitude, user_location.longitude

    # Guardamos la ubicación en el contexto del usuario
    context.user_data["lat"] = lat
    context.user_data["lon"] = lon

    # Botones para elegir carburante
    keyboard = [["Gasolina 95", "Gasolina 98"], ["Diésel"]]
    await update.message.reply_text(
        "¿Qué carburante quieres consultar? ⛽",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

    # Botones para elegir la distancia máxima, pudiendo elegir también distancia personalizada