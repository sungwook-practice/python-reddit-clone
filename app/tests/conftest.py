import sqlite3
import pytest
import os
import re
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


@pytest.fixture(scope="session", autouse=True)
def session():
    # reference: https://docs.sqlalchemy.org/en/13/core/connections.html
    engine = create_engine("sqlite://", echo=True)
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.rollback()
    # 테스트 중 DB에 반영하고 싶으면 주석 해제
    # transaction.commit()
    connection.close()


@pytest.fixture()
def setup_db(session):
    test_sql_filepath = os.path.join("tests", "test.sql")

    with open(test_sql_filepath, "r") as f:
        # reference: https://stackoverflow.com/questions/2268050/execute-sql-from-file-in-sqlalchemy
        statements = re.split(r";\s*$", f.read(), flags=re.MULTILINE)

        for statement in statements:
            session.execute(statement)

    yield session
