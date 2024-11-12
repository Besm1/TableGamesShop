import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

import texts
from config import *
from keyboards import *
from texts import *
from bot_connector import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=["start", "старт"])
async def start(message):
    await message.answer(text=texts.start,reply_markup=start_kb)

@dp.message_handler(lambda message: message.text and message.text.lower() == "стоимость")
async def price(message: Message):
    await message.answer(text="Что Вас интересует?", reply_markup=catalog_kb)

@dp.message_handler(lambda message: message.text and message.text.lower() == 'о нас')
async def price(message: Message):
    await message.answer(text=texts.about, reply_markup=start_kb)

@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(text=texts.Mgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text="large")
async def buy_l(call):
    await call.message.answer(text=texts.Lgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text="extra large")
async def buy_xl(call):
    await call.message.answer(text=texts.XLgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text="other")
async def buy_o(call):
    await call.message.answer(text=texts.other , reply_markup=buy_kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)