from currency_exchanger.currencies.models import Currency, CurrencyHistory
from currency_exchanger.currencies.serializers import (
    CurrencySerializer,
    CurrencyHistorySerializer,
)
from currency_exchanger.views import HistoricalModelViewSet


class CurrencyViewSet(HistoricalModelViewSet):
    queryset = Currency.objects.all()
    history_model = CurrencyHistory
    history_serializer_class = CurrencyHistorySerializer
    serializer_class = CurrencySerializer
