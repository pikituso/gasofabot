from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers.start import start
from handlers.location import location
from handlers.fuel_choice import fuel_choice

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, location))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fuel_choice))

    print("Bot en marcha 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
