from rest_framework import serializers

from currency_exchanger.currencies.models import Currency, CurrencyHistory, WalletCurrency


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