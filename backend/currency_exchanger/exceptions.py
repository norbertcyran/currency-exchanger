from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class NotEnoughFundsAPIException(ValidationError):
    default_code = "not_enough_funds"
    default_detail = _("Not enough funds to perform this action.")


class NotEnoughFundsException(Exception):
    pass


class NotEnoughStocksException(Exception):
    pass
