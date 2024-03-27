from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Usuario
from fast_zero.schemas import (
    Message,
    UsuarioLista,
    UsuarioPublic,
    UsuarioSchema,
)

app = FastAPI()


# Status de esperado e Modelo de resposta esperado
@app.post('/users', status_code=201, response_model=UsuarioPublic)
def criar_usuarios(
    usuario: UsuarioSchema, session: Session = Depends(get_session)
):
    db_usuario = session.scalar(
        select(Usuario).where(Usuario.username == usuario.username)
    )

    if db_usuario:
        raise HTTPException(status_code=400, detail='Username já existe')

    db_usuario = Usuario(
        username=usuario.username, email=usuario.email, senha=usuario.senha
    )
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)

    return db_usuario


@app.get('/users', status_code=200, response_model=UsuarioLista)
def ler_usuarios(
    skip: int = 0, limite: int = 100, session: Session = Depends(get_session)
):
    db_usuarios = session.scalars(
        select(Usuario).offset(skip).limit(limite)
    ).all()

    return {'usuarios': db_usuarios}


@app.put('/users/{user_id}', status_code=200, response_model=UsuarioPublic)
def atualizar_usuarios(
    user_id: int,
    usuario: UsuarioSchema,
    session: Session = Depends(get_session),
):
    db_usuario = session.scalar(select(Usuario).where(Usuario.id == user_id))

    if not db_usuario:
        raise HTTPException(
            status_code=404, detail=f'Usuário com ID {user_id} não encontrado'
        )

    db_usuario.username = usuario.username
    db_usuario.email = usuario.email
    db_usuario.senha = usuario.senha
    session.commit()
    session.refresh(db_usuario)

    return db_usuario


@app.delete('/users/{user_id}', status_code=200, response_model=Message)
def excluir_usuario(user_id: int, session: Session = Depends(get_session)):
    db_usuario = session.scalar(select(Usuario).where(Usuario.id == user_id))

    if not db_usuario:
        raise HTTPException(status_code=404, detail='O usuário não existe')

    session.delete(db_usuario)
    session.commit()

    return {'mensagem': 'Usuário excluido com sucesso!'}


@app.get('/users/{user_id}', status_code=200, response_model=UsuarioPublic)
def ler_um_usuario(user_id: int):
    usuario = database[user_id - 1]
    return usuario
