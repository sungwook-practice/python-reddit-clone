from pydantic import BaseModel, Field


class RequestCreateUser(BaseModel):
    userName: str = Field(..., description="유저 이름", example="홍길동")
    email: str = Field(..., description="이메일", example="홍길동@naver.com")
    password: str = Field(..., description="비밀번호", example="password")
