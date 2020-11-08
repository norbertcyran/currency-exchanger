from django.db import models

from currency_exchanger.currencies.models import Currency
from currency_exchanger.wallets.models import Wallet


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="stocks"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)


class WalletStock(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="wallet")
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="stocks")
    count = models.IntegerField()


class StockTransfer(models.Model):
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="stock_transfers"
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="+")
    amount = models.PositiveIntegerField()


class StockHistory(models.Model):
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="history")
    timestamp = models.DateTimeField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ["-timestamp"]
