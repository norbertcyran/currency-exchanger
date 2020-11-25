from currency_exchanger.currencies.rates import update_currency_rates
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Update currency rates to the latest"

    def handle(self, *args, **options):
        update_currency_rates()
