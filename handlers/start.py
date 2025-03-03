from aiogram import Router, types
from aiogram.filters import Command
from database import add_user

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    add_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f"Привет, {message.from_user.full_name}! Добро пожаловать в Dai Sushi 🍣\nВыберите действие в меню.")
