from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from config import TOKEN
from handlers.start import start
from handlers.location import location
from handlers.fuel_choice import fuel_choice
from handlers.distance_choice import ask_distance, set_distance
from handlers.bot_states import DISTANCIA, CARBURANTE

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            DISTANCIA: [
                MessageHandler(filters.LOCATION, location),
                MessageHandler(filters.TEXT & ~filters.COMMAND, set_distance),
            ],
            CARBURANTE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, fuel_choice),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    app.add_handler(conv_handler)

    print("Bot en marcha 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
