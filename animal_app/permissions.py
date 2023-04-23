from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Разрешение на чтение только для анонимных пользователей,
    но требует аутентификации для любых других методов.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на изменение только для владельцев объектов.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user