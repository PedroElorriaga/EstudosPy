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


def test_criar_usuario_existente_retornar_400(client, usuario):
    response = client.post(
        '/users',
        json={
            'username': 'teste',
            'email': 'teste.existente@test.com',
            'senha': 'Senh@123',
        },
    )

    assert response.status_code == 400


def test_ler_usuarios(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'usuarios': []}


def test_ler_usuarios_com_dados(client, usuario):
    user_schema = UsuarioPublic.model_validate(usuario).model_dump()
    response = client.get('/users')

    assert response.json() == {'usuarios': [user_schema]}


def test_atualizar_usuario(client, usuario, token):
    response = client.put(
        f'/users/{usuario.id}',
        headers={'Authorization': f'Bearer {token}'},
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


def test_excluir_usuario(client, usuario, token):
    response = client.delete(
        f'/users/{usuario.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'mensagem': 'Usuário excluido com sucesso!',
    }


def test_atualizar_usuario_retornar_400(client, usuario, token):
    response = client.put(
        '/users/2',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'PedroErrorTest',
            'email': 'pedroTestError@admin.com',
            'senha': 'Error404',
        },
    )

    assert response.status_code == 400


def test_excluir_usuario_retornar_400(client, usuario, token):
    response = client.delete(
        '/users/2', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 400


def test_pegar_token(client, usuario):
    response = client.post(
        '/auth/token',
        data={'username': usuario.email, 'password': usuario.clean_password},
    )

    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token
