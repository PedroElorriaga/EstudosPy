from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routes import auth, usuarios

app = FastAPI()


app.include_router(usuarios.router)
app.include_router(auth.router)


@app.get('/', response_class=HTMLResponse)
def home_page():
    return """
    <html>
        <head>
            <title>Home Page</title>
        </head>

        <body style="font-family: Arial;">
            <h1 style="margin-left: 5%;">Use o <strong>/docs</strong> para vizualizar as funcionalidades</h1>
        </body>
    </html>
    """
