from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
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
from fast_zero.security import criar_hash_de_senha, pegar_usuario_atual

Session = Annotated[Session, Depends(get_session)]
UsuarioAtual = Annotated[Usuario, Depends(pegar_usuario_atual)]

router = APIRouter(prefix='/users', tags=['users'])


# Status de esperado e Modelo de resposta esperado
@router.post('/', status_code=201, response_model=UsuarioPublic)
def criar_usuarios(
    usuario: UsuarioSchema,
    session: Session,
):
    db_usuario = session.scalar(
        select(Usuario).where(Usuario.username == usuario.username)
    )

    if db_usuario:
        raise HTTPException(status_code=400, detail='Username já existe')

    senha_encriptada = criar_hash_de_senha(usuario.senha)

    db_usuario = Usuario(
        username=usuario.username, email=usuario.email, senha=senha_encriptada
    )
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)

    return db_usuario


@router.get('/', status_code=200, response_model=UsuarioLista)
def ler_usuarios(
    session: Session,
    skip: int = 0,
    limite: int = 100,
):
    db_usuarios = session.scalars(
        select(Usuario).offset(skip).limit(limite)
    ).all()

    return {'usuarios': db_usuarios}


@router.put('/{user_id}', status_code=200, response_model=UsuarioPublic)
def atualizar_usuarios(
    user_id: int,
    usuario: UsuarioSchema,
    session: Session,
    usuario_atual: UsuarioAtual,
):
    if usuario_atual.id != user_id:
        raise HTTPException(
            status_code=400, detail='Não possui permissões suficientes'
        )

    usuario_atual.username = usuario.username
    usuario_atual.email = usuario.email
    usuario_atual.senha = criar_hash_de_senha(usuario.senha)
    session.commit()
    session.refresh(usuario_atual)

    return usuario_atual


@router.delete('/{user_id}', status_code=200, response_model=Message)
def excluir_usuario(
    user_id: int,
    session: Session,
    usuario_atual: UsuarioAtual,
):
    if usuario_atual.id != user_id:
        raise HTTPException(
            status_code=400, detail='Não possui permissões suficientes'
        )

    session.delete(usuario_atual)
    session.commit()

    return {'mensagem': 'Usuário excluido com sucesso!'}
