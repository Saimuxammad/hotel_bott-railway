import os
import logging
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder
from handlers.booking import booking_handler
from handlers.main_menu import main_menu_handler
from database import init_db
from dotenv import load_dotenv

# Настройка логов
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден! Проверьте .env или Railway.")

# Инициализация Telegram-бота
application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(main_menu_handler)
application.add_handler(booking_handler)

# 🔥 Вебхук с исправлением `async` (Flask не поддерживает async-функции напрямую)
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    logging.info(f"📩 Получено обновление: {update}")

    if update:
        telegram_update = Update.de_json(update, application.bot)
        asyncio.run(application.process_update(telegram_update))  # ✅ Теперь `async` работает!

    return 'OK', 200

if __name__ == '__main__':
    init_db()
    logging.info("🚀 Запуск Flask-сервера...")
    app.run(host='0.0.0.0', port=8080)
