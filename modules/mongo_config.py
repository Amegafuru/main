from dotenv import load_dotenv
from mongoengine import connect
import os

# Загрузка переменных среды из файла .env
load_dotenv()

# def get_mongo_connection_string():
#     ATLAS_USERNAME = os.getenv("ATLAS_USERNAME")
#     ATLAS_PASSWORD = os.getenv("ATLAS_PASSWORD")
#     ATLAS_CLUSTER = os.getenv("ATLAS_CLUSTER")
#     ATLAS_DB_NAME = os.getenv("ATLAS_DB_NAME")

#     # Формирование строки подключения к MongoDB Atlas
#     ATLAS_CONNECTION_URL = f"mongodb+srv://{ATLAS_USERNAME}:{ATLAS_PASSWORD}@{ATLAS_CLUSTER}/{ATLAS_DB_NAME}?retryWrites=true&w=majority"
#     return ATLAS_CONNECTION_URL, ATLAS_DB_NAME

def get_mongo_connection_string():
    ATLAS_USERNAME = os.getenv("ATLAS_USERNAME")
    ATLAS_PASSWORD = os.getenv("ATLAS_PASSWORD")
    ATLAS_CLUSTER = os.getenv("ATLAS_CLUSTER")
    ATLAS_DB_NAME = os.getenv("ATLAS_DB_NAME")
    # Формирование строки подключения к MongoDB Atlas
    # ATLAS_CONNECTION_URL = f"mongodb+srv://{ATLAS_USERNAME}:{ATLAS_PASSWORD}@{ATLAS_CLUSTER}/{ATLAS_DB_NAME}?retryWrites=true&w=majority"
    # return ATLAS_CONNECTION_URL, ATLAS_DB_NAME

    ATLAS_CONNECTION_URL = f"mongodb+srv://{ATLAS_USERNAME}:{ATLAS_PASSWORD}@{ATLAS_CLUSTER}/?retryWrites=true&w=majority"
    return ATLAS_CONNECTION_URL, ATLAS_DB_NAME

# Получение строки подключения и имени базы данных
connection_string, db_name = get_mongo_connection_string()

# Подключение к базе данных MongoDB
connect(
    db=db_name,
    host=connection_string,
)