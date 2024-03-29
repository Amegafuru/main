from flask import request, jsonify
from exceptions.api_error import ApiError
from service.token_service import TokenService

def authMiddleware(next):
    def middleware():
        try:
            authorizationHeader = request.headers.get('Authorization')

            if not authorizationHeader:
                return ApiError().UnauthorizedError()

            accessToken = authorizationHeader.split()[1] if ' ' in authorizationHeader else None

            if not accessToken:
                return ApiError().UnauthorizedError()

            userData = TokenService.validateAccessToken(accessToken)

            if not userData:
                return ApiError().UnauthorizedError()

            request.user = userData
            return next()

        except Exception as e:
            return ApiError().UnauthorizedError()
    return middleware

# from flask import request, jsonify
# from exceptions.api_error import ApiError
# from service.token_service import TokenService

# def authMiddleware(request, response, next):
#     try:
#         authorizationHeader = request.headers.get('Authorization')

#         if not authorizationHeader:
#             return ApiError().UnauthorizedError()  # Возвращаем ошибку "Unauthorized" в случае отсутствия заголовка авторизации

#         accessToken = authorizationHeader.split()[1] if ' ' in authorizationHeader else None

#         if not accessToken:
#             return ApiError().UnauthorizedError()  # Возвращаем ошибку "Unauthorized" если отсутствует токен доступа

#         userData = TokenService.validateAccessToken(accessToken)

#         if not userData:
#             return ApiError().UnauthorizedError()  # Возвращаем ошибку "Unauthorized" если токен недействителен или отсутствуют данные пользователя

#         # Добавление данных пользователя в объект request для использования в последующих обработчиках
#         request.user = userData
#         next()

#     except Exception as e:
#         return ApiError().UnauthorizedError()  # Обработка других исключений с возвратом ошибки "Unauthorized"
