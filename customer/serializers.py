from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import Customer


class CustomerSerializer(ModelSerializer):
    name = serializers.CharField(
        max_length=30,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    balance = serializers.IntegerField(min_value=0)

    class Meta:
        model = Customer
        fields = ("name", "balance", "user")
        read_only_fields = ("user", "balance")
