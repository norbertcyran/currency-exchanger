import logging

from celery import shared_task

from .rates import update_currency_rates

logger = logging.getLogger(__name__)


@shared_task
def update_currency_rates_async():
    update_currency_rates()
