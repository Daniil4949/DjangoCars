import factory
from users.models import UserCar
from faker import Faker

fake = Faker()


class UserCustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserCar

    username = "customer"


# class UserAutoShowFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = UserCar
#
#     username = "autoshow"
#     role = "autoshow"
