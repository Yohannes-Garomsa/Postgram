import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


pytest_plugins = [
    "core.fixtures.user",
    "core.fixtures.post",
]
