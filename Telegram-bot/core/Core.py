from aiogram.types import Message, CallbackQuery

from botconfig.Config import db, bot
from details import Details
from texts.Text import *
from datetime import date
from buttons.KeyBoards import all_keys

async def pressed_start(message: Message):
    await db.update_all_column(message.from_user.id)
    # await db.reserve_base()
    result = message.text.split(":")
    if len(result) == 2:
        print("Key is existed:User is exist!")
        await message.answer(senten["To all"]["Choose language"], reply_markup=all_keys["To all"]["Choose language"])
        await db.update_column(message.from_user.id, "barber_id", result[1])
        await db.update_column(message.from_user.id, "step", 1)

    else:
        user = await db.get_user(message.from_user.id)
        if user is None:
            await db.add_new_user(message.from_user.id)
            print("New user followed!")
        else:
            await db.update_column(user.user_id, "step", 1)
            print("No key:User is exist!")

        await message.answer(senten["To all"]["Choose language"], reply_markup=all_keys["To all"]["Choose language"])

async def message_is_text(message: Message):
    user = await db.get_user(message.from_user.id)
    text = message.text
    print("CORE " + f"{user.step}")
    if user.step <= 2:
        await Details.addNewUser(message, user)

    elif user.step == 3:
        await Details.show_the_barber_by_key(message, user)

    elif user.step == 4:
        await message.answer("BLAAA BLAAA BLAAA")
        await db.update_column(user.user_id, "step", 1)

async def user_selected_time(call: CallbackQuery):
    user = await db.get_user(call.from_user.id)
    barber = await db.get_barber(user.barber_id)
    if user.step == 3:
        await call.answer()
        buttons = await Details.calendar(call, user)
        await call.message.edit_reply_markup(reply_markup=buttons)

    elif user.step == 4:
        await call.answer("Band qilindi")
        order = await db.get_one(user.id, user.barber_id)
        id = await return_order_id(order)
        print(f"ID: {id}\t\tUSER.ID: {user.id}\n\nORDER: {order}")
        await db.update_table_orders_p2(user, call.data, id)
        await call.message.delete_reply_markup()
        await bot.send_message(barber.user_id, f"{user.username} buyurtma qildi {call.data}")
    print("CALL DATA: ",call.data)


async def return_order_id(order):
    ids = 0
    for i in order:
        print(i)
        if i[3] == None:
            ids = i[0]

    return ids


