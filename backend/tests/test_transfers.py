from currency_exchanger.currencies.models import WalletCurrency
from currency_exchanger.transfers.models import MoneyTransfer
from currency_exchanger.users.models import User
from model_bakery import baker


def test_transfer_successful(api_client, user, currencies):
    baker.make("WalletCurrency", wallet=user.wallet, currency=currencies[0], amount=100)
    second_user = baker.make(User)

    data = {
        "user_to": second_user.username,
        "currency": "PLN",
        "amount": 25,
    }

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/transfers/", data=data)

    assert rsp.status_code == 201
    transfer = MoneyTransfer.objects.first()
    assert transfer.user_from == user
    assert transfer.user_to == second_user
    assert transfer.currency == currencies[0]
    assert transfer.amount == 25

    wallet_currency_from = WalletCurrency.objects.get(wallet__user=user, currency__code="PLN")
    wallet_currency_to = WalletCurrency.objects.get(wallet__user=second_user, currency__code="PLN")

    assert wallet_currency_from.amount == 75
    assert wallet_currency_to.amount == 25


def test_transfer_not_authenticated(api_client):
    rsp = api_client.post("/api/transfers/")

    assert rsp.status_code == 401


def test_transfer_not_enough_funds(api_client, user, currencies):
    user_to = baker.make(User)
    data = {"user_to": user_to.username, "currency": "PLN", "amount": 10}

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/transfers/", data=data)

    assert rsp.status_code == 400
    assert rsp.json()["non_field_errors"] == ["Not enough funds to perform this action."]


def test_transfer_same_user(api_client, user, currencies):
    data = {"user_to": user.username, "currency": "PLN", "amount": 10}

    api_client.force_authenticate(user)
    rsp = api_client.post("/api/transfers/", data=data)

    assert rsp.status_code == 400
    assert rsp.json()["non_field_errors"] == ["Can't send transfer to yourself."]


def test_get_transfer_history(api_client, user, currencies):
    second_user, third_user = baker.make(User, _quantity=2)
    baker.make("WalletCurrency", wallet=user.wallet, currency=currencies[0], amount=100)

    baker.make(
        "MoneyTransfer", currency=currencies[0], user_from=user, user_to=second_user, amount=25
    ),
    baker.make(
        "MoneyTransfer", currency=currencies[0], user_from=second_user, user_to=user, amount=10
    ),
    baker.make(
        "MoneyTransfer",
        currency=currencies[0],
        user_from=second_user,
        user_to=third_user,
        amount=10,
    ),

    api_client.force_authenticate(user)
    rsp = api_client.get("/api/transfers/")

    assert rsp.status_code == 200
    data = rsp.json()

    assert len(data) == 2

    assert data[0]["user_from"]["id"] == user.id
    assert data[0]["user_to"]["id"] == second_user.id
    assert data[0]["amount"] == "25.00"

    assert data[1]["user_from"]["id"] == second_user.id
    assert data[1]["user_to"]["id"] == user.id
    assert data[1]["amount"] == "10.00"

    api_client.force_authenticate(second_user)
    rsp = api_client.get("/api/transfers/")

    assert rsp.status_code == 200
    data = rsp.json()

    assert len(data) == 3
