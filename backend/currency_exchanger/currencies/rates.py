import logging

from .fixer_api import get_latest_rates
from .models import Currency, CurrencyHistory

logger = logging.getLogger(__name__)


def update_currency_rates() -> None:
    rates = get_latest_rates()

    for code, rate in rates.items():
        currency, _ = Currency.objects.update_or_create(code=code, defaults={"rate": rate})
        CurrencyHistory.objects.create(currency=currency, rate=rate)
