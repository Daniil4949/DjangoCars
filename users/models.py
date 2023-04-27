from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserCar(AbstractUser):
    class Roles(models.TextChoices):
        PROVIDER = 'provider'
        CUSTOMER = 'customer'
        AUTOSHOW = 'autoshow'

    email = models.EmailField(unique=True)
    role = models.CharField(choices=Roles.choices, default=Roles.CUSTOMER)
    is_blocked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"


class Provider(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"


class Customer(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"


class AutoShow(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"
