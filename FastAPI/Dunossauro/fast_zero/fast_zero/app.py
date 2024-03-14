from fastapi import FastAPI

from fast_zero.schemas import (
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
