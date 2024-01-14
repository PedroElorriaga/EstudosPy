from fastapi import FastAPI, HTTPException, status

app = FastAPI()


cursos = {
    1: {
        'titulo': 'Azure Cloud Fundamentals',
        'aulas': 60,
        'horas': 20
    },
    2: {
        'titulo': 'Gestão de carreira',
        'aulas': 35,
        'horas': 9
    }
}


@app.get('/cursos')
async def get_cursos() -> dict:
    return {'cursos disponiveis': cursos}


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso: dict = cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    return curso


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
