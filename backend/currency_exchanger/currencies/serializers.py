from currency_exchanger.currencies.models import (
    Currency,
    CurrencyExchange,
    CurrencyHistory,
    WalletCurrency,
)
from currency_exchanger.validators import validate_transaction
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "country", "rate")


class CurrencyHistorySerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField()

    class Meta:
        model = CurrencyHistory
        fields = ("id", "currency", "rate", "timestamp")


class WalletCurrencySerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code", read_only=True)

    class Meta:
        model = WalletCurrency
        fields = ("currency", "amount")


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    currency_from = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    currency_to = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = CurrencyExchange
        fields = ("id", "currency_from", "currency_to", "amount","amount_to")
        read_only_fields = ["amount_to"]

    def validate(self, attrs):
        wallet = self.context["request"].user.wallet
        currency = attrs["currency_from"]

        if currency == attrs["currency_to"]:
            raise serializers.ValidationError("Can't exchange two the same currencies.")

        validate_transaction(wallet, currency, attrs["amount"])

        return attrs
