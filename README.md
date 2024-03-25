# RESTful API сервис для реферальной системы


**Сущности:**
* User (пользователь)
* Referral (реферальный код) 


**Релизовнный на данный момент функционал:**
* регистрация и аутентификация пользователя
* создание/удаление с реферального кода
* получение реферального кода по email адресу реферера
* возможность указать при регистрации реферальный код
* получение информации о рефералах по id реферера
* UI документация
* кеширование списка реферальных кодов с использованием бд Redis


**Права пользователей и валидация:**
* суперюзер имеет все права на все сущности
* для доступа к интерфейсам необходимо авторизоваться; без авторизации доступно создание пользователя и документация
* права на интерфейс users - создавать могут все, CRUD - владелец или суперюзер
* права на интерфейс referrals - владелец или суперюзер
* получение информации о рефералах по id реферера - только суперюзер
* получение реферального кода по email реферера - владелец или суперюзер
* для создания рефенального кода необходимо авторизоваться, код будет привязан к авторизованному пользователю 
  * код должен быть длиной 5 символов и состоять из цифр
  * код уникален в БД
  * нельзя созать активный просроченный код 
  * активный код может быть только один, при создании активного/активизации кода происходит проверка наличия в БД у текущего пользователя другого активного кода, и его деактивация
* пользователь регистрируется по email и паролю, можно дополнительно указать реферальный код
  * email уникален в БД
  * при указании реферального кода проверяется его существование в БД и статус активности, можно использовать только активный



**Команды**

* Создание виртуального окружения: python -m venv venv

* Установка зависимостей из requirements.txt: pip install -r requirements.txt  

* Создание миграций: python manage.py makemigrations

* Применение миграций: python manage.py migrate
 
* Создание суперюзера: python manage.py csu  (параметры - в файле \management\commands\csu.py)

* Запуск проекта: python manage.py runserver 

http://127.0.0.1:8000/ - интерфейс API после запуска

http://127.0.0.1:8000/admin/ - админка

http://127.0.0.1:8000/users/ - интерфейс для работы с пользователями

http://127.0.0.1:8000/referrals/- интерфейс для работы с реферальными кодами

http://127.0.0.1:8000/user/id - интерфейс получение информации о рефералах по id реферера

http://127.0.0.1:8000/user/email - интерфейс для получения реферального кода по email реферера

http://127.0.0.1:8000/token/ - получение JWT

http://127.0.0.1:8000/swagger/, http://127.0.0.1:8000/redoc/ - документация

