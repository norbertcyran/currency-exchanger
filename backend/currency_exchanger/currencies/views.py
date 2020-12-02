from currency_exchanger.currencies.models import Currency, CurrencyExchange, CurrencyHistory
from currency_exchanger.currencies.serializers import (
    CurrencyExchangeSerializer,
    CurrencyHistorySerializer,
    CurrencySerializer,
    CurrencyTransferSerializer,
)
from currency_exchanger.views import HistoricalModelViewSet
from rest_framework.viewsets import ModelViewSet


class CurrencyViewSet(HistoricalModelViewSet):
    queryset = Currency.objects.all()
    history_model = CurrencyHistory
    history_serializer_class = CurrencyHistorySerializer
    serializer_class = CurrencySerializer


class CurrencyExchangeViewSet(ModelViewSet):
    serializer_class = CurrencyExchangeSerializer

    def get_queryset(self):
        return CurrencyExchange.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)


class CurrencyTransferViewSet(ModelViewSet):
    serializer_class = CurrencyTransferSerializer

    def get_queryset(self):
        return CurrencyExchange.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)
