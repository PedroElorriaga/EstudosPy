def test_pegar_lista_de_carros(client):
    response = client.get('/catalogo')

    assert response.status_code == 200
    assert response.json() == {
        'carros': [
            {
                'modelo': 'Evoque',
                'marca': 'Range Rover',
                'ano': 2016,
                'cor': 'Vermelho Metálico',
            }
        ]
    }


def test_deletar_catalogo_carros(client):
    response = client.delete('/deletar_catalogo')

    assert response.json() == {'mensagem': 'Todos carros deletados'}


def test_tentar_pegar_lista_e_retornar_erro(client):
    response = client.get('/catalogo')

    assert response.status_code == 400
    assert response.json() == {'detail': 'Nenhum carro encontrado'}


def test_registrar_novo_carro(client):
    response = client.post(
        '/catalogo_new',
        json={
            'modelo': 'GLA 250',
            'marca': 'Mercedes',
            'ano': 2017,
            'cor': 'Cinza Espacial',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'modelo': 'GLA 250',
        'marca': 'Mercedes',
        'ano': 2017,
        'cor': 'Cinza Espacial',
    }
