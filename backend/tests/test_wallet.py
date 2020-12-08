def test_get_wallet_not_authenticated(api_client):
    rsp = api_client.get("/api/wallet/")

    assert rsp.status_code == 401


def test_get_wallet_success(api_client, wallet):
    api_client.force_authenticate(wallet.user)

    rsp = api_client.get("/api/wallet/")

    assert rsp.status_code == 200
    print(rsp.content)
    assert rsp.json() == {
        "id": wallet.id,
        "currencies": [
            {
                "currency": "PLN",
                "amount": "100.00",
            },
            {
                "currency": "EUR",
                "amount": "50.00",
            },
        ],
        "stocks": [],
    }
