import pytest
from main import app
from starlette.testclient import TestClient


@pytest.fixture()
def test_client():
    with TestClient(app) as test_client:
        yield test_client
