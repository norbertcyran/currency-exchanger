from currency_exchanger.wallets.models import Wallet
from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    country = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    rate = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.code


class CurrencyHistory(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="history")
    timestamp = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ["-timestamp"]


class WalletCurrency(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["wallet", "currency"], name="unique_wallet_currency")
        ]


class CurrencyExchange(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="exchanges")
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="+")
    currency_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="+")
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    amount_to = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class CurrencyTransfer(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transfers")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
