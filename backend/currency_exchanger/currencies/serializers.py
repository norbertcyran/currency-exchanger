from currency_exchanger.currencies.models import (
    Currency,
    CurrencyExchange,
    CurrencyHistory,
    CurrencyTransfer,
    WalletCurrency,
)
from currency_exchanger.exceptions import NotEnoughFundsAPIException
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
    id = serializers.ReadOnlyField(source="currency.id")
    code = serializers.ReadOnlyField(source="currency.code")
    rate = serializers.ReadOnlyField(source="currency.rate")

    class Meta:
        model = WalletCurrency
        fields = ("id", "code", "rate", "amount")


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    currency_from = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    currency_to = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = CurrencyExchange
        fields = ("id", "currency_from", "currency_to", "amount")

    def validate(self, attrs):
        wallet = self.context["request"].user.wallet
        currency = attrs["currency_from"]
        wallet_currency, _ = WalletCurrency.objects.get_or_create(wallet=wallet, currency=currency)

        if currency == attrs["currency_to"]:
            raise serializers.ValidationError("Can't exchange two the same currencies.")

        if wallet_currency.amount < attrs["amount"]:
            raise NotEnoughFundsAPIException

        if currency == attrs["currency_to"]:
            raise serializers.ValidationError("Can't exchange two the same currencies.")

        return attrs


class CurrencyTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyTransfer
        fields = ("id", "currency", "amount")
