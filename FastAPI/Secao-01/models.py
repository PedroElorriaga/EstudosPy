from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    titulo: str
    aulas: int
    horas: int
