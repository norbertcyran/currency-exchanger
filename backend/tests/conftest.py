from decimal import Decimal

import pytest
from currency_exchanger.currencies.models import Currency
from currency_exchanger.users.models import User
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db) -> User:
    return baker.make(User, username="test")


@pytest.fixture
def create_user(db):
    def _create_user(username, email, password, **kwargs) -> User:
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs,
        )

    return _create_user


@pytest.fixture
def currencies(db):
    return [
        baker.make(Currency, code="PLN", rate=Decimal(4.50)),
        baker.make(Currency, code="EUR", rate=1),
    ]


@pytest.fixture
def wallet(user, currencies):
    baker.make("WalletCurrency", wallet=user.wallet, currency=currencies[0], amount=100)
    baker.make("WalletCurrency", wallet=user.wallet, currency=currencies[1], amount=50)
    return user.wallet
