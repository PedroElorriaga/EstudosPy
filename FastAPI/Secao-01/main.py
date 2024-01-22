from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header
from typing import Dict, List
from pydantic import ValidationError
from models import Curso, cursos

app = FastAPI(
    title='Documentação Curso API',
    version='1.0.2',
    description='Guia para manipulação de API'
)


@app.get('/cursos')
async def get_cursos() -> dict:
    return {'cursos disponiveis': cursos}


@app.get('/cursos/{id_key}',
         description='Retorna todos os cursos ou uma lista vazia',
         summary='Retorna todos os cursos',
         response_model=List[Curso])
async def get_curso(id_key: int):
    try:
        curso: dict = cursos[id_key]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.get('/cursos/limite/{id_key}')
async def get_limited_curso(id_key: int = Path(title='ID do curso', description='O ID precisa ser entre 1 e 2', ge=1, le=2)):
    try:
        curso: dict = cursos[id_key]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    id_key: int = len(cursos) + 1
    cursos[id_key] = curso
    return {'msg': 'Curso criado com sucesso'}


@app.put('/cursos/{id_key}')
async def put_curso(id_key: int, curso: Curso):
    if id_key in cursos:
        cursos[id_key] = curso
        return {'msg': {f'Alteração no ID {id_key} efetuado com sucesso!'}}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com o ID {id_key}')


@app.delete('/cursos/{id_key}')
async def delete_curso(id_key: int):
    if id_key in cursos:
        del cursos[id_key]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'O curso com ID {id_key} não existe!')


@app.get('/calcular')
async def calcular(a: int, b: int = Query(default=10, ge=1), header: str = Header()):
    soma = a + b

    print(header)

    return {'Resultado': soma}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
