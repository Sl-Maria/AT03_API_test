import pytest
from main import get_cat_image

def test_get_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/MTUzODI1OA.jpg'}]
    image_url = get_cat_image()
    assert image_url == 'https://cdn2.thecatapi.com/images/MTUzODI1OA.jpg'

def test_get_cat_image_fail(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    image_url = get_cat_image()
    assert image_url is None

if __name__ == '__main__':
    pytest.main()