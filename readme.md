Файл с конфигурацией сервера: .env

Установка необходимых пакетов:
Команда >>> pip install -r requirements.txt

Создание файла с необходимыми пакетами:
pip freeze > requirements.txt

Пакеты входящие в проект:
pip install Flask
pip install Flask-CORS
pip install Flask-Validator
pip install WTForms
pip install pymongo
pip install mongoengine
pip install python-dotenv
pip install PyJWT
pip install bcrypt
pip install motor

Структура проекта:
ZARUBCHENKO
├── client
├── server
│ ├── controllers
│ │ ├── user_controller.py
│ ├── dtos
│ │ ├── user_dto.py
│ ├── exceptions
│ │ ├── api_error.py
│ ├── middlewares
│ │ ├── auth_middleware.py
│ │ ├── error_middleware.py
│ ├── models
│ │ ├── token_model.py
│ │ ├── user_model.py
│ ├── modules
│ │ ├── mongo_config.py
│ ├── router
│ │ ├── index.py
│ ├── service
│ │ ├── mail_service.py
│ │ ├── token_service.py
│ │ ├── user_service.py
│ ├── .env
│ ├── requirements.txt
│ ├── server.py
├── readme.md

Описание пакетов:

Flask: Фреймворк для создания веб-приложений на языке Python. Предоставляет базовую структуру и инструменты для веб-разработки.

Flask-CORS: Расширение для Flask, позволяющее решать проблемы с Cross-Origin Resource Sharing (CORS), обеспечивая безопасное взаимодействие между веб-страницами/приложениями в разных источниках (доменах).

Flask-Validator: Дополнение для Flask, предоставляющее возможности валидации данных во Flask-приложениях. (Примечание: Обычно в Flask используются библиотеки валидации типа WTForms.)

WTForms: Библиотека для создания веб-форм в приложениях Flask (и других фреймворках). Предоставляет инструменты для создания и валидации веб-форм на основе классов Python.

pymongo: Библиотека для работы с MongoDB из приложений Python. Предоставляет API для взаимодействия с базой данных MongoDB.

mongoengine: ORM (Object-Document Mapping) для MongoDB, предоставляющая более высокоуровневые абстракции для работы с базой данных, позволяя вам взаимодействовать с MongoDB как с объектами Python.

python-dotenv: Пакет, позволяющий загружать переменные окружения из файлов .env в проекте Python. Позволяет удобно управлять конфигурацией приложения через переменные окружения.

PyJWT: Библиотека для работы с JSON Web Tokens (JWT) в Python. Предоставляет возможности создания, проверки и управления JWT для аутентификации и обмена данными между сторонами.

bcrypt: Библиотека для хеширования паролей в Python. Часто используется для безопасного хранения паролей в базе данных путем их хеширования. Предоставляет алгоритм хеширования bcrypt, который считается более безопасным и медленным, что затрудняет атаки перебором на основе словарей.

- [x] Задача 1 Создать Онлайн с онлайн игроками!!!
