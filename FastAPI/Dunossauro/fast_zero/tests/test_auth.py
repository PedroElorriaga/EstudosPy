from freezegun import freeze_time


def test_pegar_token(client, usuario):
    response = client.post(
        '/auth/token',
        data={'username': usuario.email, 'password': usuario.clean_password},
    )

    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_token_expirado_depois_do_tempo(client, usuario):
    with freeze_time('2024-04-17 12:00:00'):
        response = client.post(
            '/auth/token',
            data={
                'username': usuario.email,
                'password': usuario.clean_password,
            },
        )

        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2024-04-17 12:31:00'):
        response = client.put(
            f'/users/{usuario.id}',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'username': 'admin',
                'email': 'admin@test.com',
                'senha': 'passcode123',
            },
        )

        assert response.status_code == 401
        assert response.json() == {
            'detail': 'Não foi possivel validar as credenciais'
        }
