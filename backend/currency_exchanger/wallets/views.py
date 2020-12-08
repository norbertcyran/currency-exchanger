from currency_exchanger.wallets.models import Wallet
from currency_exchanger.wallets.serializers import WalletSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class WalletView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        wallet = Wallet.objects.get(user=self.request.user)
        serializer = WalletSerializer(instance=wallet)
        return Response(serializer.data)
