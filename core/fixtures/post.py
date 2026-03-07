import pytest
from core.fixtures.user import user
from core.fixtures.post import post

@pytest.fixture
def post(db,user):
    
    return Post.objects.create(author=user,body="test post body")