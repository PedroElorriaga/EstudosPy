def test_reading_datas_from_phonestock_empty(client):
    response = client.get('/phones')

    assert response.status_code == 200
    assert response.json() == {'phones': []}


def test_include_phone_to_phonestock(client):
    response = client.post(
        '/phones',
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
        'phone_model': 'Iphone 14 Pro MAX',
        'brand': 'Apple',
        'chip': True,
        'color': 'Spacial Black',
        'price': 4.999,
    }


def test_update_phone(client, phone_factory):
    response = client.put(
        f'/phones/{1}',
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