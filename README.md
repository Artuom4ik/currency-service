# currency-service

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
___
#### Данный проект представляет из себя микросервис по работе с курсами валют. С помощью этого сервиса можно полчить информацию о разных валютах в определенную дату. 
___
>### Системные требования:
- `Python` 3.10(или выше)
- `Windows`(10, 11) или `Linux`(Ubuntu 22.*)
___
>### Запуск микросервиса:

- Скачайте код командой
```
git clone https://github.com/Artuom4ik/currency-service.git
```
- Создайте виртуальное окружение командой
```
python3 -m myvenv venv
```
- Активируйте виртуальное командой
`Linux`
```
source myvenv/bin/activate
```
`Windows`
```
source myvenv/Scripts/activate
```
- Установите зависимости командой 
```
pip install -r requirements.txt
```
- Перейдите в директорию `currency_service`
- Выполните миграции базы данных командой 
```
python3 manage.py migrate
```
- Запустите сервер командой 
```
python3 manage.py runserver
```

После этого микросервис будет запущен
___
>### Переменные окружения:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.

>### Добавление данных

#### Для добавления данных требуется отправить `GET` запрос с параметрам `date`

- Endpoint: `/api/exchange/load_rates/`
- Метод: `GET`
- Параметры: `date` (формат YYYY-MM-DD), дата курса
```
http://127.0.0.1:8000/exchange/load_rates/?date=2024-05-27
```
- Ответом данного запроса будет сообщение:
```
{
    "message": "Data successfully downloaded",
    "title": "2270745537"
}
```

>### Получение курса валюты

- Endpoint: `/api/exchange/get_rate/`
- Метод: `GET`
- Параметры: `date` (формат YYYY-MM-DD), `currency` (код валюты, напр. USD)

```
"http://127.0.0.1:8000/exchange/get_rate/?date=2024-05-27&currency=USD"
```
- Ответом данного запроса будет сообщение:
```
{
    "id": 8,
    "date": "2024-05-27",
    "currency_id": 431,
    "currency_name": "USD",
    "scale": 1,
    "rate": "3.1983",
    "change_course": "Declined",
    "rate_difference": -0.0067,
    "title": "963208902"
}
```