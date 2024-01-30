from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter mais de 2 palavras')

        return value

    @validator(*('aulas', 'horas'))
    def validar_horas_e_aulas(cls, value: int):
        if value < 10:
            raise ValueError('Aulas e Horas devem ser maiores que 10 horas')

        return value


cursos = [
    Curso(id=1, titulo='Curso de JS', aulas=44, horas=30),
    Curso(id=2, titulo='Curso de Java', aulas=64, horas=52),
]
