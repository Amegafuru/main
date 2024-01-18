from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

from modules.mongo_config import get_mongo_connection_string
from middlewares.error_middleware import error_middleware
from router.index import router

# Загрузка переменных среды из файла .env
load_dotenv()

client_url = os.environ.get('CLIENT_URL')

# Создание экземпляра Flask
app = Flask(__name__)

# Настройка CORS
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

# Загрузка переменных среды из файла .env
port = os.getenv("PORT")
host = os.getenv("API_URL")

# Получение строки подключения и имени базы данных из модуля mongo_config
ATLAS_CONNECTION_URL, ATLAS_DB_NAME = get_mongo_connection_string()

# Подключение к серверу MongoDB Atlas
try:
    client = MongoClient(ATLAS_CONNECTION_URL)
    db = client[ATLAS_DB_NAME]  # Выбор базы данных
    print("Подключение к MongoDB Atlas успешно.")
except Exception as e:
    print(f"Ошибка подключения к MongoDB Atlas: {e}")

# Применение маршрутов
app.register_blueprint(router, url_prefix='/api')

# Вывод всех зарегистрированных маршрутов
@app.route('/list_routes', methods=['GET'])
def list_routes():
    output = "<table border='1'>"
    output += "<tr><th>URL</th><th>Методы</th><th>Функция обработчика</th></tr>"
    for rule in app.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        line = f"<tr><td>{str(rule)}</td><td>{methods}</td><td>{rule.endpoint}</td></tr>"
        output += line
    output += "</table>"
    return output

# Обработчик для разрешения CORS на методы OPTIONS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Подключение обработчика ошибок
app.register_error_handler(Exception, error_middleware)

if __name__ == '__main__':
    app.run(host=host, port=port)  # Запуск сервера на порте 5000