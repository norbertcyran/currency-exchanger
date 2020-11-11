from django.contrib import admin

from .models import Stock, StockTransfer

admin.site.register(Stock)
admin.site.register(StockTransfer)
