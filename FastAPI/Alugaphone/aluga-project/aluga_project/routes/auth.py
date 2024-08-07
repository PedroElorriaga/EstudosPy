from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from aluga_project.database.database import create_session
from aluga_project.models.models import UserModels
from aluga_project.schemas.token_schema import TokenSchema
from aluga_project.security.security import (
    create_access_token,
    decripty_password_hash,
    get_current_user,
)

Session = Annotated[Session, Depends(create_session)]
FormData = Annotated[OAuth2PasswordRequestForm, Depends()]
Current_user = Annotated[UserModels, Depends(get_current_user)]
router = APIRouter(prefix='/token', tags=['token'])


@router.post('/', status_code=200, response_model=TokenSchema)
def token_post(session: Session, form_data: FormData):
    user_from_db = session.scalar(
        select(UserModels).where(UserModels.email == form_data.username)
    )

    if not user_from_db:
        raise HTTPException(
            status_code=400, detail='Email ou senha incorreto(s)'
        )

    if not decripty_password_hash(form_data.password, user_from_db.password):
        raise HTTPException(
            status_code=400, detail='Email ou senha incorreto(s)'
        )

    access_token = create_access_token({'sub': str(user_from_db.id)})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh_token', response_model=TokenSchema)
def refresh_token_post(current_user: Current_user):
    new_access_token = create_access_token({'sub': str(current_user.id)})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
