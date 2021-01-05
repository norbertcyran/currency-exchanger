from currency_exchanger.currencies.models import (
    Currency,
    CurrencyExchange,
    CurrencyHistory,
    CurrencyTransfer,
)
from currency_exchanger.currencies.serializers import (
    CurrencyExchangeSerializer,
    CurrencyHistorySerializer,
    CurrencySerializer,
    CurrencyTransferSerializer,
)
from currency_exchanger.views import HistoricalModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CurrencyViewSet(HistoricalModelViewSet):
    queryset = Currency.objects.all()
    history_model = CurrencyHistory
    history_serializer_class = CurrencyHistorySerializer
    serializer_class = CurrencySerializer


class SingleCurrencyViewSet(ModelViewSet):
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        code = self.request.GET.get("code")
        return Currency.objects.filter(code=code)


class CurrencyExchangeViewSet(ModelViewSet):
    serializer_class = CurrencyExchangeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "code"

    def get_queryset(self):
        return CurrencyExchange.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)


class CurrencyTransferViewSet(ModelViewSet):
    serializer_class = CurrencyTransferSerializer

    def get_queryset(self):
        return CurrencyTransfer.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)
