
class UserDto:
    def __init__(self, model):
        # Инициализация свойств объекта UserDto на основе модели пользователя

        # Присваиваем свойству email значение поля email из модели пользователя
        self.email = getattr(model, 'email', None)

        # Преобразуем значение _id (предполагая, что это ObjectId) в строку и присваиваем свойству id
        self.id = str(getattr(model, 'user_id', None))

        # Проверяем наличие атрибута isActivated в модели пользователя
        self.isActivated = getattr(model, 'isActivated', False)

      
