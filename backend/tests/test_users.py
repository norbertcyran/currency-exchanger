import pytest

from currency_exchanger.users.models import User


def test_login(api_client, create_user):
    create_user(
        username="test",
        email="test@example.com",
        password="test",
    )

    rsp = api_client.post("/auth/login/", data={
        "username": "test", "password": "test"
    })

    assert rsp.status_code == 200
    assert rsp.json()["key"] is not None


@pytest.mark.django_db
def test_registration(api_client):
    rsp = api_client.post("/auth/register/", data={
        "username": "test",
        "email": "test@example.com",
        "password1": "hardpassword1234",
        "password2": "hardpassword1234",
    })

    print(rsp.json())
    assert rsp.status_code == 201
    assert User.objects.filter(username="test").exists()
