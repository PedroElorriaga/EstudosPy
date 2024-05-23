def test_reading_datas_from_phonestocks_empty(client):
    response = client.get('/phones')

    assert response.status_code == 200
    assert response.json() == {'phones': []}
