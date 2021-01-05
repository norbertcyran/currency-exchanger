from currency_exchanger.stocks.models import Stock, StockHistory,StockTransfer
from currency_exchanger.stocks.serializers import StockHistorySerializer, StockSerializer,StockTransferSerializer
from currency_exchanger.views import HistoricalModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
class StockViewSet(HistoricalModelViewSet):
    queryset = Stock.objects.all()
    history_model = StockHistory
    history_serializer_class = StockHistorySerializer
    serializer_class = StockSerializer

class StockTranserferViewSet(ModelViewSet):
    serializer_class = StockTransferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StockTransfer.objects.filter(wallet__user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(wallet=self.request.user.wallet)