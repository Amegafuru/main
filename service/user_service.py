import bcrypt
import uuid
from models.user_model import UserModel
from service.mail_service import MailService
from service.token_service import TokenService
from dtos.user_dto import UserDto
from exceptions.api_error import ApiError

class UserService:
    async def registration(self, email, password, username):
        # Предположим, что UserModel.find_one, UserModel.create и mail_service.send_activation_mail определены соответствующим образом
        candidate = UserModel.find_one({"email": email})
        if candidate:
            raise ApiError.bad_request(f"Пользователь c почтовым адресом {email} уже существует")

        hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        activation_link = str(uuid.uuid4())

        user = UserModel.create(username=username, email=email, password=hash_password, activation_link=activation_link)

        # Преобразуйте user.id к строке, чтобы использовать в payload
        # TODO: ДОДЕЛАТЬ ПОЧТУ, ОТПРАВКУ ПИСЬМА И ТД
        # mail_service = MailService()  # Создаем экземпляр MailService
        # await mail_service.send_activation_mail(email, f"{os.getenv('API_URL')}/api/activate/{activation_link}")

        user_dto = UserDto(user)  # id, email, isActivated
         # Создаем payload для токена
        payload = {
            'email': user_dto.email,
            'isActivated': user_dto.isActivated
        }

        tokens = await TokenService.generate_tokens(payload)
        TokenService.save_token(user_dto.id, tokens['refreshToken'])

        return {**tokens, "user": user_dto.__dict__}
    


    async def login(self, email, password):
        # Найдем пользователя по email в базе данных
        user = UserModel.find_one({"email": email})
        
        # Если пользователь не найден, выбрасываем ошибку
        if not user:
            raise ApiError.bad_request("Пользователь с указанным email не найден")

        # Проверяем введенный пароль с хэшированным паролем в базе данных
        if not bcrypt.checkpw(password.encode(), user['password'].encode()):
            raise ApiError.bad_request("Неверный пароль")

        

        # Создаем payload для токена
        payload = {
            'email': user['email']
        }

        # Генерируем токены
        tokens = await TokenService.generate_tokens(payload)

        # Сохраняем refreshToken в базе данных
        TokenService.save_token(user['id'], tokens['refreshToken'])

        # Возвращаем токены и информацию о пользователе
        return {
    **tokens,
    "user": {
        "id": str(user['id']),
        "username": user['username'],
        "email": user['email'],
        "is_activated": user['is_activated'],
        "activation_link": user['activation_link'],
        "user_money": user['user_money'],
        "user_level": user['user_level'],
        "user_experience": user['user_experience'],
        "user_image": user['user_image'],
        "user_max_health": user['user_max_health'],
        "user_strength": user['user_strength'],
        "user_strength_total": user['user_strength_total'],
        "user_endurance": user['user_endurance'],
        "user_endurance_total": user['user_endurance_total'],
        "user_accuracy": user['user_accuracy'],
        "user_accuracy_total": user['user_accuracy_total'],
        "user_dexterity": user['user_dexterity'],
        "user_dexterity_total": user['user_dexterity_total'],
        "user_cur_health": user['user_cur_health'],
        "user_cur_endurance": user['user_cur_endurance'],
        "user_next_experience": user['user_next_experience'],
        "user_unused_points": user['user_unused_points'],
        "user_max_weight": user['user_max_weight'],
        "user_helmet_slot": user['user_helmet_slot'],
        "user_armor_slot": user['user_armor_slot'],
        "user_bracers_slot": user['user_bracers_slot'],
        "user_boots_slot": user['user_boots_slot'],
        "user_neckla_slot": user['user_neckla_slot'],
        "user_ring_slot": user['user_ring_slot'],
        "user_sword_slot": user['user_sword_slot'],
        "user_shield_slot": user['user_shield_slot'],
        "user_cristall1_slot": user['user_cristall1_slot'],
        "user_cristall2_slot": user['user_cristall2_slot'],
        "user_cristall3_slot": user['user_cristall3_slot'],
        "user_cristall4_slot": user['user_cristall4_slot'],
        "user_cristall5_slot": user['user_cristall5_slot'],
        "user_cristall6_slot": user['user_cristall6_slot'],
        "user_cristall7_slot": user['user_cristall7_slot'],
        "user_cristall8_slot": user['user_cristall8_slot'],
        "user_battles_total": user['user_battles_total'],
        "user_battles_won": user['user_battles_won'],
        "user_battles_lost": user['user_battles_lost'],
        "user_battles_draw": user['user_battles_draw'],
    }
}
    

    

