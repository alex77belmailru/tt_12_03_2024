from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models import *
from api.validators import *


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор юзера для методов кроме создания юзера"""

    class Meta:
        model = User
        fields = ('id', 'email', 'referral_code')


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор, используемый при создании юзера"""

    class Meta:
        model = User
        fields = ('id', 'email', 'referral_code', 'password')
        validators = [CodeGetValidator(field='referral_code')]

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = User.objects.create(
            email=self.validated_data.get('email'),
            referral_code=self.validated_data['referral_code']
        )
        user.set_password(password)  # хэширует пароль для хранения в бд
        user.save()
        return user


class UsersCodeSerializer(serializers.ModelSerializer):
    """Сериализатор для Класса получения реферального кода по email адресу реферера"""

    referral = SerializerMethodField()

    def get_referral(self, obj):
        referral = Referral.objects.filter(owner=obj, is_active=True).first()  # находим код
        if referral:
            if referral.expiration < datetime.now():  # проверка срока годности
                referral.is_active = False  # деактивация при просрочке
                referral.save()
            else:
                return f'Код {referral.code}, действует до {referral.expiration}'  # возвращаем код
        return f'У пользователя нет активного реферального кода.'

    class Meta:
        model = User
        fields = ('email', 'referral')


class ReferralSerializer(serializers.ModelSerializer):
    """Сериализатор для класса Реферальный код"""

    def validate(self, attrs):  # если активируем код, деактивируем другие активные коды у юзера, если такие есть
        if attrs['is_active']:
            if self.instance:  # изменение - экземпляр существует, берем юзера из экземпляра
                active_referrals = Referral.objects.filter(owner=self.instance.owner, is_active=True).first()
            else:  # создание - берем юзера из запроса
                active_referrals = Referral.objects.filter(owner=self.context['request'].user, is_active=True).first()
            if active_referrals:
                active_referrals.is_active = False
                active_referrals.save()
        return attrs

    class Meta:
        model = Referral
        fields = ('id', 'code', 'expiration', 'is_active')
        validators = [CodeCreateValidator(field='code')]
