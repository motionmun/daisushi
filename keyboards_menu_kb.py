from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍣 Меню"), KeyboardButton(text="🛒 Корзина")],
        [KeyboardButton(text="📞 Связь с оператором")]
    ],
    resize_keyboard=True
)
