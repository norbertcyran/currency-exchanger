from currency_exchanger.currencies.models import Currency
from django.conf import settings
from django.db import models


class MoneyTransfer(models.Model):
    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_transfers"
    )
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_transfers"
    )
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="+")
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    timestamp = models.DateTimeField(auto_now_add=True)
