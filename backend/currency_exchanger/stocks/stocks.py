import logging

from currency_exchanger.currencies.models import Currency

from .models import Stock, StockHistory
from .polygon_api import get_latest_rates

logger = logging.getLogger(__name__)


def update_stocks() -> None:
    stocks = get_latest_rates()

    for item in stocks:
        stock, _ = Stock.objects.update_or_create(
            symbol=item["T"], defaults={"price": item["c"], "currency": Currency.objects.get(pk=47)}
        )
        StockHistory.objects.create(stocks=stock, price=item["c"])
