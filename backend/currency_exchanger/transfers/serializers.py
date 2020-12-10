from currency_exchanger.currencies.models import Currency
from currency_exchanger.transfers.models import MoneyTransfer
from currency_exchanger.users.serializers import UserSerializer
from currency_exchanger.validators import validate_transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class MoneyTransferWriteSerializer(serializers.ModelSerializer):
    user_to = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = MoneyTransfer
        fields = ("id", "user_to", "currency", "amount")

    def validate(self, attrs):
        wallet = self.context["request"].user.wallet

        if self.context["request"].user == attrs["user_to"]:
            raise ValidationError("Can't send transfer to yourself.")

        validate_transaction(wallet, attrs["currency"], attrs["amount"])

        return attrs


class MoneyTransferReadSerializer(serializers.ModelSerializer):
    user_from = UserSerializer()
    user_to = UserSerializer()
    currency = serializers.CharField(source="currency.code")

    class Meta:
        model = MoneyTransfer
        fields = ("id", "user_from", "user_to", "currency", "amount", "timestamp")
