import pytest


@pytest.mark.parametrize(
    ('username', 'date', 'visittime', 'symptoms', 'building',
     'state', 'message'),
    (
            ('', '2018-01-01', '1', 1, 'NWC', 'NewYork',
             'Incorrect username'),
            ('c', '2018-01-01', '1', 1, 'NWC', 'NewYork',
             'Incorrect username'),
            ('a', '2018-01-01', '1', 0, 'NWC', 'NewYork', 'greenpass'),
            ('a', '2018-01-01', '1', 1, 'NWC', 'NewYork', 'yellowpass'),
            ('a', '2018-01-01', '1', 0, 'NWC', 'Alabama', 'yellowpass'),
    ))
def test_submit(client, username, date, visittime,
                symptoms, building, state, message):
    response = client.post(
        '/dailypass/submit', data={'username': username,
                                   'date': date,
                                   'visittime': visittime,
                                   'symptoms': symptoms,
                                   'building': building,
                                   'state': state}
    )

    assert client.get('/dailypass/submit').status_code == 200
    assert response.status == "200 OK"
