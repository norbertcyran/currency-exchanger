from currency_exchanger.stocks.stocks import update_stocks
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Update currency rates to the latest"

    def handle(self, *args, **options):
        update_stocks()
