import pytest


@pytest.mark.parametrize(('username', 'symptom', 'date'), (
        ('k', '0', '20201118'),
        ('test_user', '0', '20201118'),
        ('test_user2', '0', '20201118')
))
def test_log(client, username, symptom, date):
    assert client.get('/quarantine/log').status_code == 200
    response = client.post(
        '/quarantine/log', data={'username': username,
                                 'symptom': symptom, 'date': date}
    )
    assert response.status == "200 OK"
