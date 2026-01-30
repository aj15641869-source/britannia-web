import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Render ke Environment Variables se token uthayega
TOKEN = "8578243284:AAGSt3ATP-rRZaNHvFriQg030jzK-i819Wc"
WEB_URL = "https://aj15641869-source.github.io/britannia-web/" 
CHANNELS = ["@SheinVoucher4000"] # Apne channels ke username yahan dalein
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🎁 Claim Cashback Now", web_app=WebAppInfo(url=WEB_URL))
    markup.add(btn)
    
    text = "<b>बधाई हो!</b>\nBritannia की ओर से आपको Cashback मिला है।\n\nनीche button par click karke claim karein."
    await message.answer(text, reply_markup=markup)

@dp.message_handler(content_types="web_app_data")
async def check_data(message: types.Message):
    user_id = message.from_user.id
    # Membership check logic
    await message.answer("🔄 Checking membership... Please wait.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
