from rest_framework.permissions import BasePermission
from users.models import UserCar


class ProviderPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == UserCar.Roles.PROVIDER
