from currency_exchanger.stocks.models import Stock, StockTransfer, WalletStock
from currency_exchanger.validators import validate_stock_transaction
from rest_framework import serializers


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
        fields = ("id", "symbol", "currency", "price", "count")


class StockTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransfer
        fields = ("stock", "amount")
        read_only_fields = ["wallet"]

    def validate(self, attrs):
        wallet = self.context["request"].user.wallet
        validate_stock_transaction(wallet, attrs["stock"])
        return attrs
