from jwt import decode

from fast_zero.security import criar_token_de_acesso
from fast_zero.settings import Configuracoes


def test_jwt():
    data = {'test': '123'}
    token = criar_token_de_acesso(data)

    decoded = decode(token, Configuracoes().SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
