from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from times.Time import times, months
import datetime

langauges = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("uz🇺🇿"), KeyboardButton("ru🇷🇺")
)

phone_numer_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Telefon raqamni jo'natish📲", request_contact=True)
)

phone_numer_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Отправить номер телефона 📲", request_contact=True)
)

remove = ReplyKeyboardRemove()

main_menu_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("Yo'q"), KeyboardButton("Bor"),
)

main_menu_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("Нет"), KeyboardButton("Да"),
)

all_keys = {
    "To all": {
        "Choose language": langauges,
    },
    'UZ': {
        "Send PN": phone_numer_uz,
        "Main menu": main_menu_uz,
    },
    'RU': {
        "Send PN": phone_numer_ru,
        "Main menu": main_menu_ru,
    },
}


async def create_buttons(orders: list):
    buttons = InlineKeyboardMarkup(row_width=3)
    print("CREATE BUTTONS --> ORDERES: ",orders)
    red = list()

    for k in orders:
        red.append(k[3])

    print("CREATE BUTTONS --> RED:",red)
    try:
        demo = list()
        for i in times:

            if i.text in red:continue
            else:demo.append(i)

        return buttons.add(*demo)

    except TypeError:
        buttons.add(*times)

    return buttons


async def show_dates(month: int):
    all_days = InlineKeyboardMarkup(row_width=7)
    the_list = list()
    i = 1
    all_days.add(
        InlineKeyboardButton("<", callback_data=months[month - 1]),
        InlineKeyboardButton(f"{months[month]}", callback_data="empty"),
        InlineKeyboardButton(">", callback_data=months[month + 1])
    )

    while (i < 32):
        the_list.append(
            InlineKeyboardButton(str(i), callback_data=f"{i}|{months[month]}")
        )
        i += 1

    all_days.add(*the_list)
    return all_days
