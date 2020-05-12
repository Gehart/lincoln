# SpeackingNews
Сайт поддерживается на основе `Python==3.8` и `Django==3.0`
## Главные функции:
- Добавлять, удалять, делиться, редактировать статьи и категории.
- Возможность добавлять статьи в избранное.
- Подписка на категории, уведомление по почте о новых статьях из выбранной категории. 
- Возможность публиковать статьи как в новостную ленту, так и в слайдер на главной странице.
- Поддержка полнотекстового поиска статей.
- Возможность оставлять коменнатрии, включая пост-ответный комментарий.
- Регистрироваться, авторизовываться на сайте.
- Восстановление пароля, с помощью почты.
- Настройки профиля, смена фотографии пользователя, пароля, логина, почты.
## Установка:
### Виртуальное окружение
Создайте виртуальное окружение в директории проекта
- OS X / Linux, выполните следущие команды:
Создание виртуального окружения:
    ```
    python3 -m venv env
    ```
- После того, как вы создали виртуальное окружение, необходимо его активировать:
    ```
    source venv/bin/activate
    ```
- Больше информации о виртуальном окружении python вы можете найти [тут](https://python-scripts.com/virtualenv)
### Установка зависимостей
- Для того чтобы установить все необходимые пакеты для работы с проектом выполните:
    ```
    pip3 install -r requirements.txt
    ```
### Настройка PostgreSQL
В данной статье [HOW TO INSTALL POSTGRESQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) подробно описан процесс установки Postgre под LinuxOS

### Конфигурация Django
После того, как вы установили PostgreSQL, создали пользователя и базу данных, необходимо подключить ее к проекту.
- Измините файл `mysite/setting.py`, как показано ниже:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'Имя пользователя БД', 
            'PASSWORD': 'Пароль от БД',
            'HOST': 'localhost',
        }
    }
    ```
- Откройте опять терминал, в директории проекта активируйте виртуальное окружение.

- Необходимо создать таблицы в базе данных, для этого выполните следущие команды:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
### Создание суперпользователя
- Выполните команду в терминале:
    ```bash
    python3 manage.py createsuperuser
    ```
- Заполните поля

### Запуск сервера
- Запуск сервера осуществляется командой:
    ```bash
    python3 manage.py runserver
    ```
- Откройте браузер и перейдите на http://127.0.0.1:8000/.

- Если вы все прошлые пункты выполнили правильно, перед вами должна открыться страница сайта.

### О странице
Если в ходе выполнения инсталяции вы столкнулись с какими-либо ошибками, пожалуйста напише на почту `hlistunovd#yandex.ru`, я постараюсь помочь всем, что в моих силах.
