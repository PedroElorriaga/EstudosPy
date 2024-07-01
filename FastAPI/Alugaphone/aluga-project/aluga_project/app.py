from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from aluga_project.routes import auth, phones, users

app = FastAPI()
app.include_router(phones.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', response_class=HTMLResponse)
def home():
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
