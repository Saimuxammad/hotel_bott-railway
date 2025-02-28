import requests
from telegram import Update
from telegram.ext import CallbackContext

def find_restaurants_uz(update: Update, context: CallbackContext):
    # Логика как в предыдущих ответах, но с узбекским текстом
    update.callback_query.edit_message_text("附近的餐厅:\n...")