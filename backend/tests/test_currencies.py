from decimal import Decimal

import pytest
from currency_exchanger.currencies.fixer_api import FixerAPIException
from currency_exchanger.currencies.models import Currency, CurrencyHistory
from currency_exchanger.currencies.rates import update_currency_rates


@pytest.mark.django_db
def test_update_currency_rates(mocker):
    config = {
        "return_value.json.return_value": {
            "success": True,
            "rates": {
                "EUR": 1,
                "PLN": 4.5,
            },
        }
    }
    requests_mock = mocker.patch("requests.get")
    requests_mock.configure_mock(**config)

    update_currency_rates()

    eur = Currency.objects.get(code="EUR")
    pln = Currency.objects.get(code="PLN")
    assert eur.rate == Decimal(1)
    assert pln.rate == Decimal(4.5)
    assert CurrencyHistory.objects.count() == 2


def test_update_currency_rates_invalid_api_key(mocker):
    config = {
        "return_value.json.return_value": {
            "success": False,
            "error": {"info": "You have not supplied an API Access Key."},
        }
    }
    requests_mock = mocker.patch("requests.get")
    requests_mock.configure_mock(**config)

    with pytest.raises(FixerAPIException) as exc:
        update_currency_rates()
    assert str(exc.value) == (
        "Failed to retrieve currency rates: You have not supplied an API Access Key."
    )
