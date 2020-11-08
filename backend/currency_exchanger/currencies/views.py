from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet

from currency_exchanger.currencies.models import Currency, CurrencyHistory
from currency_exchanger.currencies.serializers import (
    CurrencySerializer,
    CurrencyHistorySerializer,
)


class CurrencyViewSet(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get_queryset(self):
        if self.action == "history":
            return CurrencyHistory.objects.filter(currency=self.get_object())
        return super().get_queryset()

    @action(detail=True, serializer_class=CurrencyHistorySerializer)
    def history(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
