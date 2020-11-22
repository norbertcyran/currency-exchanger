from currency_exchanger.stocks.models import Stock, StockHistory
from currency_exchanger.stocks.serializers import StockHistorySerializer, StockSerializer
from currency_exchanger.views import HistoricalModelViewSet


class StockViewSet(HistoricalModelViewSet):
    queryset = Stock.objects.all()
    history_model = StockHistory
    history_serializer_class = StockHistorySerializer
    serializer_class = StockSerializer
