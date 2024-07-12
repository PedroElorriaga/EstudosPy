from freezegun import freeze_time
from jwt import decode

from aluga_project.security.security import create_access_token
from aluga_project.setting.settings import Configs


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token, Configs().SECRET_KEY, algorithms=[Configs().ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_get_token(client, user_factory):
    response = client.post(
        '/token',
        data={
            'username': user_factory.email,
            'password': user_factory.clean_password,
        },
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_jwt_invalid(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer invalid-token'}
    )

    assert response.status_code == 401
    assert response.json() == {
        'detail': 'Suas credenciais não puderam ser verificadas'
    }


def test_expire_time_token(client, user_factory):
    with freeze_time('2024-07-08 10:00:00'):
        response = client.post(
            '/token',
            data={
                'username': user_factory.email,
                'password': user_factory.clean_password,
            },
        )

        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2024-07-08 10:31:00'):
        response = client.put(
            '/users/1',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'username': 'wrongwrong',
                'email': 'wrong@wrong.com',
            },
        )

        assert response.status_code == 401
        assert response.json() == {
            'detail': 'Suas credenciais não puderam ser verificadas'
        }


def test_expire_time_token_dont_refresh(client, user_factory):
    with freeze_time('2024-07-08 10:00:00'):
        response = client.post(
            '/token',
            data={
                'username': user_factory.email,
                'password': user_factory.clean_password,
            },
        )

        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2024-07-08 10:31:00'):
        response = client.put(
            '/users/refresh_token',
            headers={'Authorization': f'Bearer {token}'},
        )

        assert response.status_code == 401
        assert response.json() == {
            'detail': 'Suas credenciais não puderam ser verificadas'
        }


def test_login_with_wrong_password(client, user_factory):
    response = client.post(
        '/token',
        data={'username': user_factory.email, 'password': 'wrongpass'},
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Email ou senha incorreto(s)'}


def test_login_with_wrong_username(client, user_factory):
    response = client.post(
        '/token',
        data={
            'username': 'wronguser@test.com',
            'password': user_factory.clean_password,
        },
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Email ou senha incorreto(s)'}


def test_refresh_token(client, user_factory, token):
    response = client.post(
        '/token/refresh_token', headers={'Authorization': f'Bearer {token}'}
    )

    data = response.json()

    assert response.status_code == 200
    assert 'access_token' in data
    assert 'token_type' in data
    assert data['token_type'] == 'bearer'
