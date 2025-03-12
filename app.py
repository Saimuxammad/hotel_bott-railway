import os
import logging
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application
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
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(main_menu_handler)
application.add_handler(booking_handler)

def start_bot():
    """Запуск бота с webhook"""
    webhook_url = "https://web-production-199c.up.railway.app/webhook"
    loop = asyncio.get_event_loop()
    loop.run_until_complete(application.bot.set_webhook(webhook_url))
    logging.info("✅ Webhook установлен!")

@app.route('/webhook', methods=['POST'])
def webhook():
    """Обработчик вебхука"""
    update = request.get_json()
    logging.info(f"📩 Получено обновление: {update}")

    if update:
        telegram_update = Update.de_json(update, application.bot)
        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(application.process_update(telegram_update), loop)

    return 'OK', 200

def run_flask():
    """Запуск Flask в основном потоке"""
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    init_db()
    logging.info("🚀 Запуск Telegram-бота...")

    # Устанавливаем вебхук перед запуском сервера
    start_bot()

    # Запускаем Flask-сервер
    run_flask()
