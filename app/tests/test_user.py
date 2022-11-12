import pytest
from src.domain.users.service import create_user


@pytest.mark.usefixtures("setup_db")
def test_create_user(session):
    """유저 생성"""
    assert create_user(session=session) == True
