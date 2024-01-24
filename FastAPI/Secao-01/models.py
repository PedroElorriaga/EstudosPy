from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo='JS', aulas=44, horas=30),
    Curso(id=2, titulo='Java', aulas=64, horas=52),
]
