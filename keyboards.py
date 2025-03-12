from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_uz():
    keyboard = [
        [InlineKeyboardButton("🏨 Xonalar", callback_data='rooms'),
         InlineKeyboardButton("📅 Bron qilish", callback_data='book')],
        [InlineKeyboardButton("🍽 Ovqatlanish", callback_data='restaurants'),
         InlineKeyboardButton("🎉 Tadbirlar", callback_data='events')],
        [InlineKeyboardButton("🗺 Qanday yetish mumkin?", callback_data='map'),
         InlineKeyboardButton("⭐️ Sharhlar", callback_data='reviews')],
        [InlineKeyboardButton("🇺🇿 UZ", callback_data='lang_uz'),
         InlineKeyboardButton("🇷🇺 RU", callback_data='lang_ru')],
        [InlineKeyboardButton("⬅️ Asosiy menyu", callback_data='main_menu')]  # ДОБАВИЛИ КНОПКУ
    ]
    return InlineKeyboardMarkup(keyboard)

def main_menu_ru():
    keyboard = [
        [InlineKeyboardButton("🏨 Номера", callback_data='rooms'),
         InlineKeyboardButton("📅 Бронь", callback_data='book')],
        [InlineKeyboardButton("🍽 Где поесть?", callback_data='restaurants'),
         InlineKeyboardButton("🎉 Мероприятия", callback_data='events')],
        [InlineKeyboardButton("🗺 Как добраться?", callback_data='map'),
         InlineKeyboardButton("⭐️ Отзывы", callback_data='reviews')],
        [InlineKeyboardButton("🇺🇿 UZ", callback_data='lang_uz'),
         InlineKeyboardButton("🇷🇺 RU", callback_data='lang_ru')],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data='main_menu')]  # ДОБАВИЛИ КНОПКУ
    ]
    return InlineKeyboardMarkup(keyboard)
