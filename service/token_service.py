from models.user_model import UserModel
from jwt import encode as jwt_encode
from jwt import decode as jwt_decode
import os
from models.token_model import TokenModel
from datetime import datetime, timedelta

from bson import ObjectId
from mongoengine import DoesNotExist

class TokenService:
    @classmethod
    async def generate_tokens(cls, payload):
        access_token_exp = datetime.utcnow() + timedelta(seconds=15)  # Время истечения через 15 секунд
        refresh_token_exp = datetime.utcnow() + timedelta(seconds=30)  # Время истечения через 30 секунд

        access_token_payload = {**payload, 'exp': access_token_exp}
        refresh_token_payload = {**payload, 'exp': refresh_token_exp}

        access_token = jwt_encode(access_token_payload, os.getenv('JWT_ACCESS_SECRET'), algorithm='HS256')
        refresh_token = jwt_encode(refresh_token_payload, os.getenv('JWT_REFRESH_SECRET'), algorithm='HS256')

        return {
            'accessToken': access_token,
            'refreshToken': refresh_token
        }

    def validate_access_token(self, token):
        try:
            decoded_token = jwt_decode(token, os.getenv('JWT_ACCESS_SECRET'), algorithms=['HS256'])
            return decoded_token
        except jwt_decode.ExpiredSignatureError:
            return None

    def validate_refresh_token(self, token):
        try:
            decoded_token = jwt_decode(token, os.getenv('JWT_REFRESH_SECRET'), algorithms=['HS256'])
            return decoded_token
        except jwt_decode.ExpiredSignatureError:
            return None
        
    @classmethod
    async def save_token(cls, id, refresh_token):
        try:
            user = UserModel.objects(id=ObjectId(id)).first()
            token_data = await TokenModel.objects(user=user).first() 
            if token_data:
                token_data['refreshToken'] = refresh_token
                return await token_data.save()
            token = await TokenModel.create(user=user, refreshToken=refresh_token)
            return token
        except DoesNotExist:
            # Обработка случая, когда пользователя с указанным идентификатором не найдено
            return None

    async def remove_token(self, refresh_token):
        return await TokenModel.delete_one({'refreshToken': refresh_token})

    async def find_token(self, refresh_token):
        return await TokenModel.find_one({'refreshToken': refresh_token})
