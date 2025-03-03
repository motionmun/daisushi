from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок меню
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍣 Меню")],  # Кнопка для показа меню с фото
        [KeyboardButton(text="🛒 Корзина")],  # Кнопка для просмотра корзины
        [KeyboardButton(text="📞 Связаться с оператором")],  # Кнопка для связи с оператором
    ],
    resize_keyboard=True  # Уменьшаем размер клавиатуры для удобства
)
