from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    referral_code = models.CharField(max_length=5, default=None, **NULLABLE, verbose_name='Реферальный код')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)


class Referral(models.Model):
    """МОдель реферального кода"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец')
    code = models.CharField(max_length=5, unique=True, verbose_name='Код (5 цифр)')
    expiration = models.DateTimeField(verbose_name='Срок годности до',
                                      default=datetime.now().replace(microsecond=0))
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    def __str__(self):
        return f'{self.code}'

    class Meta:
        verbose_name = 'Реферальный код'
        verbose_name_plural = 'Реферальные коды'
        ordering = ('id',)

