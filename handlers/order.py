from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import place_order, get_cart

router = Router()

# Клавиатура для подтверждения заказа
confirm_order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Подтвердить заказ")],
        [KeyboardButton(text="⬅ Вернуться в меню")]
    ],
    resize_keyboard=True
)

# Оформление заказа
@router.message(lambda message: message.text == "🛒 Оформить заказ")
async def place_order_handler(message: types.Message):
    user_id = message.from_user.id
    cart_items = get_cart(user_id)

    if not cart_items:
        await message.answer("❌ Ваша корзина пуста! Добавьте товары перед оформлением заказа.")
        return

    order_id = place_order(user_id)
    await message.answer(f"✅ Ваш заказ №{order_id} оформлен!\nОжидайте подтверждения.", reply_markup=confirm_order_kb)
