from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Usuario
from fast_zero.schemas import Token
from fast_zero.security import criar_token_de_acesso, verificar_hash_de_senha

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', response_model=Token)
def criar_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    usuario = session.scalar(
        select(Usuario).where(Usuario.email == form_data.username)
    )

    if not usuario:
        raise HTTPException(
            status_code=400, detail='Senha ou email incorretos'
        )

    if not verificar_hash_de_senha(form_data.password, usuario.senha):
        raise HTTPException(
            status_code=400, detail='Senha ou email incorretos'
        )

    access_token = criar_token_de_acesso({'sub': usuario.email})

    return {'access_token': access_token, 'token_type': 'bearer'}
