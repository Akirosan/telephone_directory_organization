# telephone_directory_organization



Для установки: 
* скачайте проект к себе на компьютер 
* Установите виртуальное окружение
* Выполните миграции
* Зарегистрируйте суперпользователя

* Существующие эндпойнты

***************  Пользователи  *************

###   Список пользователей
GET http://localhost/api/users/


###   Регистрация пользователя 
POST http://localhost/api/users/ 

{
    "email": "user@user.ru",
    "username": "User",
    "first_name": "Firstname",
    "last_name": "Lastname",
    "password": "Password"
}


###  Информация о юзере
GET http://localhost/api/users/2/


###  Информация о текущем юзере
GET http://localhost/api/users/me/


###  Смена пароля
POST http://localhost/api/users/set_password/

{
    "new_password": "Password",
    "current_password": "Passwor2"
}


###  Авторизация (Получение токена)
POST http://localhost/auth/token/login/ 
content-type: application/json

{
    "email": "user@user.ru",
    "password": "Password"
}


###  Выход (Удаление токена)
POST http://localhost/auth/token/logout/


**************    Организация    *************

###   Список организаций
GET http://localhost/api/company/

###   Список моих организаций
GET http://localhost/api/company/my/

###   Создать организацию
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

###   Одна организация
GET http://localhost/api/company/5/


**************    сотрудники    *************

###   Список сотрудников
GET http://localhost/api/staffer/
content-type: application/json
Authorization: Token cbef2b4c1ec49d03161dfab5283f551abe8377d6


###   Один сотрудник
GET http://localhost/api/staffer/7/
content-type: application/json
Authorization: Token cbef2b4c1ec49d03161dfab5283f551abe8377d6


###   Создать сотрудника
POST http://localhost/api/staffer/
content-type: application/json
Authorization: Token cbef2b4c1ec49d03161dfab5283f551abe8377d6

{ 
    "staffer": "Конюхов Геннадий Петрович",
    "post": "Главный инженер",
    "work_phone": "+7 846 56232",
    "personal_phone": "+7 987 78634"
    "fax_number": "+7 987 78634"
}


**************    менеджеры    *************


###   Список менеджеров
GET http://localhost/api/manager/


###   Добавить менеджера
POST http://localhost/api/manager/

{
    "email": "stas@gatas.ru",
    "company": 2
}