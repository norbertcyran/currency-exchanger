import logging

from celery import shared_task

from .stocks import update_stocks

logger = logging.getLogger(__name__)


@shared_task
def update_stocks_async():
    update_stocks()
