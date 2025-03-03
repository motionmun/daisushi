from aiogram import Router, types
from aiogram.types import InputMediaPhoto
import sqlite3
from config import DB_PATH, PHOTO_PATH

router = Router()

@router.message(lambda msg: msg.text == "🍣 Меню")
async def show_menu(message: types.Message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, price, photo FROM menu")
    menu_items = cursor.fetchall()
    conn.close()

    if not menu_items:
        await message.answer("Меню пока пусто.")
        return

    media = [InputMediaPhoto(media=open(PHOTO_PATH + item[3], "rb"), caption=f"{item[0]}\n{item[1]}\nЦена: {item[2]}₩") for item in menu_items]
    await message.answer_media_group(media)
