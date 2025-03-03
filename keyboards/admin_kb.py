from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📜 Управление меню", callback_data="manage_menu")],
    [InlineKeyboardButton(text="📊 Статистика", callback_data="view_stats")],
    [InlineKeyboardButton(text="📦 Просмотр заказов", callback_data="view_orders")]
])
