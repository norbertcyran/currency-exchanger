from django.apps import AppConfig


class CurrenciesConfig(AppConfig):
    name = "currency_exchanger.currencies"

    def ready(self):
        from . import signals  # noqa: F401
