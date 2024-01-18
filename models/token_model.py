from mongoengine import Document, StringField, ReferenceField
from models.user_model import UserModel  # Импортируем модель User

class TokenModel(Document):
    user = ReferenceField(UserModel)  # Обновляем ссылку на модель User
    refreshToken = StringField(required=True)