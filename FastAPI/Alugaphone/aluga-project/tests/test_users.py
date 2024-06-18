def test_get_list_from_db_empty(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_post_user_to_db(client):
    response = client.post(
        '/users',
        json={
            'first_name': 'Pedro',
            'middle_name': 'Elorriaga',
            'cpf': 32724611837,
            'active_account': True,
            'active_rent': True,
        },
    )

    assert response.status_code == 201
    assert response.json() == {'message': 'Usuário cadastrado com sucesso!'}
