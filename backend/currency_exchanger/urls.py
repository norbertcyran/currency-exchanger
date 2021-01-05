"""currency_exchanger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .currencies.views import CurrencyExchangeViewSet, CurrencyViewSet
from .stocks.views import StockViewSet,StockTranserferViewSet
from .transfers.views import MoneyTransferViewSet
from .users.views import UserViewSet
from .wallets.views import WalletView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"currencies", CurrencyViewSet)
router.register(r"exchange", CurrencyExchangeViewSet, basename="exchanges")
router.register(r"stocktransfer", StockTranserferViewSet, basename="stocktransfers")
router.register(r"stocks", StockViewSet)
router.register(r"transfers", MoneyTransferViewSet, basename="transfers")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/wallet/", WalletView.as_view(), name="retrieve_wallet"),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/register/", include("dj_rest_auth.registration.urls")),
]
