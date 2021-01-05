from django.contrib import admin

from .models import Currency, CurrencyExchange,WalletCurrency

admin.site.register(Currency)
admin.site.register(CurrencyExchange)
admin.site.register(WalletCurrency)
