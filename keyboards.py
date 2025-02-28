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
         InlineKeyboardButton("🇷🇺 RU", callback_data='lang_ru')]
    ]
    return InlineKeyboardMarkup(keyboard)