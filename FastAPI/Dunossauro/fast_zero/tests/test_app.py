def test_criar_usuario(client):
    # client = TestClient(app)  # Arrange USADO SEM A FIXTURE tests\conftests.py

    response = client.post(
        '/users/',
        json={
            'username': 'PedroElorriaga',
            'email': 'pedroadm@elorriaga.com',
            'senha': 'gtavi2025',
        },
    )  # Act

    assert response.status_code == 201  # Assert
    assert response.json() == {
        'username': 'PedroElorriaga',
        'email': 'pedroadm@elorriaga.com',
        'id': 2,
    }


def test_ler_usuarios(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'usuarios': [
            {
                'username': 'PedroAdmin',
                'email': 'pedroadmin@admin.com',
                'id': 1,
            },
            {
                'username': 'PedroElorriaga',
                'email': 'pedroadm@elorriaga.com',
                'id': 2,
            },
        ]
    }
