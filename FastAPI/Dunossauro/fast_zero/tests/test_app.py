from fast_zero.schemas import UsuarioPublic


def test_criar_usuario(client):
    # client = TestClient(app)  # Arrange USADO SEM A FIXTURE tests\conftests.py

    response = client.post(
        '/users',
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
        'id': 1,
    }


def test_ler_usuarios(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'usuarios': []}


def test_ler_usuarios_com_usuarios(client, usuario):
    user_schema = UsuarioPublic.model_validate(usuario).model_dump()
    response = client.get('/users')

    assert response.json() == {'usuarios': [user_schema]}


def test_atualizar_usuario(client, usuario):
    response = client.put(
        '/users/1',
        json={
            'username': 'Pedrinho',
            'email': 'pedrinho.senior@test.com',
            'senha': 'adm123',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'Pedrinho',
        'email': 'pedrinho.senior@test.com',
        'id': 1,
    }


def test_excluir_usuario(client, usuario):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {
        'mensagem': 'Usuário excluido com sucesso!',
    }


def test_atualizar_usuario_retornar_404(client):
    response = client.put(
        '/users/3',
        json={
            'username': 'PedroErrorTest',
            'email': 'pedroTestError@admin.com',
            'senha': 'Error404',
        },
    )

    assert response.status_code == 404


def test_excluir_usuario_retornar_404(client):
    response = client.delete('/users/2')

    assert response.status_code == 404


def test_ler_um_usuario(client):
    response = client.get('/users/1')

    assert response.status_code == 200
    assert response.json() == {
        'username': 'PedroElorriaga',
        'email': 'pedroadm@elorriaga.com',
        'id': 2,
    }
