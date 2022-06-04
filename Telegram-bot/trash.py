from aiogram import executor, Dispatcher, Bot
from aiogram.types import Message

TOKEN = "5294913664:AAFaXCIfK-xDDc7TzwT19elU1K83FEX3-8Q"
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['photo'])
async def return_file_id(message: Message):
    await bot.send_message(message.from_user.id, message.photo[0]["file_id"])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
