from rest_framework import serializers

from currency_exchanger.currencies.models import Currency, CurrencyHistory


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "country", "rate")


class CurrencyHistorySerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField()

    class Meta:
        model = CurrencyHistory
        fields = ("id", "currency", "rate", "timestamp")
