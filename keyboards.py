from telebot import types


def main_menu():

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(types.KeyboardButton("🌕 Current Moon Phase"))
    keyboard.row(types.KeyboardButton("✨ Lunar Advice"))
    keyboard.row(types.KeyboardButton("🌱 Best Activities"))
    keyboard.row(types.KeyboardButton("🔮 Energy Reading"))
    keyboard.row(types.KeyboardButton("📅 Weekly Forecast"))

    return keyboard