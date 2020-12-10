from django.apps import AppConfig


class TransfersConfig(AppConfig):
    name = "currency_exchanger.transfers"

    def ready(self):
        from . import signals  # noqa: F401
