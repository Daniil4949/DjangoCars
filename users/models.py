from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class UserCar(AbstractUser):
    class Roles(models.TextChoices):
        PROVIDER = 'provider'
        CUSTOMER = 'customer'
        AUTOSHOW = 'autoshow'

    email = models.EmailField(unique=True)
    role = models.CharField(choices=Roles.choices, default=Roles.CUSTOMER, max_length=8)
    is_blocked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"


class Provider(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    year_of_foundation = models.IntegerField(null=True, blank=True,
                                             validators=[
                                                 MinValueValidator(1900),
                                                 MaxValueValidator(date.today().year)])

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"


class Customer(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    balance = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"


class AutoShow(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    location = CountryField(null=True, blank=True)
    balance = models.PositiveBigIntegerField(default=0)
    customers = models.ManyToManyField(Customer)

    def __str__(self) -> str:
        return f"{self.name} - {self.user}"


class DesirableAuto(models.Model):
    mark = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)
    autoshow = models.OneToOneField(AutoShow, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Desirable car characteristic. {self.mark} - {self.model}. Price: {self.price}"


class Auto(DesirableAuto):
    count = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"Autoshow car. {self.mark} - {self.model}. Price: {self.price}. Count: {self.count}"


class AutoProvider(DesirableAuto):
    count = models.PositiveIntegerField(default=1)
    provider = models.OneToOneField(Provider, on_delete=models.PROTECT)


class SoldAuto(DesirableAuto):
    count = models.PositiveIntegerField(default=1)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"Sold car. {self.mark} - {self.model}. Price: {self.price}. Customer - {self.customer.name}"
