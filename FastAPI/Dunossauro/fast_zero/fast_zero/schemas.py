from pydantic import BaseModel, EmailStr


class UsuarioSchema(BaseModel):
    username: str
    email: EmailStr
    senha: str


class UsuarioPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UsuarioDB(UsuarioSchema):
    id: int


class UsuarioLista(BaseModel):
    usuarios: list[UsuarioPublic]


class Message(BaseModel):
    mensagem: str
