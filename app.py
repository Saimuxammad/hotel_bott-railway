import os
import logging
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, ApplicationBuilder
from handlers.booking import booking_handler
from handlers.main_menu import main_menu_handler
from database import init_db
from dotenv import load_dotenv
import uvicorn

# Настройка логов
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден! Проверьте .env или Railway.")

# Инициализация Telegram-бота
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(main_menu_handler)
application.add_handler(booking_handler)

async def start_bot():
    """Запуск бота"""
    await application.initialize()
    await application.start()
    logging.info("✅ Бот успешно запущен!")

# Запуск бота в фоновом режиме
asyncio.create_task(start_bot())

@app.post("/webhook")
async def webhook(request: Request):
    """Обработчик Telegram Webhook"""
    update_data = await request.json()
    logging.info(f"📩 Получено обновление: {update_data}")

    update = Update.de_json(update_data, application.bot)
    await application.process_update(update)

    return {"status": "ok"}

if __name__ == "__main__":
    init_db()
    logging.info("🚀 Запуск FastAPI-сервера через uvicorn...")
    uvicorn.run("app:app", host="0.0.0.0", port=8080, workers=1)
