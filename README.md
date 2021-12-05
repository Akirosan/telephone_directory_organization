# telephone_directory_organization



Для установки: 
* скачайте проект на свой компьютер 
* Установите виртуальное окружение
* Выполните миграции
* Зарегистрируйте суперпользователя



# Существующие эндпойнты

***************  Пользователи  *************

*   Список пользователей
```python
GET http://localhost/api/users/
```

*   Регистрация пользователя 
```python
POST http://localhost/api/users/ 

{
    "email": "user@user.ru",
    "username": "User",
    "first_name": "Firstname",
    "last_name": "Lastname",
    "password": "Password"
}
```

*  Информация о юзере
```python
GET http://localhost/api/users/2/
```

*  Информация о текущем юзере
```python
GET http://localhost/api/users/me/
```

*  Смена пароля
```python
POST http://localhost/api/users/set_password/

{
    "new_password": "Password",
    "current_password": "Passwor2"
}
```

*  Авторизация (Получение токена)
```python
POST http://localhost/auth/token/login/ 
content-type: application/json

{
    "email": "user@user.ru",
    "password": "Password"
}
```

*  Выход (Удаление токена)
```python
POST http://localhost/auth/token/logout/
```


**************    Организация    *************

*   Список организаций
```python
GET http://localhost/api/company/
```

*   Список моих организаций
```python
GET http://localhost/api/company/my/
```

*   Создать организацию
```python
POST http://localhost/api/company/

{
    "name": "ООО Креативные технологии",
    "adress": "The Moscow",
    "description": "The Lagest organization",
    "created": "10",
    "staffer": [
        1,
        6
    ]
}
```

*   Одна организация
```python
GET http://localhost/api/company/5/
```


**************    сотрудники    *************

*   Список сотрудников
```python
GET http://localhost/api/staffer/
```

*   Один сотрудник
```python
GET http://localhost/api/staffer/7/
```

*   Создать сотрудника
```python
POST http://localhost/api/staffer/

{ 
    "staffer": "Конюхов Геннадий Петрович",
    "post": "Главный инженер",
    "work_phone": "+7 846 56232",
    "personal_phone": "+7 987 78634"
    "fax_number": "+7 987 78634"
}
```

**************    менеджеры    *************


*   Список менеджеров
```python
GET http://localhost/api/manager/
```


*   Добавить менеджера
```python
POST http://localhost/api/manager/

{
    "email": "stas@gatas.ru",
    "company": 2
}
```