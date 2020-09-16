import pytest
from alembic import command
from alembic.config import Config
from starlette.config import environ
from starlette.testclient import TestClient

environ["DATABASE_URL"] = "sqlite:///:memory:"


@pytest.fixture(autouse=True)
def create_test_database():
    config = Config("alembic.ini")
    command.upgrade(config, "head", "--sql")  # offline, for coverage
    command.upgrade(config, "head")
    yield
    command.downgrade(config, "base")


@pytest.fixture()
def client():
    from estuary.asgi import app
    with TestClient(app) as client:
        yield client
