Репозиторий на **GitHub**:
https://github.com/Azimjonm2333/TrainingCenter

## Установка и настройка

1. Установите [Python 3](https://www.python.org/downloads/) на свой компьютер, если он еще не установлен.

2. Склонируйте репозиторий:

```
git clone https://github.com/Azimjonm2333/TrainingCenter.git
```

3. Перейдите в директорию проекта:

```
cd TrainingCenter
```

4. Создайте виртуальное окружение:

```
python -m venv env
```

5. Активируйте виртуальное окружение:

- На Windows: `.\env\Scripts\activate`
- На Linux/Mac: `source env/bin/activete`

6. Установите зависимости:

```
pip install -r requirements.txt
```

7. Примените миграции:

```
python manage.py migrate
```

8. Создайте суперпользователя:

```
python manage.py createsuperuser
```

9. Запустите сервер:

```
python manage.py runserver
```

10. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/admin/.
