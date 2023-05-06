from rest_framework.permissions import BasePermission
from users.models import UserCar


class ProviderPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserCar.Roles.PROVIDER


class AutoShowPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserCar.Roles.AUTOSHOW


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserCar.Roles.CUSTOMER
