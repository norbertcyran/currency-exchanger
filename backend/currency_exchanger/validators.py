from decimal import Decimal

from currency_exchanger.currencies.models import Currency, WalletCurrency
from currency_exchanger.exceptions import NotEnoughFundsAPIException, NotEnoughStocksAPIException
from currency_exchanger.stocks.models import Stock, WalletStock
from currency_exchanger.wallets.models import Wallet


def validate_transaction(wallet: Wallet, currency: Currency, amount: Decimal) -> None:
    wallet_currency, _ = WalletCurrency.objects.get_or_create(wallet=wallet, currency=currency)

    if wallet_currency.amount < amount:
        raise NotEnoughFundsAPIException


def validate_stock_transaction(wallet: Wallet, stocks: Stock, amount) -> None:
    wallet_currency, _ = WalletCurrency.objects.get_or_create(
        wallet=wallet, currency=stocks.currency
    )
    wallet_stock, _ = WalletStock.objects.get_or_create(wallet=wallet, stocks=stocks)

    if amount * stocks.price > wallet_currency.amount:
        raise NotEnoughFundsAPIException

    if wallet_stock.count + amount < 0:
        raise NotEnoughStocksAPIException
