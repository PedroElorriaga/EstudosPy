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
        'detail': 'Sua credencial não pode ser verificada'
    }
