from fastapi import APIRouter
from models import cursos, Curso

router = APIRouter()


@router.get('/api/v1/cursos')
async def get_cursos():
    return cursos


@router.post('/api/v1/post')
async def post_curso(curso: Curso):
    proximo_id = len(cursos) + 1
    curso.id = proximo_id
    cursos.append(curso)

    return curso
