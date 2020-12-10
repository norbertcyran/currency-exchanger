from currency_exchanger.currencies.models import CurrencyTransfer, WalletCurrency
from currency_exchanger.users.models import User
from currency_exchanger.wallets.models import Wallet
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=CurrencyTransfer)
@transaction.atomic
def update_wallet(instance: CurrencyTransfer, created: bool, **kwargs):
    if not created:
        return

    wallet_currency, _ = WalletCurrency.objects.get_or_create(
        wallet=instance.wallet, currency=instance.currency
    )
    wallet_currency.amount += instance.amount
    wallet_currency.save(update_fields=["amount"])
