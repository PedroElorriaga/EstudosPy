from fastapi import FastAPI

from alugator_cars.routes import carros

app = FastAPI()

app.include_router(carros.router)
