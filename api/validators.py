from rest_framework.serializers import ValidationError

from api.models import Referral


class CodeCreateValidator:
    """Проверка длины реф.кода при создании"""

    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        code = dict(data).get(self.field)
        if len(code) != 5 or not code.isdigit():
            raise ValidationError('Код должен быть 5-значной цифрой.')


class CodeGetValidator:
    """Проверка наличия реф.кода в БД"""

    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        code = dict(data).get(self.field)
        if not code:  # регистрация без кода
            return True
        if not Referral.objects.filter(code=code, is_active=True).exists():  # код должен быть активен
            raise ValidationError('Активный реферальный код не найден.')
