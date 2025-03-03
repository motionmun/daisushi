import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# === ВСТАВЬ СВОЙ ТОКЕН ВМЕСТО ЭТОГО! ===
TOKEN = "7991217059:AAElJ8pA2grFQ_6cyEgl2gus-Td4rFjKPNg"

# === Создаем бота и диспетчер ===
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()  # Используем Router для Aiogram 3.x

# === Главное меню ===
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📜 Меню"), KeyboardButton(text="🛒 Корзина")]
    ],
    resize_keyboard=True
)

# === Обработчик команды /start ===
@router.message(lambda message: message.text == "/start")
async def send_welcome(message: types.Message):
    await message.answer("Привет! Добро пожаловать в Dai Sushi 🍣\nВыберите действие:", reply_markup=menu_keyboard)

# === Обработчик кнопки "📜 Меню" ===
@router.message(lambda message: message.text == "📜 Меню")
async def show_menu(message: types.Message):
    await message.answer("Здесь будет список суши и роллов 🍣")

# === Обработчик кнопки "🛒 Корзина" ===
@router.message(lambda message: message.text == "🛒 Корзина")
async def show_cart(message: types.Message):
    await message.answer("Ваша корзина пока пуста 🛒")

# === Запуск бота ===
async def main():
    dp.include_router(router)  # Подключаем Router
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
