# Weather App

Это приложение позволяет пользователям просматривать погоду в разных городах. Оно использует Open-Meteo API для получения данных о погоде и Django для разработки веб-приложения.

## Установка и запуск

1. Установите Python и Django.
2. Клонируйте репозиторий и перейдите в каталог проекта:
git clone https://github.com/Open-Meteo API/weather-app.git 
3. Создайте и активируйте виртуальное окружение:
python -m venv venv source venv/bin/activate # для Unix или Linux venv\Scripts\activate # для Windows
4. Установите зависимости:
pip install -r requirements.txt
5. Создайте базу данных и примените миграции:
python manage.py migrate
6. Создайте суперюзера
python manage.py createsuperuser
7. Запустите сервер разработки:
python manage.py runserver
8. Откройте браузер и перейдите по адресу `http://localhost:8000`.

## Использованные технологии

- Python
- Django
- Open-Meteo API
- HTML
- CSS
- JavaScript

## Что было сделано

- Создание модели `City` для хранения информации о городах.
- Создание модели `SearchHistory` для отслеживания поисков погоды.
- Реализация функции `get_weather_data` для получения данных о погоде из Open-Meteo API.
- Реализация функции `index` для отображения погоды в выбранном городе.
- Реализация функции `search_city` для поиска города по имени.
- Реализация функции `save_search_history` для сохранения истории поисков.
- Реализация шаблона `index.html` для отображения погоды и истории поисков.
- Реализация маршрутизации URL-адресов для отображения главной страницы и поиска города.
