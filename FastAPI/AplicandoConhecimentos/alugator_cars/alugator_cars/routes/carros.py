from fastapi import APIRouter, HTTPException

from alugator_cars.schemas import CarrosLista, CarrosSchema, Mensagem

router = APIRouter(prefix='/catalogo', tags=['catalogo'])


carros = [
    {
        'modelo': 'Evoque',
        'marca': 'Range Rover',
        'ano': 2016,
        'cor': 'Vermelho Metálico',
    },
]


@router.get('/', status_code=200, response_model=CarrosLista)
def get_cars_catalog():

    if not carros:
        raise HTTPException(status_code=400, detail='Nenhum carro encontrado')

    return {'carros': carros}


@router.post('/', status_code=200, response_model=CarrosSchema)
def post_registrat_carro(carros_data: CarrosSchema):
    if not carros_data:
        raise HTTPException(
            status_code=401, detail='Insira as informações corretas'
        )

    carros.append(carros_data)

    return carros_data


@router.delete('/', status_code=200, response_model=Mensagem)
def delete_cars_catalog():

    if not carros:
        raise HTTPException(status_code=400, detail='Nenhum carro encontrado')

    carros.pop()

    return {'mensagem': 'Todos carros deletados'}
