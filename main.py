import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- CONFIGURATION ---
# Aapka asali token yahan hai
TOKEN = "8349459713:AAHvrFPW6ojDKg9x5fHHGWsFcMpV1jq4dR"
# Aapka GitHub Pages wala link
WEB_URL = "https://aj15641869-source.github.io/britannia-web/"
# Jin channels ko join karwana hai unka username
CHANNELS = ["@SheinVoucher4000"] 

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    # Mini App Button
    btn = InlineKeyboardButton("🎁 Claim Cashback Now", web_app=WebAppInfo(url=WEB_URL))
    markup.add(btn)
    
    text = "<b>बधाई हो!</b>\nBritannia की ओर से आपको Cashback मिला है।\n\nनीचे button par click karke claim karein."
    await message.answer(text, reply_markup=markup)

# Jab user WebApp se "Verify" dabayega toh ye logic chalega
@dp.message_handler(content_types="web_app_data")
async def check_data(message: types.Message):
    user_id = message.from_user.id
    all_joined = True
    
    # Har ek channel ke liye check karega
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
        # Agar user ne sab join kar liya hai
        await message.answer("✅ <b>Membership Verified!</b>\nAapne saare channels join kar liye hain. Ab aap cashback rewards claim kar sakte hain.")
    else:
        # Agar koi channel bacha hai
        await message.answer("❌ <b>Error:</b> Aapne saare channels join nahi kiye hain!\nKripya saare channels join karke dubara 'Verify' par click karein.")

if __name__ == '__main__':
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)
