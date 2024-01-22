from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    titulo: str
    aulas: int
    horas: int


cursos = {
    Curso(id=1, titulo='JS', aula=44, horas=30),
}
