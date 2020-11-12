import pytest
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
