import pytest
from currency_exchanger.users.models import User


def test_login(api_client, create_user):
    create_user(
        username="test",
        email="test@example.com",
        password="test",
    )

    rsp = api_client.post("/api/auth/login/", data={"username": "test", "password": "test"})

    assert rsp.status_code == 200
    assert rsp.json()["key"] is not None


@pytest.mark.django_db
def test_registration(api_client):
    rsp = api_client.post(
        "/api/auth/register/",
        data={
            "username": "test",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "Testing",
            "billing_address": "Testing St. 1",
            "phone": "+48123456789",
            "password1": "hardpassword1234",
            "password2": "hardpassword1234",
        },
    )

    print(rsp.json())
    assert rsp.status_code == 201
    assert User.objects.filter(username="test").exists()
