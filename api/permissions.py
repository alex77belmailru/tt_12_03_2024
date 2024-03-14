from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка, что пользователь - владелец"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class UserPermissions(BasePermission):
    """Проверка текущего пользователя на владельца или суперюзера"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser
