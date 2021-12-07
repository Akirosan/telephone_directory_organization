# telephone_directory_organization

Телефонный справочник представляет собой API приложение(DFR) для поиска номеров телефонов и информации об организациях.

Для установки: 
* скачайте проект на свой компьютер 
* Установите виртуальное окружение
* Выполните миграции
* Зарегистрируйте суперпользователя
* Зарегистрируйте обычного пользователя
```python
POST http://localhost/api/users/ 
content-type: application/json

{
    "email": "user@user.ru",
    "username": "User",
    "first_name": "Firstname",
    "last_name": "Lastname",
    "password": "Password"
}
```
*  Авторизуйтесь используя email
```python
POST http://localhost/auth/token/login/ 
content-type: application/json

{
    "email": "user@user.ru",
    "password": "Password"
}
```

*   Создайте организацию
```python
POST http://localhost/api/company/
content-type: application/json
Authorization: Token <token>

{
    "name": "ООО Креативные технологии",
    "adress": "The Moscow",
    "description": "The Lagest organization",
}
```

*   Создйте сотрудника
```python
POST http://localhost/api/staffer/
content-type: application/json
Authorization: Token <token>

{ 
    "staffer": "Конюхов Геннадий Петрович",
    "post": "Главный инженер",
    "work_phone": "+7 846 56232",
    "personal_phone": "+7 387 78634",
    "fax_number": "+7 846 25885",
    "company": [
        1
    ]
}
```


# Существующие эндпойнты

### Пользователь
#

* Регистрация пользователя
```python
POST http://localhost/api/users/ 
content-type: application/json

{
    "email": "user@user.ru",
    "username": "User",
    "first_name": "Firstname",
    "last_name": "Lastname",
    "password": "Password"
}
```
*  Авторизация
```python
POST http://localhost/auth/token/login/ 
content-type: application/json


{
    "email": "user@user.ru",
    "password": "Password"
}
```

*   Список пользователей
```python
GET http://localhost/api/users/
content-type: application/json
Authorization: Token <token>
```

*  Информация о юзере
```python
GET http://localhost/api/users/2/
content-type: application/json
Authorization: Token <token>
```

*  Информация о текущем юзере
```python
GET http://localhost/api/users/me/
content-type: application/json
Authorization: Token <token>
```

*  Смена пароля
```python
POST http://localhost/api/users/set_password/
content-type: application/json
Authorization: Token <token>

{
    "new_password": "Password",
    "current_password": "Passwor2"
}
```

*  Выход (Удаление токена)
```python
POST http://localhost/auth/token/logout/
content-type: application/json
Authorization: Token <token>
```


### Организация
#

*   Список организаций
```python
GET http://localhost/api/company/
content-type: application/json
```

*   Список моих организаций
```python
GET http://localhost/api/company/my/
content-type: application/json
Authorization: Token <token>
```

*   Создать организацию
```python
POST http://localhost/api/company/
content-type: application/json
Authorization: Token <token>

{
    "name": "ООО Креативные технологии",
    "adress": "The Moscow",
    "description": "The Lagest organization",
}
```

*   Одна организация
```python
GET http://localhost/api/company/5/
content-type: application/json
```


### Сотрудник
#


*   Список сотрудников
```python
GET http://localhost/api/staffer/
content-type: application/json
```

*   Один сотрудник
```python
GET http://localhost/api/staffer/7/
content-type: application/json
```

*   Создать сотрудника
```python
POST http://localhost/api/staffer/
content-type: application/json
Authorization: Token <token>

{ 
    "staffer": "Конюхов Геннадий Петрович",
    "post": "Главный инженер",
    "work_phone": "+7 846 56232",
    "personal_phone": "+7 987 78634"
    "fax_number": "+7 987 78634"
    "company": [
        1
    ]
}
```

### Менеджер (управляющий организацией)
#


*   Список управляющих
```python
GET http://localhost/api/manager/
content-type: application/json
Authorization: Token <token>
```


*   Добавить управляющего по email и id компании
```python
POST http://localhost/api/manager/
content-type: application/json
Authorization: Token <token>

{
    "email": "stas@gatas.ru",
    "company": 2
}
```

*   Удалить управляющего по email и id компании
```python
DELETE http://localhost/api/manager/
content-type: application/json
Authorization: Token <token>

{
    "email": "stas@gatas.ru",
    "company": 2
}
```
