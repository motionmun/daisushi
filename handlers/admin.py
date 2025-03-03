from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_ID

router = Router()

@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if str(message.from_user.id) == ADMIN_ID:
        await message.answer("Добро пожаловать в панель администратора! Вы можете:\n"
                             "/add_item - добавить позицию в меню\n"
                             "/delete_item - удалить позицию\n"
                             "/stats - посмотреть статистику заказов")
    else:
        await message.answer("У вас нет доступа к админке.")
