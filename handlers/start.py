from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.bot_states import DISTANCIA

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = [[KeyboardButton("📍 Enviar ubicación", request_location=True)]]
    await update.message.reply_text(
        "Hola! Envíame tu ubicación para buscar gasolineras cercanas 🚗⛽",
        reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
    )
    return DISTANCIA
