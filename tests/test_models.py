import pytest
from users.models import UserCar, Customer, AutoShow, Provider


@pytest.mark.django_db
def test_user_customer_create():
    new_user = UserCar.objects.create(username="customer", email="customer@gmail.com")
    assert new_user.__str__() == "customer - customer"


@pytest.mark.django_db
def test_user_autoshow_create():
    new_user = UserCar.objects.create(username="autoshow", email="autoshow@gmail.com", role="autoshow")
    assert new_user.__str__() == "autoshow - autoshow"


@pytest.mark.django_db
def test_user_provider_create():
    new_user = UserCar.objects.create(username="provider", email="provider@gmail.com", role="provider")
    assert new_user.__str__() == "provider - provider"


@pytest.mark.django_db
def test_user_signals_working():
    new_user = UserCar.objects.create(username="customer", email="customer@gmail.com", role="customer")
    new_customer = Customer.objects.filter(user=new_user).first()
    assert new_user.username == new_customer.name


@pytest.mark.django_db
def test_autoshow_user_signals():
    new_user = UserCar.objects.create(username="autoshow", email="autoshow@gmail.com", role="autoshow")
    new_autoshow = AutoShow.objects.filter(user=new_user).first()
    assert new_user.username == new_autoshow.name


@pytest.mark.django_db
def test_provider_user_signals():
    new_user = UserCar.objects.create(username="provider", email="provider@gmail.com", role="provider")
    new_provider = Provider.objects.filter(user=new_user).first()
    assert new_user.username == new_provider.name
