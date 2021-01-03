from django.apps import AppConfig


class StocksConfig(AppConfig):
    name = "currency_exchanger.stocks"

    def ready(self):
        from . import signals  # noqa: F401
