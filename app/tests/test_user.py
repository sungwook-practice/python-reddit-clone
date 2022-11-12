import pytest
from src.domain.users.service import create_user
from src.domain.users.schemas import RequestCreateUser


@pytest.mark.usefixtures("setup_db")
def test_create_user(session):
    """유저 생성"""

    new_user = RequestCreateUser(
        email="testuser@test.com", userName="testuser", password="password"
    )

    assert create_user(session=session, request=new_user) == True
