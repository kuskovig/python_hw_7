import pytest
import requests
import cerberus
from test_data.get_dogapi_methods import methods


# basic validation of "get all breeds" api response
def test_all_breeds_schema(dog_all_breeds_url):
    schema = {'message': {'type': 'dict', 'required': True},
              'status': {'type': 'string', 'required': True}
              }
    v = cerberus.Validator(schema)

    dictionary_of_breeds = requests.request('get', dog_all_breeds_url).json()
    assert v.validate(dictionary_of_breeds)


# testing "get all breeds" api correct response statuses for some https methods
@pytest.mark.parametrize('method, status', methods)
def test_dog_all_breeds_correct_methods(method, status, dog_all_breeds_url):
    assert requests.request(method, dog_all_breeds_url).status_code == int(status)


# testing random breed image api
@pytest.mark.parametrize("breed, status", [('corgi', 'success'),
                                           ('germanshepherd', 'success'),
                                           ('newfoundland', 'success'),
                                           ('not_a_breed', 'error')])
def test_random_breed_image_correct_status(dog_random_breed_image_url, breed, status):
    response = requests.request('get', dog_random_breed_image_url + breed + "/images/random")
    assert response.json()["status"] == status


# testing that api return correct amount of entries
@pytest.mark.parametrize('amount', ['3', '5', '7'])
def test_random_n_images_from_all_breeds(amount, dog_random_dog_image_url):
    response = requests.request('get', dog_random_dog_image_url + amount)
    assert len(response.json()["message"]) == int(amount)


# testing that random image method returns valid image
def test_random_image_returns_valid_jpg(dog_random_dog_image_url):
    response_image_url = requests.request('get', dog_random_dog_image_url).json()["message"]

    response_image = requests.request('get', response_image_url)
    assert response_image.headers['Content-Type'] == 'image/jpeg'
    assert response_image.status_code == 200
