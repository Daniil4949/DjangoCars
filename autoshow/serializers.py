from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import AutoShow
from users.models import DesirableAuto


class AutoShowSerializer(ModelSerializer):
    name = serializers.CharField(
        max_length=30,
        validators=[UniqueValidator(queryset=AutoShow.objects.all())]
    )
    balance = serializers.IntegerField(min_value=0)

    class Meta:
        model = AutoShow
        fields = ("name", "location", "balance", "customers")
        read_only_fields = ("name", "location", "user", "balance")


class AutoShowUpdateSerializer(ModelSerializer):
    name = serializers.CharField(
        max_length=30,
        validators=[UniqueValidator(queryset=AutoShow.objects.all())]
    )
    balance = serializers.IntegerField(min_value=0)

    class Meta:
        model = AutoShow
        fields = ("id", "name", "balance", "location", "customers", "user")
        read_only_fields = ("id", "balance", "customers", "user")


class DesirableAutoReadSerializer(ModelSerializer):
    class Meta:
        model = DesirableAuto
        fields = ("mark", "model", "price", "autoshow")
        read_only_fields = ("autoshow",)


class DesirableAutoSerializer(ModelSerializer):
    class Meta:
        model = DesirableAuto
        fields = ("mark", "model", "price")


