from telegram.ext import ConversationHandler, MessageHandler, filters
from database import save_booking
from telegram.ext import CommandHandler


SELECT_DATE, SELECT_TIME = range(2)

def start_booking(update, context):
    update.message.reply_text("Введите дату заезда:")
    return SELECT_DATE

def save_date(update, context):
    context.user_data['check_in'] = update.message.text
    update.message.reply_text("Введите время:")
    return SELECT_TIME

def save_time(update, context):
    context.user_data['check_out'] = update.message.text
    # Сохранение в БД
    save_booking(context.user_data)
    update.message.reply_text("Бронь сохранена!")
    return ConversationHandler.END

booking_handler = ConversationHandler(
    entry_points=[CommandHandler('book', start_booking)],
    states={
        SELECT_DATE: [MessageHandler(filters.TEXT, save_date)],
        SELECT_TIME: [MessageHandler(filters.TEXT, save_time)]
    },
    fallbacks=[]
)