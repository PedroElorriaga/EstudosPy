from jwt import decode

from fast_zero.security import SECRET_KEY, criar_token_de_acesso


def test_jwt():
    data = {'test': '123'}
    token = criar_token_de_acesso(data)

    decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
