from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from aluga_project.database.database import create_session
from aluga_project.models.models import UserModels
from aluga_project.schemas.user_schema import Message, UserSchema, UsersList

Session = Annotated[Session, Depends(create_session)]
router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', status_code=200, response_model=UsersList)
def user_get(session: Session, skip: int = 0, limit: int = 100):

    users_list_from_db = session.scalars(
        select(UserModels).offset(skip).limit(limit)
    ).all()

    return {'users': users_list_from_db}


@router.post('/', status_code=201, response_model=Message)
def user_post(session: Session, user: UserSchema):
    user_from_db = session.scalar(
        select(UserModels).where(user.cpf == UserModels.cpf)
    )

    if not user_from_db:
        HTTPException(status_code=406, detail='CPF ja existe na base de dados')

    user_db = UserModels(
        first_name=user.first_name,
        middle_name=user.middle_name,
        cpf=user.cpf,
        active_account=user.active_account,
        active_rent=user.active_rent,
    )
    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return {'message': 'Usuário cadastrado com sucesso!'}
