import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8946898500:AAFIQtFKpJYgG_i5a5vA8Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("Shotgun", ignore_case=True))
async def cmd_shotgun(message: Message):
    text = "💥 *Дробовик заряжен!* Гилберт на связи и готов к действию!"
    await message.reply(text, parse_mode="Markdown")

async def main():
    print("Бот Гилберт успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
