from django.conf import settings
from django.db import models


class Wallet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallet"
    )
    currencies = models.ManyToManyField(
        "currencies.Currency", through="currencies.WalletCurrency"
    )
    stocks = models.ManyToManyField(
        "stocks.Stock", through="stocks.WalletStock"
    )
