from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import os
from config import ADMIN_ID  # Берем ID администратора из конфигурации

router = Router()

# Проверка, является ли пользователь админом
def is_admin(user_id):
    return str(user_id) == str(ADMIN_ID)

# Главное меню админки
@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ У вас нет доступа к админке.")
        return

    admin_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📜 Управление меню", callback_data="manage_menu")],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="view_stats")],
        [InlineKeyboardButton(text="📦 Просмотр заказов", callback_data="view_orders")],
    ])
    
    await message.answer("🔧 Админ-панель\nВыберите действие:", reply_markup=admin_kb)

# Обработчик для управления меню
@router.callback_query(lambda c: c.data == "manage_menu")
async def manage_menu(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer("❌ Нет доступа")

    menu_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Добавить позицию", callback_data="add_item")],
        [InlineKeyboardButton(text="✏️ Изменить цену", callback_data="edit_price")],
        [InlineKeyboardButton(text="❌ Удалить позицию", callback_data="delete_item")]
    ])

    await callback.message.answer("📜 Управление меню", reply_markup=menu_kb)

# Обработчик для статистики
@router.callback_query(lambda c: c.data == "view_stats")
async def view_stats(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer("❌ Нет доступа")

    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(price) FROM orders")
    total_revenue = cursor.fetchone()[0] or 0

    conn.close()

    await callback.message.answer(f"📊 Статистика:\n🛒 Заказов: {total_orders}\n💰 Выручка: {total_revenue}₩")

# Обработчик просмотра заказов
@router.callback_query(lambda c: c.data == "view_orders")
async def view_orders(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer("❌ Нет доступа")

    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, user_id, total_price FROM orders ORDER BY id DESC LIMIT 10")
    orders = cursor.fetchall()
    
    conn.close()

    if not orders:
        await callback.message.answer("📦 Нет заказов")
    else:
        orders_text = "\n".join([f"📌 Заказ {order[0]}: {order[2]}₩ (пользователь {order[1]})" for order in orders])
        await callback.message.answer(f"📦 Последние заказы:\n{orders_text}")
