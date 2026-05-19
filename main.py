import telebot

from config import TOKEN
from moon_phase import MoonPhase, get_week_forecast
from advisor import LunarAdvisor
from keyboards import main_menu
from user_manager import UserManager

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    username = message.from_user.username
    if username is None:
        username = "Unknown"

    UserManager.save_user(
        message.from_user.id,
        username
    )

    bot.send_message(
        message.chat.id,
        "🌙 Welcome to Lunar Cycle Bot!\n\n"
        "Discover moon phases, lunar energy, and weekly forecasts.",
        reply_markup=main_menu()
    )


@bot.message_handler(commands=['help'])
def help_command(message):

    help_text = (
        "🌙 LunarCycle Bot Commands\n\n"
        "/start — Start the bot\n"
        "/help — Show help menu\n"
        "/stats — Show a number of users\n\n"
        "Available features:\n"
        "🌕 Current Moon Phase\n"
        "✨ Lunar Advice\n"
        "🔮 Energy Reading\n"
        "📅 Weekly Forecast\n"
        "🌱 Best Activities"
    )

    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['stats'])
def stats(message):

    count = UserManager.get_user_count()

    bot.send_message(
        message.chat.id,
        f"🌙 Total users: {count}"
    )


@bot.message_handler(func=lambda message: message.text == "🌕 Current Moon Phase")
def current_phase(message):

    moon = MoonPhase()

    phase = moon.get_phase_name()
    description = moon.get_phase_description()

    bot.send_message(
        message.chat.id,
        f"{phase}\n\n{description}"
    )


@bot.message_handler(func=lambda message: message.text == "✨ Lunar Advice")
def lunar_advice(message):

    advisor = LunarAdvisor()
    advice = advisor.get_advice()

    bot.send_message(message.chat.id, advice)

@bot.message_handler(func=lambda message: message.text == "🌱 Best Activities")
def best_activities(message):

    advisor = LunarAdvisor()
    activities = advisor.get_best_activities()

    bot.send_message(message.chat.id, activities)


@bot.message_handler(func=lambda message: message.text == "🔮 Energy Reading")
def energy_reading(message):

    bot.send_message(
        message.chat.id,
        "🔮 The moon encourages you to trust your intuition today."
    )


@bot.message_handler(func=lambda message: message.text == "📅 Weekly Forecast")
def weekly_forecast(message):

    forecast = get_week_forecast()

    bot.send_message(message.chat.id, forecast)



print("🌙 LunarCycle Bot is running...")

bot.infinity_polling()