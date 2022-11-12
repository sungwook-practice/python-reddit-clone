from sqlalchemy.orm import Session
from .repository import UserRepository
from .schemas import RequestCreateUser
from .models import User


def create_user(session: Session, request: RequestCreateUser) -> User:
    """user 생성"""

    new_user = User(
        email=request.email, userName=request.userName, password=request.password
    )

    user_repository = UserRepository(session=session)
    try:
        user_repository.add(new_user)
    except Exception as e:
        print(f"error: {e}")
        return False

    return new_user
