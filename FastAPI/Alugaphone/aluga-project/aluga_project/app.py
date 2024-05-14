from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


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