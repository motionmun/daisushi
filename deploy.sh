#!/bin/bash

echo "Запуск процесса деплоя..."

# Останавливаем текущий контейнер, если он есть
docker stop dai_sushi_bot || true
docker rm dai_sushi_bot || true

# Собираем новый образ
docker build -t dai_sushi_bot .

# Запускаем контейнер
docker run -d --name dai_sushi_bot dai_sushi_bot

echo "Бот успешно запущен!"
