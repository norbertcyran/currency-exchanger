from currency_exchanger.stocks.models import Stock, StockHistory, StockTransfer, WalletStock
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
        model = StockHistory
        fields = ("id", "stock", "price", "timestamp")


class WalletStockSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="stocks.id")
    symbol = serializers.ReadOnlyField(source="stocks.symbol")
    price = serializers.ReadOnlyField(source="stocks.price")

    class Meta:
        model = WalletStock
        fields = ("id", "symbol", "price", "count")


class StockTransferSerializer(serializers.ModelSerializer):
    stock = serializers.SlugRelatedField(slug_field="symbol", queryset=Stock.objects.all())

    class Meta:
        model = StockTransfer
        fields = ("id", "stock", "amount")
        read_only_fields = ["wallet"]

    def validate(self, attrs):
        wallet = self.context["request"].user.wallet
        validate_stock_transaction(wallet, attrs["stock"], attrs["amount"])
        return attrs
