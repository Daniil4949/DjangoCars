import pytest
from pytest_factoryboy import register
from tests.factory import UserCustomerFactory # UserAutoShowFactory
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cars.test_settings')

register(UserCustomerFactory)
# register(UserAutoShowFactory)


@pytest.fixture
def customer(db, customer_factory):
    new_customer = customer_factory.create()
    return new_customer


# @pytest.fixture()
# def autoshow(db, autoshow_factory):
#     new_autoshow = autoshow_factory.create()
#     return new_autoshow
