# stripe

Простое приложение для теста Stripe Api

## Как запустить

Скачайте код, перейдите в каталог проекта

Создайте .env файл со следущим содержимым:

```sh
STRIPE_PUBLIC_KEY=публичный ключ stripe
STRIPE_SECRET_KEY=приватный ключ stripe
SECRET_KEY=секретный ключ django
```

Далле создайте образ и запустите контейнер
```sh
docker compose up
```
Выполните команды
```sh
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```
Заполните таблицу Item тестовыми данными и перейдите на страницу для проведения платежа  
http://0.0.0.0:8000/item/1
