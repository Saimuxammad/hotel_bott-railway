from keyboards import main_menu_uz, main_menu_ru  # Теперь обе функции есть в keyboards.py
from telegram.ext import CallbackQueryHandler

def handle_main_menu(update, context):
    user_lang = context.user_data.get('lang', 'uz')
    if user_lang == 'uz':
        update.message.reply_text("Bosh menyu:", reply_markup=main_menu_uz())
    else:
        update.message.reply_text("Главное меню:", reply_markup=main_menu_ru())

main_menu_handler = CallbackQueryHandler(handle_main_menu, pattern="main_menu")