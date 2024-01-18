class ApiError(Exception):
    def __init__(self, status, message=None, errors=None):
        super().__init__(message)
        self.status = status
        self.message = message if message is not None else 'Ошибка сервера'
        self.errors = errors if errors is not None else []

    @staticmethod
    def unauthorized_error():
        return ApiError(401, 'Пользователь не авторизован')

    @staticmethod
    def bad_request(message=None, errors=None):
        return ApiError(400, message, errors)
