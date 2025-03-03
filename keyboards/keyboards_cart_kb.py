from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cart_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Просмотреть корзину")],
        [KeyboardButton(text="✅ Оформить заказ"), KeyboardButton(text="🔙 Назад в меню")]
    ],
    resize_keyboard=True
)
