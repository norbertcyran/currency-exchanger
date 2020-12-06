from decimal import Decimal

from currency_exchanger.currencies.models import Currency, WalletCurrency
from currency_exchanger.exceptions import NotEnoughFundsAPIException
from currency_exchanger.wallets.models import Wallet


def validate_transaction(wallet: Wallet, currency: Currency, amount: Decimal) -> None:
    wallet_currency, _ = WalletCurrency.objects.get_or_create(wallet=wallet, currency=currency)

    if wallet_currency.amount < amount:
        raise NotEnoughFundsAPIException
