import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="request  url"

    )
    parser.addoption(
        "--status_code",
        default=200,
        help="expected status code of response"
    )


@pytest.fixture()
def addoption_base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def addoption_status_code(request):
    return request.config.getoption("--status_code")


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


@pytest.fixture()
def jp_base_url():
    return "https://jsonplaceholder.typicode.com/"
