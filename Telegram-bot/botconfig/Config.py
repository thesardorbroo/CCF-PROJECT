from aiogram import Dispatcher, Bot
from database.botdb import BotDB

TOKEN = "5142075282:AAGCfmrVVsGbK4OP9cN9lDASZvcTI1jmbrU"

bot = Bot(TOKEN)
dp = Dispatcher(bot)
db = BotDB()