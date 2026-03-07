from aiogram import Bot , Dispatcher , executor , types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import logging
import os


PORT = int(os.environ.get('PORT',5000))
logging.basicConfig(level=logging.INFO)
API_TOKEN = '8494742069:AAH6iybcnf2Ev7eAyndc71nWuTNchiaQs-I'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add( KeyboardButton ("Help[مساعدة]"))
keyboard.add( KeyboardButton ("information[معلومات]"))
keyboard.add( KeyboardButton ("call us[اتصل بنا]"))

@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.reply(
    "Hi I am your first bot \n"
    "to see the availeble commands send \Help \n",
    reply_markup = keyboard
    )
    
@dp.message_handler(commands=['Help'])
async def send_help(message:types.Message):
    help_text=(
        "[الأوامر المتاحة]: \n"
        "/start : بدء التشغيل\n"
        "/Help  : مساعدة\n"
        "/about : معلومات عن البوت"
    )
    await message.reply(help_text,parse_mode="Markdown")
    
@dp.message_handler()
async def echo(message:types.Message):
    text=message.text.lower()
    
    if text =="Help[مساعدة]" :
        await send_help(message)
    elif text =="information[معلومات]" :
        await message.reply("أنا بوت مصنوع باستخدام بايثون.المطور:م رشا")
    elif text == "call us[اتصل بنا]" :
        await message.reply("email : rashamahfoudeng@gmail.com")
    elif "Hi" in text or "Hello" in text or "مرحبا" in text or "أهلا" in text :
        await message.reply("welcome!,أهلا وسهلا")
    else :
        await message.reply(f"you said:{message.text}")
print("running")
if __name__=='__main__' :
    print("bot is runing")
    executor.start_polling(dp)
print("done")
executor.start_polling(dp, skip_updates=True)