import pytest
from users.models import UserCar


@pytest.mark.django_db
def test_user_customer_create():
    new_user = UserCar.objects.create(username="customer", email="customer@gmail.com")
    assert new_user.__str__() == "customer - customer"


@pytest.mark.django_db
def test_user_autoshow_create():
    new_user = UserCar.objects.create(username="autoshow", email="autoshow@gmail.com", role="autoshow")
    assert new_user.__str__() == "autoshow - autoshow"


