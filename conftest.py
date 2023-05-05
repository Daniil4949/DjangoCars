import pytest
from pytest_factoryboy import register
from tests.factory import UserCustomerFactory
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cars.test_settings')

register(UserCustomerFactory)


@pytest.fixture
def customer(db, customer_factory):
    new_customer = customer_factory.create()
    return new_customer


