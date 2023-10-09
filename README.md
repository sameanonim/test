# Веб-приложение для моделирования сети по продаже электроники

Это веб-приложение, созданное с помощью фреймворка Django, позволяет моделировать иерархическую структуру сети по продаже электроники. Сеть состоит из трех уровней: заводов, розничных сетей и индивидуальных предпринимателей. Каждое звено сети имеет свои характеристики, такие как название, контакты, продукты, поставщик и задолженность перед поставщиком. Веб-приложение предоставляет API интерфейс и админ-панель для управления данными сети.

## Технические требования

Для запуска веб-приложения необходимо иметь следующие компоненты:

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

## Установка и запуск

Для установки и запуска веб-приложения выполните следующие шаги:

1. Клонируйте репозиторий с кодом веб-приложения на свой компьютер:

```
git clone https://github.com/sameanonim/test/
```

2. Перейдите в каталог веб-приложения:
```
cd test
```
3. Создайте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
4. Установите необходимые зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Создайте базу данных PostgreSQL и настройте соединение с ней в файле settings.py:

6. Выполните миграции для создания таблиц в базе данных:
```
python manage.py migrate
```
7. Создайте суперпользователя для доступа к админ-панели:
```
python manage.py createsuperuser
```
8. Запустите сервер разработки:
```
python manage.py runserver
```

Описание модели данных
Веб-приложение использует следующую модель данных для представления сети по продаже электроники:

!Модель данных

Модель данных состоит из четырех классов:

NetworkNode - абстрактный базовый класс для всех звеньев сети, содержит общие поля для всех звеньев сети, такие как название, контакты, продукты, поставщик, задолженность перед поставщиком и уровень иерархии.
Product - класс для продукта, содержит поля для названия, модели и даты выхода продукта на рынок.
Factory - класс для завода, наследуется от NetworkNode, содержит дополнительное поле для продуктов, производимых заводом.
RetailNetwork - класс для розничной сети, наследуется от NetworkNode, содержит дополнительное поле для веб-сайта розничной сети и продуктов, продаваемых розничной сетью.
IndividualEntrepreneur - класс для индивидуального предпринимателя, наследуется от NetworkNode, содержит дополнительное поле для пользователя, связанного с индивидуальным предпринимателем и продуктов, продаваемых индивидуальным предпринимателем.