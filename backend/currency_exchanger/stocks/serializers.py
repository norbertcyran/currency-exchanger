from rest_framework import serializers

from currency_exchanger.stocks.models import Stock, WalletStock


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


class WalletStockSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="stock.id")
    symbol = serializers.ReadOnlyField(source="stock.symbol")
    currency = serializers.StringRelatedField(source="stock.currency")
    price = serializers.ReadOnlyField(source="stock.price")

    class Meta:
        model = WalletStock
        fields = ("id", "symbol", "currency", "price", "amount")
