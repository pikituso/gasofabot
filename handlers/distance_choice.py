from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.bot_states import DISTANCIA, CARBURANTE

DISTANCES = ["5", "10", "15", "20", "25", "Personalizada"]

async def ask_distance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[d] for d in DISTANCES]
    await update.message.reply_text(
        "¿Qué distancia máxima quieres buscar? (km)",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

async def set_distance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Personalizada":
        await update.message.reply_text("Escribe la distancia máxima en km (ejemplo: 8):")
        return DISTANCIA
    try:
        distancia = int(text)
        context.user_data["distancia"] = distancia
        await update.message.reply_text(f"Distancia establecida: {distancia} km")

        keyboard = [["Gasolina 95", "Gasolina 98"], ["Diésel"]]
        await update.message.reply_text(
            "¿Qué carburante quieres consultar? ⛽",
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        return CARBURANTE
    except ValueError:
        await update.message.reply_text("Por favor, introduce un número válido.")
        return DISTANCIA