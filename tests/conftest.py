import pytest


@pytest.fixture()
def dog_all_breeds_url():
    return "https://dog.ceo/api/breeds/list/all"


@pytest.fixture()
def dog_random_breed_image_url():
    return "https://dog.ceo/api/breed/"

@pytest.fixture()
def dog_random_dog_image_url():
    return "https://dog.ceo/api/breeds/image/random/"

@pytest.fixture()
def brewery_get_breweries_url():
    return "https://api.openbrewerydb.org/breweries/"
