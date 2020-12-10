from currency_exchanger.transfers.models import MoneyTransfer
from currency_exchanger.transfers.serializers import (
    MoneyTransferReadSerializer,
    MoneyTransferWriteSerializer,
)
from django.db.models import Q
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class MoneyTransferViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return MoneyTransferWriteSerializer
        return MoneyTransferReadSerializer

    def get_queryset(self):
        return MoneyTransfer.objects.filter(
            Q(user_from=self.request.user) | Q(user_to=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(user_from=self.request.user)
