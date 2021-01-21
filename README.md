# V.it

Это студенческий проект курса [learn.python](https://learn.python.ru). 
Он подберет самые свежие вакансии на сайте [hh.ru](hh.ru), связанные с python, специально для Вас.

## Установка / Использование / Разработка
### Скачайте и установите зависимости
Выполните в консоли:
```
git clone https://github.com/StGrail/v_it.git
cd v_it
pip3 install -r requirements.txt
cd django_site
```

### Выполните настройку
Переименуйте файл config.example в config.py и замените  следующие данные:
```
DJANGO_SECRET_KEY = DJANGO_SECRET_KEY

PG_USER = Пользователь базы данных
PG_PASSWORD = Пароль базы данных

EMAIL_USER = Имейл для восстановления пароля
EMAIL_PASSWORD = Пароль к имейлу
```
### Наполните базу данных
```
python3 manage.py parser
```
Дождитесь, пока таблицы заполнятся вакансиями.

### Запустите сервер
```
python3 manage.py runserver
```
### Перейдите на [локальный сервер](http://127.0.0.1:8000)

## Участие в проекте
Пулл реквесты приветствуются. Для значительных изменений, пожалуйста,  сначала задайте вопрос на гитхаб для обсуждения того, что бы Вы хотели изменить.

Помните, что участие в опенсорсе часто == опыту разработк. Это может помочь пройти собеседование и стать "вайтишником".

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)
