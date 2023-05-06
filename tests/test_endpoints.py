import pytest
from django.urls import reverse
from rest_framework import status
from users.models import UserCar
from django.test import Client


@pytest.mark.django_db
def test_anonymous_user():
    client = Client()
    url = reverse("all-autoshows")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
