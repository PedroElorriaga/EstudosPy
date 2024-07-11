def test_get_phones_from_phonestock_empty(client):
    response = client.get('/phones')

    assert response.status_code == 200
    assert response.json() == {'phones': []}


def test_include_phone_to_phonestock(client, token):
    response = client.post(
        '/phones',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'phone_model': 'Iphone 14 Pro MAX',
            'brand': 'Apple',
            'chip': True,
            'color': 'Spacial Black',
            'price': 4.999,
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'message': 'O item Iphone 14 Pro MAX foi incluido com sucesso!'
    }


def test_error_to_include_phone(client, token):
    response = client.post(
        '/phones',
        headers={'Authorization': f'Bearer {token}'},
        json={},
    )

    assert response.status_code == 422


def test_update_phone(client, phone_factory, token):
    response = client.put(
        '/phones/1',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'phone_model': 'Iphone 15 PRO',
            'brand': 'Apple',
            'chip': True,
            'color': 'Gray',
            'price': 7.999,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'phone_model': 'Iphone 15 PRO',
        'brand': 'Apple',
        'chip': True,
        'color': 'Gray',
        'price': 7.999,
    }


def test_error_update_phone(client, token):
    response = client.put(
        '/phones/1',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'phone_model': 'Iphone 15 PRO',
            'brand': 'Apple',
            'chip': True,
            'color': 'Gray',
            'price': 7.999,
        },
    )

    assert response.status_code == 404


def test_delete_phone_from_db(client, phone_factory, token):
    response = client.delete(
        '/phones/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'message': 'O item foi exlcuido com sucesso!'}


def test_error_delete_phone(client, token):
    response = client.delete(
        '/phones/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 404
