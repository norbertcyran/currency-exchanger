from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet


class HistoricalModelViewSet(ReadOnlyModelViewSet):
    history_model = None
    history_serializer_class = None

    def get_serializer_class(self):
        if self.action == "history":
            return self.history_serializer_class
        return self.serializer_class

    def get_queryset(self):
        if self.action == "history":
            return self.history_model.objects.filter(currency=self.get_object())
        return super().get_queryset()

    @action(detail=True)
    def history(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
