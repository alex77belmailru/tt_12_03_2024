from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.permissions import *
from api.serializers import *


class UserModelViewSet(viewsets.ModelViewSet):
    """Класс для работы с моделью 'Пользователь'"""
    queryset = User.objects.all()
    permission_classes = [UserPermissions]

    def get_serializer_class(self, **kwargs):  # выбор сериализатора
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def list(self, request, *args, **kwargs):  # получение списка юзеров
        if request.user.is_anonymous:  # для просмотра списка нужна авторизация
            raise serializers.ValidationError('Для просмотра списка пользователей необходимо авторизоваться')

        if request.user.is_staff:  # модератор видит все
            queryset = self.queryset.order_by('id')
        else:  # не-модератор видит свой
            queryset = User.objects.filter(pk=request.user.pk)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UsersCodeRetrieveAPIView(RetrieveAPIView):
    """Класс для получения реферального кода по email адресу реферера"""
    permission_classes = [UserPermissions]
    queryset = User.objects.all()
    serializer_class = UsersCodeSerializer
    lookup_field = 'email'


class UsersIdListAPIView(ListAPIView):
    """Класс для получения информации о рефералах по ID реферера"""
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        referrer = User.objects.filter(pk=self.kwargs['pk']).first()
        code = Referral.objects.filter(owner=referrer, is_active=True).first()
        queryset = User.objects.filter(referral_code=code)
        return queryset


class ReferralModelViewSet(viewsets.ModelViewSet):
    """Класс для работы с моделью 'Реферальный код'"""

    permission_classes = [IsAdminUser | IsOwner]
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    def perform_create(self, serializer):  # получение текущего авторизованного пользователя
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):  # получение списка кодов
        if request.user.is_anonymous:  # для просмотра списка нужна авторизация
            return Response(data=None)

        if request.user.is_staff:  # модератор видит все коды
            queryset = self.queryset.order_by('id')
        else:  # не-модератор видит список своих кодов
            queryset = Referral.objects.filter(owner=request.user)

        serializer = ReferralSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):  # создание кода
        if request.user.is_anonymous:
            raise serializers.ValidationError('Для создания реферального кода необходимо авторизоваться.')
        self.check_expiration(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_expiration(request)
        return super().update(request, *args, **kwargs)

    @staticmethod
    def check_expiration(request):  # проверка возможности установки статуса активности кода
        if request.data.get('is_active'):
            if not request.data['expiration'] or datetime.strptime(request.data['expiration'],
                                                                   "%Y-%m-%dT%H:%M") < datetime.now():
                raise serializers.ValidationError('Срок годности кода истек, код не может быть активным.')
