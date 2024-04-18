from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError, decode, encode
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Usuario
from fast_zero.schemas import TokenData
from fast_zero.settings import Configuracoes

configuracoes = Configuracoes()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def criar_token_de_acesso(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=configuracoes.ACESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        to_encode, configuracoes.SECRET_KEY, algorithm=configuracoes.ALGORITHM
    )

    return encoded_jwt


def criar_hash_de_senha(senha: str):
    return pwd_context.hash(senha)


def verificar_hash_de_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


async def pegar_usuario_atual(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possivel validar as credenciais',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode(
            token,
            configuracoes.SECRET_KEY,
            algorithms=[configuracoes.ALGORITHM],
        )
        # 'sub' normalmente usado para armazenar o identificador do usuário no token JWT
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
        token_data = TokenData(username=username)
    except DecodeError:
        raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception

    usuario = session.scalar(
        select(Usuario).where(Usuario.email == token_data.username)
    )

    if not usuario:
        raise credentials_exception

    return usuario
