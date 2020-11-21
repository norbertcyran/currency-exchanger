import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_exchanger.settings")

app = Celery("currency_exchanger")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
