from jwt import decode

from aluga_project.security.security import SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_get_token(client, user_factory):
    response = client.post(
        '/tokens',
        data={
            'username': user_factory.email,
            'password': user_factory.clean_password,
        },
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token
