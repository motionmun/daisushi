from aiogram import Router, types
import sqlite3
from config import DB_PATH

router = Router()

@router.message(lambda msg: msg.text.startswith("/add_roll "))
async def add_roll(message: types.Message):
    parts = message.text.split(" | ")
    if len(parts) != 4:
        await message.answer("Используйте формат: `/add_roll Название | Описание | Цена | Файл_фото`")
        return

    name, description, price, photo = parts[1], parts[2], float(parts[3]), parts[4]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menu (name, description, price, photo) VALUES (?, ?, ?, ?)", (name, description, price, photo))
    conn.commit()
    conn.close()

    await message.answer(f"Блюдо '{name}' добавлено в меню ✅")
