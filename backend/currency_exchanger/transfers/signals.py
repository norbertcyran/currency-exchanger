from currency_exchanger.currencies.models import WalletCurrency
from currency_exchanger.exceptions import NotEnoughFundsException
from currency_exchanger.transfers.models import MoneyTransfer
from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=MoneyTransfer)
@transaction.atomic
def update_wallets(instance: MoneyTransfer, created, **kwargs):
    if not created:
        return

    wallet_from = instance.user_from.wallet
    wallet_to = instance.user_to.wallet

    wallet_currency_from, _ = WalletCurrency.objects.get_or_create(
        wallet=wallet_from, currency=instance.currency
    )

    wallet_currency_to, _ = WalletCurrency.objects.get_or_create(
        wallet=wallet_to, currency=instance.currency
    )

    if instance.amount > wallet_currency_from.amount:
        raise NotEnoughFundsException

    WalletCurrency.objects.filter(id=wallet_currency_from.id).update(
        amount=F("amount") - instance.amount
    )
    WalletCurrency.objects.filter(id=wallet_currency_to.id).update(
        amount=F("amount") + instance.amount
    )
