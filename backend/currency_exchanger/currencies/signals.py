from currency_exchanger.currencies.models import CurrencyExchange, WalletCurrency
from currency_exchanger.exceptions import NotEnoughFundsException
from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CurrencyExchange)
@transaction.atomic
def update_wallet(instance: CurrencyExchange, created: bool, **kwargs) -> None:
    if not created:
        return

    wallet_currency_from, _ = WalletCurrency.objects.get_or_create(
        wallet=instance.wallet, currency=instance.currency_from
    )
    wallet_currency_to, _ = WalletCurrency.objects.get_or_create(
        wallet=instance.wallet, currency=instance.currency_to
    )

    if instance.amount > wallet_currency_from.amount:
        raise NotEnoughFundsException

    WalletCurrency.objects.filter(id=wallet_currency_from.id).update(
        amount=F("amount") - instance.amount
    )

    amount_to = instance.amount * (instance.currency_to.rate / instance.currency_from.rate)

    WalletCurrency.objects.filter(id=wallet_currency_to.id).update(amount=F("amount") + amount_to)

    instance.amount_to = amount_to
    instance.save()
