import sqlite3
import pytest
import os
import re


@pytest.fixture(scope="session", autouse=True)
def session():
    connection = sqlite3.Connection(":memory:")
    db_session = connection.cursor()

    yield db_session
    connection.close()


@pytest.fixture()
def setup_db(session):
    test_sql_filepath = os.path.join("tests", "test.sql")

    with open(test_sql_filepath, "r") as f:
        # reference: https://stackoverflow.com/questions/2268050/execute-sql-from-file-in-sqlalchemy
        statements = re.split(r";\s*$", f.read(), flags=re.MULTILINE)

        for statement in statements:
            session.execute(statement)
