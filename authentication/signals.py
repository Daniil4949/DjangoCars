from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserCar
from users.models import Customer, AutoShow, Provider


@receiver(post_save, sender=UserCar)
def create_instances(sender, instance, created, **kwargs):
    if created:
        role = instance.role
        match role:
            case UserCar.Roles.CUSTOMER:
                customer = Customer.objects.create(name=instance.username, user=instance)
                customer.save()
            case UserCar.Roles.PROVIDER:
                provider = Provider.objects.create(name=instance.username, user=instance)
                provider.save()
            case UserCar.Roles.AUTOSHOW:
                autoshow = AutoShow.objects.create(name=instance.username, user=instance)
                autoshow.save()
