from aiogram import Router, types

router = Router()

cart = {}

@router.message(lambda msg: msg.text.startswith("Добавить"))
async def add_to_cart(message: types.Message):
    item = message.text.replace("Добавить ", "")
    user_id = message.from_user.id

    if user_id not in cart:
        cart[user_id] = []
    
    cart[user_id].append(item)
    await message.answer(f"{item} добавлен в корзину ✅")

@router.message(lambda msg: msg.text == "🛒 Корзина")
async def show_cart(message: types.Message):
    user_id = message.from_user.id
    if user_id not in cart or not cart[user_id]:
        await message.answer("Ваша корзина пока пуста.")
        return

    cart_items = "\n".join(cart[user_id])
    await message.answer(f"Ваш заказ:\n{cart_items}\n\nДля оформления заказа нажмите 'Заказать'.")
