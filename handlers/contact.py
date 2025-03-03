from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(lambda message: message.text == "📞 Связь с оператором")
async def contact_support(message: types.Message):
    phone_number = "+821074221986"
    whatsapp_link = f"https://wa.me/{phone_number.replace('+', '')}"
    telegram_link = f"https://t.me/{message.from_user.username}"  # Или укажи логин оператора

    contact_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Позвонить", url=f"tel:{phone_number}")],
        [InlineKeyboardButton(text="💬 WhatsApp", url=whatsapp_link)],
        [InlineKeyboardButton(text="✉️ Telegram", url=telegram_link)]
    ])

    await message.answer("Выберите способ связи с оператором:", reply_markup=contact_kb)
