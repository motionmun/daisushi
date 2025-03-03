import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from database import create_tables
from handlers import start, menu, cart, admin

async def main():
    create_tables()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(cart.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
