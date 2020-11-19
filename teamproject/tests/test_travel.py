def test_getinfo(client):
    assert client.get('/travel/update').status_code == 200
    response = client.post(
        '/travel/update'
    )
    assert response.status == "405 METHOD NOT ALLOWED"
