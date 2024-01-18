from mongoengine import Document, StringField, BooleanField, ObjectIdField, IntField
import bson

class UserModel(Document):
    user_id = ObjectIdField(unique=True)
    username = StringField()
    email = StringField(unique=True, required=True)
    password = StringField(required=True)
    is_activated = BooleanField(default=False)
    activation_link = StringField()

    # Характеристики персонажа

    # Деньги персонажа
    user_money = IntField(default=200)
    # Уровень персонажа
    user_level = IntField(default=0)
    # Опыт персонажа
    user_experience = IntField(default=0)
    # Путь к изображению персонажа на фронтенде (путь относительно папки 'public')
    user_image = StringField(default='avatars/avatar.png')

    # Максимальное здоровье с учетом вещей
    user_max_health = IntField(default=20)

    
    user_battles_total = IntField(default=0)      # Количество всего битв
    user_battles_won = IntField(default=0)        # Количество побед
    user_battles_lost = IntField(default=0)       # Количество поражений
    user_battles_draw = IntField(default=0)       # Количество ничьих
   


    # Сила персонажа
    user_strength = IntField(default=3)
    # Сила персонажа с учетом вещей
    user_strength_total = IntField(default=3)

    # Выносливость персонажа
    user_endurance = IntField(default=3)
    # Выносливость персонажа с учетом вещей
    user_endurance_total = IntField(default=3)

    # Точность персонажа
    user_accuracy = IntField(default=3)
    # Точность персонажа с учетом вещей
    user_accuracy_total = IntField(default=0)

    # Ловкость персонажа
    user_dexterity = IntField(default=3)
    # Ловкость персонажа с учетом вещей
    user_dexterity_total = IntField(default=0)


    # Текущее здоровье во время боя
    user_cur_health = IntField(default=0)
    # Текущяя выносливость во время боя
    user_cur_endurance = IntField(default=0)

    
    # Следующая граничная точка опыта
    user_next_experience = IntField(default=10)
    # Неиспользованные очки для распределения в статы (сила, ловкость и т. д.)
    user_unused_points = IntField(default=3)


    # Максимальный вес предметов в рюкзаке
    user_max_weight = IntField(default=20)

    # Слоты для экипировки (шлем, щит, оружие и так далее)
    # Левая сторона
    user_helmet_slot = IntField(default=0)
    user_armor_slot = IntField(default=0)
    user_bracers_slot = IntField(default=0)
    user_boots_slot = IntField(default=0)

    #Правая сторона
    user_neckla_slot = IntField(default=0)
    user_ring_slot = IntField(default=0)
    user_sword_slot = IntField(default=0)
    user_shield_slot = IntField(default=0)
    
    #Кристаллы
    user_cristall1_slot = IntField(default=0)
    user_cristall2_slot = IntField(default=0)
    user_cristall3_slot = IntField(default=0)
    user_cristall4_slot = IntField(default=0)
    user_cristall5_slot = IntField(default=0)
    user_cristall6_slot = IntField(default=0)
    user_cristall7_slot = IntField(default=0)
    user_cristall8_slot = IntField(default=0)

    meta = {'collection': 'users'}

    @classmethod
    def find_one(cls, query):
        return cls.objects(**query).first()

    @staticmethod
    def create(**kwargs):
        new_user = UserModel(**kwargs)
        new_user.user_id = bson.ObjectId()
        new_user.save()
        return new_user

    async def save_async(self):
        # Асинхронно сохраняем пользователя с использованием MongoEngine
        await self.save()