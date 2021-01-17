from currency_exchanger.stocks.models import Stock, StockHistory, StockTransfer
from currency_exchanger.stocks.serializers import (
    StockHistorySerializer,
    StockSerializer,
    StockTransferSerializer,
)
from currency_exchanger.views import HistoricalModelViewSet
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class StockViewSet(HistoricalModelViewSet):
    queryset = Stock.objects.order_by("symbol")
    lookup_field = "symbol"
    history_serializer_class = StockHistorySerializer
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["symbol", "price"]
    search_fields = ["symbol"]

    def get_history_queryset(self):
        return StockHistory.objects.filter(stocks__symbol=self.kwargs["symbol"])


class StockTransferViewSet(ModelViewSet):
    serializer_class = StockTransferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StockTransfer.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)
