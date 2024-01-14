from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return {'Msg': 'Server is running now!'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                reload=True, log_level='info')
