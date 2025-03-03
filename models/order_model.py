class Order:
    def __init__(self, id, user_id, items, total_price, status):
        self.id = id
        self.user_id = user_id
        self.items = items
        self.total_price = total_price
        self.status = status

import sqlite3

# Функция для создания таблицы заказов в БД
def setup_db():
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        items TEXT,
        total_price INTEGER,
        status TEXT DEFAULT 'В обработке',
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

# Функция для добавления заказа в базу данных
def add_order(user_id, items, total_price):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO orders (user_id, items, total_price) VALUES (?, ?, ?)",
                   (user_id, items, total_price))

    conn.commit()
    conn.close()

# Функция для получения списка заказов
def get_orders(limit=10):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, user_id, items, total_price, status, timestamp FROM orders ORDER BY id DESC LIMIT ?", (limit,))
    orders = cursor.fetchall()

    conn.close()
    return orders
