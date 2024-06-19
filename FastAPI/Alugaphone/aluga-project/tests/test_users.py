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


def test_update_user_from_db(client, user_factory):
    response = client.put(
        '/users/1',
        json={
            'first_name': 'Pedro',
            'middle_name': 'Elorriaga',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'message': 'O ID: 1 foi atualizado com sucesso!'
    }


def test_delete_user_from_db(client, user_factory):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {
        'message': 'O ID: 1 foi excluido com sucesso da base de dados!'
    }
