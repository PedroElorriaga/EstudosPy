from fastapi import FastAPI
from routes import curso_router
from routes import usuario_router


app = FastAPI()
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(curso_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
