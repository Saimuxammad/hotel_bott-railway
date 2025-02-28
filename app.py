from flask import Flask, request
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.booking import booking_handler
from database import init_db
from handlers.main_menu import main_menu_handler
import os
app = Flask(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Инициализация бота
application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(main_menu_handler)
application.add_handler(booking_handler)

# Вебхук для Railway
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    application.process_update(update)
    return '', 200

if __name__ == '__main__':
    init_db()  # Создаем таблицы в БД
    app.run(host='0.0.0.0', port=8080)