import asyncio
from datetime import timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8946898500:AAF3tIqyyQJ83OW3xkXti_xMczPLOzdjovI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Счётчик сообщений для текущей сессии бота
total_messages_count = 0

@dp.message(Command("Shotgun", ignore_case=True))
async def cmd_shotgun(message: Message):
    text = "💥 **Дробовик заряжен!** Гилберт на связи и готов к действию!"
    await message.reply(text, parse_mode="Markdown")

# Команда /st — быстрая проверка количества сообщений
@dp.message(Command("st", ignore_case=True))
async def cmd_st(message: Message):
    await message.reply(f"📊 Всего сообщений в чате: **{total_messages_count}**", parse_mode="Markdown")

@dp.message(Command("kick", ignore_case=True))
async def cmd_kick(message: Message):
    if message.chat.type == "private":
        await message.reply("Эту команду можно использовать только в беседах и группах!")
        return

    if not message.reply_to_message:
        await message.reply("Пожалуйста, ответьте командой `/kick` на сообщение пользователя, которого нужно исключить.")
        return

    user_to_kick = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        await bot.ban_chat_member(chat_id=chat_id, user_id=user_to_kick.id)
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_to_kick.id)
        await message.reply(f"🔨 Пользователь {user_to_kick.full_name} был исключен из чата.")
    except Exception as e:
        await message.reply(f"Не удалось кикнуть пользователя. Ошибка: {e}")

# Команда /mute (дает мут на 10 минут)
@dp.message(Command("mute", ignore_case=True))
async def cmd_mute(message: Message):
    if message.chat.type == "private":
        await message.reply("Эту команду можно использовать только в беседах и группах!")
        return

    if not message.reply_to_message:
        await message.reply("Пожалуйста, ответьте командой `/mute` на сообщение пользователя, которого нужно замутить.")
        return

    user_to_mute = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        until_date = timedelta(minutes=10)
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_to_mute.id,
            permissions=types.ChatPermissions(can_send_messages
        
