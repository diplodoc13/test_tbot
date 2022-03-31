import os, sys

activate_this = "/Users/User/PycharmProjects/test_tbot/venv/Scripts/activate_this.py"  ## Local
# activate_this = '/home/bot/python3.10_projects/telegram_bots/bot_1_test/venv_bot_1_test/bin/activate_this.py'   ##Server
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    answer_message = f"Hello, <b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, answer_message, parse_mode="html")


@bot.message_handler()
def send_photo(message):
    if message.text == "photo":
        sending_photo = open("img/2.png", "rb")
        bot.send_photo(message.chat.id, sending_photo)


bot.polling(none_stop=True, interval=0)
