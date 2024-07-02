from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, decode, encode
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from aluga_project.database.database import create_session
from aluga_project.models.models import UserModels
from aluga_project.schemas.token_schema import TokenData

Session = Annotated[Session, Depends(create_session)]
oauth2_token = Annotated[OAuth2PasswordBearer(tokenUrl='token'), Depends()]

SECRET_KEY = 'uncystvcfwqomxmxnscidopkoihj'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = PasswordHash.recommended()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def make_password_hash(password: str):
    return pwd_context.hash(password)


def decripty_password_hash(original_password: str, hashed_password: str):
    return pwd_context.verify(original_password, hashed_password)


async def get_current_user(session: Session, token: oauth2_token):
    credentials_error = HTTPException(
        status_code=401,
        detail='Sua credencial não pode ser verificada',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise credentials_error
        token_data = TokenData(username=username)
    except DecodeError:
        raise credentials_error

    user_from_db = session.scalar(
        select(UserModels).where(token_data.username == UserModels.email)
    )

    if not user_from_db:
        raise credentials_error

    return user_from_db
