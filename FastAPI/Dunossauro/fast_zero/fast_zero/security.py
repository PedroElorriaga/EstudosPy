from datetime import datetime, timedelta

from jwt import encode
from passlib.context import CryptContext

SECRET_KEY = 'chave-secreta'
ALGORITHM = 'HS256'
ACESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def criar_token_de_acesso(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def criar_hash_de_senha(senha: str):
    return pwd_context.hash(senha)


def verificar_hash_de_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)
