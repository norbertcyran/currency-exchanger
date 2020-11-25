from django.apps import AppConfig


class WalletsConfig(AppConfig):
    name = "currency_exchanger.wallets"

    def ready(self):
        import currency_exchanger.wallets.signals  # noqa F401
