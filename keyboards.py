from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Стоимость"), KeyboardButton(text="О нас")]]
                               , resize_keyboard=True)

catalog_kb = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="Средняя игра", callback_data="medium")]
    , [InlineKeyboardButton(text="Большая игра", callback_data="large")]
    , [InlineKeyboardButton(text="Очень большая игра", callback_data="extra large")]
    , [InlineKeyboardButton(text="Другие предложения", callback_data="other")]
])

buy_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Купить", url="https://market.yandex.ru")]])