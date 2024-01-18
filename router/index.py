from flask import jsonify, Blueprint
from controllers.user_controller import UserController
from flask import request
from flask_validator import ValidateEmail
from middlewares.auth_middleware import authMiddleware
import asyncio

from exceptions.api_error import ApiError

# Создаем Blueprint для маршрутов
router = Blueprint('router', __name__)

# Создаем экземпляр UserController
user_controller = UserController()

# Проверка параметров с использованием flask_validator для email
# validate_email = ValidateEmail(field='email')

# Роуты
@router.route('/registration', methods=['POST', 'OPTIONS'])
# @validate_email.params('password')
def registration_route():
    if request.method == 'OPTIONS':
        response = jsonify(success=True)
        response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') 
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    else:
        # Ваша логика обработки POST-запроса
        return asyncio.run(user_controller.registration(request))

@router.route('/login', methods=['POST'])
def login_route():
    try:
        return asyncio.run(user_controller.login(request))
    except ApiError as e:
        return jsonify(error=str(e)), 400  # Возвращаем ош

@router.route('/logout', methods=['POST'])
def logout_route():
    return user_controller.logout(request)

@router.route('/activate/<link>', methods=['GET'])
def activate_route(link):
    return user_controller.activate(link)

@router.route('/refresh', methods=['GET'])
def refresh_route():
    return user_controller.refresh(request)

@router.route('/users', methods=['GET'])
@authMiddleware
def getUsers_route():
    return user_controller.get_users(request)

# Другие роуты...