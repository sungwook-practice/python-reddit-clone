from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.engine.cursor import CursorResult
from .models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, user_model: User):
        """item 추가"""
        statement = text(
            """
        INSERT INTO
            USERS (email, userName, password, createdAt, updatedAt)
        VALUES(:email, :userName, :password, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)
        """
        )

        response: CursorResult = self.session.execute(
            statement,
            {
                "email": user_model.email,
                "userName": user_model.userName,
                "password": user_model.password,
            },
        )
        self.session.commit()

        user_model.id = response.lastrowid

        return user_model

    def delete(self):
        """item 삭제"""
        raise NotImplementedError

    def update(self):
        """item 업데이트"""
        raise NotImplementedError

    def getUserByUsername(self):
        """username으로 user찾기"""
        raise NotImplementedError
