import pytest
from alembic import command
from alembic.config import Config
from starlette.testclient import TestClient
from sqlalchemy_utils import database_exists, create_database, drop_database

from estuary import app, settings


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    test_url = str(settings.TEST_DATABASE_URL)
    assert not database_exists(test_url)
    create_database(test_url)
    config = Config("alembic.ini")
    try:
        command.upgrade(config, "head")
        yield
        command.downgrade(config, "base")
    finally:
        drop_database(test_url)


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
