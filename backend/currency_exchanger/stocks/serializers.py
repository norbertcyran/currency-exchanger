from rest_framework import serializers

from currency_exchanger.stocks.models import Stock


class StockSerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField()

    class Meta:
        model = Stock
        fields = ("id", "symbol", "currency", "price")


class StockHistorySerializer(serializers.ModelSerializer):
    stock = serializers.StringRelatedField()

    class Meta:
        model = Stock
        fields = ("id", "stock", "price", "timestamp")
