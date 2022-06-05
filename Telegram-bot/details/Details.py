from aiogram.types import Message, CallbackQuery

from texts.Text import *
from user.User import *
from psycopg2.errors import UndefinedColumn
from buttons.KeyBoards import *
from botconfig.Config import bot, db
from times.Time import *


async def addNewUser(message: Message, user: UserOS):
    user_id = message.from_user.id
    text = message.text
    if user.step == 1:
        if text == "uz🇺🇿":
            await db.update_column(user_id, "language", 'UZ')
            await bot.send_message(user_id, senten["UZ"]["Enter name"], reply_markup=remove)
            await db.update_column(user_id, "step", 2)
        elif text == "ru🇷🇺":
            await db.update_column(user_id, "language", 'RU')
            await bot.send_message(user_id, senten["RU"]["Enter name"], reply_markup=remove)
            await db.update_column(user_id, "step", 2)

    elif user.step == 2:
        if user.barber_id is None:
            await bot.send_message(user.user_id, senten[user.language]["Main menu"])
            await message.answer(senten[user.language]["WEB"])
            # await bot.send_message(user_id, senten[user.language]["Send PN"], reply_markup=all_keys[user.language]["Send PN"])
            await db.update_column(user_id, "username", f"{text}")
            await db.update_column(user_id, "step", 3)
        else:
            await show_the_barber_by_id(message, user)

async def sendPhoneNumber(message: Message):
    user = await db.get_user(message.from_user.id)
    # await db.update_column(user.user_id, "phone_number", message.contact.phone_number)
    await bot.send_message(user.user_id, senten[user.language]["Main menu"], reply_markup=all_keys[user.language]["Main menu"])


async def get_user_location(message: Message, user: UserOS):
    """
    Userni locationni shu metod qabul qiladi
    """
    await bot.send_message()
    await db.update_column(user.user_id, "location", f"{message.location.latitude}:{message.location.longitude}")
    await db.update_column(user.user_id, "step", 13)

async def show_the_barber_by_id(message: Message, user: UserOS):

    try:
        barber = await db.get_barber(user.barber_id)
        buttons = await show_dates(datetime.date.today().month)
        caption = await get_caption(user, barber)
        print(barber.photo)
        await bot.send_photo(user.user_id, photo=open(f"photo/{barber.photo}", 'rb'), caption=caption, reply_markup=buttons)
        await db.update_column(user.user_id, "step", 3)

    except UndefinedColumn:
        await message.answer(senten[user.language]["Expected error"])

async def show_the_barber_by_key(message: Message, user: UserOS):

    try:
        barber = await db.get_barber_key(message.text)
        if barber is None:
            return None
        buttons = await show_dates(datetime.date.today().month)
        caption = await get_caption(user, barber)
        print("BY KEY: ",barber)
        await bot.send_photo(user.user_id, photo=open(f"photo/{barber.photo}", 'rb'), caption=caption, reply_markup=buttons)
        # await message.answer(f"{barber.id}\n{barber.user_id}\n{barber.shop_id}\n{barber.start_time}\n{barber.end_time}\n{barber.fullname}", reply_markup=buttons)
        await db.update_column(user.user_id, "step", 3)

    except UndefinedColumn:
        await message.answer(senten[user.language]["Expected error"])


async def calendar(call: CallbackQuery, user: UserOS):
    day, month = call.data.split("|")
    month = months_in_number[month]
    await db.update_column(user.user_id, "step", 4)
    orders = await db.get_barber_orders(user.barber_id, f"{day}-{month}")
    keys = await create_buttons(orders)
    await db.update_table_orders_p1(user, f"{day}-{month}")
    return keys

async def get_caption(user: UserOS,barber: Barber):
    if user.language == 'RU':
        return f"""
Имя барбера: {barber.fullname}
Время работы барбера(начало): {barber.start_time}
Время работы барбера(конец): {barber.end_time}
"""

    elif user.language == 'UZ':
        return f"""
Barber ismi: {barber.fullname}
Barber ish vaqti(start): {barber.start_time}
Barber ish vaqti(end): {barber.end_time}
"""



