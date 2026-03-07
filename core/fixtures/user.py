import pytest
from core.user.models import User

data_user={
    "username":"test_user",
    "first_name":"test",
    "last_name":"user",
    "email":"test@gmail.com",
    "password":"test_password"

}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)