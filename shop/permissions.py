from rest_framework.permissions import BasePermission


class IsCartOwner(BasePermission):
    """ Разрешение, которое проверяет, что пользователь является владельцем корзины. """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user