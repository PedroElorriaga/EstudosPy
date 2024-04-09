from fastapi import FastAPI

from fast_zero.routes import auth, usuarios

app = FastAPI()


app.include_router(usuarios.router)
app.include_router(auth.router)
