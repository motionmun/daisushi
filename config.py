import os
from dotenv import load_dotenv

# Загружаем переменные окружения (.env)
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # Токен бота (берем из .env)
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))  # ID администратора
DB_PATH = "data/database.db"  # Путь к базе данных
PHOTO_PATH = "data/photos/"  # Папка с фото роллов
