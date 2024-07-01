from datetime import datetime, timedelta

from jwt import encode
from pwdlib import PasswordHash

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
