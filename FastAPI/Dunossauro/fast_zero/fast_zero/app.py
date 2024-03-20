from fastapi import FastAPI, HTTPException

from fast_zero.schemas import (
    Message,
    UsuarioDB,
    UsuarioLista,
    UsuarioPublic,
    UsuarioSchema,
)

app = FastAPI()

database = [
    {
        'id': 1,
        'username': 'PedroAdmin',
        'email': 'pedroadmin@admin.com',
        'senha': 'HASH554781412',
    },
]


# Status de esperado e Modelo de resposta esperado
@app.post('/users/', status_code=201, response_model=UsuarioPublic)
def criar_usuarios(usuario: UsuarioSchema):
    usuario_com_id = UsuarioDB(**usuario.model_dump(), id=len(database) + 1)
    database.append(usuario_com_id)
    return usuario_com_id


@app.get('/users/', status_code=200, response_model=UsuarioLista)
def ler_usuarios():
    return {'usuarios': database}


@app.put('/users/{user_id}', status_code=200, response_model=UsuarioPublic)
def atualizar_usuarios(user_id: int, usuario: UsuarioSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')

    usuario_com_id = UsuarioDB(**usuario.model_dump(), id=user_id)
    # REFERE AO PRIMEIRO ITEM DA LISTA DATABASE [0]
    database[user_id - 1] = usuario_com_id

    return usuario_com_id


@app.delete('/users/{user_id}', status_code=200, response_model=Message)
def excluir_usuario(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')

    del database[user_id - 1]

    return {'mensagem': 'Usuário excluido com sucesso!'}


@app.get('/users/{user_id}', status_code=200, response_model=UsuarioPublic)
def ler_um_usuario(user_id: int):
    usuario = database[user_id - 1]
    return usuario
