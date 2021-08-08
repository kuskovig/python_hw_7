import requests
import cerberus
import pytest
from test_data.get_openbrewery_testdata import ob_schema
from test_data.get_openbrewery_testdata import brewery_amount_per_page
from test_data.get_openbrewery_testdata import brewery_http_methods


# testing for correct schema
def test_get_breweries_schema(brewery_get_breweries_url):
    schema = ob_schema
    response = requests.request('get', brewery_get_breweries_url).json()
    v = cerberus.Validator(schema)

    for i in response:
        assert v.validate(i)


# testing api return correct bar type
@pytest.mark.parametrize('key', ['by_type'])
@pytest.mark.parametrize('value', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning',
                                   'bar', 'contract', 'proprietor', 'closed'])
def test_get_breweries_by_type(key, value, brewery_get_breweries_url):
    response = requests.request('get', brewery_get_breweries_url, params={key: value}).json()

    for i in response:
        assert i["brewery_type"] == value


# testing api return correct amount of entries
@pytest.mark.parametrize('key', ['per_page'])
@pytest.mark.parametrize('value, expected_value', brewery_amount_per_page,
                         ids=['zero', 'less_than_default', 'maximum', 'more_than_maximum'])
def test_breweries_correct_amount_of_items(key, value, expected_value, brewery_get_breweries_url):
    response = requests.request('get', brewery_get_breweries_url, params={key: value}).json()

    assert len(response) == int(expected_value)


# testing api return correct status for different http methods
@pytest.mark.parametrize('method, status', brewery_http_methods)
def test_brewery_correct_status(method, status, brewery_get_breweries_url):
    response = requests.request(method, brewery_get_breweries_url)

    assert response.status_code == int(status)


# testing api returns correct answer for request with incorrect brewery id
@pytest.mark.parametrize('incorrect_id', ['qwe', '-1', '2,6'], ids=['string', 'negative int', 'float number'])
def test_correct_answer_with_incorrect_id(brewery_get_breweries_url, incorrect_id):
    response = requests.request('get', brewery_get_breweries_url + incorrect_id).json()
    schema = {'message': {'type': 'string',
                          'required': True,
                          'allowed': [
                              "Couldn't find Brewery with 'id'={incorrect_id}".format(incorrect_id=incorrect_id)]}
              }
    v = cerberus.Validator(schema)

    assert v.validate(response)
