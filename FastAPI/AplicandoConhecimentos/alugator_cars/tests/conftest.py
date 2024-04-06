import pytest
from fastapi.testclient import TestClient

from alugator_cars.app import app


@pytest.fixture
def client():
    return TestClient(app)
