from currency_exchanger.stocks.models import Stock, StockHistory, StockTransfer
from currency_exchanger.stocks.serializers import (
    StockHistorySerializer,
    StockSerializer,
    StockTransferSerializer,
)
from currency_exchanger.views import HistoricalModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class StockViewSet(HistoricalModelViewSet):
    queryset = Stock.objects.all()
    lookup_field = "symbol"
    history_serializer_class = StockHistorySerializer
    serializer_class = StockSerializer

    def get_history_queryset(self):
        return StockHistory.objects.filter(stocks__symbol=self.kwargs["symbol"])


class StockTransferViewSet(ModelViewSet):
    serializer_class = StockTransferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StockTransfer.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)
