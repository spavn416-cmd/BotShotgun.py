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

    user_to_kick = None

    # Вариант 1: Если команда вызвана ответом на сообщение
    if message.reply_to_message:
        user_to_kick = message.reply_to_message.from_user
    else:
        # Вариант 2: Если написали через пробел (например, /kick @username или ID)
        args = message.text.split(maxsplit=1)
        if len(args) > 1:
            target = args[1].strip()
            try:
                # Пробуем найти пользователя по юзернейму или ID
                if target.startswith("@"):
                    chat_member = await bot.get_chat_member(message.chat.id, target)
                    user_to_kick = chat_member.user
                else:
                    user_to_kick = await bot.get_chat(target)
            except Exception:
                pass

    if not user_to_kick:
        await message.reply("Использование команды:\n1. Ответьте на сообщение пользователя командой `/kick`\n2. Или напишите: `/kick @username`")
        return

    try:
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_to_kick.id)
        await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_to_kick.id)
        await message.reply(f"🔨 Пользователь {user_to_kick.full_name} был исключен из чата.")
    except Exception as e:
        await message.reply(f"Не удалось кикнуть пользователя. Проверьте права администратора у бота.\nОшибка: {e}")

async def main():
    print("Бот Гилберт успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
