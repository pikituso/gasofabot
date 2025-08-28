from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.bot_states import DISTANCIA, CARBURANTE
from handlers.distance_choice import ask_distance

async def handle_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    choice = query.data
    
    if choice == "change_location":
        # Pedir nueva ubicación
        button = [[KeyboardButton("📍 Enviar ubicación", request_location=True)]]
        await query.message.reply_text(
            "Envíame tu nueva ubicación 📍",
            reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
        )
        return DISTANCIA
        
    elif choice == "change_radius":
        # Pedir nueva distancia
        await ask_distance(update, context)
        return DISTANCIA
        
    elif choice == "change_fuel":
        # Pedir nuevo carburante
        keyboard = [["Gasolina 95", "Gasolina 98"], ["Diésel"]]
        await query.message.reply_text(
            "¿Qué carburante quieres consultar? ⛽",
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        return CARBURANTE