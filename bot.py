import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from database import create_tables
from handlers import start, menu, cart, order, admin

# Создаем таблицы в БД (если их нет)
create_tables()

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем хендлеры
dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(cart.router)
dp.include_router(order.router)
dp.include_router(admin.router)

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
