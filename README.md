# Dai Sushi Bot 🍣

### Описание:
Этот бот позволяет пользователям:
- Просматривать меню с фото
- Добавлять роллы в корзину
- Оформлять заказы
- Оплачивать через KakaoPay/Naver Pay
- Связываться с оператором
- Администраторам управлять меню и видеть статистику продаж

### 📂 Структура проекта:
```
daisushi_bot/
│── bot.py                    # Главный файл бота
│── config.py                  # Файл с настройками (API-ключи, БД)
│── database.py                # Работа с базой данных (SQLite)
│── handlers/                  # Обработчики команд и кнопок
│── keyboards/                 # Клавиатуры
│── models/                    # Модели данных
│── data/                      # Папка для хранения данных
│── logs/                      # Логи работы бота
│── requirements.txt           # Зависимости
│── .env                       # Переменные окружения (НЕ ДОБАВЛЯТЬ В GIT)
│── Dockerfile                 # Контейнеризация
│── deploy.sh                  # Скрипт для быстрого запуска на сервере
```

### 🚀 Запуск бота:
1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Запустите бота:
```
python bot.py
```
3. Для деплоя в Docker:
```
bash deploy.sh
```

### 🔧 Настройка .env файла:
Создайте файл `.env` и укажите:
```
BOT_TOKEN=твой_токен_бота
ADMIN_ID=123456789
```
