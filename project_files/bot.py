import os, sys
from config import TOKEN

activate_this = "/Users/User/PycharmProjects/test_tbot/venv/Scripts/activate_this.py"  ## Local
# activate_this = '/home/bot/python3.10_projects/telegram_bots/bot_1_test/venv_bot_1_test/bin/activate_this.py'   ##Server
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

from aiogram import Bot, dispatcher

bot = Bot(token=TOKEN)
dp = dispatcher(bot)
