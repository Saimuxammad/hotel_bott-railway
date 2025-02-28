# handlers/booking.py
from telegram.ext import ConversationHandler

def start_booking(update, context):
    update.message.reply_text("Выберите дату заезда:")
    return "SELECT_DATE"

booking_handler = ConversationHandler(
    entry_points=[...],  # Укажите точку входа (например, CommandHandler)
    states={...},
    fallbacks=[]
)