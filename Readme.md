## Описание ТЗ

Сервис управления категориями, товарами и корзиной.

## Технологии

- python
- django
- postgresql
- drf
- docker
- docker-compose
- swagger
- jwt
- djoser
- cors

## Эндпоинты для товаров и корзины

- Для управления категориями.
- Для управления подкатегориями
- Для управления корзиной

## Эндпоинты для управления пользователем

- Для создания и редактирования пользователя

## Права доступа

- Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
- Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной

## Модели

- Category
- SubCategory
- Product
- Basket
- BasketProduct
- User

## Админ панель Django

Для редактирования заказов, продуктов, категорий и подкатегорий

## Установка и запуск

Следуйте этим шагам для установки и запуска проекта.

### Клонирование проекта

git clone https://github.com/burnaschev/Task_test_Sundress.git

### Создание и активация виртуального окружения

python3 -m venv venv
source venv/bin/activate

### Переменные окружения

Все необходимые переменные окружения находятся в файле .env_sample

Нужно создать свой переменные окружения в файле .env

### Установка зависимостей

pip install -r requirements.txt

### Запуск сервера

python manage.py runserver

После чего вы сможете получить доступ к API по адресу `http://localhost:8000/`.

## Документация к API

Приложение будет доступно по адресу http://localhost:8000/docs/.
