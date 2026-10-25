import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8946898500:AAF3tIqyyQJ83OW3xkXti_xMczPLOzdjovI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("Shotgun", ignore_case=True))
async def cmd_shotgun(message: Message):
    text = "💥 **Дробовик заряжен!** Гилберт на связи и готов к действию!"
    await message.reply(text, parse_mode="Markdown")

@dp.message(Command("kick", ignore_case=True))
async def cmd_kick(message: Message):
    if message.chat.type == "private":
        await message.reply("Эту команду можно использовать только в беседах и группах!")
        return

    if not message.reply_to_message:
        await message.reply("Пожалуйста, ответь командой `/kick` на сообщение того пользователя, которого нужно исключить.")
        return

    user_to_kick = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        await bot.ban_chat_member(chat_id=chat_id, user_id=user_to_kick.id)
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_to_kick.id)
        await message.reply(f"🔨 Пользователь {user_to_kick.full_name} был исключен из чата.")
    except Exception as e:
        await message.reply(f"Не удалось кикнуть пользователя. Убедитесь, что у бота есть права администратора на удаление участников.\nОшибка: {e}")

async def main():
    print("Бот Гилберт успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
