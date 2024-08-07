from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from aluga_project.database.database import create_session
from aluga_project.models.models import UserModels
from aluga_project.schemas.user_schema import (
    Message,
    UserSchema,
    UsersList,
    UserUpdate,
)
from aluga_project.security.security import (
    get_current_user,
    make_password_hash,
)

Session = Annotated[Session, Depends(create_session)]
Current_user = Annotated[UserModels, Depends(get_current_user)]
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

    if user_from_db:
        raise HTTPException(
            status_code=406, detail='CPF ja existe na base de dados'
        )

    user_db = UserModels(
        first_name=user.first_name,
        middle_name=user.middle_name,
        cpf=user.cpf,
        email=user.email,
        password=make_password_hash(user.password),
        active_account=True,
        active_rent=True,
    )

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return {'message': 'Usuário cadastrado com sucesso!'}


@router.put('/{id}', status_code=200, response_model=Message)
def user_put(
    id: int, session: Session, user: UserUpdate, current_user: Current_user
):
    user_from_db = session.scalar(
        select(UserModels).where(id == UserModels.id)
    )

    if not user_from_db:
        raise HTTPException(
            status_code=400, detail=f'O ID: {id} não existe na base de dados'
        )

    if current_user.id != user_from_db.id:
        raise HTTPException(
            status_code=400, detail='Sem permissões suficientes'
        )

    if user.password:
        user.password = make_password_hash(user.password)

    user_from_db.first_name = user.first_name or user_from_db.first_name
    user_from_db.middle_name = user.middle_name or user_from_db.middle_name
    user_from_db.email = user.email or user_from_db.email
    user_from_db.password = user.password or user_from_db.password
    user_from_db.active_account = (
        user.active_account or user_from_db.active_account
    )
    user_from_db.active_rent = user.active_rent or user_from_db.active_rent

    session.commit()
    session.refresh(user_from_db)

    return {'message': f'O ID: {id} foi atualizado com sucesso!'}


@router.delete('/{id}', status_code=200, response_model=Message)
def user_delete(id: int, session: Session, current_user: Current_user):
    user_from_db = session.scalar(
        select(UserModels).where(id == UserModels.id)
    )

    if not user_from_db:
        raise HTTPException(
            status_code=400, detail=f'O ID: {id} não existe na base de dados'
        )

    if current_user.id != user_from_db.id:
        raise HTTPException(
            status_code=400, detail='Sem permissões suficientes'
        )

    session.delete(user_from_db)
    session.commit()

    return {
        'message': f'O ID: {id} foi excluido com sucesso da base de dados!'
    }
