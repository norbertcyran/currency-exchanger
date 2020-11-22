from currency_exchanger.currencies.serializers import WalletCurrencySerializer
from currency_exchanger.stocks.serializers import WalletStockSerializer
from currency_exchanger.wallets.models import Wallet
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "user", "currencies", "stock"]

    currencies = WalletCurrencySerializer(many=True, source="walletcurrency_set")
    stock = WalletStockSerializer(many=True, source="walletstock_set")
