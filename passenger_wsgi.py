# /home/gasofabot/www/passenger_wsgi.py - OPCIONAL
from flask import Flask
application = Flask(__name__)

@application.route('/')
def home():
    return "Bot Telegram activo ✅ - Ejecuta el bot manualmente via SSH"