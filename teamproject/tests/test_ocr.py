import pytest


@pytest.mark.parametrize(('username', 'image', 'image_name'), (
        ('k', None, ""),
        ('k', None, None)
))
def test_upload(client, username, image, image_name):
    data = {
        'username': username, 'file': (image, image_name)
    }
    response = client.post('/ocr/upload', data=data)
    assert response.status_code == 200


def test_ocr(client):
    image = "test.jpg"
    data = {'username': 'username', 'file': (open(image, 'rb'), image)}
    response = client.post('/ocr/upload', data=data)
    assert response.status == '200 OK'


def test_ocr2(client):
    image = "test2.jpg"
    data = {'username': 'username', 'file': (open(image, 'rb'), image)}
    response = client.post('/ocr/upload', data=data)
    assert response.status == '200 OK'
