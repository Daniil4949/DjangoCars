from users.models import AutoShow, Customer, Provider, UserCar
from django.db import transaction


@transaction.atomic()
def change_username(user: UserCar, username):
    role: str = user.role
    user.username = username
    user.save()
    match role:
        case UserCar.Roles.AUTOSHOW:
            autoshow = AutoShow.objects.get(user=user)
            autoshow.name = user.username
            autoshow.save()
        case UserCar.Roles.CUSTOMER:
            customer = Customer.objects.get(user=user)
            customer.name = user.username
            customer.save()
        case UserCar.Roles.PROVIDER:
            provider = Provider.objects.get(user=user)
            provider.name = user.username
            provider.save()
