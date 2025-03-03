from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить блюдо"), KeyboardButton(text="✏️ Изменить блюдо")],
        [KeyboardButton(text="🗑 Удалить блюдо"), KeyboardButton(text="📊 Статистика продаж")],
        [KeyboardButton(text="🔙 Выйти из админки")]
    ],
    resize_keyboard=True
)
