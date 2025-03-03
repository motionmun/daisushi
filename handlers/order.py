from aiogram import Router, types
from aiogram.filters import Command
from database import create_tables

router = Router()

@router.message(Command("order"))
async def process_order(message: types.Message):
    await message.answer("Ваш заказ оформлен! Мы свяжемся с вами для подтверждения.")
