from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retornar_using_fastapi_e_retornar_status_200():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == 200  # Assert
    assert response.text == '\n    <h1>Olá mundo!</h1>\n    '  # Assert
