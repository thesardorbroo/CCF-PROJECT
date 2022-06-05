from aiogram import executor
from aiogram.types import Message, CallbackQuery
from botconfig.Config import dp
from core import Core
from details import Details

@dp.message_handler(commands=['start'])
async def say_hi(message: Message):
    await Core.pressed_start(message)

@dp.message_handler(content_types=['text'])
async def message_is_text(message: Message):
    await Core.message_is_text(message)

@dp.message_handler(content_types=['contact'])
async def send_phone_number(message: Message):
    # await Details.sendPhoneNumber(message, )
    pass

@dp.callback_query_handler()
async def selected_times(call: CallbackQuery):
    await Core.user_selected_time(call)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)