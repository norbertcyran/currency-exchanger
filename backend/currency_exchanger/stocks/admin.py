from django.contrib import admin

from .models import Stock, StockTransfer,StockHistory

admin.site.register(Stock)
admin.site.register(StockTransfer)
admin.site.register(StockHistory)
