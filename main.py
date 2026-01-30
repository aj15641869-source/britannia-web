import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Configuration
TOKEN = "8349459713:AAEk-uQMqKvefYt-O7kICsCMIb2KIS9B5PY"
WEB_URL = "https://aj15641869-source.github.io/britannia-web/"
CHANNELS = ["@SheinVoucher4000"] 

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🎁 Claim Cashback Now", web_app=WebAppInfo(url=WEB_URL))
    markup.add(btn)
    
    text = "<b>बधाई हो!</b>\nBritannia की ओर se aapko Cashback mila hai.\n\nNiche button par click karke claim karein."
    await message.answer(text, reply_markup=markup)

@dp.message_handler(content_types="web_app_data")
async def check_data(message: types.Message):
    user_id = message.from_user.id
    all_joined = True
    
    for ch in CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=ch, user_id=user_id)
            if member.status in ["left", "kicked"]:
                all_joined = False
                break
        except Exception:
            all_joined = False
            break
            
    if all_joined:
        await message.answer("✅ <b>Membership Verified!</b>\nAapne saare channels join kar liye hain.")
    else:
        await message.answer("❌ <b>Error:</b> Aapne saare channels join nahi kiye hain!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
