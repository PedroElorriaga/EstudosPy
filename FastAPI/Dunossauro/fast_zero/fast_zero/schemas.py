from pydantic import BaseModel, ConfigDict, EmailStr


class UsuarioSchema(BaseModel):
    username: str
    email: EmailStr
    senha: str


class UsuarioPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UsuarioLista(BaseModel):
    usuarios: list[UsuarioPublic]


class Message(BaseModel):
    mensagem: str
