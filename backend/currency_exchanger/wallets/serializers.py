from currency_exchanger.currencies.serializers import WalletCurrencySerializer
from currency_exchanger.stocks.serializers import WalletStockSerializer
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    currencies = WalletCurrencySerializer(many=True, source="walletcurrency_set")
    stock = WalletStockSerializer(many=True, source="walletstock_set")
