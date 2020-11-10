from django.db import models

from currency_exchanger.currencies.models import Currency
from currency_exchanger.wallets.models import Wallet


class MoneyTransfer(models.Model):
    wallet_from = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="sent_transfers"
    )
    wallet_to = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="received_transfers"
    )
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="+")
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    timestamp = models.DateTimeField(auto_now_add=True)
