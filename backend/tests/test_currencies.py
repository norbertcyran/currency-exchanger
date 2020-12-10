from decimal import Decimal

import pytest
from currency_exchanger.currencies.fixer_api import FixerAPIException
from currency_exchanger.currencies.models import (
    Currency,
    CurrencyExchange,
    CurrencyHistory,
    WalletCurrency,
)
from currency_exchanger.currencies.rates import update_currency_rates
from model_bakery import baker


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


def test_currency_exchange_successful(api_client, user, currencies):
    baker.make("WalletCurrency", wallet=user.wallet, currency=currencies[1], amount=100)
    data = {"currency_from": "EUR", "currency_to": "PLN", "amount": 10}

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/exchange/", data=data)

    exchange = CurrencyExchange.objects.first()
    assert rsp.status_code == 201
    assert exchange.currency_to == currencies[0]
    assert exchange.currency_from == currencies[1]

    wallet_pln = WalletCurrency.objects.get(wallet=user.wallet, currency=currencies[0])
    assert wallet_pln.amount == 45

    wallet_eur = WalletCurrency.objects.get(wallet=user.wallet, currency=currencies[1])
    assert wallet_eur.amount == 90


def test_currency_exchange_not_enough_funds(api_client, user, currencies):
    data = {"currency_from": "EUR", "currency_to": "PLN", "amount": 10}

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/exchange/", data=data)
    rsp_json = rsp.json()

    assert rsp.status_code == 400
    assert rsp_json["non_field_errors"] == ["Not enough funds to perform this action."]


def test_currency_exchange_same_currency(api_client, user, currencies):
    data = {"currency_from": "EUR", "currency_to": "EUR", "amount": 10}

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/exchange/", data=data)
    rsp_json = rsp.json()

    assert rsp.status_code == 400
    assert rsp_json["non_field_errors"] == ["Can't exchange two the same currencies."]


def test_currency_exchange_not_authenticated(api_client):
    rsp = api_client.post("/api/exchange/")

    assert rsp.status_code == 401
