from currency_exchanger.currencies.serializers import WalletCurrencySerializer
from currency_exchanger.stocks.serializers import WalletStockSerializer
from currency_exchanger.wallets.models import Wallet
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "currencies", "stocks")

    currencies = WalletCurrencySerializer(many=True, source="walletcurrency_set")
    stocks = WalletStockSerializer(many=True, source="walletstock_set")
