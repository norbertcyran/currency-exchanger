from currency_exchanger.currencies.models import WalletCurrency
from currency_exchanger.exceptions import NotEnoughFundsException, NotEnoughStocksException
from currency_exchanger.stocks.models import StockTransfer, WalletStock
from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=StockTransfer)
@transaction.atomic
def stock_update(instance: StockTransfer, created: bool, **kwargs) -> None:
    if not created:
        return
    wallet_stock, _ = WalletStock.objects.get_or_create(
        wallet=instance.wallet, stocks=instance.stock
    )

    stock = instance.stock
    wallet_currency, _ = WalletCurrency.objects.get_or_create(
        wallet=instance.wallet, currency=stock.currency
    )

    currency_amount = instance.amount * stock.price

    if currency_amount > wallet_currency.amount:
            raise NotEnoughFundsException

    if instance.amount + wallet_stock.count < 0:
            raise NotEnoughStocksException
            
    WalletStock.objects.filter(id=wallet_stock.id).update(
        count=F("count") + instance.amount
    )
    WalletCurrency.objects.filter(id=wallet_currency.id).update(
        amount=F("amount") - currency_amount
    )

    instance.save()
