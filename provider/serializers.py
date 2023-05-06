from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import Provider
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class ProviderSerializer(ModelSerializer):
    name = serializers.CharField(
        max_length=30,
        validators=[UniqueValidator(queryset=Provider.objects.all())]
    )
    year_of_foundation = serializers.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(date.today().year)
        ]
    )

    class Meta:
        model = Provider
        fields = ("name", "year_of_foundation")
