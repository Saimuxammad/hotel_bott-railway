from keyboards import main_menu_uz, main_menu_ru
from telegram.ext import CallbackQueryHandler

def handle_main_menu(update, context):
    """Обрабатывает нажатие на кнопку 'Главное меню'."""
    query = update.callback_query
    query.answer()

    user_lang = context.user_data.get('lang', 'uz')
    if user_lang == 'uz':
        query.message.edit_text("Bosh menyu:", reply_markup=main_menu_uz())
    else:
        query.message.edit_text("Главное меню:", reply_markup=main_menu_ru())

main_menu_handler = CallbackQueryHandler(handle_main_menu, pattern="main_menu")
