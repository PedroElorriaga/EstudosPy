from pydantic import BaseModel


class CarrosSchema(BaseModel):
    modelo: str
    marca: str
    ano: int
    cor: str


class CarrosLista(BaseModel):
    carros: list[CarrosSchema]


class Mensagem(BaseModel):
    mensagem: str
